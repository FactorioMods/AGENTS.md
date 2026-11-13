"""Private, cooperative worker assignments and fail-closed resource claims."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import uuid


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def create(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def key(value):
    require(re.fullmatch(r"[a-z][a-z0-9]*(?:[-.:/][a-z0-9]+)*", value), "invalid canonical key")
    return value


def agent_dir(root, agent):
    key(agent)
    return root / "agents" / hashlib.sha256(agent.encode()).hexdigest()


def claim_dir(root, resource):
    return root / "claims" / hashlib.sha256(resource.encode()).hexdigest()


def git_snapshot(source):
    source = Path(source).resolve(strict=True)
    def git(*args):
        return subprocess.check_output(["git", "-C", str(source), *args], stderr=subprocess.PIPE)
    actual = Path(os.fsdecode(git("rev-parse", "--show-toplevel")).strip()).resolve()
    require(source == actual, "source must be the actual Git root")
    untracked = []
    for raw in git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0"):
        if not raw:
            continue
        relative = os.fsdecode(raw)
        path = actual / relative
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            kind, fingerprint = "symlink", hashlib.sha256(os.fsencode(os.readlink(path))).hexdigest()
        else:
            require(stat.S_ISREG(mode), f"unsupported untracked input: {relative}")
            kind, fingerprint = "file", digest(path)
        untracked.append({"path": relative, "type": kind, "sha256": fingerprint})
    return {"root": str(actual), "common_dir": str(Path(os.fsdecode(git("rev-parse", "--path-format=absolute", "--git-common-dir")).strip()).resolve()),
            "untracked": untracked, "branch": os.fsdecode(git("symbolic-ref", "--short", "-q", "HEAD")).strip()
            if git("rev-parse", "--abbrev-ref", "HEAD").strip() != b"HEAD" else "HEAD",
            "head": git("rev-parse", "HEAD").decode().strip(),
            "status": os.fsdecode(git("status", "--porcelain=v1", "--untracked-files=all")),
            "tracked_diff_sha256": hashlib.sha256(git("diff", "--binary", "HEAD", "--")).hexdigest()}


def state(root):
    session = read(root / "session.json")
    require(session["schema"] == 1 and isinstance(session["goal"], str), "invalid session")
    require(isinstance(session["resources"], list), "invalid resources")
    require(len(set(session["resources"])) == len(session["resources"]), "duplicate resources")
    require(isinstance(session["references"], list), "invalid references")
    for ref in session["references"]:
        require(Path(ref["path"]).is_absolute() and re.fullmatch(r"[0-9a-f]{64}", ref["sha256"]), "invalid reference")
    for resource in session["resources"]:
        key(resource)
    agents = {}
    for folder in (root / "agents").iterdir():
        assignment = read(folder / "assignment.json")
        name = assignment["agent"]
        require(folder == agent_dir(root, name) and name not in agents, "invalid assignment directory")
        require(digest(folder / "task.md") == assignment["brief_sha256"], "assignment brief drift")
        require(isinstance(assignment["source"], dict), "invalid source snapshot")
        result = read(folder / "result.json") if (folder / "result.json").exists() else None
        if result is not None:
            validate_result(result)
        agents[name] = {"assignment": assignment, "result": result}
    require(len(agents) <= 10, "worker limit exceeded")
    claims = []
    for folder in (root / "claims").iterdir():
        claim = read(folder / "owner.json")
        require(claim["resource"] in session["resources"], "undeclared claim")
        require(folder == claim_dir(root, claim["resource"]), "invalid claim directory")
        require(claim["agent"] in agents and isinstance(claim["claim_id"], str)
                and re.fullmatch(r"[0-9a-f]{32}", claim["claim_id"]), "invalid claim owner/token")
        claims.append(claim)
    return session, agents, claims


def validate_result(result):
    require(result["status"] in ("complete", "blocked", "needs-review"), "invalid result status")
    require(isinstance(result["summary"], str) and result["summary"].strip(), "missing summary")
    require(isinstance(result["evidence"], list), "invalid evidence")
    for item in result["evidence"]:
        require(Path(item["path"]).is_absolute(), "evidence paths must be absolute")
        require(digest(item["path"]) == item["sha256"], "evidence drift")


def run(args):
    root = Path(args.workspace).resolve()
    if args.command == "init":
        require(not root.exists(), "workspace already exists")
        resources = [key(item) for item in args.resource]
        require(len(set(resources)) == len(resources), "duplicate resources")
        refs = [{"path": str(Path(p).resolve(strict=True)), "sha256": digest(p)} for p in args.reference]
        root.mkdir(parents=True)
        (root / "agents").mkdir()
        (root / "claims").mkdir()
        create(root / "session.json", {"schema": 1, "goal": args.goal, "resources": resources,
                                      "references": refs, "permissions": "Cooperative locks only; no tool or sandbox permissions granted."})
        return {"workspace": str(root), "initialized": True}
    session, agents, claims = state(root)
    if args.command == "assign":
        require(len(agents) < 10, "worker limit is ten, including root")
        snapshot = git_snapshot(args.source)
        brief = Path(args.brief).read_bytes()
        folder = agent_dir(root, args.agent)
        # Serialize registration, including the worker-count check, without retry.
        guard = root / ".assigning"
        guard.mkdir()
        try:
            _, current, _ = state(root)
            require(len(current) < 10, "worker limit is ten, including root")
            folder.mkdir()
            (folder / "scratch").mkdir()
            (folder / "evidence").mkdir()
            with (folder / "task.md").open("xb") as stream:
                stream.write(brief)
            create(folder / "assignment.json", {"agent": args.agent, "brief_sha256": hashlib.sha256(brief).hexdigest(),
                                                "source": snapshot})
        finally:
            guard.rmdir()
        return {"agent": args.agent, "directory": str(folder)}
    if args.command in ("claim", "release", "finish"):
        require(args.agent in agents, "unknown agent")
    if args.command == "claim":
        require(agents[args.agent]["result"] is None, "agent already finished")
        require(len(set(args.resources)) == len(args.resources), "duplicate requested resources")
        require(all(r in session["resources"] for r in args.resources), "undeclared resource")
        token, owned = uuid.uuid4().hex, []
        try:
            for resource in args.resources:
                folder = claim_dir(root, resource)
                folder.mkdir()
                owned.append(folder)
                create(folder / "owner.json", {"resource": resource, "agent": args.agent, "claim_id": token})
        except Exception:
            for folder in reversed(owned):
                owner = folder / "owner.json"
                if owner.exists():
                    owner.unlink()
                folder.rmdir()
            raise
        return {"claim_id": token, "resources": args.resources}
    if args.command == "release":
        require(len(set(args.resources)) == len(args.resources), "duplicate requested resources")
        selected = []
        for resource in args.resources:
            matches = [c for c in claims if c["resource"] == resource]
            require(len(matches) == 1 and matches[0]["agent"] == args.agent
                    and matches[0]["claim_id"] == args.claim_id, "claim owner/token mismatch")
            selected.append(claim_dir(root, resource))
        for folder in selected:
            (folder / "owner.json").unlink()
            folder.rmdir()
        return {"released": args.resources}
    if args.command == "finish":
        require(not any(c["agent"] == args.agent for c in claims), "release claims before finishing")
        result = read(Path(args.result))
        validate_result(result)
        result["after_source"] = git_snapshot(agents[args.agent]["assignment"]["source"]["root"])
        create(agent_dir(root, args.agent) / "result.json", result)
        return {"agent": args.agent, "status": result["status"]}
    if args.command == "check":
        drift = []
        for ref in session["references"]:
            if not Path(ref["path"]).is_file() or digest(ref["path"]) != ref["sha256"]:
                drift.append({"reference": ref["path"]})
        if args.agent:
            require(args.agent in agents, "unknown agent")
            before = agents[args.agent]["assignment"]["source"]
            if git_snapshot(before["root"]) != before:
                drift.append({"source": before["root"]})
        return {"ok": not drift, "drift": drift}
    return {"goal": session["goal"], "agents": {name: item["result"]["status"] if item["result"] else "assigned"
                                              for name, item in agents.items()}, "claims": claims}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--goal", required=True)
    init.add_argument("--resource", action="append", default=[])
    init.add_argument("--reference", action="append", default=[])
    assign = commands.add_parser("assign")
    assign.add_argument("--agent", required=True)
    assign.add_argument("--brief", required=True)
    assign.add_argument("--source", required=True)
    for command in ("claim", "release"):
        sub = commands.add_parser(command)
        sub.add_argument("--agent", required=True)
        sub.add_argument("resources", nargs="+")
        if command == "release":
            sub.add_argument("--claim-id", required=True)
    check = commands.add_parser("check")
    check.add_argument("--agent")
    finish = commands.add_parser("finish")
    finish.add_argument("--agent", required=True)
    finish.add_argument("--result", required=True)
    commands.add_parser("status")
    try:
        args = parser.parse_args()
        require(not (Path(args.workspace) / ".assigning").exists(), "assignment pending; inspect state")
        if args.command in ("claim", "release", "finish"):
            guard = Path(args.workspace).resolve() / ".claims-mutating"
            guard.mkdir()
            try:
                result = run(args)
            finally:
                guard.rmdir()
        else:
            require(not (Path(args.workspace) / ".claims-mutating").exists(), "claims mutation pending; inspect state")
            require(not (Path(args.workspace) / ".assigning").exists(), "assignment pending; inspect state")
            result = run(args)
        print(json.dumps(result, ensure_ascii=True))
        return 1 if result.get("ok") is False else 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

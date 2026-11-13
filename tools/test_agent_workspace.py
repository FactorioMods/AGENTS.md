"""Isolated CLI regression checks; no game or live workspace access."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("agent_workspace.py")


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "private"
        self.repo = self.base / "repo"
        self.repo.mkdir()
        self.git("init")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "file").write_text("baseline")
        self.git("add", ".")
        self.git("commit", "-m", "fixture")
        self.brief = self.base / "brief.md"
        self.brief.write_text("Only disposable fixtures.")
        self.reference = self.base / "reference"
        self.reference.write_text("pinned")
        self.call("init", "--goal", "test", "--resource", "renderer", "--resource", "source", "--reference", str(self.reference))
        for name in ("root", "worker"):
            self.call("assign", "--agent", name, "--brief", str(self.brief), "--source", str(self.repo))

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True)

    def command(self, *args):
        return [sys.executable, str(SCRIPT), "--workspace", str(self.root), *args]

    def call(self, *args, ok=True):
        process = subprocess.run(self.command(*args), capture_output=True, text=True)
        self.assertEqual(process.returncode == 0, ok, process.stderr or process.stdout)
        return json.loads(process.stdout if process.returncode == 0 else process.stderr or process.stdout)

    def test_exclusive_subprocess_contention(self):
        children = [subprocess.Popen(self.command("claim", "--agent", name, "renderer"), stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True) for name in ("root", "worker")]
        results = [(child.communicate(), child.wait()) for child in children]
        self.assertEqual(sum(code == 0 for _, code in results), 1)
        self.assertEqual(len(self.call("status")["claims"]), 1)

    def test_release_owner_token_and_rollback(self):
        claim = self.call("claim", "--agent", "root", "renderer")
        self.call("release", "--agent", "worker", "--claim-id", claim["claim_id"], "renderer", ok=False)
        self.call("release", "--agent", "root", "--claim-id", "wrong", "renderer", ok=False)
        self.call("claim", "--agent", "worker", "source", "renderer", ok=False)
        self.assertEqual([x["resource"] for x in self.call("status")["claims"]], ["renderer"])
        self.call("release", "--agent", "root", "--claim-id", claim["claim_id"], "renderer")
        self.assertEqual(self.call("status")["claims"], [])

    def test_partial_and_orphaned_claims_fail_closed(self):
        folder = self.root / "claims" / hashlib.sha256(b"renderer").hexdigest()
        folder.mkdir()
        self.call("status", ok=False)
        self.call("claim", "--agent", "root", "source", ok=False)
        (folder / "owner.json").write_text(json.dumps({"resource": "renderer", "agent": "absent", "claim_id": "a" * 32}))
        self.call("status", ok=False)

    def test_create_only_and_drift(self):
        self.call("init", "--goal", "again", ok=False)
        self.call("assign", "--agent", "root", "--brief", str(self.brief), "--source", str(self.repo), ok=False)
        self.call("check", "--agent", "root")
        (self.repo / "file").write_text("changed")
        process = subprocess.run(self.command("check", "--agent", "root"), capture_output=True, text=True)
        self.assertEqual(process.returncode, 1)
        self.assertIn("source", json.loads(process.stdout)["drift"][0])
        self.reference.write_text("drift")
        process = subprocess.run(self.command("check"), capture_output=True, text=True)
        self.assertEqual(process.returncode, 1)
        self.assertIn("reference", json.loads(process.stdout)["drift"][0])

    def test_existing_untracked_bytes_and_common_directory(self):
        untracked = self.repo / "new.py"
        untracked.write_text("before")
        self.call("assign", "--agent", "observer", "--brief", str(self.brief), "--source", str(self.repo))
        folder = self.root / "agents" / hashlib.sha256(b"observer").hexdigest()
        snapshot = json.loads((folder / "assignment.json").read_text())["source"]
        self.assertEqual(Path(snapshot["common_dir"]), (self.repo / ".git").resolve())
        self.assertEqual(snapshot["untracked"][0]["type"], "file")
        before = self.git("status", "--porcelain=v1").stdout
        untracked.write_text("after")
        self.assertEqual(before, self.git("status", "--porcelain=v1").stdout)
        process = subprocess.run(self.command("check", "--agent", "observer"), capture_output=True, text=True)
        self.assertEqual(process.returncode, 1)
        self.assertIn("source", json.loads(process.stdout)["drift"][0])

    def test_immutable_finish_and_evidence(self):
        evidence = self.base / "evidence"
        evidence.write_text("proof")
        result = self.base / "result.json"
        result.write_text(json.dumps({"status": "complete", "summary": "Done", "evidence": [
            {"path": str(evidence), "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest()}]}))
        self.call("finish", "--agent", "root", "--result", str(result))
        self.call("finish", "--agent", "root", "--result", str(result), ok=False)
        self.call("claim", "--agent", "root", "renderer", ok=False)
        evidence.write_text("changed")
        self.call("status", ok=False)

    def test_stale_guards_and_malformed_result(self):
        guard = self.root / ".claims-mutating"
        guard.mkdir()
        self.call("status", ok=False)
        self.call("claim", "--agent", "root", "renderer", ok=False)
        guard.rmdir()
        guard = self.root / ".assigning"
        guard.mkdir()
        self.call("status", ok=False)
        self.call("claim", "--agent", "root", "renderer", ok=False)
        guard.rmdir()
        folder = self.root / "agents" / hashlib.sha256(b"root").hexdigest()
        (folder / "result.json").write_text("{}")
        self.call("status", ok=False)

    def test_worker_cap_and_brief_integrity(self):
        for number in range(8):
            self.call("assign", "--agent", f"worker-{number}", "--brief", str(self.brief), "--source", str(self.repo))
        self.call("assign", "--agent", "extra", "--brief", str(self.brief), "--source", str(self.repo), ok=False)
        folder = self.root / "agents" / hashlib.sha256(b"root").hexdigest()
        (folder / "task.md").write_text("changed assignment")
        self.call("status", ok=False)


if __name__ == "__main__":
    unittest.main()

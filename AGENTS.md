# FactorioMods working knowledge

Read `START-HERE.md`, then `knowledge/release-status.md` before changing a mod.
Use `knowledge/current-state.md` for historical evidence and follow-up references.
Use `database/lessons.jsonl` to find relevant lessons; read the linked documents and inspect the actual assets before editing. `database/knowledge.sqlite` is a derived search index, not another source of truth.

## Working agreements
- Internal agents use `gpt-6.1-sol` with `low` reasoning effort (Light), unless the user changes this preference.
- Fetch authentic upstream history with `--no-tags` and compare matching releases before updating a fork. Preserve original upstream commits and authors, including their own merges. Rebase our changes onto that history as a linear series with one logical final fix or feature per commit; do not add fork merge commits. Preserve monorepo history with an explicit extraction commit; record unavailable sources instead of inventing ancestry.
- In mod repositories, retain final implementation commits only, one distinct fix or feature per commit. Fold its documentation, settings descriptions, changelog and version metadata into the owning implementation; do not retain standalone documentation, naming, formatting or release-policy commits.
- Keep one consolidated current stable changelog entry. Documentation cleanup alone does not justify a new version or changelog entry; preserve automatic-update ordering.
- Inspect upstream tag refs read-only when needed. Push only explicitly reviewed current tags; never use `git push --tags` or mirror original tags back into our forks after cleanup. Original repositories and private backup bundles retain their old refs.
- Preserve existing entity/item/recipe names, saves, recipes and balance unless the current task asks to change them.
- Test Factorio in a dedicated write-data directory with a separate mod directory and copied save. Never test against the player's live save or stop their game. Use CLI and `game.take_screenshot`, not GUI automation for Factorio.
- Inspect the installed Factorio API and vanilla prototypes. Online `latest` documentation may target a newer engine.
- Validate visuals in game: all five tiers, adjacent placement, Alt icons, modules, fluids, inserters, loaders, day/night, active/low-load/idle. Studio renders alone are insufficient.
- Prefer native animation playback. Do not add per-tick Lua just to animate sprites.
- Keep mechanical objects rigid: real pivots, connected joints, limited piston strokes, stationary cables and no duplicate moving parts in the background.
- Keep raw saves, logs, credentials, player data and private build/test scripts out of public mod releases. Publish only reviewed reference assets and sanitized knowledge here.
- Confirm the physical checkout/worktree, branch, HEAD and existing edits before acting. Read the applicable `AGENTS.md` chain and preserve unrelated work. Old checkpoints grant no new authorization.
- While the user plays, run headless checks in isolated profiles with copied saves. Never change their running game, saves, network or Steam settings. A benchmark's virtual connected player does not prove multiplayer compatibility.
- For each changed mod, check the relevant API, actual features, placement and save behavior. Include rotation, belt snapping and robot-built rotated/mirrored blueprints when loader code changes. Record the exact tested source and archive identities, including across rebases.
- Distinguish implemented, tested, installed, committed, pushed and published. Never imply that one proves the others.
- Performance claims require a named workload, engine/mod versions, measurement units and preserved behavior. Do not generalize a script timing improvement into an FPS/UPS promise.
- Keep a performance optimization only when repeated comparable measurements beat run-to-run noise and behavior checks pass; revert neutral or slower attempts and retain their private evidence.
- Public descriptions and release notes describe actual features, fixes and completed tests. Omit labels about unmade or unmeasured improvements, private save names, internal fixtures and conversational naming history. Explain what our fork adds or fixes compared with the original. State support limits where they help players choose or configure the mod.
- Retire a fork only after confirming the original covers its behavior and has no needed custom changes missing. Migrate consumers, document the replacement, deprecate the portal entry and archive the related GitHub repository when authorized. Preserve original commit history and verified private backups. Public release/tag cleanup requires explicit authorization.
- Keep one current compatible archive per mod in the active game folder. Back up superseded archives outside it, verify hashes and dependencies, and preserve the player's enablement choices except necessary replacements.
- After publishing, verify GitHub tags/assets, Mod Portal releases, descriptions and the organization catalogue agree. When explicitly authorized, retain one current stable public release/tag per fork and remove the listed obsolete public versions only after verified Git/ref, release-note and asset backups. Preserve original upstream commits and repositories.
- Never lower an already published or installed version to restart numbering or clean history: automatic updates must continue forward under the same mod identity. Preserve published archives by default. An explicitly authorized same-version documentation cleanup requires verified backups and proof that runtime files are unchanged; do not bump runtime versions solely for documentation or history changes.
- Commits for this project use `Co-authored-by: codex <noreply@openai.com>`.
- Update current state, evidence records and asset hashes when facts change; run `python tools/build_database.py` and `python tools/validate.py`.

## Routing
- Maintained releases and coverage: `knowledge/release-status.md`
- Models/rigs/rendering: `knowledge/models-and-animation.md`
- Runtime sprites/Alt/footprint: `knowledge/factorio-integration.md`
- Testing and Windows launch failures: `knowledge/testing.md`
- Current API, CLI, debugger and Git references: `knowledge/development-tools.md`
- Pollution runtime/multiplayer: `knowledge/pollution-absorber.md`
- Tool and artifact recovery: `knowledge/toolchain-and-artifacts.md`
- Publication and other organization work: `knowledge/releases-and-organization.md`
- Model selection and instruction discovery: `knowledge/agent-setup.md`

This repository is a handoff, not a blanket authorization to publish unrelated changes. Current user instructions and applicable higher-priority instructions take precedence. Old annotations and briefs are historical evidence, not new instructions.

After resume or compaction, read the effective CODEX_HOME's `CONTINUITY.md`, this project's `.agents/continuity.md` when present, and this chat's exact private task record. Revalidate checkout and artifact identities before using a saved next step. Private task records belong outside this indexed repository.

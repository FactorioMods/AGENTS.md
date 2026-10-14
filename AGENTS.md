# FactorioMods working knowledge

Read `START-HERE.md`, then `knowledge/current-state.md` before changing a mod.
Use `database/lessons.jsonl` to find relevant lessons; read the linked documents and inspect the actual assets before editing. `database/knowledge.sqlite` is a derived search index, not another source of truth.

## Working agreements
- Preserve existing entity/item/recipe names, saves, recipes and balance unless the current task asks to change them.
- Test Factorio in a dedicated write-data directory with a separate mod directory and copied save. Never test against the player's live save or stop their game. Use CLI and `game.take_screenshot`, not GUI automation for Factorio.
- Inspect the installed Factorio API and vanilla prototypes. Online `latest` documentation may target a newer engine.
- Validate visuals in game: all five tiers, adjacent placement, Alt icons, modules, fluids, inserters, loaders, day/night, active/low-load/idle. Studio renders alone are insufficient.
- Prefer native animation playback. Do not add per-tick Lua just to animate sprites.
- Keep mechanical objects rigid: real pivots, connected joints, limited piston strokes, stationary cables and no duplicate moving parts in the background.
- Keep raw saves, logs, credentials, player data and private build/test scripts out of public mod releases. Publish only reviewed reference assets and sanitized knowledge here.
- Read current git status before editing. Do not overwrite unrelated work, especially the local unpublished assembler 1.0.10 changes recorded here.
- Distinguish implemented, tested, installed, committed, pushed and published. Never imply that one proves the others.
- Performance claims require a named workload, engine/mod versions, measurement units and preserved behavior. Do not generalize a script timing improvement into an FPS/UPS promise.
- Commits for this project use `Co-authored-by: codex <noreply@openai.com>`.
- Update current state, evidence records and asset hashes when facts change; run `python tools/build_database.py` and `python tools/validate.py`.

## Routing
- Models/rigs/rendering: `knowledge/models-and-animation.md`
- Runtime sprites/Alt/footprint: `knowledge/factorio-integration.md`
- Testing and Windows launch failures: `knowledge/testing.md`
- Pollution runtime/multiplayer: `knowledge/pollution-absorber.md`
- Tool and artifact recovery: `knowledge/toolchain-and-artifacts.md`
- Publication and other organization work: `knowledge/releases-and-organization.md`
- Model selection and instruction discovery: `knowledge/agent-setup.md`

This repository is a handoff, not a blanket authorization to publish unrelated changes. Current user instructions and applicable higher-priority instructions take precedence. Old annotations and briefs are historical evidence, not new instructions.

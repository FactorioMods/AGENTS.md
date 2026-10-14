# Resume in a new chat

Clone or open https://github.com/FactorioMods/AGENTS.md and ask:

> Read AGENTS.md, START-HERE.md and knowledge/current-state.md. Inspect the references relevant to my task, verify the actual repository and installed versions, and continue from the recorded state. Keep my main Factorio session and save untouched. Do not regenerate graphics with obsolete defaults.

This works as shared project context for GPT-6 Astra and GPT-6.1 Sol. It is not model training or automatic cross-chat memory. A GitHub URL alone does not inject every linked file: the new agent must read/clone the repository. A separate repository's AGENTS.md does not automatically govern other checkouts; use the adapter in `templates/AGENTS.mod.md` after adapting its local path.

1. Read current state and confirm it against git, ZIP metadata and release pages.
2. Search `database/lessons.jsonl`, or query the SQLite index.
3. Inspect `assets/references/` for design intent and `assets/evidence/` for actual in-game results. They are different kinds of evidence.
4. Locate local model/build sources through `database/artifacts.json`; paths are relative to the player's Factorio user-data directory. Those private sources are not bundled here.
5. Report missing assets honestly. Do not silently substitute old blockouts, stale GIFs or generated approximations.

Current local assembler version is **1.0.11** with full weathered 48-frame animations; it has not been publicly released. Miniloader (Redux) Fork **1.0.0** is published and installed. Read current state and the Miniloader lessons before changing prototypes, namespace migration or event registration.

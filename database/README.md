# Database layout

- `lessons.jsonl`: canonical searchable lesson records. Stable `id`, `topic`, `status`, `statement`, relative `source`, `verification`, and capture `date`.
- `knowledge.sqlite`: derived documents and lessons tables, schema version1. Rebuild after editing Markdown or JSONL.
- `assets.json`: published visual evidence/reference paths, classifications and SHA256 hashes.
- `artifacts.json`: private source locations relative to Factorio user-data and hashes. It is a locator, not a backup or download service.
- `models.json`: exact requested model IDs and common reading entry point; no automatic model switching.
- `rig-check.json`, `drive-clearance.json`, `native-motion-check.json`: sanitized historical quantitative reports. In native-motion-check, tier1–5 maps to speeds20,40,80,160,320. In rig-check, tier values are actual speeds. These reports predate the layout-only1.0.10 adjustment.

Evidence statuses:
- `verified-local`: code/artifact inspected or action verified in the captured session; not universal correctness.
- `historical-evidence`: earlier tests/results or a changelog record, with scope stated.
- `user-requirement`: explicit desired behavior/design, not proof of implementation.
- `open-gap`: missing verification or unfinished work.

Update procedure: edit the canonical document and corresponding records, refresh changed asset/artifact hashes, rebuild SQLite, then run validate.py. Do not manually patch only the SQLite copy. Public remote state must be refreshed from actual release pages rather than inferred from local info.json.

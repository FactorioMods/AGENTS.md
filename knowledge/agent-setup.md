# AGENTS.md and model setup

Official Codex guidance says project instructions are discovered along the path from project root to working directory. `AGENTS.override.md` takes precedence over `AGENTS.md` in the same directory; deeper instructions take precedence over broader ones. Default combined instruction budget is32KiB. Keep this root entry concise and explicitly route to detailed files. A sibling GitHub repository is not automatically loaded.

Both requested models can use this same repository. Verified official model pages identify `gpt-6-astra` and `gpt-6.1-sol`. No special model-specific memory database format is established by those pages. We therefore use portable Markdown/JSONL with a derived SQLite search index. This is an engineering choice, not an OpenAI-prescribed memory architecture.

Choose the model in the app/session. Files cannot silently switch the active model. `database/models.json` records the requested IDs and common handoff entry point, not pricing, service guarantees or automatic routing. API capabilities/settings may differ from the desktop app; consult current official docs for configuration rather than copying stale settings.

Canonical lessons have stable IDs, a topic, evidence status, source paths, actionable correction and verification expectations. Record uncertainty and superseded guidance. Load only relevant documents and images; do not paste an entire raw history every turn. On completion, update current state and evidence, rebuild the search DB and validate links/hashes.

For a new chat: use the START-HERE prompt. For work in a mod checkout: adapt `templates/AGENTS.mod.md` to point to an available local clone. The template is not installed into existing mod repositories by this task.

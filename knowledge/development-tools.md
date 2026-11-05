# Current development references

Checked 2026-11-05. Start with the installed engine's `doc-html/runtime-api.json`, `prototype-api.json` and vanilla prototypes. The [official API index](https://lua-api.factorio.com/latest/index.html) currently reports Factorio 2.1.24; verify it still matches before using `latest`.

Use Context7 on demand for a specific gap. Reuse the known IDs `/websites/lua-api_factorio` and `/websites/wiki_factorio`; query the needed topic rather than retrieving a broad catalogue. Check returned examples against the installed API and use the primary reference when an indexed answer misses the requested detail.

## Native CLI checks

Use separate `--config`, write-data and `--mod-directory` paths with copied input saves. The [official command-line reference](https://wiki.factorio.com/Command_line_parameters) documents these useful modes:

| Option | Use |
| --- | --- |
| `--test-save FILE` / `--test-scenario NAME` | Run a native headless test with a player; have assertions finish through `script.finish_test(passed)`. |
| `--test-ticks N` | Bound a test run. Reaching the limit can exit successfully without the test calling its finish function, so verify the assertion/result marker too. |
| `--benchmark FILE`, `--benchmark-ticks`, `--benchmark-runs` | Repeat a preserved workload and retain exact archive, save and configuration identities. |
| `--benchmark-consistency` | Check scenario consistency before the first and after the last update. |
| `--dump-data` | Export final `data.raw` JSON into the private script-output directory for prototype comparisons. |
| `--check-unused-prototype-data` | Find ignored or obsolete prototype fields during loading. |
| `--log-spritesheets-to-optimize N` | Identify sheets with nearly transparent noise worth inspecting before deterministic crop/packing work. |

Read the installed executable's `--help` before running an option. The documented `--threads` switch controls map-preview generation; use an explicit launcher CPU limit when test CPU use needs bounding. Keep native test results distinct from real connected-client and rendering evidence.

## Optional editor and debugger tools

Factorio exposes a native [LuaDebugAdapter](https://lua-api.factorio.com/latest/classes/LuaDebugAdapter.html) through `--dap`. The optional [Factorio Mod Tool Kit](https://github.com/justarandomgeek/vscode-factoriomod-debug) integrates that adapter for debugging/profiling and supplies JSON, locale and changelog tooling. Its current README points to EmmyLua language-server integrations. This refresh did not install FMTK; check local availability before relying on it. No editor add-on replaces native loading and feature tests.

## Git series maintenance

The [Git rebase manual](https://git-scm.com/docs/git-rebase) documents interactive editing, reordering and splitting commits. Preserve authentic upstream commits; arrange our additions as separate final fixes/features without fork merge commits. Before rewriting our published series, keep a verified bundle and exact ref snapshot, use the authorized scope, and compare final trees and artifact hashes. Fetch upstream with `--no-tags`, inspect original tag refs read-only, and push only explicitly reviewed current refs.

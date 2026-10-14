# Current state — 2026-10-15

## Advanced Assembly Machines: Improved

- Source: https://github.com/FactorioMods/advanced-assembling-machine-improved
- Portal: https://mods.factorio.com/mod/advanced-assembling-machine-improved
- Public release confirmed in this chat: **1.1.0**, squashed commit `0b3f2b7`.
- Public ZIP SHA256: `931664080279c7cb6a6c6037b5c60384710ddd01867168d983a0bfffc4f6719f`.
- Latest installed local version: **1.0.11**, published on GitHub and the Mod Portal. ZIP SHA256 `931664080279c7cb6a6c6037b5c60384710ddd01867168d983a0bfffc4f6719f`.
- 1.0.11 adds matte planetary weathering, contained Fulgora coil discharges, Vulcanus billet light cycling, a subtle Aquilo bed pulse, and a clean static idle image. Body and shadow shift down by .25 tiles; compact .44 scale and Alt icon placement remain.
- All five tiers have 48 distinct final GPU-rendered frames. Factorio screenshot comparisons showed all four sampled working-state transitions changed and all four idle-machine comparisons stayed static. Neighboring moving belts were excluded from the machine comparison crop.
- Source frames/models: `optimization-work/assembler-improved/astra-models/planet-weathered/<tier>/`. Production packer: `pack_weathered.py full`; static pilot packaging is now explicitly rejected. The 1.0.11 ZIP is installed in the player's mods directory.
- Additional integration: real robots built loader/belt/assembler blueprints beside vanilla plus all five machines; all 48 direction/input-output cases transferred items.
- The following 1.0.10 notes are historical context, superseded by the installed 1.0.11 package.
- Historical local correction: **1.0.10**, not committed/pushed/published at that handoff. Four modified files: `changelog.txt`, `data.lua`, `info.json`, `prototypes/graphics.lua`.
- 1.0.10 changes: sprite scale .50 → .44, corresponding sprite/shadow shifts and shadow scale multiplied by .88; recipe icon scale .60 and shift `{0,.65}`.
- Why: 206-pixel sheet frames at scale .50 occupied 103 pixels, exceeding a 3-tile/96-pixel width. At .44 width is 90.64 pixels. Adjacent in-game screenshot confirms a visible gap.
- Latest check: five adjacent tiers with productivity-module recipe Alt icons, Factorio 2.0.77, dedicated runtime, normal exit. It is a layout test; the showcase machines lacked that recipe's ingredients, so it is not proof of active animation in 1.0.10.
- 1.0.9 earlier checks: 40 retained existing machines, 45 Miniloaders Redux/Matt's combinations, 20 fluid/rotation cases, four planetary milestones, adjacent ordinary inserters, base-only save creation, active/low/idle image sequences.
- Low-load evidence showed intermittent motion with one craft per second; do not claim a continuously smooth slow motion curve from that test.
- Outstanding visual coverage: module overlays at high slot counts, legendary quality indicators, mixed recipes and vertically adjacent rows should be checked before declaring every overlay layout solved. The 1.0.10 horizontal comparison uses the same recipe on five tiers.

## Pollution Absorber: Improved

Local source version **1.0.3**, commit `daaf516`, title preserved. Source:
https://github.com/FactorioMods/pollution-absorber-improved
Portal: https://mods.factorio.com/mod/pollution-absorber-improved

1.0.3 repairs multiplayer event registration across save/load. The changelog records a real upgrade/join/save/reload/rejoin test on 2.0.77 and overlapping-absorber behavior checks. This handoff inspected code/changelog; it did not rerun multiplayer or independently check the latest Portal listing. Verify remote state before another release.

## Historical material that is stale

`astra-assembler-handoff/HANDOFF.md` predates the finished models and public 1.0.9. Its blockout/release statuses and requests for hinges/latches are superseded. The latest user explicitly removed those fittings.

Old review GIFs predate final weathering/fitting removal. Current production frames are tier directories `000.png` through `047.png`; do not use old review previews as final proof.

`integrate.py` still sets VERSION=1.0.9 and emits .50 scale. `package_and_fixture.py` still targets 1.0.9 and rewrites the test fixture. Update these private scripts before rerunning; otherwise they undo the newer local fixes.

## Miniloader (Redux) Fork

- Repository: https://github.com/FactorioMods/factorio-miniloader-redux-fork
- Portal: https://mods.factorio.com/mod/miniloader-redux-fork
- Release: https://github.com/FactorioMods/factorio-miniloader-redux-fork/releases/tag/fork-v1.0.0
- Public and installed version **1.0.0**, source commit `632f4ea`, baseline upstream `690af52` (2.2.4), Factorio 2.0.77. ZIP SHA256 `1133d3a0f4436eb61c05b6f250b25663ea98042f5ea676b2288cf2b119deb7e8`.
- New mod identity `miniloader-redux-fork`; old `miniloader-redux` is disabled locally. Entity/item names remain compatible. Do not enable both.
- Fixes the eight-state R/reverse-R cycle and robot-built rotated/mirrored tagged ghosts. Adopts existing physical components when changing mod identities.
- Verified 1,152 rotations, 72 direct cases, four 72-case robot/blueprint groups, 48 assembler integration cases, 807 recovered loader configurations, and multiplayer join/save/reload/rejoin with the clean release ZIP.
- Per-loader spill/discard preferences reset to the startup preference during identity migration; default is spill. Other optional integrations beyond the tested base/Space Age/Matt's set have not been independently verified.
- See [Miniloader lessons](miniloaders-redux.md). Keep all private fixture saves/logs/credentials outside published repositories.


## Release consolidation — 2026-10-15

Assembler 1.1.0 is published and installed; code and graphics are byte-identical to tested 1.0.11. Only metadata and changelog changed. SHA256: 3a6d6c3f0d7c067e4c9d55358ce3fae34194804641daf7dae74c7f5025339b81. GitHub releases retain only 1.0.0 and 1.1.0. Intermediate local packages are archived outside the active mods directory. Portal removal of 1.0.1, 1.0.2, 1.0.9 and 1.0.11 is complete. Both Portal and GitHub releases/tags retain only 1.0.0 and 1.1.0; README and release notes match the consolidated changes. Main history is consolidated into two release commits: original 1.0.0 and squashed 1.1.0. The original history is backed up locally in optimization-work/assembler-release-backups/before-history-squash.bundle. The 1.1.0 tree is unchanged (6d5a2fe3687d4db1772bb22d7051bab2cbf4434c), and its tag matches main.




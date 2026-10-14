# Current state — 2026-10-14

## Advanced Assembly Machines: Improved

- Source: https://github.com/FactorioMods/advanced-assembling-machine-improved
- Portal: https://mods.factorio.com/mod/advanced-assembling-machine-improved
- Public release confirmed in this chat: **1.0.9**, commit `1ebf036`.
- Public ZIP SHA256: `b80259c8a55a8995936224bc1e0d69bc7c825a35a048fae9e6be955626fdcdb8`.
- Local source and installed ZIP: **1.0.10**, not committed/pushed/published at handoff. Four modified files: `changelog.txt`, `data.lua`, `info.json`, `prototypes/graphics.lua`.
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

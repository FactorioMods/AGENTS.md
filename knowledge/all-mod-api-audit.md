# Published mod API audit — 2026-10-15

The authenticated Mod Portal profile lists four mods. Latest public releases and exact local ZIP hashes match:

| Mod | Version | Portal/local SHA-1 |
|---|---|---|
| Advanced Assembly Machines: Improved | 1.1.0 | e6ccc3757943842fcd166199c05c6fe31d0d5ff6 |
| Miniloader (Redux) Fork | 1.0.2 | 1f47002882f0cf884fa613da28f9f643e7144af0 |
| Pollution Absorber: Improved | 1.0.3 | a61644047331b44e34aed1f619b70189e57fb5eb |
| Magic Science Chest: Improved | 1.0.0 | 49863810504613f2042658a9697689633e6a7ce6 |

Version-pinned Factorio 2.0.77 runtime/prototype schemas used. Scanned 92 Lua files (6 assembler, 4 pollution, 10 science chest, 72 loader including vendored libraries). All referenced defines exist: 2/12/19/80 distinct per repository. Engine-global member and post-2.0 member candidates reviewed. No additional incompatible API names confirmed; loader underground-neighbour fix retained. Prototype fields must be checked against prototype rather than runtime schemas; magic-chest gui_mode/erase_contents_when_mined are prototype assignments and load successfully.

All four exact release ZIPs loaded together in an isolated instance on a copied validation save. Five assembler entities, loader entities, underground-belt creation, science filter unlock/native refill and fuelled pollution absorption passed; 2401 ticks completed normally. A fresh empty-world fixture initially failed a native-refill assertion even with valid filters; the copied existing save passed both sampled checks. Do not claim the isolated empty-world discrepancy is fully diagnosed.

GitHub releases for science chest and pollution match 1.0.0 and 1.0.3; assembler/loader releases were verified during publication. Latest means latest published versions of these forks, not latest engine APIs or automatically updated upstream libraries. Mods intentionally target 2.0.77.

Static scanning cannot prove every dynamic argument or branch. Optional external-mod integrations are not fully covered. Prior isolated animation, robot/rotation, fluid, migration and multiplayer tests complement this audit. No additional code patch or version bump required by the confirmed findings.

Private evidence: optimization-work/all-mod-api-validation/existing-player.out; player saves/main game untouched. API schemas: optimization-work/miniloader-api-audit.

# Isolated tests and evidence

Use separate config, write-data, mod-directory and copied save. Fresh runtime paths prevent collision with earlier tests. Never remove a live lock or kill the player's main game to make a test start.

## Current headless testing requirement

For the all-save migration, the user requires tests without physical Factorio windows. Use native headless servers for conversion and logic checks. The official full Linux client can also run in a private Xvfb framebuffer for genuine multiplayer joins and rendering checks, provided it cannot connect to the physical desktop. A hidden Windows window does not satisfy this requirement.

The isolated Factorio 2.1.24 offscreen route completed a real client join, synchronized play, disconnect, host save/reload and rejoin. The proof uses software Mesa and establishes the multiplayer method; each mod graph and save still needs its own checks. It does not establish hardware rendering performance. Keep account credentials out of evidence, use copied input saves, and preserve the player's network and Steam settings.

## Save content and settings gates

Inspect current `level.dat0` metadata rather than creation-only `level-init.dat`. Run native prototype-removal reporting on a disposable original-save copy, then inspect actual state that names alone cannot protect. Same-name prototype changes can reset valve thresholds or reduce equipment/module capacity without reporting a removed prototype. Use authentic old mod versions and the matching old engine when a property baseline is needed.

Capture inventories including crafter trash, qualities, stack metadata, fluids, paid crafting progress, circuit/fluid connections and entity references when conversion touches them. Native fast replacement may discard trash or clamp fluid buffers; passing a fresh empty-machine check cannot establish populated-machine migration safety.

Compare saved startup settings with their effective native values. Computed and table-defined defaults should come from `prototypes.mod_setting`, queried only on disposable verification hosts. Keep source-bound receipts for intentional renames, unit conversions or required upstream setting changes; do not classify an active removed control as inert merely because its old name disappeared.

Read-only blueprint checks must distinguish physical books, game records and personal preview records. An unreadable preview is unknown, not an empty blueprint. Never call personal-library setters to complete coverage. Final exports must remain separate from long-running tests, console queries and QA helpers.

Example PowerShell, after adapting paths:

```powershell
$testRoot = Join-Path $env:APPDATA 'Factorio/optimization-work/my-isolated-check'
# config.ini must set read-data to the installation/data and write-data to this test's runtime.
$testArgs = @('--config', "$testRoot/config.ini", '--mod-directory', "$testRoot/mods",
  '--benchmark', "$testRoot/copied-save.zip", '--benchmark-ticks', '720', '--disable-audio')
Start-Process $factorioExe -WorkingDirectory "$testRoot/runtime" -ArgumentList $testArgs `
  -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput "$testRoot/test.log" `
  -RedirectStandardError "$testRoot/test.err"
```

A Windows Steam build once exited before testing because Steam relaunch discarded CLI arguments. Starting the installed Steam client silently and placing Steam's development `steam_appid.txt` containing427520 in the isolated working directory resolved that session. This is an environment-specific workaround, not a substitute for a licensed installation. Do not alter binaries/authentication or put it in the user's live data directory.

Another run failed to rename test player-data and mod-list files under sandbox restrictions. Running the same isolated test through the normal approved escalation path worked. A zero launcher exit alone is not proof: inspect loaded mod versions, test assertions, screenshots and the final Factorio log. Lock errors can mean overlapping test instances or an incorrect write-data path.

## Validation matrix

- Load a copied representative save, count retained existing entities and verify recipe/progression state.
- Feed every tier through each installed Miniloader variant, collect outputs and assert production/output transfer.
- Exercise two fluid inputs and two outputs at four rotations per tier.
- Place ordinary inserters on four sides and verify actual supply/production.
- Unlock each independent starter milestone in separate forces; test base without Space Age.
- Capture day/night, adjacent machines, vanilla context, active/low-load/idle sequences and Alt overlays.
- Multiplayer changes need a real host/client join after upgrade, save/reload and rejoin; two single-player runs are not equivalent.

1.0.9 recorded45loader combinations,20fluid cases,4milestones,40retained machines. Native frame comparisons:31unique active frames;2-3 low-load frames;1idle frame. This is evidence of state-sensitive playback, not measured UPS improvement.

1.0.10 only reran a200tick layout scene with all tiers side-by-side and Alt recipe icons; it did not repeat the entire functional/multiplayer suite. Public evidence here is sanitized; raw local logs can expose Steam IDs and save information.

## Clock-sensitive upgrade checks

Prefer headless creation, logic and consistency checks. Use graphical clients only when actual joins/rejoins or rendering must be verified. Never change the running player game to prepare a test.

For exact financial/inventory comparisons, freeze the private test clock and restore that freeze after configuration changes. UPS+ applies its always-day option and unfreezes daytime during configuration changes; this can legitimately execute additional automatic trading periods while a client loads. Record the runtime setting, surface always_day, freeze_daytime and daytime before blaming a migration. Modify another mod's runtime settings only through the owning mod/player; keep any owner hook inside private copies. Use fresh per-run profiles and copy each immutable checkpoint before passing it to a server, which can write back to its input on quit.

## Avoiding redundant migration work

Check dependency closure, hashes, settings transfers, exact reviewed omissions and evaluated asset references before long host or renderer checks. Include icon dimensions and locale `info.json` font aliases; a successful headless load cannot validate every graphical resource. Evaluate the selected sprite layout rather than dormant legacy `hr_version` fields.

Store an omission dictionary and hashed source/classification evidence inside each immutable profile, with the save and transformed settings identities. An active setting rename needs an explicit value transfer. A retired default, scope change or equivalent enabled replacement needs its own accurate reason; none becomes inert merely because its name disappeared. Missing, changed or unreviewed exceptions must fail before simulation.

Use simulation progress to end a host phase once its required wall time and native tick count both pass. The current private verifier requires at least 35 seconds and 1,800 ticks for each of two host phases, with a bounded timeout for slow worlds. A measured representative run reduced those phases from 360.562 to 70.973 seconds while retaining both consistency runs, exact input/mod hashes and the unchanged final checkpoint. This measures verification overhead, not gameplay performance.

For large originals, convert once into a paused clean checkpoint and run long checks on separate copies. No QA helper or console query belongs in the exported player checkpoint. Reuse a prior property proof only when a recorded content comparison establishes that the relevant runtime stayed identical; retain its original artifact identity and limitations. Run independent profiles concurrently within assigned CPU and port ranges, with private paths and lower priority.

Renderer atlas checks must cover every frame and line, including shadows, rather than only the first frame. Proof reused after a settings-only revision must bind exact control/prototype bytes and native evaluated-domain parity; record the original test identity and the exact engine and artifacts used for graphical or peer checks.

## Native numeric validation

A successful cold load checks accepted serialized prototype fields; native inherited values and derived calculations also need inspection. Exercise the supported minimum, default and maximum settings, enumerate relevant native getter families, and check finite values after inheritance and arithmetic. Large finite input values can overflow a float-backed field or derived health calculation. Some engine fields already clamp values to their native destination range.

Use each destination's actual field limits and preserve unrelated bonuses and value types. Compare the full evaluated data.raw graph: disabled behavior should retain exact bytes where required, and enabled differences should match only the intended bonus or feature. A collector-bonus cap retained existing quality levels and other prototype values; native checks covered finite inherited getters and genuine peer save/reload/rejoin with physical feature checks. Keep further bounds changes tied to a demonstrated supported configuration and its native getter results.

## Native UI stall diagnosis

Use a native stack with symbols matched to the exact executable to identify the blocked subsystem. A sampled Windows menu-background stall followed the simulation widget into space-platform collector navigation. An earlier HTTP log line described request chronology; the stack identified the active work. Verify any menu-background workaround on the affected platform and preserve save files. A separate offscreen Linux background-disabled run establishes that Linux path and clean shutdown.

## Quality multiplier boundary checks

The reviewed IC More Qualities adaptation applies native destination limits separately to the default multiplier and seven float-backed multiplier fields. Its health bound is calculated from the largest positive base health in the selected prototype graph. This preserves quality names, levels, links and unrelated numeric properties while keeping inherited and derived values finite.

Native Factorio 2.1.24 checks exercised the configured multiplier minimum, default and maximum with the other selected startup inputs retained. At default, the full evaluated data.raw output was byte-identical to the baseline. At both boundaries, all 42 numeric getters across 42 qualities and representative derived health, crafting, inserter, module and inventory values were finite. Actual assembler and beacon creation produced positive finite health, followed by 60 native updates. Canonical source b97edcab10c9296b8698c82726d48b578acd5537 retains the tested runtime bytes; its final archive folds in the README and changelog updates. These boundary checks use the selected graph's native host, while connected-peer coverage is recorded separately with its tested settings.

## Exact current-save regression checks

Read the current save header and explicitly set every installed builtin true or false. An omitted Space Age or Quality entry can default on, invalidating a base-only test before the world loads. Validate archive identities, dependencies, conflicts and serialized settings before launching.

Use the installed engine API for required observations. In Factorio 2.1, query entity fluids with `fluids_count` and `get_fluid`; an obsolete `fluidbox` read hidden by `pcall` is an unmeasured field, not an empty or preserved buffer. Recipe generators must recognize `RecipePrototype.categories` as well as legacy single-category inputs. Native category fixtures and a full evaluated graph caught a recycling-cost regression that metadata and successful loading missed.

Compare clean server exports against an unchanged control at the same native tick; saving can advance a paused world. Keep console-marked verification copies separate from player exports. A saved player may have no associated character; record that controller state and guard character-only getters rather than treating an absent character as a load failure. When a third-party configuration handler recreates entities, retain the raw unit-ID difference and verify owners, caches, connections and contents before treating the new IDs as an intentional lifecycle. Never normalize away an unexplained inventory or reference change.

Real-peer proof must include native join, synchronized ticks, host save/reload and same-player rejoin. A newly created test character can disappear on disconnect; isolate it only by its exact identity and proven absence from the input, while retaining checks for every original entity and player. Store electrical member partitions once per network rather than expanding a full member list at every device.

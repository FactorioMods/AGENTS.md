# Miniloader Redux fork lessons

## Baseline and compatibility

Use the latest upstream baseline the user requested, not the older 2.0 maintenance tag. Upstream 690af52/2.2.4 declares Factorio 2.1/base >=2.1.7; 2.0.77 rejects this metadata. After declaring 2.0/base >=2.0.77, data and runtime load successfully. Still exercise all runtime paths; metadata changes alone do not prove compatibility.

The public fork is `miniloader-redux-fork`, not a release under the upstream author's Mod Portal listing. Its graphics root must match the mod identity. Item/entity names `hps__ml-*` stay stable for save/blueprint compatibility; declare a conflict with the original mod.

## Orientation and construction

Configuration direction points toward the belt side. Output flow uses that direction; input flow uses its opposite. Do not put a north input loader's housing facing south merely because the belt flows south. An earlier assembler fixture made that mistake.

The upstream rotation used a 180-degree direction change and toggled input/output, trapping R on one axis. The corrected eight-state cycle visits each cardinal facing in both modes; reverse is its exact inverse. Tests must use actual `LuaEntity.rotate{by_player=...}`. `on_player_rotated_entity` cannot be fabricated with `script.raise_event`.

A serialized blueprint's direction describes its original layout. Robots do not provide a same-tick player `on_pre_build` event. On ghost/robot/revive construction, discard the stored configuration direction and use the built entity's actual transformed direction. Preserve the input/output mode and explicit blueprint no-snapping intent; ordinary untagged placement snaps to connected belt flow.

Native `build_blueprint` and real robots verified arbitrary loader/belt/chest build ordering. Mirrored blueprint layouts were also built in all rotations. Real bots additionally verified vanilla and all five custom assemblers. Do not replace these tests with synthetic robot events.

## Save adoption and event loading

A different mod name has different private storage. Recover the controller index by adopting surviving physical main/loader/inserter entities on init/configuration change. Keep unit numbers, held items, transport lines and wires rather than destroying/replacing components. Sort the surviving internal inserters by unit number to retain creation order. Seed the recovered state mode/filter fields so reconfiguration does not rebuild or flush the loader needlessly.

Input inserters are deliberately forced to maximum stack size. Recover the user's stack preference from `loader_belt_stack_size_override`, not the main inserter override. This fixed 201 mismatches; all 807 saved configurations then matched.

Spill/discard preferences only lived in upstream private storage and cannot be inferred from physical entities. Document the startup-setting fallback; default spill avoids silent loss.

Import migration modules during control parsing. Factorio forbids `require` inside on_init/on_load/event execution. A graphics benchmark error handler crashed while displaying this mistake; headless CLI revealed the underlying Lua error clearly. The corrected import is a top-level local function binding, invoked by init/configuration handlers.

## Reliable tests

- Use valid dry terrain: script entity creation can ignore water, while construction robots cannot build there.
- Supply actual items and powered roboports/provider chests. The 2.0 entity is `passive-provider-chest`, not the old `logistic-chest-passive-provider` name.
- Keep fixture power equipment outside rotated/mirrored and three-tile assembler footprints.
- Use headless `--benchmark` for fast logic/robot checks; use graphics benchmarks only for visual evidence.
- Give each simultaneous process separate write-data. Wait for server readiness and process exit; asynchronous quit/restart otherwise causes lock failures.
- `--start-server` can save back to the loaded filename on quit. Copy an input save into the private server's saves directory first. Never pass a main user save or a shared pristine fixture directly.
- Benchmark mode did not produce a requested autosave. Use a private localhost server/RCON for actual save/reload/rejoin evidence.
- Use current dependencies. A copied Pollution Absorber 1.0.2 caused a known join mismatch; replacing it with fixed 1.0.3 yielded successful joins and rejoin.

## Release evidence

Public 1.0.0: upstream baseline 690af52, fork source 632f4ea; 75 Lua/JSON runtime files in the final ZIP were checked against the multiplayer-tested ZIP (only line endings/docs changed). Portal version 1.0.0 and Factorio 2.0 were visibly confirmed. Original MIT copyright was retained, and the upstream public loader gallery GIF was credited/reused.

Private fixtures, user save snapshots, credentials and multiplayer profiles are not bundled in either public repository.

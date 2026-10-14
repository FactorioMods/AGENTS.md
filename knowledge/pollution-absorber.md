# Pollution Absorber lessons

## Runtime and equivalence

Keep internal entity name `pollution-absorber` even though the fork mod name is `pollution-absorber-improved`; declare conflict with the original mod. Current code uses radius80, rate800 and CHECK_INTERVAL60. It absorbs only when the entity has energy, allocating30%to the center and70%across the original circular16tile sample grid.

Pollution is chunk-based (32tiles). Group repeated sample positions by chunk, but retain sample counts and sequential clamped subtraction semantics. Share reads between overlapping absorbers within one update; immediately update cached values after each write. Read fresh on the next update. Refcount shared chunk entries and release them on removal. Do not assume algebraic regrouping is bit-identical under floating-point arithmetic.

Historical changelog evidence: initial comparison35absorbers/33energized, median update1.56–1.58ms original versus.38–.41ms fork. Later1.0.1 handler mean.0049–.0052ms/tick versus.0070–.0078ms/tick for1.0.0. These are different metrics/workloads; never combine them into one headline.280overlap comparisons and save checkpoint totals were reported matching within floating-point rounding. These were prior tests, not rerun while writing this knowledge base.

The user interpreted a debug-overlay triplet's last value as an average. Verify the exact Factorio version's overlay semantics and capture a controlled timing distribution before responding with performance claims. Distinguish per-update spikes, average per tick and FPS/UPS.

## Multiplayer regression and fix

1.0.3 fixes mismatched client/server event handler registrations after load. Current control.lua registers events and on_nth_tick deterministically at file scope. It stores absorber references, shared chunk pool and update_id in `storage`. on_load only rebinds local references; it does not register a temporary rebuild tick handler or mutate persisted state. Initialization/configuration change rebuilds the indexes.

Use this lifecycle as a design principle, not a claim that every conditional event registration is invalid. The crucial property is deterministic matching handlers/state on both sides. Verify upgrades and join/save/reload/rejoin with actual multiplayer. Changelog records such a1.0.2→1.0.3 test on2.0.77 and overlap equivalence after reload.

## Art direction

The user wants an air-conditioning/filter unit: compact vented metal cabinet, visible top rotor, fixed protective grille, no human-sized access door, correct elevated game view and adequate height. Heating-tower styling and flat neon-green placeholder art were rejected.

Animate only blades under a fixed grille/housing. Static and animated layers must share the same frame size, anchor and scale; a displaced layer previously made a lower fan appear active while the top fan stayed still. Indicator red without fuel and green while working. Keep all four adjacent inserter directions clear. Show both on and off screenshots on the Portal.

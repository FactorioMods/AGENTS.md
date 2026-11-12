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


## Bound function lookup optimization — 1.0.5 / Factorio 2.1.23

Repeated LuaSurface method lookup was measurable overhead. Bind get_pollution once per energized absorber callback and acquire pollute lazily when pollution is present. Keep these references local; never store native functions in persisted storage. Numeric iteration is valid for entry.samples because cache_samples constructs a dense array and never removes individual samples. Preserve sample and native-write order and sequential math.min subtraction.

The final copied-save comparison improved median natural-pollution callback time from 0.333 to 0.211 ms/update; the candidate won all 14 balanced measured blocks. Individual p95 sampling was separate, 400 updates per variant, 1.047 to 0.408 ms. Exact in-engine equality (not serialized tolerance) passed 18,700 chunk comparisons, and real multiplayer fuel/depletion/refuel/save/reload/rejoin checks passed with the exact final archive. The exact release and workload identities are retained in private verification records.

Pin immutable baseline release archives when rerunning private benchmarks. Alternate baseline/candidate within one process, restoring identical pollution outside the timer; retain an experiment ledger. A branch-based minimum replacement was discarded after no demonstrated gain, and an unconditional writer lookup incurred unnecessary clean-chunk work. Final cached-reader confirmation improved natural/high/zero pollution workloads; do not substitute only a heavily polluted stress result for the real saved pollution snapshot.


## Normal-speed follow-up — 2026-10-24

A copied world ran headlessly with normal fuel use, diffusion and physics at speed 1. A wrapper observed 150 scheduled updates over 9,034 ticks with 34 active cleaners: median 0.415 ms/update, p95 0.5822, maximum observed 0.6946; average across game ticks 0.006927 ms/tick. No seeding or direct callback calls. This normal-speed observation measures scheduled absorber callbacks with native diffusion and fuel use. The public PERFORMANCE.md distinguishes both workloads.

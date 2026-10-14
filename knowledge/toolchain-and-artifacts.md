# Toolchain and local recovery

Paths in `database/artifacts.json` are relative to Factorio user-data, usually `%APPDATA%/Factorio` on Windows. Discover installation paths rather than hardcoding a personal drive. Local sources are not downloadable from this knowledge repository.

|Tool|Actual role / caution|
|---|---|
|Blender5.2.2 / bpy|Model generation, analytical rigs, materials, Cycles HIP rendering|
|Python / Pillow|Frame union-crop, sprite packing, icons and preview exports; use for deterministic pipeline work|
|Shapely|Sampled planar tooth-clearance check; not full physical simulation|
|Factorio2.0.77 CLI|Isolated loading, benchmark-graphics, native screenshot fixtures|
|PowerShell / Start-Process|Hidden process launch, separate working directories and redirected logs|
|rg / git / gh|Source discovery, diffs, identity, commits, pushes and releases|
|Browser automation|Mod Portal ZIP/image upload and visible success verification; not Factorio gameplay automation|
|Image-generation tools|Early artwork/concept exploration; cannot guarantee rigid mechanical animation|
|Web / official documentation|Factorio API, Blender features and Codex setup verification|
|Game Development Studio|User installed plugin; historical inspection found game-dev CLI unavailable; do not claim it powered final models|

## Private script map

Under `optimization-work/assembler-improved/astra-models/`:
- `factory_models.py`: main geometry/rig builder, green drive and tier mechanisms.
- `cabinet.py`: vanilla-style continuous shell.
- `industrial_detail.py`, `finish_details.py`, `vanilla_refinement.py`: details/materials/secondary movement; inspect interactions before regeneration.
- `fix_front_tabs.py`: removed front latch/hinge objects from saved models.
- `render_production.py`: GPU-only Cycles render settings and48frame loops.
- `render_shadows.py`: separate directional shadows.
- `integrate.py`: crop/pack/prototype export; currently STALE1.0.9 version/scale defaults.
- `package_and_fixture.py`: package/test fixture setup; STALE1.0.9 defaults and overwrites fixtures.
- `check_rigs.py`: transform-loop and animated-scale checks.
- `check_drive.py`:721position gear outline/symmetry checks.
- `build_review.py`, older reviewGIFs: historical outputs; do not regenerate final evidence blindly.
- `20|40|80|160|320/factory.blend`: current editable models; matching000–047production frames.

Capture hashes before and after a rebuild. A changed script does not update existing .blend files automatically, and editing .blend files does not update exported sheets automatically. Track each stage independently.

Windows gh appeared unauthenticated inside the restricted network sandbox but worked with the existing keyring outside it. Diagnose network/sandbox boundaries before replacing credentials. Never print/copy tokens into a public knowledge file. User permitted WSL-token assistance, but it was unnecessary; no token transfer was performed.

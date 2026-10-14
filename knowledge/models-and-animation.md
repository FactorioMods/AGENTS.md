# Models, design and mechanical animation

## Approved visual direction

Use vanilla assembler construction as the silhouette reference: a continuous protective box, chamfered outer outline, open top, and a raised internal processing deck. The machine has hidden machinery below the visible deck; the visible components must not appear laid on the lowest floor. Keep processing components inside the casing footprint. Tall rods can project upward, but preserve neighboring machine/inserter readability.

Use layered machined housings, collars, bolts where structurally appropriate, vents, pressure lines, gauges, bearings and meaningful mechanism density. The user rejected sparse CAD-like blockouts, unrelated futuristic shapes, empty interior space and undriven decorative moving parts. Do not fill space with disconnected gears. Avoid large door-like panels that imply a person enters the machine. Remove protruding front latch tabs and top/front hinge knuckles; the user also rejected excessive side-corner bolts.

Tier identity follows Matt's Logistics colors and planetary progression:

|Speed|Color|Mechanism/theme|Surface treatment|
|---|---|---|---|
|20|Green|Nauvis motor, connected gears, articulated rockers/piston|Most wear, restrained oxidation|
|40|Orange|Vulcanus guided metalworking press, hot solid billet|Industrial service grime|
|80|Purple|Fulgora placement heads, quills, tape feeders, circuit substrate|Cleaner precision metal|
|160|Blue|Aquilo cryogenic work bed and rotary tooling|Clean material, subtle dirt|
|320|White/graphite|Radial tools, contained violet process chamber|High-quality material, subtle dirt|

Only the last tier uses fictional dark matter. Not every tier needs fluids or a glowing liquid. Fluid-capable gameplay does not require a liquid interior in every design. All tiers should feel placed on a planet: localized grime and roughness variation, not uniformly spotless plastic or excessive rust.

## Rigging constraints learned through failed revisions

- Identify every moving and stationary part before rigging. User annotation: red articulated arms; grey piston sliders; lime vertical gear wheels; blue shaft stays stationary. Orange bearing supports/cables stay stationary. These identify intent, not exact engineering dimensions.
- Gears are vertical wheels rotating around horizontal axles. Use rigid 3D geometry and fixed axle centers; no image-plane spinning, resizing, wobble or changing radius.
- Show the motor, shaft, bearings and gear drive that explain movement. Meshing wheels rotate in opposite directions with angular speeds proportional to inverse tooth count. Maintain tooth phase/clearance; use separate axial planes when needed.
- Connect rods at actual pin centers with constant rod length. Shared rockers should follow the same shaft; independent parts require independent joints. Grey rods slide inside fixed bores with continuous engagement over the full stroke.
- Fixed cables must not deform or move just because they cross a moving object in the source image. Earlier masks captured cable pixels and created holes. Rebuilding with separate geometry avoids that class of failure.
- Remove the static original behind any replacement moving part. Duplicate background gears are a visible failure even if the overlay animates correctly.
- Loop closure must include tooth/face symmetry, not just object transforms. Do not claim a rigid-body physical simulation when using analytical kinematics.

The final green model used five supported involute gears in two axial planes. A private Shapely polygon check sampled 721 positions, with reported zero tooth intersection area and loop symmetry. This checks the sampled planar gear outlines, not arbitrary 3D collision or force behavior of the whole machine.

## Production rendering

Prepared local Blender: 5.2.2 portable, as inspected in this session. Use installed version/help; do not assume a release announcement guarantees a feature works. Working pipeline used Python/bpy and Cycles, not an unavailable game-dev CLI or a promised node-physics shortcut.

Final render settings: HIP GPU (RX 7900 XTX), CPU render device disabled, 96 samples, denoising, 512×512 transparent output, 48 frames, persistent data, four preparation threads. CPU work during scene preparation remains normal; GPU selection does not eliminate it.

Camera recorded in design-review.json: position `(0,-6,7.1)`, target `(0,0,.53)`, orthographic size3.85. This is project-specific and must be rechecked after geometry changes. Match vanilla lighting and directional shadows rather than studio-only beauty lighting. Shadows were rendered separately.

Preview full machine, close-ups, phase/contact sheet and actual in-game scale before expensive final renders. Confirm silhouettes, joints, fixed cables and loop seams. Show the real animations; a still or assertion that frames differ does not establish believable motion.

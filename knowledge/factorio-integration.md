# Factorio sprite and gameplay integration

Target used here: Factorio 2.0.77. Prefer installed `doc-html` and vanilla prototype Lua over online `latest` when they differ.

## Sprite export

1. Render all48frames from the same camera/anchor.
2. Downsample from512 to256 using a high-quality filter.
3. Compute a single union alpha bounding box across all frames; crop every frame identically. Per-frame auto-crops cause visible jitter.
4. Pack8columns×6rows, preserve transparency. Validate48frames and meaningful unique frames.
5. Derive sprite shift from the projected ground origin, not the rectangular canvas center. The camera target is above ground.
6. Give static and animated layers identical dimensions/scale/anchor where they overlap. Match separate shadow projection/scale to the body.

Current sheets: green206×222 per frame; other tiers206×205. Native animation uses48frames, line_length8, animation_speed.5. Current 1.0.10 body scale.44, with original shifts×.88. Static shadow frame repeats48times to match the animated layer. Preserve these corrections if rebuilding with `integrate.py`.

## Playback

`match_animation_speed_to_activity=true`; perceived_performance minimum0 maximum2 in current prototype. The engine drives motion. No runtime animation control.lua is needed. Working-light effects exist on40/160/320; do not call them a performance improvement.

Test actual crafting with sufficient inputs and empty outputs, starved slow supply, output blockage and full idle. A blocked machine with a selected recipe is not necessarily crafting. Verify sampled images, not just an object's animated flag. Previous animations were invisible or moved the wrong feature; static/active layers and matching clocks need inspection.

## Footprint and overlays

Keep selection_box±1.5tiles and collision_box±1.2tiles. Preserve four fluid-port coordinates and directions and existing entity IDs. Current body width206×.44=90.64px, below96px for three tiles; .50 was103px and visibly overlapped neighboring casings.

Current recipe overlay: `icon_draw_specification={scale=.6,shift={0,.65}}` on the base machine, inherited by tiers. It sits on the front apron. Existing module_info_icon_shift is `{0,.5}`; high module-count overlap still requires explicit visual verification, not an assumption that the recipe fix solved all overlays.

Test direct horizontal and vertical adjacency, mixed tiers, all orientations, Alt on/off, recipes with large/complex icons, quality markers, module rows, warnings and selection boxes. Maintain feeder readability on all sides. Screenshots must include nearby vanilla machines and ordinary loaders/inserters, not only isolated showroom spacing.

## Gameplay continuity

Current crafting speeds20/40/80/160/320, active normal-quality power375kW/750kW/1.5MW/3MW/6MW. Planet recipe gates are independent early milestones (foundry/tungsten-carbide, holmium processing, lithium processing, cryogenic plant). Do not replace starter recipes with late-game burdens during a graphical task. Check exact ingredients in current `prototypes/tiers.lua` rather than inferring from the art.

Base-game progression exists without Space Age. Higher tiers must not upgrade back to the first tier. Preserve compatibility with Miniloaders Redux and Matt's Logistics; functional input/output tests matter more than visual proximity.

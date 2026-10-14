# Releases and organization work

For a release, verify info.json, changelog, ZIP root/version, dependency compatibility, licensing/attribution and artifact hash. Pack only runtime assets. Preserve original authors and identifiers. A missing source repository does not mean the distributed mod has no license; inspect the ZIP/Portal before forking.

Use a fresh version for immutable published updates. Commit reviewed changes with the project co-author trailer. Push main/tag only after checks. `gh release create` rejected a short target SHA in this session; using the full commit SHA worked. Verify the resulting release and uploaded assets. Do not claim Portal publication because GitHub succeeded.

Mod Portal uses its own ZIP upload and final Submit flow. Wait for explicit 'Release published.' Then update description/screenshots and wait for 'Mod saved.' Capture website evidence. Browser upload may temporarily show Uploading or time out during navigation: inspect current state before repeating submission to avoid duplicates. New local ZIP installation is another separate step; compare hashes and verify enabled mod-list state. Both multiplayer peers must use matching versions and restart.

Descriptions should state native animation behavior and measured validation precisely. Do not claim FPS gains from model replacements, universal compatibility from a limited matrix, or multiplayer testing when only single-player fixtures ran. Do not publish stale preview GIFs as final assets.

## Other work from this conversation

The organization needed a public profile banner, description and avatar with one consistent Factorio industrial visual style. The initial default pink avatar and mismatched line artwork were rejected. GitHub organization profile content belongs in `.github/profile/README.md`; repository links and mod availability should be maintained there. Local `optimization-work/org-profile` contains a profile snapshot with a banner asset link and Magic Science Chest/Pollution Absorber sections; do not assume it is the latest remote state or that assemblers are already listed.

Magic Science Chest: Improved source is https://github.com/FactorioMods/factorio-mod-magic-science-chest-improved and Portal slug `magic-science-chest-optimized`. Local snapshot description reports preservation of native refill and an endgame comparison with2,509chests/5,011biolabs and2,771,479combined science packs over3,000ticks. Treat these as historical snapshot claims, not fresh validation or current release status. Inspect its own current code before changing refill/GUI/cache behavior.

Website references from the early chat did not identify a separate current website codebase beyond GitHub/Mod Portal. Do not invent deployment details. This new knowledge repository is explicitly requested public project context; prior private model/test sources remain excluded unless separately authorized for publication.

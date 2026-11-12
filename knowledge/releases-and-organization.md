# Releases and organization work

For a release, verify info.json, changelog, ZIP root/version, dependency compatibility, licensing/attribution and artifact hash. Pack only runtime assets. Preserve original authors and identifiers. A missing source repository does not mean the distributed mod has no license; inspect the ZIP/Portal before forking.

Use a fresh version for immutable published updates. Commit reviewed changes with the project co-author trailer. Push main/tag only after checks. `gh release create` rejected a short target SHA in this session; using the full commit SHA worked. Verify the resulting release and uploaded assets. Do not claim Portal publication because GitHub succeeded.

Mod Portal uses its own ZIP upload and final Submit flow. Wait for explicit 'Release published.' Then update description/screenshots and wait for 'Mod saved.' Capture website evidence. Browser upload may temporarily show Uploading or time out during navigation: inspect current state before repeating submission to avoid duplicates. New local ZIP installation is another separate step; compare hashes and verify enabled mod-list state. Both multiplayer peers must use matching versions and restart.

Descriptions should state native animation behavior and measured validation precisely. Do not claim FPS gains from model replacements, universal compatibility from a limited matrix, or multiplayer testing when only single-player fixtures ran. Do not publish stale preview GIFs as final assets.

## Other work from this conversation

The organization needed a public profile banner, description and avatar with one consistent Factorio industrial visual style. The initial default pink avatar and mismatched line artwork were rejected. GitHub organization profile content belongs in `.github/profile/README.md`; repository links and mod availability should be maintained there. Local `optimization-work/org-profile` contains a profile snapshot with a banner asset link and Magic Science Chest/Pollution Absorber sections; do not assume it is the latest remote state or that assemblers are already listed.

Magic Science Chest: Improved source is https://github.com/FactorioMods/factorio-mod-magic-science-chest-improved and Portal slug `magic-science-chest-optimized`. Local snapshot description reports preservation of native refill and an endgame comparison with2,509chests/5,011biolabs and2,771,479combined science packs over3,000ticks. Treat these as historical snapshot claims, not fresh validation or current release status. Inspect its own current code before changing refill/GUI/cache behavior.

Website references from the early chat did not identify a separate current website codebase beyond GitHub/Mod Portal. Do not invent deployment details. This new knowledge repository is explicitly requested public project context; prior private model/test sources remain excluded unless separately authorized for publication.


## Changelog parsing and authorized history rewrites

Factorio 2.1.23 requires exactly 99 separator dashes immediately followed by Version:, unique version numbers, correct category/entry indentation, and no duplicate date within a block. The installed auxiliary/changelog-format.html is the matching reference. Upstream history copied beneath a fork can collide with new 1.0.x versions or omit separators. Keep such original text in docs/UPSTREAM-CHANGELOG.txt and use only valid fork blocks in the in-game root changelog. Fold documentation and changelog corrections into the owning implementation and verify gameplay-file identity. Documentation alone does not justify a new runtime version. Preserve immutable published ZIPs.

The 2026-10-24 history cleanup used verified bundles/mirrors, exact tree and identity checks, unchanged upstream objects, and atomic leased pushes. All old uploaded assets stayed unchanged. Canonical commit IDs changed; mappings/backups remain private under public-cleanup. Restoration must audit newer work and protect it with fresh exact-ref leases. Windows local file lookup is case-insensitive; GitHub Contents paths are not. Matt repositories track readme.md. Normalize CRLF/LF when verifying browser form text and Git blobs.

Preserve original upstream Git commit IDs and authorship with our changes on top wherever recoverable. Avoid snapshot-only forks. For monorepos, preserve the original commit as parent of a clearly identified extraction commit. Use real matching-release ancestry, not unrelated repositories or synthetic author identities. Missing/deleted upstream repositories are explicit exceptions pending recovery. Verified private ancestry records preserve the earlier-to-current commit mappings.

Public descriptions: keep product descriptions about actual features, settings and relevant compatibility limits. Never include local save/world names, fixture/debugging history, private test counts, naming churn, or statements about unmade performance improvements. Keep validation in a concise separate guide. Preserve original mod naming and change only its suffix. Use patch increments for automatic player updates; lower renumbering does not update users already on higher versions.

## Complete Git objects before publication

A valid current tree and release archive can coexist with missing historical objects in a non-shallow partial clone. Before pushing, disable lazy fetching for the inspection and run `git rev-list --objects --missing=print HEAD`, then a full `git fsck`. Inspect the complete reachable history rather than only the current package tree.

A release checkout with 322 missing historical objects was repaired from its pinned authentic upstream using a bounded fetch with `--refetch --no-filter --no-tags --no-write-fetch-head --refmap=`. Verification retained the exact HEAD, tree, index, refs, configuration, archive and publication plan, then found zero missing HEAD-reachable objects and passed full fsck across the remaining publication checkouts. The subsequent guarded atomic HEAD/current-tag push completed with exact remote readback. Fetch scope must match the authorized upstream and cache repair; preserve source history and publication identities.

After a failed or interrupted write, inspect remote refs and release state before another attempt. Resume completed rows through readback and continue only the remaining planned writes.

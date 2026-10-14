# Isolated tests and evidence

Use separate config, write-data, mod-directory and copied save. Fresh runtime paths prevent collision with earlier tests. Never remove a live lock or kill the player's main game to make a test start.

Example PowerShell, after adapting paths:

```powershell
$testRoot = Join-Path $env:APPDATA 'Factorio/optimization-work/my-isolated-check'
# config.ini must set read-data to the installation/data and write-data to this test's runtime.
$testArgs = @('--config', "$testRoot/config.ini", '--mod-directory', "$testRoot/mods",
  '--benchmark-graphics', "$testRoot/copied-save.zip", '--benchmark-ticks', '720', '--disable-audio')
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

1.0.9 recorded45loader combinations,20fluid cases,4milestones,40retained machines. Native frame comparisons:31unique active frames;2–3 low-load frames;1idle frame. This is evidence of state-sensitive playback, not measured UPS improvement.

1.0.10 only reran a200tick layout scene with all tiers side-by-side and Alt recipe icons; it did not repeat the entire functional/multiplayer suite. Public evidence here is sanitized; raw local logs can expose Steam IDs and save information.

# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Published Plugin v0.4.0

- GitHub Release: `plugin-v0.4.0`.
- Release title: `Engineering Governance Plugin v0.4.0`.
- Package version: `0.4.0`.
- Exact release/source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Asset: `engineering-governance-plugin.zip`.
- Asset size: `54754` bytes.
- Asset SHA-256 / GitHub digest: `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`.

## Accepted reusable capability baseline

Plugin v0.4.0 contains exactly three top-level Skills:

- `project-governance`
- `domain-navigation`
- `incident-doctor`

Accepted behavior:

1. Project Governance is the normal engineering entry and scales down for simple low-risk work.
2. Domain Navigation is conditional when semantic/source/authority routing is unclear.
3. Incident Doctor is reactive only for blocking problems with insufficient evidence.
4. Global routing adoption is managed and idempotent.
5. Worktree lifecycle and verification effort are bounded and risk-proportional.

## Mac mini source/install/runtime state

- Canonical source checkout: `/Volumes/Jack-Dev/Projects/Engineering-Governance`.
- Source checkout is `main`, clean, and matched fresh `origin/main` at control head `36c6392323a55df246202561d8aa3962e8f607a4` for the activation task.
- Previous mini-internal source checkout has been retired; its unique historical ZIP was archived separately with matching SHA-256.
- Installed plugin source path: `/Users/ox_miles/.codex/plugins/engineering-governance`.
- Installed plugin version: `0.4.0`.
- Previous `0.3.0` installation backup remains preserved and verified.
- Sole enabled registration: `engineering-governance-personal / engineering-governance`.
- Active runtime cache path: `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.4.0`.
- Active runtime version: `0.4.0`.
- Enabled registration count: `1`.
- Enabled `0.3.0` registration remaining: `NO`.
- Global managed routing block count: `1`.
- Unrelated global rules preserved.
- Runtime acceptance passed for default Project Governance, conditional Domain Navigation, and reactive-only Incident Doctor.

## Task 044 resolution

Task `EG-PLUGIN-V0.4.0-RUNTIME-CACHE-ACTIVATION-044` is complete.

The prior stale-cache observation was not reproducible in the fresh authoritative run: before any refresh, the sole enabled registration, cache, and current runtime already resolved to `0.4.0`; the previously recorded `0.3.0` cache path was absent. No refresh, reinstall, cache deletion, or client restart was required.

No source, Plugin payload, global routing, unrelated plugin, or business-project mutation occurred.

## Current posture

```text
SOURCE_AUTHORITY=JACK_DEV
PUBLISHED_PLUGIN_VERSION=0.4.0
INSTALLED_PLUGIN_SOURCE_VERSION=0.4.0
ACTIVE_RUNTIME_CACHE_VERSION=0.4.0
ENABLED_REGISTRATION_COUNT=1
ENABLED_0_3_REGISTRATION=NO
GLOBAL_ROUTING_BLOCK_COUNT=1
ROUTING_ACCEPTANCE=PASS
PLUGIN_V0_4_RUNTIME_ACTIVATION=PASS
SOURCE_FIX_REQUIRED=NO
RUNTIME_CACHE_REFRESH_REQUIRED=NO
```

## Next milestone

No Engineering-Governance corrective is currently required. Return to normal project work; only reopen plugin/runtime diagnosis if a concrete routing or activation failure recurs.

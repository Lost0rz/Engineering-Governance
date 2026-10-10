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
- Installed plugin source path: `/Users/ox_miles/.codex/plugins/engineering-governance`.
- Installed plugin/runtime version: `0.4.0`.
- Sole enabled registration: `engineering-governance-personal / engineering-governance`.
- Active runtime cache version: `0.4.0`.
- Global managed routing block count: `1`.
- Runtime acceptance passed for default Project Governance, conditional Domain Navigation, and reactive-only Incident Doctor.

## Task 044 resolution

Task `EG-PLUGIN-V0.4.0-RUNTIME-CACHE-ACTIVATION-044` is complete with `EG_PLUGIN_V040_RUNTIME_ACTIVATION_PASS`.

## New owner-approved rule direction

The next reusable Project Governance rule must keep development storage aligned with the canonical project's actual storage location instead of hard-coding a machine or external volume.

Required semantics:

- resolve the canonical project root first;
- project-controlled development assets follow the storage location of that canonical project root;
- if the canonical project is on external storage, project-controlled worktrees, durable diagnostics, archives, task staging, and other durable development state should remain on that same storage authority;
- if the canonical project is on local host storage, those project-controlled assets remain local unless the project explicitly declares an exception;
- do not create durable project state in unrelated locations such as `/private/tmp`, `/tmp`, Desktop, Downloads, or arbitrary home-directory paths merely for convenience;
- OS/tool-required ephemeral scratch may use system temporary locations, but unique/durable project state must not remain there;
- machine/runtime state such as CI runners, LaunchAgents, package-manager/runtime services, host caches, and other host-operational state remains machine-local unless the project explicitly owns it as portable data;
- project-specific explicit path rules override the derived same-storage default;
- no universal `/Volumes/Jack-Dev` rule is allowed.

This rule belongs in Project Governance/workspace guidance, not as duplicated procedure inside the global routing block.

## Current posture

```text
SOURCE_AUTHORITY=JACK_DEV
PUBLISHED_PLUGIN_VERSION=0.4.0
INSTALLED_PLUGIN_VERSION=0.4.0
PLUGIN_RUNTIME_VERSION=0.4.0
GLOBAL_ROUTING_BLOCK_COUNT=1
STORAGE_AFFINITY_RULE=NOT_YET_IMPLEMENTED
HARD_CODED_JACK_DEV_GLOBAL_RULE=FORBIDDEN
NEW_TOP_LEVEL_SKILL_REQUIRED=NO
GLOBAL_ROUTING_REWRITE_REQUIRED=NO
NEXT_ACTION=IMPLEMENT_PROJECT_STORAGE_AFFINITY_RULE
```

## Next milestone

Implement and verify the bounded Project Governance storage-affinity rule in reusable source, with the smallest coherent documentation/Skill diff and no unrelated release, runtime, or business-project changes. After independent audit, decide release/version/install follow-up separately.

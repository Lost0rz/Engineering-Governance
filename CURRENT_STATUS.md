# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Published Plugin v0.4.0

- GitHub Release: `plugin-v0.4.0`.
- Release title: `Engineering Governance Plugin v0.4.0`.
- Package version: `0.4.0`.
- Exact release/source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Tag `refs/tags/plugin-v0.4.0` resolves directly to that exact commit.
- Release state: published, `draft=false`, `prerelease=false`.
- Asset: `engineering-governance-plugin.zip`.
- Asset size: `54754` bytes.
- Asset SHA-256 / GitHub digest: `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`.
- Package entries: `44`.
- Publisher workflow run: `37916223246`, conclusion `success`.

## Accepted reusable capability baseline

Plugin v0.4.0 contains exactly three top-level Skills:

- `project-governance`
- `domain-navigation`
- `incident-doctor`

Accepted capabilities include:

1. managed global Skill routing and idempotent global `AGENTS.md` adoption/upgrade;
2. Project Governance as the normal project/repository engineering entry while simple low-risk work remains lightweight;
3. Domain Navigation as conditional semantic/source routing that reuses accepted maps;
4. Incident Doctor as reactive evidence-gated investigation only;
5. construction-time responsibility/Domain/authority-based code structure independent of line count or edit size;
6. one canonical authority per fact/state/behavior class and explicit migration boundaries for temporary coexistence;
7. bounded worktree lifecycle checkpoints during normal development, with full legacy archaeology reserved for accumulated historical debt;
8. control identity semantics that distinguish provenance/current/explicit locked heads;
9. `V0`–`V3` risk/scope tiers with separate construction/corrective/task/merge-release verification cadence.

## Mac mini source/install state

- Canonical source checkout: `/Volumes/Jack-Dev/Projects/Engineering-Governance`.
- Source checkout is `main`, clean, and matched `origin/main` at `221bcd597e1b45aceae73bf1088792ca6df6cfb4` at the latest local receipt.
- The previous mini-internal source checkout was retired after its only unique untracked ZIP was archived with matching SHA-256.
- Installed plugin source path `/Users/ox_miles/.codex/plugins/engineering-governance` now reports version `0.4.0` with the three accepted Skills.
- Previous `0.3.0` install was backed up and hash-verified.
- The official v0.4.0 release asset identity was verified before local installation.
- Global managed routing block count is exactly `1`; unrelated global rules were preserved; repeated adoption was idempotent.
- Read-only routing acceptance passed for default Project Governance, conditional Domain Navigation, reactive-only Incident Doctor, and bounded worktree lifecycle behavior.

## Remaining activation blocker

The sole enabled Codex registration still resolves to a stale runtime cache entry:

`/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.3.0/plugin.json`

Therefore local filesystem installation is v0.4.0, but runtime activation of v0.4.0 is not yet proven.

Current evidence supports a registration/cache refresh boundary, not a source or routing-content defect. Do not modify Plugin source or global routing to address this symptom.

OpenAI plugin documentation states that installed marketplace plugins are loaded from the Codex plugin cache and that marketplace/local-plugin updates require refresh/reinstall plus client restart/activation before the new cached copy is used.

## Current posture

```text
SOURCE_AUTHORITY=JACK_DEV
SOURCE_MAIN_MATCH_ORIGIN=YES
PUBLISHED_PLUGIN_VERSION=0.4.0
INSTALLED_PLUGIN_SOURCE_VERSION=0.4.0
GLOBAL_ROUTING_BLOCK_COUNT=1
GLOBAL_ROUTING_IDEMPOTENT=YES
ROUTING_ACCEPTANCE=PASS
ENABLED_RUNTIME_CACHE_VERSION=0.3.0
PLUGIN_V0_4_RUNTIME_ACTIVATION=UNVERIFIED
SOURCE_FIX_REQUIRED=NO
ROUTING_REWRITE_REQUIRED=NO
NEXT_ACTION=REFRESH_REGISTERED_PLUGIN_RUNTIME_CACHE
```

## Next milestone

Refresh the existing Engineering Governance plugin registration/runtime cache through supported plugin/marketplace mechanisms, preserve the verified v0.4.0 installed payload and global routing block, then prove the enabled runtime resolves to v0.4.0. If client restart is required, record that boundary explicitly rather than deleting caches speculatively.

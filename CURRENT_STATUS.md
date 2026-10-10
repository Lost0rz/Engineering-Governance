# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Published Plugin baseline

- Latest published Release: `plugin-v0.4.0`.
- Exact published source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Published package version: `0.4.0`.
- Published asset: `engineering-governance-plugin.zip`.
- Published asset SHA-256: `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`.
- Current `main` Plugin payload still matches the published v0.4.0 payload; intervening main commits before this integration task were control-only.

## Accepted reusable architecture

Exactly three top-level Skills remain authoritative:

- `project-governance`
- `domain-navigation`
- `incident-doctor`

Global routing remains selection-only. No fourth Router Skill, storage Skill, Findings Skill, daemon, database, installer, or automatic remediation runtime is accepted.

## Audited pending reusable inputs

### v0.5 Navigation Refresh + Follow-ups

- Frozen accepted reusable candidate A2: `ecadcf67bf00a5a82cd644cd822ad4d45a76a420`.
- Branch: `codex/navigation-learning-followups-v0.5.0-implementation`.
- Detailed Web source re-audit: PASS; Critical `0`, Important `0` at A2.
- A2 has remained reusable-frozen; later branch commits are control-only.
- This branch predates current main and must be reconciled, not merged blindly.

### Project Storage Affinity

- Reusable implementation head: `c250b9b081a93949f1d000165e64dcaa53610bdb`.
- Branch: `codex/project-storage-affinity-v1`.
- Source/contract audit: PASS.
- Later branch commits are control-only.
- Rule: durable project-controlled development state follows the canonical project's storage authority by default, with explicit project-local override and separate machine/runtime + ephemeral-scratch classes.

## Integration finding

The two accepted reusable lines overlap at least in:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/development-flow.md`

Therefore neither old branch is the final release source. A new integrated candidate must be constructed from fresh `main`, preserve both semantics, and be audited as a new exact source identity.

## Engineering-Governance repository-specific execution split

For this repository only:

- Web/remote owns reusable source construction, remote GitHub mutation, integration, source audit, and release preparation.
- Local AI is used primarily for actual installed/runtime/behavior validation.
- A reusable defect found locally returns to Web/remote construction for correction before validation resumes.
- Other repositories keep their own accepted execution model; this rule is not global routing policy.

Root `AGENTS.md` still needs this repository-specific durable rule reconciled during integration.

## Remote lifecycle state

The repository currently has many historical non-main branches and zero open PRs. Several are known merged-PR or completed publisher branches and therefore terminal lifecycle debt. Some branches may retain unique historical evidence and must be classified before deletion.

Lifecycle cleanup will occur only after the integrated v0.5 candidate is audited and merged to `main`.

## Active task

Task: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`.

State: `AUTHORIZED_REMOTE_INTEGRATION`.

Mode: `INTEGRATE_AUDIT_MERGE_THEN_LIFECYCLE_CLOSEOUT`.

Planned integration branch:

`codex/v0.5-storage-affinity-integration-v1`

## Current posture

```text
PUBLISHED_PLUGIN_VERSION=0.4.0
CURRENT_MAIN_PAYLOAD=V0.4.0_EQUIVALENT_BEFORE_INTEGRATION
V0.5_A2_SOURCE_AUDIT=PASS
STORAGE_AFFINITY_SOURCE_AUDIT=PASS
INTEGRATED_V0.5_CANDIDATE=NOT_YET_CREATED
LOCAL_V1_AUTHORIZED=NO
V0.5_RELEASE_AUTHORIZED=NO
OLD_BRANCH_CLEANUP=AFTER_INTEGRATED_MERGE
NEXT_ACTION=BUILD_AND_AUDIT_ONE_INTEGRATED_V0.5_CANDIDATE
```

## Next milestone

Create the integrated v0.5 candidate from fresh main, reconcile overlapping Project Governance files and the repository-specific execution rule, audit the exact integrated source, merge it to `main`, then close terminal historical branches until `main` is the sole active development authority (plus only explicitly justified retained historical branches, if any). Only after that clean baseline may local installation/runtime behavior testing begin.

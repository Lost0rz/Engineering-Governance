# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

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
- Publisher checked out exact source `204f74952ce53fb97180e42f537fdf3236d1c48e`, verified package version `0.4.0`, exactly three top-level Skills, required routing/adoption/structure/workspace files, final no-edit-size-bypass wording, and normal-development lifecycle checkpoints before packaging.
- ZIP validation passed: one `engineering-governance/` root; only `plugin.json` and `skills/**`; no root controls, `.github`, docs, examples, root references, symlinks, or publisher transport files.
- GitHub Release asset size/digest exactly matches publisher evidence.
- Tagged source contains no `.github` publisher workflow.

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

## Release verification

- Governance/routing PR #14 merged from exact head `3b969e45230923629d23bb0d1a432c1740b4ae3b` to merge commit `879521028a056a9fed4ce6fb9be89a6221eb80bf`; comparison showed zero file differences.
- Final audited reusable payload was sealed at `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`; subsequent PR #14 changes were control-only.
- Release-source PR #15 merged control-only release authorization; final release source `204f74952ce53fb97180e42f537fdf3236d1c48e` differs from the accepted v0.4.0 merged source only in `CURRENT_STATUS.md` and `CURRENT_TASK.md`.
- Release/tag identity was verified unused before publication.
- All publisher steps passed: identity preflight, exact-source checkout, package verification, release-note construction, exact release publication.
- Publisher transport branch is not the Release target and is not part of `main`, the tag, or the ZIP.

## Current task

- Task: `EG-PLUGIN-V0.4.0-RELEASE-043`.
- State: `CLOSED`.
- Outcome: `RELEASED_VERIFIED`.
- No local workspace-cleanliness or local installation claim is made by this remote-only release task.

## Next milestone

Synchronize the local Engineering Governance source/install state to published Plugin v0.4.0, reinstall/upgrade the Plugin and its managed global routing block under the installation completion contract, verify idempotency and preservation of unrelated global rules, then run real routing acceptance against representative development scenarios before broader project rollout.

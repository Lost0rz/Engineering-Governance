# CURRENT TASK — Final PR Head Freeze Rule

Task ID: `EG-FINAL-PR-HEAD-FREEZE-052`

State: `ACTIVE`

Date: 2026-10-12

Repository: `Lost0rz/Engineering-Governance`

## Objective

Prevent exact-head verification from creating a self-triggering loop where CI or independent-audit results are written back as control-file commits, thereby changing the PR HEAD and requiring another exact-head CI run.

## Evidence

A live Gift lifecycle closeout demonstrated the failure mode:

`final PR head → exact-head CI PASS → controls-only evidence commit → new PR head → another exact-head CI`.

The reusable governance contract currently binds evidence to identities and requires exact-head evidence at merge/release boundaries, but it does not explicitly freeze the final PR head or prohibit control churn that exists only to record external verification results.

## Authorized scope

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/references/control-plane.md`
- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

No new Skill, runtime, daemon, storage subsystem, CI mechanism, or enforcement tool is authorized.

## Required rule

Before exact-head CI / independent audit at a merge boundary, complete source and control changes and designate the current PR head as the frozen candidate.

After freeze:

- CI, review, audit, mergeability, and other repository-host evidence are live external evidence for that immutable head;
- do not create a source/control commit solely to record that those checks passed or failed;
- if evidence requires an actual source/control correction, explicitly unfreeze, make the correction, and begin a new exact-head cycle on the new head;
- if evidence passes, audit and merge the same frozen head;
- post-merge CI may verify the merge commit, but its result must not cause another commit solely to record the result.

## Verification

Risk tier: `V0/V1 process-contract change`.

Verify the reusable wording is consistent across Project Governance, control-plane ownership, and verification cadence. The rule must preserve legitimate control updates before freeze and after material scope/authorization changes while prohibiting evidence-only head churn after freeze.

## Stop conditions

- The change would require a fourth Skill or runtime enforcement mechanism.
- The rule would prevent a necessary source/control correction after failed audit evidence.
- The rule would weaken exact-head identity binding.

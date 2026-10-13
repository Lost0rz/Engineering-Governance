# CURRENT TASK — Engineering Governance Plugin v0.5.5 Release and Web Update

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.5-RELEASE-WEB-059`

State: `ACTIVE_RELEASE_PREPARATION`

Mode: bounded Plugin distribution and release

## Objective

Publish the already accepted Task 058 governance source as formal Plugin version `0.5.5`, then update the existing ChatGPT Web Plugin to the same `0.5.5` payload while preserving Plugin identity, scope, audience, and exactly three top-level Skills.

## Planning context

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Document section / work package: accepted v0.5.5 design and release boundary
- Document revision basis: accepted repository source at `58f06da1d4e5d0e86d2cb17bd13aa786d7a22cc6`; subsequent `6dbf83ea24b0322669bb384b9ed7c78474dcb860` is control-only closeout.
- Relationship to plan: this task distributes the accepted design; it does not change governance semantics.

## Start baseline

- Literal `main`: `6dbf83ea24b0322669bb384b9ed7c78474dcb860`.
- Accepted source merge: `58f06da1d4e5d0e86d2cb17bd13aa786d7a22cc6`.
- Independently audited semantic source: `eed269cab32ecdfb52da87627386bcc77a9e42c6`.
- Current portable Plugin version: `0.5.4`.
- Current formal release: `plugin-v0.5.4`.
- Current ChatGPT Web Plugin: `0.5.4`.
- `plugin-v0.5.5` tag and release were verified absent before mutation.
- Task branch: `codex/plugin-v0.5.5-release-web`.

## In scope

1. Bump root `plugin.json` from `0.5.4` to `0.5.5` only.
2. Add one-shot formal release workflow for `plugin-v0.5.5`.
3. Verify the exact release package contains only `plugin.json` and `skills/**`, exactly three top-level Skills, and the accepted v0.5.5 planning/control-alignment semantics.
4. Merge release preparation to `main` after source audit and live host gates pass.
5. Verify formal tag, GitHub Release, asset digest/size/file count, and publication source.
6. Update the existing ChatGPT Web Plugin to version `0.5.5` using the released/accepted payload while preserving existing Plugin ID, USER/PRIVATE scope/audience, and three-Skill boundary.

## Out of scope

- Mac mini or MacBook Air Plugin convergence.
- Any governance semantic/source correction.
- New Skill, runtime, daemon, service, database, installer, or automatic remediation.
- Moving or replacing historical release tags.

## Verification contract

`V0/V1 distribution verification`:

- manifest name/version exact;
- exactly three top-level Skills;
- package boundary only `plugin.json` and `skills/**`;
- package file-entry count derived from current source, expected `30`;
- required v0.5.5 semantics include durable planning linkage, mandatory Control Alignment Gate, `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and separate repository-host gate boundary;
- release tag is immutable and points to the frozen publication source;
- Web Plugin update retains the same backend Plugin identity and private audience.

## Stop conditions

- Stop if `main` gains non-control delivery changes before merge.
- Stop if `plugin-v0.5.5` tag/release appears unexpectedly.
- Stop if package contents escape `plugin.json` + `skills/**`, top-level Skill count differs from three, or required semantics are absent.
- Stop if the existing Web Plugin identity/scope/audience cannot be preserved.
- Do not update Mini/Air under this task phase.

## Required order

1. Formal GitHub release `plugin-v0.5.5`.
2. ChatGPT Web Plugin update to `0.5.5`.
3. Control Alignment Gate and receipt.

## Handoff / current stop point

Task authorized. Release preparation may begin on `codex/plugin-v0.5.5-release-web`.

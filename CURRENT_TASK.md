# CURRENT TASK — Plugin v0.6.6 Release

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V066-RELEASE-078`

Task class: `RELEASE`

State: `ACTIVE`

## Objective

Publish the accepted Web candidate as formal GitHub Plugin release `plugin-v0.6.6`, then hand off the immutable release identity and local update commands for Local Codex acceptance.

## Release candidate

- PR: `#26`
- branch: `codex/capability-model-v0.6.0`
- current Web Plugin version: `0.6.6`
- current Web release: `pluginrel_6acf45f2c8208191937f142f6c7198a8`
- current Delivery / Semantic candidate: `edf20c44a5ec32b49d2494b7a1c9511af8ca32cd`
- exact eight top-level Skills are the v0.6.x capability model.

## Accepted prerequisite

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is closed for the Web boundary:

- Project Profile regressions PASS across Gift, Merloom, MemoX and FloatTabs;
- previously established Web routing/discovery behavior remains valid and later Profile-only correctives did not change non-Profile routing Skills;
- no material Web blocker remains for publication.

This does **not** claim full cross-environment integrated acceptance. Local Codex acceptance follows installation from the formal release asset.

## Authorized mutation

1. add a dedicated `0.6.6` release workflow on this branch;
2. verify release workflow/package scope and current PR host state;
3. update PR release evidence;
4. make PR #26 ready and merge only if release-readiness evidence is PASS;
5. verify the main-triggered release workflow, immutable tag, GitHub Release asset and package provenance;
6. reconcile `CURRENT_STATUS.md` / `CURRENT_TASK.md` after publication.

## Release contract

The GitHub release asset contains only:

- `plugin.json`;
- `skills/**`.

It must report version `0.6.6`, contain exactly the eight accepted top-level Skills, and publish as:

`plugin-v0.6.6`

with asset:

`engineering-governance-plugin.zip`

## Stop conditions

STOP before merge/release if:

- PR #26 is no longer mergeable or main moved unexpectedly;
- manifest/version/Skill set differs from the accepted candidate;
- package workflow would include repository controls/docs/workflows in the Plugin ZIP;
- required release provenance cannot be established;
- another material source defect appears.

## Post-release boundary

After formal publication, Local Codex is updated from the immutable `plugin-v0.6.6` release asset and receives the remaining local integrated acceptance. Full integrated acceptance is not claimed until that succeeds.

Control Alignment:

- `RELATED_DOCUMENT`: `references/V060_INTEGRATED_ACCEPTANCE.md`
- `WEB_ACCEPTANCE`: `PASS`
- `LOCAL_ACCEPTANCE`: `PENDING_POST_RELEASE_UPDATE`
- `CONTROL_ALIGNMENT`: `PASS`

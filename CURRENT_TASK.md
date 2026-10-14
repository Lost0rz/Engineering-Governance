# CURRENT TASK — Plugin v0.6.6 Release

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V066-RELEASE-078`

Task class: `RELEASE`

State: `WAITING_LOCAL_ACCEPTANCE`

## Objective

Publish the accepted Web candidate as formal GitHub Plugin release `plugin-v0.6.6`, then converge Local Codex onto that released Plugin and complete the remaining local integrated acceptance.

## Published release

- PR #26: `MERGED`;
- merge/release source SHA: `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`;
- release workflow run: `38549662373` — `success`;
- tag: `plugin-v0.6.6` -> release source SHA;
- release asset: `engineering-governance-plugin.zip`;
- size: `90618` bytes;
- SHA-256: `433831130c2f85358ba75c4f07ef5063318a8ef00b255a8fa5966b2e7f16b93b`;
- package entries: `47`;
- package scope: `plugin.json` + `skills/**` only;
- package version: `0.6.6`;
- top-level Skills: exactly `8`.

## Accepted Web prerequisite

Web candidate acceptance is PASS for the release boundary, including Gift, Merloom, MemoX and FloatTabs Project Profile regressions.

Full Web+Local integrated acceptance is not yet claimed.

## Remaining authorized work

Local Codex only:

1. refresh the configured `engineering-governance-personal` marketplace from repository `main`;
2. update/refresh the installed `engineering-governance` Plugin to `0.6.6` through the supported plugin/marketplace mechanism; do not manually patch active cache/source files;
3. verify one active canonical Plugin authority, version `0.6.6`, and exactly eight top-level Skills;
4. verify the current Engineering Governance routing surface is singular/current where the local environment uses authoritative global guidance;
5. exercise bounded routing/continuation/profile/handoff evidence needed by `references/V060_INTEGRATED_ACCEPTANCE.md` for the Local surface;
6. return the local receipt for Web audit and final Control Alignment.

## Local update source

Marketplace:

`engineering-governance-personal`

Repository source:

`https://github.com/Lost0rz/Engineering-Governance.git`

Repository ref:

`main`

Formal release identity:

`plugin-v0.6.6`

## Stop conditions

STOP local acceptance if:

- marketplace refresh does not resolve repository `main` containing `plugin-v0.6.6` source;
- installed Plugin does not report `0.6.6`;
- more than one active Engineering Governance Plugin authority exists;
- the installed Plugin does not expose exactly the eight accepted Skills;
- local update requires manual mutation of active Plugin cache/source rather than the supported marketplace/plugin mechanism;
- authoritative global routing contains conflicting/duplicate managed regions that cannot be safely reconciled;
- a material reusable defect appears.

## Terminal boundary

Task 078 closes only after the formal release provenance is accepted **and** Local Codex `0.6.6` acceptance succeeds. Any reusable local defect returns to Engineering-Governance source through a separately authorized corrective before final integrated PASS.

Control Alignment:

- `RELATED_DOCUMENT`: `references/V060_INTEGRATED_ACCEPTANCE.md`
- `WEB_ACCEPTANCE`: `PASS`
- `FORMAL_RELEASE`: `PASS`
- `LOCAL_ACCEPTANCE`: `PENDING`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`

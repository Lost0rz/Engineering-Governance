# CURRENT TASK — Web Candidate Acceptance v0.6.x

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `VERIFY`

State: `WAITING_FRESH_WEB_SESSION`

## Objective

Validate the corrected installed Engineering Governance Plugin across fresh Web discovery/routing/Profile behavior before formal GitHub release or PR merge, using bounded source correctives only when real reusable defects are exposed.

## Corrective history / current source identity

Completed acceptance-driven correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff request/receipt templates aligned with the accepted Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile output contract hardened so Profiles remain compact landing indexes and do not duplicate generic Engineering Governance procedure.

Current corrected Delivery / Semantic candidate:

`ca64841b141888675c2670eeaf4c6cbccb8a5395`

This is Task 072 semantic source `e08c77aa...` plus the package-version alignment `plugin.json: 0.6.0 -> 0.6.1`; no Skill behavior changed after the focused Task 072 audit.

## Web candidate evidence

- existing personal Plugin identity preserved: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- prior Web candidate `0.6.0` was refreshed through the guarded Plugin update path;
- current Web candidate version: `0.6.1`;
- current Web release: `pluginrel_6acf006fb68c81918d269b6ee46719e6`;
- scope/discoverability remain `USER / PRIVATE`;
- platform-managed `.codex-plugin/plugin.json` and root `plugin.json` both report `0.6.1`;
- only the manifest and three `project-profile` shipped files were overlaid for the Task 072 regression candidate;
- installed `project-profile` Skill, template and contract contain the Task 072 compression/dedup rules.

The source manifest has now been aligned to `0.6.1`; formal GitHub v0.6.1 release/tag is still not created.

## Web acceptance evidence already established

- fresh Web session discovers the exact eight top-level Skills: PASS;
- ordinary project status/progress inspection -> `project-governance`: PASS;
- advisory inspection did not over-route to Evidence Audit / Domain Navigation / Incident Doctor: PASS;
- Project Profile request reached the Project Profile capability and excluded live PR/HEAD/CI/current-task content: PASS for routing/authority/freshness boundary;
- first Project Profile output duplicated reusable routing/handoff/verification/incident/artifact procedure and was too long: reusable finding corrected by Task 072.

## Remaining Web boundary

Open a fresh Web conversation/session against current candidate `0.6.1`, then rerun the same Engineering-Governance Project Profile generation case and remaining routing positive/negative scenarios from `references/V060_INTEGRATED_ACCEPTANCE.md`.

Project Profile retest must establish:

- explicit known Profile surface + PRIMARY/MIRROR/single-surface role;
- template-first compact output;
- stable project-specific facts/pointers retained;
- live STATUS/TASK/PR/CI content excluded;
- reusable routing/Handoff/verification/Doctor/artifact/control procedure not duplicated;
- no extra top-level procedure sections unless genuinely project-specific.

## Out of scope

- formal immutable GitHub `plugin-v0.6.1` release/tag;
- PR #26 merge;
- Local Codex / Mac mini / MacBook Air acceptance until Web surface is ready;
- patching installed caches as source authority;
- further source architecture expansion without a new real acceptance finding.

## Stop conditions

Stop before formal release/merge/local acceptance if a fresh Web session does not observe the corrected 0.6.1 Project Profile behavior, eight-Skill discovery regresses, generic-workflow duplication persists, or another reusable source defect appears.

## Terminal boundary

Task 070 closes only after required Web routing/Profile acceptance evidence is recorded. Formal GitHub release remains a later integrated-acceptance boundary.

Control Alignment:

- `RELATED_DOCUMENT`: `references/V060_INTEGRATED_ACCEPTANCE.md`
- `DOCUMENT_ALIGNMENT`: `UNCHANGED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`

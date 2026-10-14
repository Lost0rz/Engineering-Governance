# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.x release has been created yet.

## v0.6.x source architecture / current semantic candidate

The eight-Skill architecture remains accepted. Current corrected Delivery / Semantic candidate:

`c6d412d46fdda7ba04df277ff82471a8f246cac7`

Completed acceptance-driven correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff templates aligned with Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile contract/template/acceptance hardened against generic-workflow duplication and handbook-sized output.
- `EG-V060-PROFILE-BOUNDARY-CORRECTIVE-073` — Project Profile surface-role evidence, established-Domain deduplication, meta-procedure exclusion, and normative-rule compression hardened.

Task 073 focused source diff is bounded to:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` package version alignment.

No other Skill or capability architecture changed.

PR #26 remains OPEN / DRAFT / UNMERGED. Host facts are reread at their own boundary; CI/check PASS is not claimed without current evidence.

## Project Profile corrected contract

Current Profile contract now additionally requires:

- `MIRROR` only with verified/explicit primary Profile evidence;
- `PRIMARY` only with explicit project/user designation among multiple Profile surfaces;
- `single surface` when this is the only established current Profile surface and no competing surface is verified; otherwise use `UNKNOWN` rather than guessing;
- established Domain/navigation authority is pointed to rather than rebuilt as a reduced Domain Model/source-symbol map;
- `Planning & navigation` contains durable pointers, not numbered startup/read/check workflow;
- generated Profiles do not add Profile-maintenance/classification/freshness meta-sections such as `Project Profile Rule`;
- detailed project-specific MUST/MUST-NOT execution rules remain in `AGENTS.md`; Profile keeps compact priorities/anti-goals/risk cues only.

Integrated acceptance now has explicit negative cases for surface-role evidence, established Domain Map deduplication, and Profile meta-procedure.

## Web Plugin candidate acceptance

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is restored to `WAITING_FRESH_WEB_SESSION`.

Current installed personal Web Plugin candidate:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.2`;
- release: `pluginrel_6acf0b3b77a081918da5d86718bfef23`;
- scope/discoverability: `USER / PRIVATE`;
- root `plugin.json` and platform-managed `.codex-plugin/plugin.json` both report `0.6.2`;
- Task 073 overlay contained only the manifest plus the three corrected `project-profile` shipped files;
- overlay ZIP SHA-256: `e47258bf25e7999fd305114d978a8cc01bf3001a2fc140b5f86221318c31f04a`;
- local overlay Git-blob identities matched the repository blob SHAs for all four uploaded files before installation;
- post-update installed-file readback confirms the corrected Skill/template/contract content is active.

Fresh Web evidence already established from earlier candidates:

- exact eight top-level Skill discovery: PASS;
- ordinary status/progress inspection -> `project-governance`: PASS;
- advisory inspection avoids over-routing: PASS;
- Project Profile routing/authority/live-state exclusion: PASS;
- Task 072 generic-governance compactness regression: materially improved;
- FloatTabs regression exposed the remaining Task 073 defects, now corrected in source and Web 0.6.2 but not yet regression-tested by the user.

## Next milestone

Open a new Web conversation against Plugin `0.6.2` and regenerate the FloatTabs Project Profile using the same prompt. The regression should show evidence-supported surface role, no reduced Domain Map, no numbered startup workflow, no Profile-maintenance meta-section, and only compact normative risk cues. If that passes, continue remaining Task 070 Web routing scenarios before Local Codex integrated acceptance.

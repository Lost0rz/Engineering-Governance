# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.x release has been created yet.

## v0.6.x source architecture / current semantic candidate

The eight-Skill architecture remains accepted. Pre-Task-074 corrected Delivery / Semantic candidate:

`c6d412d46fdda7ba04df277ff82471a8f246cac7`

Completed acceptance-driven correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff templates aligned with Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile contract/template/acceptance hardened against generic-workflow duplication and handbook-sized output.
- `EG-V060-PROFILE-BOUNDARY-CORRECTIVE-073` — Project Profile surface-role evidence, established-Domain deduplication, meta-procedure exclusion, and normative-rule compression hardened.

Active corrective:

- `EG-V060-PROFILE-GROUNDING-CORRECTIVE-074` — Project Profile fact grounding, Memory/history isolation, old-Profile revalidation, and authority-class preservation.

PR #26 remains OPEN / DRAFT / UNMERGED. Host facts are reread at their own boundary; CI/check PASS is not claimed without current evidence.

## Task 074 audit finding

Fresh cross-project Web acceptance established a reusable source-contract gap.

Current Project Profile source already says the Profile is compiled from verified authorities and warns not to infer business truth from memory, but it does not define an explicit claim-level source eligibility gate. In practice this allowed derived/contextual material to be promoted into durable-looking Profile facts:

- previous Project Instructions could be re-ingested during rebuild rather than revalidated against current authority;
- prior conversational Memory could supply project constraints absent from repository authority;
- materially distinct fact classes could be over-compressed into a universal Authority statement.

Selected boundary:

- Project Profile is a **fact-grounded derived projection**;
- Memory/conversation remains a separate contextual layer for normal dialogue;
- Memory/history/old Profile may suggest what to verify, but cannot independently establish a substantive Profile claim;
- explicit current user decisions may establish durable user-authorized context, but must not be presented as repository-established facts when they are not persisted there;
- existing Profile/Project Instructions are derived context and must be revalidated when rebuilt;
- materially distinct project authority classes must remain distinct.

This is a bounded `project-profile` corrective. It does not change ChatGPT Memory behavior and does not add a new Skill or control plane.

## Task 074 source scope

Bounded source paths:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` patch-version alignment.

No other Skill or capability architecture is in scope.

## Web Plugin candidate acceptance

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is temporarily interrupted by Task 074 corrective execution.

Currently installed Web Plugin remains the pre-corrective candidate:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.2`;
- release: `pluginrel_6acf0b3b77a081918da5d86718bfef23`;
- scope/discoverability: `USER / PRIVATE`.

The corrected Task 074 candidate has not yet been packaged/installed or regression-tested.

## Next milestone

Complete the bounded Task 074 source corrective, verify the exact diff and acceptance text, bump the candidate patch version, refresh the existing personal Web Plugin identity from repository source, then restore parent Task 070 and rerun fresh cross-project Project Profile regressions before any formal release/merge.

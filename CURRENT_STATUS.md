# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Published Plugin release: `plugin-v0.5.3`.

Accepted release source:

`255bd32b1414a9555a7280d6e7562411ed3c7d96`

Published asset:

- `engineering-governance-plugin.zip`
- size: `56926` bytes
- SHA-256: `4bec949b09d5178f205ce07a34fb5e2223b3d52fe492464aa4f661876b9b9aa4`
- package entries: `29`
- exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

The release workflow verified manifest version `0.5.3`, the exact three-Skill boundary, the Final PR-head freeze source, and the 29-file package before publishing the immutable tag/release. Release run `38332704281` completed successfully for frozen source `255bd32b1414a9555a7280d6e7562411ed3c7d96`.

## Final PR-head freeze corrective

`plugin-v0.5.3` now publishes the previously accepted `EG-FINAL-PR-HEAD-FREEZE-052` corrective:

- finish intended source/control edits before designating the final PR head;
- freeze that head for exact-head CI, review, independent audit, mergeability, and repository-host evidence;
- treat those results as live external evidence for the immutable identity;
- do not create source/control commits solely to record external evidence state;
- if evidence requires a real correction, unfreeze and restart exact-head verification on the corrected head;
- if evidence passes, merge the same frozen head;
- post-merge verification must not create another evidence-only commit loop.

Reusable source authority remains:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/references/control-plane.md`

## ChatGPT Plugin state

Owned private ChatGPT Plugin `engineering-governance` is now version `0.5.3`.

Its current release retains the accepted Final PR-head freeze source in the three reusable Project Governance files above. The Plugin identity and audience were preserved during the version update.

## Local Codex installation state

The previously accepted Air and Mac mini installations were `0.5.0`. This Web release task does **not** claim those machine-local installations have been upgraded yet.

Next machine-local milestone:

- install/upgrade the Plugin payload to `0.5.3` on Air and Mac mini;
- verify `project-governance`, `domain-navigation`, and `incident-doctor` resolve from the new payload;
- verify exactly one current Engineering Governance managed routing block remains in the authoritative global guidance;
- verify no older active Plugin registration competes with `0.5.3`.

Do not hand-edit active Plugin caches as a substitute for the upgrade path.

## Current repository state

- Release task `EG-PLUGIN-V0.5.3-RELEASE-053`: **COMPLETE**.
- Open release blocker: **none**.
- Active authorized repository task: **none**.
- The one-shot release workflow used for v0.5.3 publication was removed from active `main` after publication.

Normal business-project use may proceed after the consuming environment is upgraded/verified to the intended Plugin version. Project-local controls are not rewritten merely because the reusable Plugin version changed.

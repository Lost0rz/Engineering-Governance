# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.x release has been created yet.

## v0.6.x source architecture / current semantic candidate

The eight-Skill architecture remains accepted. Current corrected Delivery / Semantic candidate:

`aa310bec3550c5e7e2ede2436b2f6f59ff2b9b59`

Completed acceptance-driven correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff templates aligned with Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile contract/template/acceptance hardened against generic-workflow duplication and handbook-sized output.
- `EG-V060-PROFILE-BOUNDARY-CORRECTIVE-073` — surface-role evidence, established-Domain deduplication, meta-procedure exclusion, and normative-rule compression hardened.
- `EG-V060-PROFILE-GROUNDING-CORRECTIVE-074` — fact grounding, Memory/history isolation, old-Profile revalidation, and authority-class preservation hardened.

PR #26 remains OPEN / DRAFT / UNMERGED. Host facts are reread at their own boundary; CI/check PASS is not claimed without current evidence.

## Project Profile grounding contract

Task 074 established the missing source-eligibility boundary:

- Project Profile is a **fact-grounded derived projection**, not a Memory summary or independent authority;
- every substantive project-specific Profile claim must trace to current verified project authority appropriate to the claim, or to an explicit durable user decision/reaffirmation in the current Profile task;
- ChatGPT/model Memory, prior chats, previous assistant output, previous Project Instructions/Profile, and old handoff/audit/task/PR/status/history artifacts may suggest what to verify but cannot independently establish a Profile fact;
- previous Profile/Project Instructions are `DERIVED_PROJECT_CONTEXT` and retained claims must be revalidated during rebuild/audit;
- unsupported candidates are omitted from the Profile or reported separately as unverified;
- current user-authorized durable context may be represented without being mislabeled as repository-established fact;
- storage, Raw Evidence, projections, implementation authority, runtime evidence, and explicitly canonical state remain distinct when the owning project distinguishes them;
- this boundary does not disable or weaken ordinary conversational Memory use.

Task 072/073 compactness, Domain-deduplication, surface-role, live-state-exclusion, and normative-rule boundaries remain in force.

## Task 074 source verification

Focused source compare from the Task-074 control checkpoint changed only:

- `plugin.json`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `skills/project-profile/SKILL.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `skills/project-profile/references/profile-contract.md`.

No other Skill or capability architecture changed.

Integrated acceptance now includes:

- Memory / prior-conversation contamination negative case;
- previous Profile / Project Instructions inheritance negative case;
- explicit current durable user-decision positive case;
- authority-class preservation case.

The final profile-contract commit also aligned repository bytes with the packaged overlay; it did not change Task-074 semantics.

## Web Plugin candidate acceptance

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is restored to `WAITING_FRESH_WEB_SESSION`.

Current installed personal Web Plugin candidate:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.3`;
- release: `pluginrel_6acf295fe3f08191bf7bc52f6a70eb43`;
- scope/discoverability: `USER / PRIVATE`;
- root `plugin.json` and platform-managed `.codex-plugin/plugin.json` both report `0.6.3`;
- Task-074 overlay contained only `plugin.json` plus the three corrected `project-profile` shipped files;
- overlay ZIP SHA-256: `b7d7ff6196721811dd56602272f62dcc4de64047be36031892f754e29376dd3d`;
- packaged Git-blob identities matched repository source for all four uploaded files before installation;
- post-update installed-file readback confirms the Task-074 Skill/template/contract content is active.

Fresh Web evidence retained from earlier candidates:

- exact eight top-level Skill discovery: PASS;
- ordinary status/progress inspection -> `project-governance`: PASS;
- advisory inspection avoids over-routing: PASS;
- Project Profile routing and live-state exclusion: PASS;
- Task 072/073 regressions materially improved Profile compactness and boundary behavior.

Task 074 source/package corrective is complete; behavioral acceptance of the new grounding rules is still pending on fresh Web `0.6.3` sessions.

## Next milestone

Run fresh cross-project Project Profile regressions against Web Plugin `0.6.3`:

1. Gift-like case: Memory-only merchandise/visual preferences absent current authority must not enter the Profile unless explicitly reaffirmed in the current Profile task.
2. MemoX-like case: storage/evidence/projection/canonical authority classes must remain distinct.
3. FloatTabs-like rebuild: old Project Instructions may guide verification but must not bootstrap their own truth.
4. Positive current-user-decision case: an explicitly established durable decision may appear as user-authorized context without being presented as repository-established fact.

If those grounding regressions and the remaining Task-070 routing scenarios pass, proceed to Local Codex integrated acceptance. Formal GitHub release/merge remains deferred until that boundary is supported.

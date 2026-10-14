# CURRENT TASK — Project Profile Grounding Corrective

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-GROUNDING-CORRECTIVE-074`

Task class: `CORRECTIVE`

State: `ACTIVE`

Parent purpose task: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

## Objective

Correct the reusable Project Profile source-grounding defect exposed during fresh Web acceptance: a generated Profile must remain a fact-grounded derived projection and must not promote ChatGPT Memory, prior conversation, previous assistant output, previous Project Instructions/Profile text, or historical workflow artifacts into project facts merely because they look stable.

Memory/context may suggest what to verify, but it must not independently satisfy the evidence requirement for a substantive Profile claim.

## Verified defect evidence

Fresh cross-project Web regression exposed the same failure class in more than one form:

- FloatTabs showed that previous Project Instructions can be re-ingested as if they were source authority unless the generated Profile revalidates claims against current authorities.
- Gift generated durable-looking merchandise and visual constraints from prior conversational memory even though the current repository business authorities did not establish those claims.
- MemoX showed a related authority-semantic compression risk: a storage/evidence layer can be over-summarized into a universal fact Authority even when the project explicitly separates Raw Evidence, projections, and canonical fact classes.

Current `project-profile` source says not to infer business truth from memory, and `profile-contract.md` says the Profile is compiled from verified project authorities, but neither defines a sufficiently explicit source-eligibility/grounding gate or old-Profile revalidation rule. This is therefore a reusable source-contract defect, not a project-specific content correction.

## Selected design

Project Profile is the **fact-grounded derived layer**. Conversation Memory remains a separate context layer and continues to help normal dialogue; this corrective does not disable or weaken Memory globally.

For Project Profile generation/rebuild/audit:

- a substantive project-specific claim must be traceable to a current verified project authority appropriate to that claim, or to an explicit current user decision that clearly establishes/changes durable project context;
- model memory, prior chats, previous assistant output, old Profile/Project Instructions, old handoffs/audits/task cards/PR prose, and historical summaries may be discovery clues only and do not independently ground a Profile claim;
- an existing Profile/Project Instructions surface is `DERIVED_PROJECT_CONTEXT`, not source authority; rebuilding must revalidate its substantive claims rather than inherit them;
- if a memory/history-derived candidate cannot be verified, omit it or keep it explicitly unknown outside the Profile rather than silently promote it;
- when a current user establishes a durable decision that is not yet persisted in repository authority, it may be represented as user-authorized context but must not be misrepresented as repository-established fact;
- preserve materially distinct authority classes; storage, evidence, projection, implementation, and canonical truth must not be collapsed into one universal Authority unless the owning project authority actually defines that relationship.

## Scope

Allowed source changes are bounded to:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` version alignment for the corrected Web candidate;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` reconciliation;
- PR #26 description refresh if the corrected candidate identity changes.

No other Skill or capability architecture is in scope.

## Acceptance

Source acceptance requires all of the following:

1. explicit source-grounding gate in the Project Profile Skill/contract;
2. Memory/prior-chat/old-Profile/old-Project-Instructions content cannot independently establish Profile facts;
3. old Profile surfaces may seed a verification checklist but must be revalidated claim-by-claim;
4. explicit current durable user decisions remain usable without being mislabeled as repository-established facts;
5. authority-class semantics are preserved rather than flattened;
6. the shipped template reinforces the grounding boundary without turning the Profile into a provenance report;
7. integrated acceptance contains negative cases for Memory/history contamination and old-Profile inheritance, plus a positive current-user-decision case and a fact-class preservation case;
8. no regression to Task 072/073 compactness, Domain deduplication, surface-role evidence, or live-state exclusion;
9. corrected package/Web candidate uses a new patch version after source verification.

## Out of scope

- changing ChatGPT Memory product behavior or account memory settings;
- making Memory unavailable to ordinary conversation;
- adding a ninth Skill or new control file;
- importing Gift/FloatTabs/MemoX project-specific rules into Engineering Governance;
- formal immutable GitHub v0.6.x release/tag;
- PR #26 merge;
- Local Codex acceptance before the corrected Web candidate is ready.

## Stop conditions

Stop before release/merge if the corrective would require changing global Memory behavior, adding a new project authority/control plane, or expanding beyond the Project Profile contract/acceptance surface.

## Return to parent acceptance

After focused source verification and corrected Web candidate installation, restore `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` with Task 074 recorded in corrective history and rerun fresh Profile regressions against the corrected candidate.

TASK_RECONCILIATION_REQUIRED: NO
REASON: Parent Task 070 explicitly permits bounded source correctives when fresh Web acceptance exposes a reusable defect; this Task 074 records that corrective slice before mutation.

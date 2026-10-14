# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal release remains `plugin-v0.5.5`; accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has run.

## v0.6.0 source architecture — REOPENED FOR BOUNDED HARDENING

Task `EG-CAPABILITY-PROFILE-HANDOFF-LIFECYCLE-068` is ACTIVE on PR #26.

- Prior source freeze: `f3d47b00cac41ebd19408cef18563c91be67ae53`.
- Task 067 installed-acceptance start was superseded before acceptance because additional reusable-source gaps were identified.
- Current work is source/governance hardening only; installed/runtime acceptance remains deferred.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- No CI PASS is claimed where commit/check status is absent.

## Bounded hardening goals

- introduce a lightweight `project-profile` derived-context capability without making it an authority;
- keep `AGENTS.md` normative, Profile descriptive/indexing, Domain Map navigational, STATUS/TASK current-control, and planning long-lived design;
- standardize handoff Card/Receipt transport contracts and a compact human-facing engineering status receipt;
- reconcile only affected semantic owners when project artifacts become stale;
- reduce repeated workflow prose in project-local guidance;
- preserve environment-owned runtime/config values and existing lightweight governance principles.

## Next milestone

Finish Task 068 source implementation, run a complete remote source audit, freeze the new semantic candidate, then reconsider the deferred consolidated installed Plugin/Web/Codex acceptance.

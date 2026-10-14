# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.0 release has been created yet.

## v0.6.0 source architecture — FROZEN

Current frozen Architecture Delivery / Semantic HEAD:

`d8bdf9da4094a0550d59afe33e02b179582150b2`

- Task `EG-CAPABILITY-CONTRACT-CORRECTIVE-069` is COMPLETE with V2 remote source-architecture audit PASS (`AUDIT_INDEPENDENCE: SELF_CHECK`).
- Packaging precheck for Task 070 found stale Agent Handoff request/receipt templates.
- Bounded corrective Task `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` is COMPLETE; the shipped request/receipt templates now match the accepted `CARD_ID` / `CAPABILITY` / `MODE` Card/Receipt contract.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- No semantic-head CI/check PASS is claimed unless current host evidence reports it.

## Current acceptance task

Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is ACTIVE again after Task 071 corrective closeout.

Current boundary:

- build an exact Web Plugin candidate from frozen Semantic HEAD `d8bdf9da...`;
- update the existing personal ChatGPT `engineering-governance` Plugin from 0.5.5 to 0.6.0 on the same Plugin identity;
- run Web-side discovery/routing acceptance before formal GitHub release, PR merge, or Local Codex installation.

Formal GitHub `plugin-v0.6.0` publication is intentionally deferred until required installed/integrated acceptance supports that boundary.

## Accepted architecture

- Exactly eight top-level Skills; global routing is policy, not a ninth Skill.
- `project-profile` is a derived context/index. Repository/project-managed Profile mutation requires compatible task authorization.
- A project keeps one current Profile projection surface, or one primary surface plus a derived mirror.
- Project `AGENTS.md` is normative; Domain/navigation owns detailed routing; durable planning owns long-lived design; STATUS/TASK own current state/authorization.
- Handoff separates `CAPABILITY` from `MODE`; required Card/Receipt core fields are standardized and shipped templates now match that contract.
- Artifact lifecycle separates normative/design/current/implementation authority, derived projections and observed evidence; unchanged semantics produce no write/commit.
- Advisory read-only status/evidence inspection can remain in Project Governance; formal acceptance/readiness verdicts use Evidence Audit.
- Project Governance emits one compact human status receipt for governed engineering/status/audit/CI/PR/merge responses without duplicating a full Handoff Receipt.
- Same-purpose continuation preserves the active task and prefers a safe current PR/workspace for in-scope corrections.
- Runtime/model/tool/capacity configuration remains environment-owned; stronger-model escalation remains disabled during stabilization.

## Next milestone

Complete Task 070 exact Web candidate packaging/update and Web-side routing acceptance. Reusable defects return to a bounded source corrective task; do not patch installed caches.

# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal release remains `plugin-v0.5.5`; accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has run.

## v0.6.0 source architecture — FROZEN FOR CONSOLIDATED ACCEPTANCE

Task `EG-CAPABILITY-CONTRACT-CORRECTIVE-069` is COMPLETE.

- Frozen Architecture Delivery / Semantic HEAD: `7be11aae70c42b075034eb4613a7dc66b242bb80`.
- PR #26 remains OPEN / DRAFT / UNMERGED; final source audit observed `mergeable=true`.
- Semantic head commit/check statuses: none reported; **CI PASS is not claimed**.
- Installed integrated acceptance: `NOT_RUN`.

## Accepted architecture

- Exactly eight top-level Skills; global routing is policy, not a ninth Skill.
- `project-profile` is a derived context/index. Repository/project-managed Profile mutation requires compatible task authorization.
- A project keeps one current Profile projection surface, or one primary surface plus a derived mirror.
- Project `AGENTS.md` is normative; Domain/navigation owns detailed routing; durable planning owns long-lived design; STATUS/TASK own current state/authorization.
- Handoff separates `CAPABILITY` from `MODE`; required Card/Receipt core fields are standardized and a mode never replaces Skill routing.
- Artifact lifecycle separates normative/design/current/implementation authority, derived projections and observed evidence; unchanged semantics produce no write/commit.
- Advisory read-only status/evidence inspection can remain in Project Governance; formal acceptance/readiness verdicts use Evidence Audit.
- Project Governance emits one compact human status receipt for governed engineering/status/audit/CI/PR/merge responses without duplicating a full Handoff Receipt.
- Same-purpose continuation preserves the active task and prefers a safe current PR/workspace for in-scope corrections.
- Runtime/model/tool/capacity configuration remains environment-owned; stronger-model escalation remains disabled during stabilization.

## Task 069 source audit

`V2 remote source-architecture audit: PASS` for semantic head `7be11aae70c42b075034eb4613a7dc66b242bb80`.

Audit independence: `SELF_CHECK` — complete source audit in the same implementation context; this is not independent installed/runtime acceptance.

Verified: exact eight-Skill directory set; Plugin metadata `0.6.0`; Skill triggers/authority boundaries remain distinct; Profile mutation/surface rules are coherent; Handoff Card/Receipt schema is internally consistent; `CAPABILITY` and `MODE` are orthogonal; implementation authority is separated from observed evidence; advisory vs formal audit routing is coherent; Domain Navigation uses progressive disclosure; durable design, README and global routing template are aligned; no runtime/daemon/database/model-router/automatic enforcement was added.

## Next milestone

Run one consolidated v0.6.0 installed Plugin/Web/Codex acceptance using `references/V060_INTEGRATED_ACCEPTANCE.md`. Reusable defects return to a bounded source corrective task; do not patch installed caches.

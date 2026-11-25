# Engineering Governance v0.6.0 — Architecture Hardening

Status: ACTIVE DESIGN AUTHORITY through Task `EG-CAPABILITY-CONTRACT-CORRECTIVE-069`

Date: 2026-10-14

Parent architecture: `documents/engineering-governance-capability-model-v0.6.0.md`

## Purpose

Keep Engineering Governance lightweight while making routing, context recovery, delegation, handoff, evidence and lifecycle reliable across Web/Local/Sub Agent use. Do not add a second control plane, Router Skill, runtime service, or mandatory large forms.

## Stable model

- Eight top-level Skills; global routing is policy, not a ninth Skill.
- `CURRENT_TASK.md` remains the single active execution authorization.
- Project Profile is a derived context/index, not authority; repository/project-managed Profile mutation requires compatible task authorization.
- Project `AGENTS.md` remains normative; Domain/navigation remains detailed routing; STATUS/TASK remain current controls; durable planning owns long-lived design when justified.
- One current Profile projection surface is preferred; if a mirror is needed, one surface is primary and the mirror remains derived.
- Task purpose, execution unit and execution context are distinct.
- Safe useful Sub Agent parallelism is encouraged.
- Formal audit/acceptance remains separate from advisory read-only inspection and implementation self-check when independence matters.
- Incident Doctor stays evidence-gated.

## Accepted hardening

### Routing and environment

Routing may use explicit Skill selection, Skill metadata, project guidance, supported global guidance, or platform/runtime routing. Keywords alone do not select Skills. Concrete model/reasoning/capacity/tool/runtime values remain owned by the execution environment that provides them.

### Project Profile

`project-profile` creates/rebuilds/audits a compact derived landing page from verified project authorities. It classifies candidate information rather than copying everything into one file. Authority wins whenever a Profile is stale. Read-only drafting/audit does not grant mutation authority.

### Artifact lifecycle

Reconcile affected semantic owners, not every file. Keep normative authority, durable design, current controls, implementation authority, derived projections and observed evidence distinct. No semantic change means no write/commit.

### Handoff and receipts

Agent Handoff uses one common Card schema. `CAPABILITY` identifies the bounded Skill/capability requested; `MODE` identifies receiver action/side-effect class. A mode does not replace routing. Required Card core fields stay stable; conditional fields such as `PURPOSE`, `PROFILE`, claim/evidence and context are added only when useful. Structured receipts begin with Card/task/mode/capability/target/outcome identity before mode-specific evidence.

EXECUTE is state-changing; AUDIT/REVIEW/VERIFY/DIAGNOSE are read-only. Normal test runs map to VERIFY; changing tests or instrumentation maps to EXECUTE with explicit purpose.

Project Governance emits one compact human-facing engineering status receipt for governed engineering/status/audit/CI/PR/merge responses; it does not duplicate a full machine/context transfer receipt.

### Audit boundary

Advisory read-only evidence/status inspection may remain in Project Governance and does not require a new formal AUDIT task. Formal acceptance/readiness verdicts use Evidence Audit; when that purpose is materially distinct, Project Governance authorizes the corresponding AUDIT/VERIFY task boundary.

### Continuation / workspace economy

If the active task remains accurate, `continue/resume/start` continues it directly. A same-task correction should reuse a safe current PR/workspace rather than spawning a successor by default. Predecessor writer/unique-work/conflict rules still apply.

## Acceptance sequence

1. complete Task 069 bounded contract corrective and durable-design alignment;
2. run complete remote source consistency audit;
3. freeze one new v0.6.0 Semantic HEAD;
4. run one consolidated installed Plugin/Web/Codex acceptance pass;
5. return only real reusable defects to bounded corrective work;
6. merge/release preparation after acceptance.

Do not test one Skill at a time during construction and do not expand this into a general agent platform.

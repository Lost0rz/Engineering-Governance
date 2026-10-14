# Engineering Governance v0.6.0 — Architecture Hardening

Status: ACTIVE DESIGN AUTHORITY for v0.6.0 through Task `EG-CAPABILITY-ROUTING-ENVIRONMENT-HARDENING-066`

Date: 2026-10-14

Parent architecture: `documents/engineering-governance-capability-model-v0.6.0.md`

## Purpose

Keep the seven-Skill architecture while making routing, delegation, and authority lightweight enough for real Web/Local/Sub Agent use. Hardening must improve clarity without adding a new control plane, router Skill, runtime service, or large mandatory forms.

## Stable model

- Seven top-level Skills only.
- `CURRENT_TASK.md` remains the single active execution authorization.
- Task purpose, execution unit, and execution context are distinct.
- Safe useful Sub Agent parallelism is encouraged.
- Formal audit/acceptance remains separate from implementation self-check when independence matters.
- Incident Doctor stays evidence-gated.

## Task 063–065 accepted corrections

- Use safe parallel Sub Agents when independence makes them useful; do not optimize for minimum agent count.
- Context change (Web/local/session/machine/Sub Agent) does not create a new task by itself.
- `ENVIRONMENT_DEFAULT_ONLY` is active for delegated models during stabilization.
- Concrete model/reasoning configuration belongs to the execution environment that owns it and does not propagate across contexts.
- Stronger-model escalation remains disabled until explicit re-authorization.

## Task 066 routing / environment hardening

### 1. Routing surfaces

Routing may be supplied by explicit Skill selection, Skill metadata, project guidance, authoritative global guidance where supported, or platform/runtime routing. Local-style global AGENTS is one supported surface, not a universal requirement.

Routing is semantic/outcome-based. Keywords such as `CI`, `PR`, `bug`, or `audit` do not alone select a Skill.

### 2. Rule ownership

Portable workflow lives in `skills/**`. Root repository `AGENTS.md` contains only rules for maintaining this source repository. Durable design documents explain accepted architecture/rationale but do not duplicate the full runtime procedure.

### 3. Environment capability authority

The current execution environment owns concrete runtime values unless an accepted project artifact explicitly makes a value portable.

Only resolve capabilities that can change the current execution decision, such as:

- Sub Agent default;
- parallel capacity;
- delegation/depth constraints;
- material tools/connectors;
- workspace/runtime/network constraints.

Reusable governance defines the resolution protocol, not the values. Unknown/unexposed values remain `UNKNOWN`/platform-managed rather than guessed or imported from another context.

### 4. Cross-repository work

Project Governance owns the governing task and, only when material, names participating repositories, per-repo writer authority, shared contract authority, integration order, and acceptance owner. Each repository/system remains authoritative for its own source/runtime facts.

Domain Navigation may trace upstream/downstream source/test/runtime routes across those named participants; it does not create cross-repository task authority.

### 5. Bounded quality fixes

- Evidence Audit metadata selects a verdict request, not CI/PR keywords.
- `DIAGNOSE` handoff is read-only; a state-changing diagnostic probe uses `EXECUTE` with `PURPOSE: DIAGNOSTIC_PROBE`.
- Solution Design records material quality attributes and reversibility only when decision-relevant.
- Diagnostic probes declare observer-effect/safety/privacy risk and cleanup when material.
- No-op control reconciliation produces no write/commit.

## Acceptance sequence

1. finish Task 066 source hardening as one architecture;
2. run bounded remote source consistency audit;
3. freeze one new v0.6.0 Semantic HEAD;
4. run one consolidated installed Plugin/Web/Codex acceptance pass;
5. return only real reusable defects to bounded corrective work;
6. merge/release preparation only after acceptance.

Do not test one Skill at a time during construction and do not expand this hardening into a general agent platform.

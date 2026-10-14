# Engineering-Governance Repository Rules

## Purpose

This repository is the source for reusable Engineering Governance Skills, routing contracts, templates, and acceptance specifications. It is not a governance runtime, daemon, scheduler, database, installer service, or automatic remediation system.

## Repository authority

- `AGENTS.md` contains durable rules for maintaining this source repository.
- `CURRENT_STATUS.md` is the concise verified current snapshot.
- `CURRENT_TASK.md` is the single active execution authorization.
- Reusable engineering workflow belongs in `skills/**`; do not duplicate Skill procedure here.
- `documents/**` may preserve durable design rationale, but does not replace live controls.

## Capability model

Exactly eight top-level Skills are supported:

1. `project-governance`
2. `project-profile`
3. `solution-design`
4. `execution-orchestrator`
5. `agent-handoff`
6. `evidence-audit`
7. `domain-navigation`
8. `incident-doctor`

Global routing is policy, not a ninth Skill. `project-profile` is derived context/navigation, not a fourth control source or replacement for project `AGENTS.md`, Domain authority, STATUS/TASK, or durable planning.

## Environment boundary

Reusable source defines what environment capability must be resolved, not concrete machine/platform values. Runtime/model/tool/capacity facts remain owned by the current execution environment unless a project explicitly defines a portable configuration artifact.

## Source development rules

- Inspect actual repository/PR/source evidence before changing governance.
- Keep one canonical owner per semantic class; link instead of duplicating.
- Preserve unknown/unique work and existing project authorities.
- Keep changes proportional; no extra Skill/document/test ceremony without material value.
- Do not add runtime/daemon/database/model-router/automatic-enforcement behavior unless repository purpose explicitly changes.
- No-op reconciliation means no write and no commit.

## Release / acceptance boundary

Source construction, installed/runtime acceptance, merge and release are separate lifecycle steps. Do not claim CI, installed behavior or release readiness without evidence for the exact relevant identity.

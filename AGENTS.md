# Engineering-Governance Repository Rules

## Purpose

This repository is the source for reusable Engineering Governance Skills, routing contracts, templates, and acceptance specifications. It is not a governance runtime, daemon, scheduler, database, installer service, or automatic remediation system.

## Repository authority

- `AGENTS.md` contains only durable rules for maintaining this source repository.
- `CURRENT_STATUS.md` is the concise verified current snapshot.
- `CURRENT_TASK.md` is the single active execution authorization.
- Reusable engineering workflow belongs in `skills/**`; do not duplicate Skill procedure here.
- `documents/**` may preserve durable design rationale, but does not replace live controls or become a second runtime procedure source.

## Capability model

Exactly seven top-level Skills are supported:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing is policy, not an eighth Skill. Follow `references/SKILL_ENGINEERING.md` for Skill quality and `skills/project-governance/references/global-routing.md` for capability selection.

## Environment boundary

Reusable source defines what environment capability must be resolved, not concrete machine/platform values. Model/reasoning defaults, parallel capacity, delegation limits, tool availability, workspace/runtime constraints, and similar execution facts remain owned by the execution environment unless a project explicitly defines a portable configuration artifact.

Do not copy one environment's runtime values into reusable Plugin policy or another context's defaults. See `skills/execution-orchestrator/references/environment-capabilities.md`.

## Source development rules

- Inspect actual repository/PR/source evidence before changing governance.
- Keep one canonical owner per semantic rule; reference rather than duplicate.
- Preserve unknown/unique work and existing project authorities.
- Keep changes proportional: no extra Skill, worktree, agent, document, or test ceremony without material value.
- Do not add runtime/daemon/database/model-router/automatic-enforcement behavior unless a future task explicitly changes repository purpose.
- External projects are references, not hidden dependencies; record attribution/licensing posture before copying material.
- No-op reconciliation means no write and no commit. Control alignment is mandatory; control mutation is conditional on semantic change.

## Current repository execution convention

For this repository today, Web/remote work commonly owns reusable-source construction and remote GitHub audit, while local Codex is commonly used for installed Plugin/runtime acceptance. This is an operational convention, not the reusable meaning of DESIGN/EXECUTION/AUDIT or any Skill.

## Release / acceptance boundary

For multi-Skill architecture work, bounded source checks may occur during construction, but installed/runtime acceptance should follow the task-defined cadence. Do not claim CI, installed behavior, or release readiness without evidence for the exact relevant identity.

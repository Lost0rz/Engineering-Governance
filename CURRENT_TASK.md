# CURRENT TASK — Routing & Environment Hardening v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ROUTING-ENVIRONMENT-HARDENING-066`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Finish the v0.6.0 architecture with a lightweight routing/configuration cleanup before consolidated installed acceptance.

## Scope

1. Make routing surfaces environment-neutral: explicit selection, Skill metadata, global/project guidance, or platform routing where available.
2. Keep portable workflow rules in Skills/references; keep root repository guidance focused on this source repository.
3. Generalize environment-owned capability resolution beyond Sub Agent model values without hardcoding local/runtime settings.
4. Add only the missing bounded cross-repository governance/navigation semantics.
5. Tighten Evidence Audit metadata, DIAGNOSE side-effect semantics, Solution Design reversibility, Doctor probe safety/cleanup, and no-op control-write acceptance.

## Constraints

- No eighth Skill.
- No runtime, daemon, installer, model-router, database, or automatic enforcement service.
- Do not add large mandatory forms; environment capability fields are read only when material to the current task.
- Preserve `ENVIRONMENT_DEFAULT_ONLY` and safe useful Sub Agent parallelism.
- Do not run Skill-by-Skill installed acceptance during construction.

## Baseline

- Branch: `codex/capability-model-v0.6.0`.
- Start literal HEAD: `b6bb90a4abfb1c99ef7fe91bcfa0b3ba0aa18b2a`.
- Prior frozen semantic HEAD: `b7fb0051b8c51b5c846a507fad9037518dcf18db`.
- PR #26: OPEN / DRAFT / UNMERGED.

## Verification

Use bounded source/static consistency checks during construction. Freeze one new semantic head only after the whole Task 066 scope is coherent, then update the consolidated acceptance specification.

## Stop conditions

Stop if the change would create a new control plane, hardcode environment-specific runtime values, or materially expand beyond the seven-Skill architecture.

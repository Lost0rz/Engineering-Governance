---
name: project-profile
description: Use when creating, rebuilding, shrinking, or auditing a project's compact durable context/profile so an agent can quickly understand what the project is and where authoritative facts live. Do not use for current task/status, detailed Domain-to-code mapping, or generic engineering workflow.
---

# Project Profile

Create or refresh a **derived project context/index**, not a new authority.

## Boundary

A Project Profile answers: what is this project, what stable concepts/constraints matter, and where should an agent go for authoritative detail?

It must not replace:

- project `AGENTS.md` normative rules;
- `CURRENT_STATUS.md` current facts;
- `CURRENT_TASK.md` active authorization;
- detailed Domain/navigation authority;
- durable design/planning authority;
- code/schema/runtime/host evidence.

If Profile text conflicts with an authority, the authority wins and the Profile is stale.

## Workflow

Classify each candidate item before writing:

1. current state/task -> STATUS/TASK;
2. reusable cross-project workflow -> Engineering Governance Skill;
3. project-specific MUST/MUST-NOT execution rule -> `AGENTS.md` or the accepted normative authority;
4. detailed Domain -> authority/source/test/runtime route -> Domain/navigation authority;
5. long-lived design rationale/work packages -> durable planning authority;
6. stable descriptive context or an authority pointer -> Project Profile.

Read only sources needed to establish the profile. Keep unknowns explicit; do not infer business truth from filenames or memory.

## Output

Use the compact sections in `assets/templates/PROJECT_PROFILE.md`. Prefer pointers over copied detail. A typical profile should remain small enough to serve as an entry page rather than a project knowledge dump.

Refresh only when a profile-owned summary/pointer is materially stale. See `references/profile-contract.md`.

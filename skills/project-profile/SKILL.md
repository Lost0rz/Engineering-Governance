---
name: project-profile
description: Use when creating, rebuilding, shrinking, or auditing a project's compact durable context/profile so an agent can quickly understand what the project is and where authoritative facts live. Do not use for current task/status, detailed Domain-to-code mapping, or generic engineering workflow.
---

# Project Profile

Create or refresh a **derived project context/index**, not a new authority.

## Boundary

A Project Profile answers: what is this project, what stable concepts/constraints matter, and where should an agent go for authoritative detail?

It must not replace project `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, detailed Domain/navigation authority, durable design/planning authority, or implementation/runtime/host truth. If Profile text conflicts with an authority, the authority wins and the Profile is stale.

Generating or auditing Profile content may be read-only/output-only. **Writing or refreshing a repository/project-managed Profile is state-changing and requires compatible Project Governance / `CURRENT_TASK.md` authorization.** This Skill never creates that authorization by itself.

## Workflow

Classify each candidate item before writing:

1. current state/task -> STATUS/TASK;
2. reusable cross-project workflow -> Engineering Governance Skill;
3. project-specific MUST/MUST-NOT execution rule -> `AGENTS.md` or accepted normative authority;
4. detailed Domain -> authority/source/test/runtime route -> Domain/navigation authority;
5. long-lived design rationale/work packages -> durable planning authority;
6. stable descriptive context or authority pointer -> Project Profile.

Read only sources needed to establish the profile. Keep unknowns explicit; do not infer business truth from filenames or memory.

## Output

Use `assets/templates/PROJECT_PROFILE.md`. Prefer pointers over copied detail. Keep one current Profile projection surface, or an explicit primary surface plus derived mirror; do not maintain independently edited competing Profiles. See `references/profile-contract.md`.

A current Profile may be used as an optional landing page for context recovery when available and cheap to read. It never removes the need to read authoritative controls/rules required for the actual decision.

Refresh only when a profile-owned summary/pointer is materially stale.

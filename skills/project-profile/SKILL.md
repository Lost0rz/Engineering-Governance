---
name: project-profile
description: Use when creating, rebuilding, shrinking, or auditing a project's compact durable context/profile so an agent can quickly understand what the project is and where authoritative facts live. Do not use for current task/status, detailed Domain-to-code mapping, or generic engineering workflow.
---

# Project Profile

Create or refresh a **derived project context/index**, not a new authority or a second governance manual.

## Boundary

A Project Profile answers: what is this project, what stable concepts/constraints matter, and where should an agent go for authoritative detail?

It must not replace project `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, detailed Domain/navigation authority, durable design/planning authority, reusable Engineering Governance Skill contracts, or implementation/runtime/host truth. If Profile text conflicts with an authority, the authority wins and the Profile is stale.

Generating or auditing Profile content may be read-only/output-only. **Writing or refreshing a repository/project-managed Profile is state-changing and requires compatible Project Governance / `CURRENT_TASK.md` authorization.** This Skill never creates that authorization by itself.

## Classification workflow

Classify each candidate item before writing:

1. current state/task -> STATUS/TASK;
2. reusable cross-project workflow/protocol -> Engineering Governance Skill/reference, not Profile;
3. project-specific MUST/MUST-NOT execution rule -> `AGENTS.md` or accepted normative authority;
4. detailed Domain -> authority/source/test/runtime route -> Domain/navigation authority;
5. long-lived design rationale/work packages -> durable planning authority;
6. stable descriptive context, stable project-specific priority/anti-goal, environment role, or authority pointer -> Project Profile.

Read only sources needed to establish the profile. Keep unknowns explicit; do not infer business truth from filenames or memory.

## Compression gate

Before returning a Profile, remove content that merely restates reusable governance mechanics. In particular, a Profile normally does **not** reproduce:

- full Skill routing tables or per-Skill trigger explanations;
- Handoff Card/Receipt field schemas;
- verification-tier definitions or testing procedure;
- Incident Doctor workflow/probe procedure;
- artifact-lifecycle taxonomy/mechanics beyond a short project-relevant pointer;
- continuation/workspace/PR lifecycle procedure;
- Control Alignment or `CONTROL_ONLY_DRIFT` mechanics;
- generic rules already owned by Engineering Governance Skills/references.

If such material is useful for orientation, replace it with one short pointer/invariant. Preserve only project-specific stable facts that materially help an agent understand this project.

## Output discipline

Start from `assets/templates/PROJECT_PROFILE.md`.

- Prefer the template's existing top-level sections; add another section only when stable **project-specific** context cannot fit cleanly into them.
- Prefer concise bullets and authority pointers over explanatory procedure.
- When the target Profile surface is known, state `Profile surface` and `Primary/mirror role` explicitly.
- Keep one current Profile projection surface, or one explicit primary surface plus derived mirror; do not maintain independently edited competing Profiles.
- A Profile should be substantially smaller than the combined authorities it indexes. If it reads like a governance handbook, run the compression gate again.

See `references/profile-contract.md` for the full contract.

A current Profile may be used as an optional landing page for context recovery when available and cheap to read. It never removes the need to read authoritative controls/rules required for the actual decision.

Refresh only when a profile-owned summary/pointer is materially stale.

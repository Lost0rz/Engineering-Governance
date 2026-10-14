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
6. stable descriptive context, stable project-specific priority/anti-goal/risk cue, environment role, or authority pointer -> Project Profile.

Read only sources needed to establish the profile. Keep unknowns explicit; do not infer business truth, Profile-surface relationships, or authority from filenames or memory.

## Compression gate

Before returning a Profile, remove content that merely restates reusable governance mechanics or another established project authority. In particular, a Profile normally does **not** reproduce:

- full Skill routing tables or per-Skill trigger explanations;
- Handoff Card/Receipt field schemas;
- verification-tier definitions or testing procedure;
- Incident Doctor workflow/probe procedure;
- artifact-lifecycle taxonomy/mechanics beyond a short project-relevant pointer;
- continuation/workspace/PR lifecycle procedure;
- Control Alignment or `CONTROL_ONLY_DRIFT` mechanics;
- detailed Domain lists, ownership/source/symbol/test maps already owned by an established Domain/navigation authority;
- ordered startup/read/check workflows already owned by Project Governance or project rules;
- instructions for how to maintain, classify, refresh, or write the Project Profile itself;
- copied project-specific MUST/MUST-NOT rule lists already owned by normative authority.

If such material is useful for orientation, replace it with one short pointer or stable invariant. Preserve only project-specific stable facts that materially help an agent understand this project.

## Surface-role evidence

When the target Profile surface is known, state it explicitly. Do **not** invent its relationship to another Profile surface.

Use:

- `MIRROR` only when a specific primary Profile surface is verified or explicitly identified by project/user authority;
- `PRIMARY` only when project/user authority explicitly designates this surface as primary/canonical among multiple Profile surfaces;
- `single surface` when this is the only established current Profile surface and no competing Profile surface is verified.

If the relationship cannot be established, keep it explicit as unknown rather than guessing `PRIMARY` or `MIRROR`.

## Output discipline

Start from `assets/templates/PROJECT_PROFILE.md`.

- Prefer the template's existing top-level sections; add another section only when stable **project-specific** context cannot fit cleanly into them.
- Prefer concise bullets and authority pointers over explanatory procedure.
- If a detailed Domain/navigation authority exists, point to it; keep only the few broad Domain concepts needed for orientation and do not add a separate `Domain Model`/mini-map section by default.
- `Planning & navigation` contains durable pointers, not a numbered engineering startup sequence.
- Do not add a `Project Profile Rule`, maintenance guide, classification guide, freshness procedure, or similar meta-section to the generated Profile.
- `Priorities / constraints` may contain compact priorities, anti-goals, and risk cues; detailed normative execution rules remain in `AGENTS.md`/accepted normative authority.
- Keep one current Profile projection surface, or one explicit primary surface plus derived mirror; do not maintain independently edited competing Profiles.
- A Profile should be substantially smaller than the combined authorities it indexes. If it reads like a governance handbook, mini Domain Map, or Profile-maintenance guide, run the compression gate again.

See `references/profile-contract.md` for the full contract.

A current Profile may be used as an optional landing page for context recovery when available and cheap to read. It never removes the need to read authoritative controls/rules required for the actual decision.

Refresh only when a profile-owned summary/pointer is materially stale.

# Project Profile contract

## Role

`PROJECT_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT`

The Profile is a concise context/index compiled from verified project authorities. It helps Web/local/agent context recovery but has no independent power to authorize work or override truth.

A healthy Profile is a **landing index**, not a summarized copy of the governance system behind it.

## Current projection surface

A project should have **one current Profile projection surface**. It may be a repository file such as `PROJECT_PROFILE.md`, ChatGPT Project Instructions, or another accepted project context surface.

If the target surface is known, state:

```text
Profile surface: <repository file | project instructions | other accepted surface>
Primary/mirror role: <PRIMARY | MIRROR | single surface>
```

If two surfaces are operationally required, declare one `PRIMARY_PROFILE_SURFACE` and treat the other as a derived mirror. Do not maintain two independently edited current Profiles. A stale mirror never overrides the primary projection or underlying authorities.

Do not create a new manifest merely to name the surface. Record the pointer in an existing project authority/context surface when that is useful and supported by the project.

## Mutation authority

Profile generation, comparison, or draft output can be read-only. Creating/updating a repository/project-managed Profile is state-changing and requires compatible active task authorization through Project Governance. Profile staleness by itself does not grant write authority.

## Recommended contents

Keep only stable context that materially reduces orientation cost:

- purpose and core business/product loop;
- a few stable concepts needed to understand the project;
- authority map/pointers;
- durable planning/navigation pointers;
- stable project environment roles;
- project-specific priorities, anti-goals, or risk cues;
- a short Engineering Governance hook.

Project-specific stable facts may summarize a concept, but reusable procedure should be linked rather than re-explained.

## Anti-content / deduplication

Do **not** turn the Profile into a second `AGENTS.md`, routing manual, handoff protocol, verification guide, incident runbook, or control-plane specification.

Normally remove or replace with a short pointer:

- complete Skill routing tables or per-Skill trigger prose;
- Handoff Card/Receipt schemas and mode procedures;
- V0-V3 definitions, verification cadence, or testing procedure;
- Incident Doctor evidence/probe workflow;
- artifact-lifecycle class tables/mechanics;
- continuation, branch/worktree/PR lifecycle procedure;
- detailed Control Alignment / semantic-head / `CONTROL_ONLY_DRIFT` procedure;
- detailed Domain-to-source/test/runtime maps;
- current progress, current Task contract, PR/CI/release/host state;
- runtime-local model/tool/capacity values.

A short stable invariant is allowed when it materially helps orientation. Example: `Semantic delivery evidence and live GitHub host gates are evaluated separately; see Project Governance authority.` Do not reproduce the underlying procedure.

## Template-first compression

Use the shipped Profile template as the default shape. Prefer its existing top-level sections:

- Purpose
- Stable concepts
- Authority map
- Planning & navigation
- Environment
- Priorities / constraints
- Engineering Governance

Add another top-level section only when a stable **project-specific** context class cannot fit cleanly into these sections. Do not add a section merely because a reusable Skill has its own concept/procedure.

Before returning a Profile, apply this compression check:

```text
For each paragraph/bullet:
1. Is this stable project-specific context or an authority pointer?
   YES -> candidate to keep.
2. Is it current status/task/host evidence?
   YES -> remove; point to STATUS/TASK/live evidence if needed.
3. Is it a project-specific normative MUST/MUST-NOT?
   YES -> move/point to AGENTS or accepted normative authority.
4. Is it reusable Engineering Governance procedure/protocol?
   YES -> remove and replace with the shortest useful pointer/invariant.
5. Is it detailed Domain/design content?
   YES -> move/point to Domain or planning authority.
```

A Profile should be substantially smaller than the combined authorities it indexes. Concision is semantic deduplication, not omission of project-specific facts.

## Freshness

Refresh when a profile-owned summary or pointer materially changes: project purpose, stable concepts, authority locations, durable planning/navigation entry points, stable environment roles, or durable priorities/anti-goals.

Routine schema fields, task completion, PR/CI changes, or implementation details do not trigger Profile writes unless they change one of those summaries.

When stale:

```text
AUTHORITY_WINS: YES
PROFILE_STATE: STALE
```

Read-only work reports staleness without mutation. Profile staleness alone does not invalidate a correct underlying authority.

## Context recovery

When a current Profile surface exists and is cheap/available, it may be used first as a landing index:

```text
Profile? -> AGENTS / STATUS / TASK as required for the decision
         -> linked plan only when task-relevant
         -> Domain/navigation only when route is needed
         -> runtime/host evidence only when decision-relevant
```

`Profile?` is optional. Before state-changing or authority-sensitive decisions, read the actual normative/current authorities required by Project Governance; do not treat the Profile summary as their substitute.

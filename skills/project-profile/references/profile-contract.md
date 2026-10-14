# Project Profile contract

## Role

`PROJECT_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT`

The Profile is a concise context/index compiled from verified project authorities. It helps Web/local/agent context recovery but has no independent power to authorize work or override truth.

## Current projection surface

A project should have **one current Profile projection surface**. It may be a repository file such as `PROJECT_PROFILE.md`, ChatGPT Project Instructions, or another accepted project context surface.

If two surfaces are operationally required, declare one `PRIMARY_PROFILE_SURFACE` and treat the other as a derived mirror. Do not maintain two independently edited current Profiles. A stale mirror never overrides the primary projection or underlying authorities.

Do not create a new manifest merely to name the surface. Record the pointer in an existing project authority/context surface when that is useful and supported by the project.

## Mutation authority

Profile generation, comparison, or draft output can be read-only. Creating/updating a repository/project-managed Profile is state-changing and requires compatible active task authorization through Project Governance. Profile staleness by itself does not grant write authority.

## Recommended contents

- purpose and core business/product loop;
- a few stable concepts needed to understand the project;
- authority map/pointers;
- durable planning/navigation pointers;
- stable project environment roles;
- project-specific priorities, anti-goals, or risk cues;
- short Engineering Governance hook.

Do not copy detailed workflow, current progress, active task contracts, complete Domain maps, CI/PR state, handoff procedures, or runtime-local configuration.

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

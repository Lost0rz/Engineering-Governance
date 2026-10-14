# Project Profile contract

## Role

`PROJECT_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT`

The Profile is a concise, versioned context/index compiled from verified project authorities. It is useful for Web/local/agent context recovery, but has no independent power to authorize work or override a source of truth.

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

Refresh when a profile-owned summary or pointer materially changes, for example project purpose, stable concepts, authority locations, durable planning/navigation entry points, stable environment roles, or durable priorities/anti-goals.

Routine schema fields, task completion, PR/CI changes, or implementation details do not trigger Profile writes unless they change one of those profile-owned summaries.

When stale:

```text
AUTHORITY_WINS: YES
PROFILE_STATE: STALE
```

Refresh when authorized/useful. Read-only work reports staleness without mutation. Profile staleness alone does not invalidate a correct underlying authority.

## Context recovery

Use Profile as a landing page, then progressively disclose detail:

```text
Profile -> AGENTS / STATUS / TASK
        -> linked plan only when task-relevant
        -> Domain/navigation only when route is needed
        -> runtime/host evidence only when decision-relevant
```

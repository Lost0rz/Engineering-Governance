# Execution environment capabilities

Reusable governance defines **what capability must be resolved**; the current execution environment owns the concrete value.

Resolve a capability only when it can change the current execution decision. Common examples:

- Sub Agent model/reasoning default;
- usable parallel capacity;
- delegation/depth limits;
- material tool/connector availability;
- workspace/runtime/network constraints relevant to the task.

## Resolution order

1. current environment authoritative configuration/runtime metadata, when exposed;
2. current platform-managed default/capability, when it is the owning source;
3. `UNKNOWN` when the environment does not expose enough evidence.

Do not infer from another machine/context, controller model, handoff, repository prose, memory, or historical observation. Do not copy a Local value into Web/cloud policy or vice versa.

A project may explicitly define a portable configuration artifact; only then may that artifact govern the values/classes it owns.

## Optional evidence snapshot

Use only fields material to the task:

```text
ENVIRONMENT_CAPABILITY_SOURCE: <config | runtime/platform | portable project authority | UNKNOWN>
SUBAGENT_CONFIG: <observed environment-specific value | PLATFORM_DEFAULT | UNKNOWN>
PARALLEL_CAPACITY: <value | platform-managed | UNKNOWN>
DELEGATION_LIMIT: <value | platform-managed | UNKNOWN>
MATERIAL_TOOLS: <only task-relevant tools/capabilities | UNKNOWN>
WORKSPACE_RUNTIME_CONSTRAINTS: <only task-relevant constraints | NONE | UNKNOWN>
```

This snapshot is evidence about the current environment, not project task authority and not a cross-context default.

If a required capability is unavailable/unknown, use a safe topology or return the capability/environment gap to the controller rather than inventing a value.

# Execution environment capabilities

Reusable governance defines **what capability must be resolved**; the current execution environment owns the concrete value.

Resolve a capability only when it can change the current execution decision. Common examples:

- Sub Agent enablement and available role/profile support;
- Sub Agent model/reasoning configuration and observable effective runtime identity;
- usable parallel capacity;
- delegation/depth limits;
- material tool/connector availability;
- workspace/runtime/network constraints relevant to the task.

## Resolution order

1. current environment authoritative runtime metadata, when exposed;
2. current environment authoritative configuration for the relevant Sub Agent/default/role, when exposed;
3. current platform-managed default/capability, when it is the owning source;
4. `UNKNOWN` when the environment does not expose enough evidence.

Do not infer from another machine/context, controller model, handoff, repository prose, memory, or historical observation. Do not copy a Local value into Web/cloud policy or vice versa.

A project may explicitly define a portable configuration artifact; only then may that artifact govern the values/classes it owns.

## Configured versus effective runtime identity

Keep configuration evidence separate from runtime evidence:

```text
MODEL_SOURCE: <parent inheritance | agents default | role/custom config | runtime/platform | UNKNOWN>
MODEL_CONFIG: <configured model value | PLATFORM_DEFAULT | UNKNOWN>
REASONING_CONFIG: <configured reasoning value | PLATFORM_DEFAULT | UNKNOWN>
MODEL_EFFECTIVE: <observed runtime model | UNKNOWN>
REASONING_EFFECTIVE: <observed runtime reasoning | UNKNOWN>
```

A configured value may explain expected resolution but does not prove the effective runtime identity. If the runtime does not expose the final value, report `MODEL_EFFECTIVE: UNKNOWN` / `REASONING_EFFECTIVE: UNKNOWN` rather than copying configuration into those fields.

When no explicit delegated override exists and the platform defines parent/default inheritance, record the source as such only when the current environment/configuration evidence supports that resolution rule. Runtime verification is still preferred when available.

## Optional evidence snapshot

Use only fields material to the task:

```text
ENVIRONMENT_CAPABILITY_SOURCE: <config | runtime/platform | portable project authority | UNKNOWN>
SUBAGENT_ENABLED: <YES | NO | UNKNOWN>
SUBAGENT_ROLE_SUPPORT: <observed roles/profiles | platform-managed | UNKNOWN>
SUBAGENT_CONFIG: <bounded configured defaults/overrides | PLATFORM_DEFAULT | UNKNOWN>
SUBAGENT_RUNTIME: <effective observed model/reasoning | UNKNOWN>
PARALLEL_CAPACITY: <value | platform-managed | UNKNOWN>
DELEGATION_LIMIT: <value | platform-managed | UNKNOWN>
MATERIAL_TOOLS: <only task-relevant tools/capabilities | UNKNOWN>
WORKSPACE_RUNTIME_CONSTRAINTS: <only task-relevant constraints | NONE | UNKNOWN>
```

This snapshot is evidence about the current environment, not project task authority and not a cross-context default.

If a required capability is unavailable/unknown, choose a safe topology or return the capability/environment gap to the controller rather than inventing a value.

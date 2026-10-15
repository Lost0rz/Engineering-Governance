# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.1`.

Release provenance:

- Task: `EG-DESIGN-ROUTING-HARDENING-083`;
- source / merge SHA: `208279e5f3b7974c13a3446a3db2e8f27de7b688`;
- source PR: `#32 — feat: harden Design routing composition` — merged;
- main release run: `38658367623` — success;
- tag: `plugin-v0.7.1`;
- asset SHA-256: `8a2482eb4c0e28c642b5d27ffe34c0e64c0b8d64afbf9c51c6b83325013055db`;
- package scope: `plugin.json` + `skills/**` only;
- top-level Skills: exactly `9`.

`V071_RELEASE_ACCEPTANCE`: `PASS`.
`WEB_PLUGIN_SYNC_071`: `PASS`.

## Active capability hardening

Task `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084` is `ACTIVE` on branch:

`codex/local-execution-subagent-hardening-v072`

Start main HEAD:

`0a2febb5cc294609d5ebfe54a4e84da1216de2dd`

Purpose:

- make Sub Agent use explicitly efficiency-first rather than agent-count-first;
- connect planning work-package structure to execution-time topology selection without freezing runtime-specific choices in durable plans;
- add a concrete Sub Agent value gate, stable execution roles, dependency/writer-boundary analysis, and bounded redelegation behavior;
- distinguish configured Sub Agent model/reasoning values from observed effective runtime identity;
- expose execution topology, Sub Agent use, and observable model/reasoning evidence in governed execution receipts;
- add Local Codex runtime acceptance before any release/Web synchronization claim.

This task does **not** authorize a Web Plugin update in the current phase.

## Current execution capability baseline

The existing `execution-orchestrator` already supports:

- `INLINE`;
- `SEQUENTIAL_DELEGATED`;
- `PARALLEL_READ_ONLY`;
- `PARALLEL_DISJOINT_WRITERS`;
- environment-owned delegated-model policy;
- one-writer safety for overlapping semantic authority;
- bounded cross-context Agent Handoff and controller-side integration.

Task 084 hardens efficiency selection, planning/execution linkage, runtime model observability, role semantics, and receipts; it does not create a new top-level Skill or model-router runtime.

## Local distribution state

The last directly observed Air Local Codex installation remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

No local v0.7.x runtime freshness is inferred without a fresh local readback.

`LOCAL_PLUGIN_UPDATE_AVAILABLE`: `YES`.
`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`.

The source hardening will be prepared as a v0.7.2 candidate and tested locally before any release/Web Plugin synchronization decision.

## Published Web Plugin

The existing private personal Web Plugin remains v0.7.1:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- current Web release ID: `pluginrel_6ad01a9215e88191829245c5571fd160`;
- scope/discoverability: `USER / PRIVATE`.

No Task 084 Web synchronization has been performed or authorized.

## Control identity

Released semantic Plugin identity remains:

`208279e5f3b7974c13a3446a3db2e8f27de7b688`

Active Task 084 branch is an unreleased source candidate. Branch/source commits must not be reported as a released or installed runtime identity until the corresponding lifecycle step is actually verified.

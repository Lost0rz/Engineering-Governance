# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub tagged release remains `plugin-v0.7.1`.

Task 084 source is now on `main` as Plugin manifest version `0.7.2` for Local/Web runtime trial. This source merge and Web Plugin update are distribution steps; they do not by themselves establish Local runtime acceptance or a formal GitHub v0.7.2 tag/release.

## Active capability hardening

Task `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084` is:

`ACTIVE — DISTRIBUTED_FOR_RUNTIME_TRIAL`

PR #33 is merged. Main delivery merge:

`29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`

Accepted semantic candidate:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Latest pre-merge candidate validation:

- workflow: `Validate Plugin v0.7.2 Candidate`;
- run: `38663053412`;
- result: `success`;
- publication: none.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## Task 084 behavior now distributed

- Sub Agent use is efficiency-first, not mandatory;
- planning may expose bounded work packages/dependencies/writer boundaries/acceptance without selecting runtime topology;
- `execution-orchestrator` performs `SUBAGENT_DECISION: USE | DO_NOT_USE` at execution time;
- stable execution roles are `EXPLORER`, `WORKER`, `VERIFIER`, `REVIEWER`;
- overlapping semantic authority defaults to one writer;
- parallel writers require proven-disjoint authority/workspaces plus an integration boundary;
- Sub Agent redelegation is disabled by default;
- configured/default model/reasoning values are distinct from observed effective runtime identity;
- execution receipts expose `Execution topology`, `Subagents`, and `Subagent runtime`;
- cross-context EXECUTE Handoff Receipts preserve the same execution evidence;
- effective model/reasoning remains `UNKNOWN` when the runtime does not expose it.

## Local distribution / runtime state

Air Local Codex marketplace has been converted to a Git-backed marketplace for `engineering-governance-personal`, refreshed from `main`, and the plugin cache readback shows:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.7.2`

`LOCAL_PLUGIN_CACHE_072`: `OBSERVED`.

This proves local distribution/cache freshness, not runtime behavior inside a fresh Codex session.

Next Local evidence boundary:

- fresh session loaded plugin identity;
- local Sub Agent config/default source;
- inline negative case (`Subagents: NO`);
- useful delegated read-only case;
- writer-safety behavior;
- model/reasoning effective runtime observation where available, otherwise explicit `UNKNOWN`;
- execution/Handoff receipt readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`.

## Web Plugin

The existing private personal Web Plugin has been updated **in place** to v0.7.2:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.2`;
- current Web release ID: `pluginrel_6ad02855852c8191a7addd05d6026361`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root `plugin.json`: `0.7.2` read back;
- platform `.codex-plugin/plugin.json`: `0.7.2` read back;
- `execution-orchestrator`: Sub Agent value gate, stable roles and configured-vs-effective model evidence read back;
- `subagent-execution.md`: present and read back;
- Project Governance receipt: `Execution topology`, `Subagents`, `Subagent runtime` read back;
- Agent Handoff EXECUTE receipt: execution topology/Sub Agent/runtime evidence fields read back.

`WEB_PLUGIN_SYNC_072`: `PASS`.

## Control identity

Formal tagged release identity remains the v0.7.1 release source until a later formal v0.7.2 release lifecycle is authorized.

Task 084 semantic candidate identity:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Main merge carrying v0.7.2 source:

`29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`

Web runtime release identity:

`pluginrel_6ad02855852c8191a7addd05d6026361`

Later STATUS/TASK-only commits are control-only.

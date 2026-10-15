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

Task `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084` is:

`ACTIVE — MERGED_TO_MAIN_FOR_LOCAL_TRIAL`

PR #33 is merged. Main delivery merge:

`29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`

Post-merge control-only alignment may move literal `main` without changing the v0.7.2 semantic source.

Accepted semantic candidate:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Latest pre-merge candidate validation:

- workflow: `Validate Plugin v0.7.2 Candidate`;
- run: `38663053412`;
- result: `success`;
- publication: none.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## Task 084 source behavior now on main

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
- effective model/reasoning remains `UNKNOWN` when the Local runtime does not expose it.

## Local distribution / runtime state

The repository `main` manifest is now `0.7.2`, enabling repo-backed Local Codex refresh/install testing.

The last directly observed Air Local Codex installation remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

That local installation remains stale until a real refresh/install readback proves otherwise.

Next evidence boundary:

- refresh/install the repo-backed plugin from current `main`;
- read back installed version/path;
- inspect local Sub Agent config/default source;
- run inline/delegated/writer-safety/model-observation/receipt acceptance.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`.

## Published Web Plugin

The existing private personal Web Plugin remains v0.7.1:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- current Web release ID: `pluginrel_6ad01a9215e88191829245c5571fd160`;
- scope/discoverability: `USER / PRIVATE`.

`WEB_PLUGIN_UPDATE_084`: `NOT_PERFORMED / NOT_AUTHORIZED_THIS_PHASE`.

## Control identity

Formal released Plugin identity remains:

`208279e5f3b7974c13a3446a3db2e8f27de7b688`

Task 084 semantic candidate identity is:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Main merge carrying v0.7.2 source for Local trial:

`29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`

Later STATUS/TASK-only commits are control-only.

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

`ACTIVE — MAIN_MERGE_AUTHORIZED_FOR_LOCAL_TRIAL`

Branch:

`codex/local-execution-subagent-hardening-v072`

PR:

`#33 — feat: harden local execution and Sub Agent orchestration`

Start main HEAD:

`0a2febb5cc294609d5ebfe54a4e84da1216de2dd`

Accepted semantic candidate for Local trial:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Latest pre-merge candidate validation for branch HEAD before control-only merge authorization:

- workflow: `Validate Plugin v0.7.2 Candidate`;
- run: `38663053412`;
- result: `success`;
- publication: none.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## Task 084 source behavior

The v0.7.2 source candidate establishes:

- Sub Agent use is efficiency-first, not mandatory;
- planning may expose bounded work packages, dependencies, writer boundaries, acceptance and useful parallelizability without selecting runtime topology;
- `execution-orchestrator` performs `SUBAGENT_DECISION: USE | DO_NOT_USE` at execution time;
- stable execution roles are `EXPLORER`, `WORKER`, `VERIFIER`, `REVIEWER`;
- overlapping semantic authority defaults to one writer;
- parallel writers require proven-disjoint authority/workspaces plus an integration boundary;
- Sub Agent redelegation is disabled by default;
- configured/default model/reasoning values are distinct from observed effective runtime identity;
- Project Governance execution receipts expose `Execution topology`, `Subagents`, and `Subagent runtime`;
- cross-context EXECUTE Handoff Receipts can preserve the same execution evidence;
- effective model/reasoning remains `UNKNOWN` when the Local runtime does not expose it.

Task 084 does not create a new top-level Skill or a reusable model router.

## Distribution / runtime boundary

The user has authorized merging PR #33 to `main` before Local runtime acceptance because the repo-backed Local Codex plugin must see the new `0.7.2` source in order to test the new execution/receipt behavior.

This main merge is a **distribution/testing step only**:

- it does not establish `LOCAL_RUNTIME_ACCEPTANCE`;
- it does not create a formal v0.7.2 GitHub release/tag;
- it does not update the private Web Plugin.

The last directly observed Air Local Codex installation remains `0.6.8` at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

The repository manifest is now `0.7.2`, but that is not evidence that Local Codex has installed or executed it.

Next evidence boundary is Local Codex refresh/install from `main` followed by runtime acceptance covering:

- installed plugin identity readback;
- local Sub Agent configuration/default source;
- an inline negative case (`Subagents: NO`);
- a useful delegated read-only case;
- writer-safety behavior;
- model/reasoning effective runtime observation where available, otherwise explicit `UNKNOWN`;
- execution/Handoff receipt readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`.

## Published Web Plugin

The existing private personal Web Plugin remains v0.7.1:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- current Web release ID: `pluginrel_6ad01a92191829245c5571fd160`;
- scope/discoverability: `USER / PRIVATE`.

`WEB_PLUGIN_UPDATE_084`: `NOT_PERFORMED / NOT_AUTHORIZED_THIS_PHASE`.

## Control identity

Released formal Plugin identity remains:

`208279e5f3b7974c13a3446a3db2e8f27de7b688`

Task 084 semantic candidate identity for Local trial is:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

STATUS/TASK-only commits after that candidate are control-only and do not change its semantic content.

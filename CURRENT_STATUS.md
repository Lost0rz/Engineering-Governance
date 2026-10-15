# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published / distributed baseline

Formal GitHub tagged release remains `plugin-v0.7.1`.

Task 084 source is on `main` as Plugin manifest version `0.7.2`, the private Web Plugin is `0.7.2`, and Local Codex runtime acceptance has passed. A formal GitHub `plugin-v0.7.2` tag/release has not yet been created.

## Task 084 closeout

Task `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084` is:

`COMPLETE — LOCAL_RUNTIME_ACCEPTANCE_PASS`

Source delivery:

- PR `#33 — feat: harden local execution and Sub Agent orchestration` — `MERGED`;
- main delivery merge: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`;
- accepted semantic candidate: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- latest pre-merge candidate validation: run `38663053412` — `success`.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## v0.7.2 execution behavior

The distributed 0.7.2 capability establishes:

- Sub Agent use is efficiency-first, not mandatory;
- plans may expose work packages/dependencies/writer boundaries/acceptance without selecting runtime topology;
- `execution-orchestrator` performs `SUBAGENT_DECISION: USE | DO_NOT_USE` at execution time;
- stable roles are `EXPLORER`, `WORKER`, `VERIFIER`, `REVIEWER`;
- overlapping semantic authority defaults to one writer;
- parallel writers require proven-disjoint authority/workspaces plus an integration boundary;
- Sub Agent redelegation is disabled by default;
- configured/default model/reasoning values remain distinct from observed effective runtime identity;
- execution receipts expose `Execution topology`, `Subagents`, and `Subagent runtime`;
- cross-context EXECUTE Handoff Receipts preserve the same execution evidence;
- unobservable effective model/reasoning remains explicitly `UNKNOWN`.

## Local runtime acceptance

Disposable Air acceptance fixture:

`/Users/jack7788/Documents/eg-subagent-test`

Final fixture identity:

`0e0b6512af2b67b6cc689ba650597bf308d53b8d`

Final working tree: `CLEAN`.

Observed environment:

- Codex CLI `0.160.0`;
- Engineering Governance `0.7.2`;
- runtime-loaded plugin path: `/Users/jack7788/.codex/plugins/cache/created-by-me-remote/engineering-governance/0.7.2`;
- Sub Agent enabled;
- configured delegated model `gpt-6-luna`;
- configured delegated reasoning `xhigh`;
- configured max concurrent threads/session `3`;
- configured max depth `1`;
- effective controller/delegated model and reasoning identity not exposed and therefore reported `UNKNOWN`.

Acceptance results:

- inline negative control: `PASS`;
- parallel read-only `EXPLORER ×2`: `PASS`;
- shared semantic writer safety with one `WORKER`: `PASS`;
- disjoint-writer case: `NOT_USED` because Value Gate judged coordination cost greater than value;
- project-local override case: `NOT_TESTED` because the current CLI/config evidence did not establish a supported mechanism;
- user-level `~/.codex/config.toml` remained unchanged.

`LOCAL_RUNTIME_ACCEPTANCE`: `PASS`.

## Web Plugin

The existing private personal Web Plugin is updated in place to v0.7.2:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.2`;
- current Web release ID: `pluginrel_6ad02855852c8191a7addd05d6026361`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and platform manifests read back as `0.7.2`;
- Execution Orchestrator/Sub Agent contracts and Project Governance/Handoff receipt fields read back.

`WEB_PLUGIN_SYNC_072`: `PASS`.

## Residual non-blocking observations

- exact Sub Agent effective model/reasoning identity is not exposed by the observed runtime;
- exact overlap timestamps for the two read-only explorers were not exposed;
- project-local Sub Agent override support remains unproven;
- local distribution/cache naming has been observed under both `engineering-governance-personal` and `created-by-me-remote`. Both observed plugin versions are `0.7.2`; this is a future distribution-authority hygiene concern rather than a Task 084 blocker.

## Control identity

Formal tagged release identity remains the v0.7.1 release source until a separate v0.7.2 formal release lifecycle is authorized.

Task 084 semantic candidate:

`23b05c7f8847dd1868f05dd3fe5257aed94f635a`

Main merge carrying v0.7.2 source:

`29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`

Web runtime release identity:

`pluginrel_6ad02855852c8191a7addd05d6026361`

Local runtime acceptance fixture identity:

`0e0b6512af2b67b6cc689ba650597bf308d53b8d`

Task 084 closeout/control commits after semantic delivery remain control-only.

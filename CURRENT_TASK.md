# CURRENT TASK — Local Execution / Sub Agent Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

Task class: `CAPABILITY_HARDENING`

State: `COMPLETE — LOCAL_RUNTIME_ACCEPTANCE_PASS`

## Objective

Harden Local Codex execution so Sub Agents are used only when they materially improve throughput, context isolation, or verification quality.

Sub Agent use is an execution optimization, not a goal. Planning exposes executable structure; `execution-orchestrator` decides at execution time whether delegation is worthwhile in the current environment.

## Delivered behavior

- planning may expose bounded work packages, dependencies, writer boundaries and acceptance without freezing runtime topology;
- `execution-orchestrator` performs `SUBAGENT_DECISION: USE | DO_NOT_USE` at execution time;
- stable roles are `EXPLORER`, `WORKER`, `VERIFIER`, `REVIEWER`;
- overlapping semantic authority defaults to one writer;
- parallel writers require proven-disjoint authority/workspaces plus an integration boundary;
- Sub Agent redelegation is disabled by default;
- configured/default model/reasoning values remain distinct from observed effective runtime identity;
- Project Governance and cross-context EXECUTE receipts expose execution topology, Sub Agent use and runtime evidence without inventing unobserved effective identity.

## Source / distribution result

- Plugin manifest: `0.7.2`;
- semantic candidate HEAD: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- latest pre-merge validation run: `38663053412` — `success`;
- PR `#33 — feat: harden local execution and Sub Agent orchestration` merged to `main`;
- merge commit: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`;
- private Web Plugin updated in place to `0.7.2`;
- Web Plugin ID unchanged: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web release ID: `pluginrel_6ad02855852c8191a7addd05d6026361`;
- Web readback confirmed both manifests plus Execution Orchestrator, Sub Agent execution, Project Governance receipt, and Handoff execution evidence contracts.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.
`WEB_PLUGIN_SYNC_072`: `PASS`.

## Local runtime acceptance

Disposable Air fixture:

`/Users/jack7788/Documents/eg-subagent-test`

Observed final fixture identity:

`0e0b6512af2b67b6cc689ba650597bf308d53b8d`

Working tree: `CLEAN`.

Observed runtime:

- Codex CLI: `0.160.0`;
- Engineering Governance: `0.7.2`;
- runtime-loaded plugin path: `/Users/jack7788/.codex/plugins/cache/created-by-me-remote/engineering-governance/0.7.2`;
- Sub Agent enabled: `YES`;
- configured delegated model: `gpt-6-luna`;
- configured delegated reasoning: `xhigh`;
- configured `max_concurrent_threads_per_session`: `3`;
- configured `max_depth`: `1`;
- effective controller/Sub Agent model and reasoning identity: `UNKNOWN` because runtime did not expose them.

Acceptance cases:

- `CASE_INLINE`: `PASS` — small bounded work stayed `INLINE`, `Subagents: NO`;
- `CASE_PARALLEL_READ_ONLY`: `PASS` — independent `EXPLORER ×2` units were delegated before awaiting either result;
- `CASE_SHARED_WRITER`: `PASS` — one `WORKER` changed the shared semantic authority;
- `CASE_DISJOINT_WRITERS`: `NOT_USED` — Value Gate correctly judged two trivial edits not worth parallel-writer coordination;
- `PROJECT_LOCAL_OVERRIDE_TEST`: `NOT_TESTED` — current CLI/config evidence did not establish a supported project-local override mechanism;
- user-level `~/.codex/config.toml` hash remained unchanged during acceptance.

`LOCAL_RUNTIME_ACCEPTANCE`: `PASS`.

## Residual non-blocking observations

- effective model/reasoning identity remains unobservable and therefore correctly reported `UNKNOWN`;
- exact overlap timestamps for parallel explorers were not exposed;
- project-local Sub Agent override support remains unproven;
- local distribution has been observed under both `engineering-governance-personal` and runtime-loaded `created-by-me-remote` cache/source naming. Both observed versions are `0.7.2`; source/alias cleanup is distribution hygiene, not a Task 084 acceptance blocker.

## Explicit boundaries after closeout

- Task 084 does not authorize new feature work;
- do not create a reusable model router;
- do not hardcode one machine's model/capacity into reusable policy;
- formal GitHub v0.7.2 tag/release remains a separate lifecycle decision;
- further local marketplace/cache authority cleanup should be treated as bounded distribution maintenance if undertaken.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ROUTING-HARDENING-083` (`COMPLETE`)
- `PR`: `#33` (`MERGED`)
- `MERGE_COMMIT`: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`
- `TARGET_VERSION`: `0.7.2`
- `SEMANTIC_CANDIDATE_HEAD`: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`
- `SOURCE_VALIDATION`: `PASS`
- `WEB_PLUGIN_UPDATE`: `PASS`
- `WEB_RELEASE_ID`: `pluginrel_6ad02855852c8191a7addd05d6026361`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PASS`
- `LOCAL_ACCEPTANCE_FIXTURE_HEAD`: `0e0b6512af2b67b6cc689ba650597bf308d53b8d`
- `FORMAL_GITHUB_RELEASE_072`: `NOT_PERFORMED`
- `TASK_STATE`: `COMPLETE — LOCAL_RUNTIME_ACCEPTANCE_PASS`

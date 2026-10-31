# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-31.

## Formal published baseline

Formal GitHub Plugin release remains `plugin-v0.7.3`.

Publication identity:

- release PR: `#36` — `MERGED`;
- publication source SHA: `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- release workflow run: `38678260676` — `success`;
- tag: `plugin-v0.7.3` -> `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- release ID: `413399094`;
- asset: `engineering-governance-plugin.zip`;
- included top-level Skills: exactly `9`.

The formal GitHub release/tag was not moved by Task 091.

## Current distributed source

Task `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091` is source-complete and Web-distributed as Plugin version `0.7.5`.

Source semantic/plugin head before final control closeout: `109763036328e9616e417ebba3f075dc64212459`.

Distributed behavior:

- governed software/repository engineering remains inside the Engineering Governance capability graph once `project-governance` owns the task;
- external engineering frameworks/Skills/plugins may be read as reference/provenance/evidence but are not automatic runtime dependencies or peer routers;
- generated Handoff/Construction Cards may name only an Engineering Governance `CAPABILITY` or `NONE` and must not require external engineering Skill/plugin/framework names;
- TDD/debugging/review/planning/verification/completion expectations are expressed as behavior/acceptance requirements or owned Engineering Governance capability behavior, not imported external Skill dependencies;
- `execution-orchestrator` remains the reusable owner for decomposition, Sub Agent topology, delegation and review/integration lifecycle;
- concrete model/reasoning values remain environment-owned; external frameworks cannot escalate or override them as Engineering Governance policy;
- after a bounded reviewer finding is corrected, scoped re-review is preferred unless the correction invalidates the prior full-review evidence or owning acceptance explicitly requires another full review;
- historical/reference paths may retain external framework names without creating execution authority;
- no tenth top-level Skill was added.

Focused acceptance authority: `references/V075_ENGINEERING_FRAMEWORK_OWNERSHIP_ACCEPTANCE.md`.

Root `plugin.json`: `0.7.5`.

Top-level Skills remain exactly `9`.

## Web Plugin

The existing private personal Web Plugin is synchronized in place to `0.7.5`:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.5`;
- current Web release ID: `pluginrel_6ae578380c8c8191a7c1f7175fded5a4`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and `.codex-plugin` manifests read back as `0.7.5`;
- Project Governance framework ownership, global routing/composition, Execution Orchestrator ownership, Agent Handoff card gate, and Handoff contract changes read back from the current Web release.

`WEB_PLUGIN_SYNC_075`: `PASS`.

## Distribution model

Source authority: `Lost0rz/Engineering-Governance`.

Intentional projections:

1. persistent Local Git-backed Plugin installation;
2. account-synced Web/remote Plugin projection.

Local marketplace/source remains:

- marketplace: `engineering-governance-personal`;
- plugin/source: `engineering-governance`;
- Git source: `https://github.com/Lost0rz/Engineering-Governance.git`;
- ref: `main`.

The marketplace definition is Git-backed to `main` but the installed local plugin is a separate cached installation. Because the marketplace itself is local rather than a Git marketplace, local refresh uses plugin remove/add rather than `codex plugin marketplace upgrade`.

## Current task

Task `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`: `SOURCE_WEB_COMPLETE / LOCAL_REFRESH_PENDING`.

Task 090's pending local 0.7.4 refresh is superseded; local users should refresh directly to 0.7.5.

## Repository lifecycle

- Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- Task `EG-HUMAN-UI-ACCEPTANCE-089`: `MERGED / DISTRIBUTED_AS_0.7.4`;
- Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`: `WEB_SYNC_COMPLETE / LOCAL_0.7.4_REFRESH_SUPERSEDED_BY_091`;
- Task `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`: `SOURCE_WEB_COMPLETE / LOCAL_REFRESH_PENDING`.

## Downstream installation state

- private Web Plugin: `0.7.5` — `PASS`;
- Air Local Git-backed Plugin: 0.7.5 refresh pending observation;
- Mac mini Local Git-backed Plugin: 0.7.5 refresh pending observation;
- local refresh must be followed by a new Codex/Desktop session before loaded-version/Skill-catalog verification;
- no local installed/runtime 0.7.5 PASS is inferred from source or Web synchronization.

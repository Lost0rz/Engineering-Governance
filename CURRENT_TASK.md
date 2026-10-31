# CURRENT TASK — Engineering Framework Ownership Hardening / v0.7.5 Distribution

Date: 2026-10-31

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`

Task class: `CORRECTIVE / DISTRIBUTION`

State: `SOURCE_WEB_COMPLETE / LOCAL_REFRESH_PENDING`

## Objective

Make Engineering Governance the sole reusable engineering workflow/routing framework for governed software/repository work, so generated construction/handoff cards and runtime orchestration do not prescribe or depend on external engineering frameworks/Skills/plugins.

External frameworks may be inspected as reference input. Reusable methods that are worth keeping must be absorbed into the owning Engineering Governance Skill/module before they become part of governed execution.

## Delivered source behavior

Implemented in Plugin source version `0.7.5`:

- `project-governance` now owns the engineering framework boundary and keeps governed execution inside the Engineering Governance capability graph;
- `global-routing` and `capability-composition` define external frameworks as reference/provenance/evidence rather than peer runtime controllers;
- `execution-orchestrator` is the reusable owner for decomposition, Sub Agent topology, delegation, environment-owned model/reasoning resolution, review/integration lifecycle, and proportional scoped re-review;
- `agent-handoff` and `handoff-contract` reject external engineering Skill/plugin/framework names as required execution dependencies while allowing genuine reference-only mentions;
- global routing template carries the same framework-ownership boundary into adopted environments;
- `references/V075_ENGINEERING_FRAMEWORK_OWNERSHIP_ACCEPTANCE.md` covers routing, handoff-card, historical-path, capability-gap, execution/model, and review-loop regression cases;
- top-level Skill count remains exactly `9`.

Source semantic/plugin head before final control closeout:

`109763036328e9616e417ebba3f075dc64212459`

## Web Plugin result

Existing private Web Plugin updated in place:

- Plugin ID unchanged: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.5`;
- Web release ID: `pluginrel_6ae578380c8c8191a7c1f7175fded5a4`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and `.codex-plugin` manifests read back as `0.7.5`;
- Project Governance, global routing/composition, Execution Orchestrator, Agent Handoff, and Handoff contract changes read back from the current release.

`WEB_PLUGIN_SYNC_075`: `PASS`.

## Local update boundary

Local marketplace/source remains:

- marketplace: `engineering-governance-personal`;
- plugin/source: `engineering-governance`;
- source: `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`.

Task 090's pending 0.7.4 local refresh is superseded. Refresh directly to 0.7.5 with:

```bash
codex plugin remove engineering-governance@engineering-governance-personal --json
codex plugin add engineering-governance@engineering-governance-personal --json
codex plugin list --marketplace engineering-governance-personal --json
```

After refresh, start a new Codex/Desktop session and verify the loaded/cache manifest reports `0.7.5` and the current Skill catalog no longer contains any removed external framework plugin that should not participate in governed engineering.

Local runtime/install acceptance remains `PENDING_USER_EXECUTION`; no local PASS is inferred from source/Web synchronization.

## Release boundary

This task does not create or move a formal GitHub Release/tag. Formal GitHub release remains `plugin-v0.7.3` unless a separate formal-release task is requested.

## Stop boundary

Source and Web distribution are complete. Stop here pending local refresh evidence from the target machine.

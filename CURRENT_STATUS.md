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

The formal GitHub release/tag is not being moved by the current Web/local distribution task.

## Distributed source baseline before current task

Task `EG-HUMAN-UI-ACCEPTANCE-089` was merged and distributed as Plugin source version `0.7.4`.

- PR `#37 — feat: make product UI acceptance human-owned`: `MERGED` at `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- PR `#38 — chore: prepare plugin v0.7.4 web/local sync`: `MERGED`;
- v0.7.4 distribution source/merge commit: `57d118ae807414b593d39561653c0a5ee586587d`;
- root `plugin.json`: `0.7.4`;
- top-level Skills: exactly `9`.

The existing private Web Plugin was synchronized in place to `0.7.4`:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web release ID: `pluginrel_6ad448c957ec8191836973db40769c44`;
- scope/discoverability: `USER / PRIVATE`.

## Current task

Task `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`: `AUTHORIZED / IN_PROGRESS`.

Purpose: harden Engineering Governance so governed engineering remains inside the Engineering Governance capability graph. External engineering frameworks/Skills/plugins may be reference inputs but must not become execution dependencies, routing owners, model/delegation authorities, review-lifecycle controllers, or required Skill names in generated construction/handoff cards.

Planned distribution target: Plugin source/Web version `0.7.5`.

Task 090's pending local 0.7.4 refresh is superseded by Task 091; local users should refresh directly to 0.7.5 after the new source/Web delivery is complete.

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

Because the marketplace itself is local rather than a Git marketplace, local refresh uses plugin remove/add rather than `codex plugin marketplace upgrade`.

## Repository lifecycle

- Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- Task `EG-HUMAN-UI-ACCEPTANCE-089`: `MERGED / DISTRIBUTED_AS_0.7.4`;
- Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`: `WEB_SYNC_COMPLETE / LOCAL_0.7.4_REFRESH_SUPERSEDED_BY_091`;
- Task `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`: `AUTHORIZED / IN_PROGRESS`.

## Downstream installation state

- private Web Plugin: `0.7.4` before Task 091 update;
- Air Local Git-backed Plugin: 0.7.5 refresh not yet observed;
- Mac mini Local Git-backed Plugin: 0.7.5 refresh not yet observed;
- local refresh must be followed by a new Codex/Desktop session before loaded-version verification.

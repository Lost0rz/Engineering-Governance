# CURRENT TASK — Plugin v0.7.4 Web / Local Sync

Date: 2026-10-18

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`

Task class: `RELEASE / DISTRIBUTION`

State: `WEB_SYNC_COMPLETE / LOCAL_PENDING`

## Objective

Distribute the merged human UI acceptance boundary from Task 089 to the existing Web Plugin and the persistent Local Git-backed Plugin path without changing Plugin identity or sharing.

## Source basis

- Task `EG-HUMAN-UI-ACCEPTANCE-089`: source implementation accepted for distribution by the user;
- PR `#37 — feat: make product UI acceptance human-owned`: `MERGED` at `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- PR `#38 — chore: prepare plugin v0.7.4 web/local sync`: `MERGED`;
- v0.7.4 distribution source/merge commit: `57d118ae807414b593d39561653c0a5ee586587d`;
- source/plugin version: `0.7.4`.

## Web Plugin result

Existing private Web Plugin updated in place:

- Plugin ID unchanged: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.4`;
- Web release ID: `pluginrel_6ad448c957ec8191836973db40769c44`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and platform manifests read back as `0.7.4`;
- `skills/design/SKILL.md`, `skills/project-governance/references/verification-tiers.md`, `skills/agent-handoff/SKILL.md`, and `skills/agent-handoff/references/handoff-contract.md` read back with the human UI acceptance boundary present.

`WEB_PLUGIN_SYNC_074`: `PASS`.

## Local update boundary

Local marketplace/source remains:

- marketplace: `engineering-governance-personal`;
- plugin/source: `engineering-governance`;
- source: `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`.

Because the marketplace itself is local rather than a Git marketplace, refresh the plugin by remove/add rather than `codex plugin marketplace upgrade`.

Required user-executed commands:

```bash
codex plugin remove engineering-governance@engineering-governance-personal --json
codex plugin add engineering-governance@engineering-governance-personal --json
codex plugin list --marketplace engineering-governance-personal --json
```

After refresh, start a new Codex/Desktop session and verify the loaded/cache manifest reports `0.7.4`.

Local runtime/install acceptance remains `PENDING_USER_EXECUTION`; no local PASS is inferred from Web synchronization.

## Release boundary

This task does not create or move a formal GitHub Release/tag. Formal GitHub release remains `plugin-v0.7.3` unless a separate formal-release task is requested.

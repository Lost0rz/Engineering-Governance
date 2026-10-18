# CURRENT TASK — Plugin v0.7.4 Web / Local Sync

Date: 2026-10-18

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`

Task class: `RELEASE / DISTRIBUTION`

State: `ACTIVE`

Branch: `codex/plugin-v0.7.4-web-local-sync`

Control parent: `ae149990e0b86105642f2df3c1e50efd9f61e73c`

## Objective

Distribute the merged human UI acceptance boundary from Task 089 to the existing Web Plugin and the persistent Local Git-backed Plugin path without changing Plugin identity or sharing.

## Source basis

- Task `EG-HUMAN-UI-ACCEPTANCE-089`: source implementation accepted for distribution by the user;
- PR `#37 — feat: make product UI acceptance human-owned`: `MERGED`;
- merge commit: `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- source behavior keeps Playwright/Cypress/E2E/browser automation valid while making material product-interface acceptance human-owned by default.

## Distribution target

- source/plugin version: `0.7.4`;
- existing private Web Plugin ID remains `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web scope/discoverability must remain unchanged;
- Local marketplace remains `engineering-governance-personal` with plugin/source `engineering-governance` from `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`;
- local refresh must use plugin remove/add, not `codex plugin marketplace upgrade`, because the personal marketplace itself is local rather than a Git marketplace.

## Required checks

- merge the `0.7.4` manifest bump to `main`;
- update the existing Web Plugin in place from the same source content;
- read back Web Plugin version/release metadata and the changed human-acceptance rules;
- provide Local refresh and verification commands for `0.7.4`;
- do not claim Local runtime acceptance until the user runs the commands on the target machine.

## Boundary

This task authorizes Web Plugin synchronization and source distribution through `main`. It does not require creation of a new GitHub Release/tag; the last formal GitHub release may remain `plugin-v0.7.3` unless a separate formal-release task is requested.

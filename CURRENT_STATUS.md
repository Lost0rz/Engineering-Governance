# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-18.

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

The formal GitHub release/tag was not moved by the current Web/local distribution task.

## Source / distribution state

Task `EG-HUMAN-UI-ACCEPTANCE-089` is merged and distributed as Plugin source version `0.7.4`.

- PR `#37 — feat: make product UI acceptance human-owned`: `MERGED` at `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- PR `#38 — chore: prepare plugin v0.7.4 web/local sync`: `MERGED`;
- v0.7.4 distribution source/merge commit: `57d118ae807414b593d39561653c0a5ee586587d`;
- root `plugin.json`: `0.7.4`;
- top-level Skills remain exactly `9`.

Distributed behavior:

- Playwright/Cypress/E2E, DOM/state, accessibility and screenshot/visual-regression automation remain valid engineering verification;
- AI browser/Computer Use inspection remains allowed for debugging, diagnosis, evidence gathering, internal Design review and corrective work;
- AI/manual-style browser inspection cannot become `AUDIT_INDEPENDENCE: HUMAN` or `HUMAN_UI_ACCEPTANCE: PASS`;
- material real-product interface changes default to `HUMAN_UI_ACCEPTANCE: PENDING` until an explicit human decision;
- `NOT_REQUIRED` cannot be inferred from omission and requires an owning waiver or a non-product-interface acceptance surface;
- cross-context Handoff cards/receipts preserve the same acceptance owner.

## Web Plugin

The existing private personal Web Plugin is synchronized in place to `0.7.4`:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.4`;
- current Web release ID: `pluginrel_6ad448c957ec8191836973db40769c44`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root and `.codex-plugin` manifests read back as `0.7.4`;
- Design, Project Governance verification, Agent Handoff, and Handoff contract human-acceptance changes read back from the current release.

`WEB_PLUGIN_SYNC_074`: `PASS`.

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

## Current task

Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`: `WEB_SYNC_COMPLETE / LOCAL_PENDING`.

Web synchronization is complete. Local installation/runtime acceptance remains pending user execution on the target machine; no local PASS is inferred from the Web result.

## Repository lifecycle

- Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- Task `EG-HUMAN-UI-ACCEPTANCE-089`: `MERGED / DISTRIBUTED_AS_0.7.4`;
- PR #37: `MERGED`;
- PR #38: `MERGED`;
- Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`: `WEB_SYNC_COMPLETE / LOCAL_PENDING`.

## Downstream installation state

- private Web Plugin: `0.7.4` — `PASS`;
- Air Local Git-backed Plugin: `0.7.4` update pending observation;
- Mac mini Local Git-backed Plugin: `0.7.4` update pending observation;
- local update must be followed by a new Codex/Desktop session before loaded-version verification.

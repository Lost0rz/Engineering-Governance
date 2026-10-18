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

The formal GitHub release is not being moved or replaced by the current Web/local distribution task.

## Source state

Task `EG-HUMAN-UI-ACCEPTANCE-089` source work is merged.

- PR `#37 — feat: make product UI acceptance human-owned`: `MERGED`;
- merge commit / current source basis: `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- V0 documentation/rule self-check: `PASS`;
- no CI PASS was claimed or required for that bounded rule correction.

Merged behavior:

- Playwright/Cypress/E2E, DOM/state, accessibility and screenshot/visual-regression automation remain valid engineering verification;
- AI browser/Computer Use inspection remains allowed for debugging, diagnosis, evidence gathering, internal Design review and corrective work;
- AI/manual-style browser inspection cannot become `AUDIT_INDEPENDENCE: HUMAN` or `HUMAN_UI_ACCEPTANCE: PASS`;
- material real-product interface changes default to `HUMAN_UI_ACCEPTANCE: PENDING` until an explicit human decision;
- `NOT_REQUIRED` cannot be inferred from omission and requires an owning waiver or a non-product-interface acceptance surface;
- cross-context Handoff cards/receipts preserve the same acceptance owner.

## Web Plugin baseline

Before Task 090 synchronization, the existing private personal Web Plugin remains:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.3`;
- current Web release ID: `pluginrel_6ad04f006d348191928277d9a0e82c15`;
- scope/discoverability: `USER / PRIVATE` unchanged.

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

## Active task

Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090` is `ACTIVE` on branch `codex/plugin-v0.7.4-web-local-sync` from source/control parent `ae149990e0b86105642f2df3c1e50efd9f61e73c`.

Target:

- source manifest: `0.7.4`;
- merge version bump to `main`;
- update existing Web Plugin in place to `0.7.4` with identity/scope unchanged;
- provide user-executed Local refresh/verification commands for `0.7.4`;
- do not claim Local runtime acceptance until observed on the user's machine.

Formal GitHub release/tag remains `plugin-v0.7.3` unless a separate formal-release task is requested.

## Repository lifecycle

- Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- Task `EG-HUMAN-UI-ACCEPTANCE-089`: `MERGED`;
- PR #37: `MERGED` at `ae149990e0b86105642f2df3c1e50efd9f61e73c`;
- Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090`: `ACTIVE`.

## Downstream installation state

- private Web Plugin: `0.7.3` pending Task 090 sync;
- Air Local Git-backed Plugin: `0.7.4` update not yet observed;
- Mac mini Local Git-backed Plugin: `0.7.4` update not yet observed.

# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.4` pending Task 059 publication.

- Current formal release: `plugin-v0.5.4`.
- ChatGPT Web Plugin: `0.5.4`.
- Mac mini canonical Codex authority: `engineering-governance@engineering-governance-personal / 0.5.4`.
- MacBook Air canonical Codex authority: `engineering-governance@engineering-governance-personal / 0.5.4`.
- Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.

## Accepted v0.5.5 governance source

Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058` is complete and merged.

- Durable planning document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Independently audited Delivery / Semantic HEAD: `eed269cab32ecdfb52da87627386bcc77a9e42c6`.
- Accepted source merge commit: `58f06da1d4e5d0e86d2cb17bd13aa786d7a22cc6`.
- Post-merge control-only closeout: `6dbf83ea24b0322669bb384b9ed7c78474dcb860`.

Accepted semantics include:

- durable planning documents as optional long-lived design/plan authority, not a fourth control file;
- `CURRENT_TASK.md` as the single active execution authorization with optional bounded planning-document linkage;
- `CURRENT_STATUS.md` as the concise current project/planning snapshot;
- mandatory final Control Alignment Gate for governed state-changing handoff;
- mandatory alignment checking with conditional writes;
- explicit `UPDATED` / `UNCHANGED` receipt results;
- strict read-only stale-control reporting;
- continued `CONTROL_ONLY_DRIFT` / Delivery-Semantic HEAD separation and separate live repository-host gates.

## Current planning context

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Current work package: Plugin 0.5.5 formal release then ChatGPT Web update.
- Current task: `EG-PLUGIN-V0.5.5-RELEASE-WEB-059`.
- Task branch: `codex/plugin-v0.5.5-release-web`.
- Required sequence: GitHub Release first, Web Plugin second.

## Active development state

Task 059 is authorized and in release preparation.

Preflight verified:

- `main = 6dbf83ea24b0322669bb384b9ed7c78474dcb860`;
- root `plugin.json = 0.5.4` before bump;
- `plugin-v0.5.5` tag absent;
- `plugin-v0.5.5` GitHub Release absent;
- current `skills/**` adds one packaged reference relative to 0.5.4, so the expected Plugin payload entry count is `30` (`plugin.json` + 29 files under `skills/**`).

## Active problems and blockers

No release-preparation blocker is currently known.

## Next intended milestone

1. Bump manifest and integrate the one-shot `plugin-v0.5.5` release workflow.
2. Publish and verify the formal GitHub Release.
3. Update the existing ChatGPT Web Plugin to `0.5.5` while preserving identity/scope/audience.

Mac mini / MacBook Air convergence is intentionally deferred until after the Web update.

## Control alignment at task authorization

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Document alignment: `UNCHANGED`.
- `CURRENT_STATUS.md`: `UPDATED` — Task 059 is now the active distribution/release work.
- `CURRENT_TASK.md`: `UPDATED` — Task 059 is authorized.
- Control alignment: `PASS`.

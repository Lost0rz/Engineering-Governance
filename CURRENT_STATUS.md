# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release is now `plugin-v0.5.5`.

- Release title: `Engineering Governance Plugin v0.5.5`.
- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- Release asset: `engineering-governance-plugin.zip`.
- Asset size: `70649` bytes.
- SHA-256: `5a207ccd7f0a1c1449aa977f3fd2aa9cbf51512783a5abfeff106404855a0365`.
- Package file entries: `30`.
- Included top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- Package boundary: only `plugin.json` and `skills/**`.

The first release run `38395340941` failed before packaging/tag/release creation because its planning-document semantic assertion did not account for Markdown emphasis. PR #25 corrected only that workflow assertion; the Plugin payload did not change. The succeeding publication source is `8871327915396b8de458f3e5709e3f67e36eff8f`.

## Accepted v0.5.5 governance source

Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058` remains the accepted governance source baseline.

- Durable planning document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Independently audited Delivery / Semantic HEAD: `eed269cab32ecdfb52da87627386bcc77a9e42c6`.
- Accepted source merge commit: `58f06da1d4e5d0e86d2cb17bd13aa786d7a22cc6`.
- Post-merge control-only closeout: `6dbf83ea24b0322669bb384b9ed7c78474dcb860`.

Accepted semantics include durable planning-document linkage, a mandatory final Control Alignment Gate with conditional writes, explicit document/status/task reconciliation results, `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD separation, and separate live repository-host gates.

## ChatGPT Web Plugin

The existing ChatGPT Web Plugin has been updated in place to `0.5.5`.

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517` — unchanged.
- Web release ID: `pluginrel_6ace21fad9688191b0da844efcb6992e`.
- Scope: `USER` — unchanged.
- Discoverability: `PRIVATE` — unchanged.
- Both Web manifests report version `0.5.5`.
- Exactly three top-level Skills remain.
- `skills/project-governance/references/planning-documents.md` is present.
- Project Governance contains the mandatory Control Alignment Gate and accepted v0.5.5 semantics.

## Local Codex distribution state

Local convergence is intentionally not part of Task 059.

- Mac mini canonical Codex authority remains verified at `engineering-governance@engineering-governance-personal / 0.5.4` from the prior acceptance.
- MacBook Air canonical Codex authority remains verified at `engineering-governance@engineering-governance-personal / 0.5.4` from the prior acceptance.
- The Git-backed personal marketplace model remains the intended path for the next local convergence task.

## Active problems and blockers

No formal-release or ChatGPT Web Plugin blocker is currently known.

Local Mini/Air are intentionally one version behind the newly published/Web baseline until a separate local convergence task is authorized.

## Next intended milestone

Authorize a separate local Plugin convergence task to move Mac mini and MacBook Air from `0.5.4` to `0.5.5` through the existing Git-backed `engineering-governance-personal` marketplace, preserving one active authority on each machine.

This milestone is not execution authorization by itself.

## Control alignment at Task 059 closeout

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Document alignment: `UNCHANGED` — distribution/release did not change durable design.
- `CURRENT_STATUS.md`: `UPDATED` — formal release and Web Plugin now reflect `0.5.5`, while local machines remain explicitly pending.
- `CURRENT_TASK.md`: `UPDATED` — Task 059 reached its terminal release/Web-update outcome.
- Control alignment: `PASS`.

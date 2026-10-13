# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.4`.

- Release title: `Engineering Governance Plugin v0.5.4`
- Frozen publication source: `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`
- ChatGPT Web Plugin: `0.5.4`
- Mac mini canonical Codex authority: `engineering-governance@engineering-governance-personal / 0.5.4`
- MacBook Air canonical Codex authority: `engineering-governance@engineering-governance-personal / 0.5.4`
- Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.

## Accepted governance source

Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058` is complete and merged.

- Durable planning document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Independently audited Delivery / Semantic HEAD: `eed269cab32ecdfb52da87627386bcc77a9e42c6`
- PR #22: merged by squash.
- Merge commit / accepted repository source identity: `58f06da1d4e5d0e86d2cb17bd13aa786d7a22cc6`
- V0 scenario audit A–G: `PASS`.
- Independent Web audit: `PASS` with no design-level blocker.

Accepted semantics now include:

- durable planning documents as optional long-lived design/plan authority, not a fourth control file;
- `CURRENT_TASK.md` as the single active execution authorization with optional bounded planning-document linkage;
- `CURRENT_STATUS.md` as the concise current project/planning snapshot;
- mandatory final Control Alignment Gate for governed state-changing handoff;
- conditional control writes: checked every closeout, written only when owned semantics changed;
- mandatory receipt reporting of document/status/task alignment;
- strict read-only stale-control reporting without unauthorized mutation;
- continued `CONTROL_ONLY_DRIFT` / Delivery-Semantic HEAD separation and separate live repository-host gates.

## Active problems and blockers

No Task 058 source, audit, or merge blocker is known.

Plugin distribution remains intentionally at `0.5.4`; Task 058 did not bump, publish, or install `0.5.5`.

## Next intended milestone

Authorize a separate Plugin `0.5.5` distribution/release task to:

1. bump the portable manifest only after the merged source baseline is accepted;
2. update ChatGPT Web Plugin;
3. converge Mac mini and MacBook Air through the Git-backed personal marketplace;
4. publish the formal `plugin-v0.5.5` GitHub release.

This milestone is not yet an active execution authorization.

## Control alignment at merge closeout

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Document alignment: `UNCHANGED` — the merge did not change the durable design.
- `CURRENT_STATUS.md`: `UPDATED` — project state advanced from waiting for merge to merged/accepted source.
- `CURRENT_TASK.md`: `UPDATED` — Task 058 is terminal/complete.
- Control alignment: `PASS`

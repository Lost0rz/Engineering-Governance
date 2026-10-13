# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release is `plugin-v0.5.4`.

- Release title: `Engineering Governance Plugin v0.5.4`
- Frozen publication source: `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`
- GitHub Actions run: `38346638985` — `success`
- Release asset: `engineering-governance-plugin.zip`
- Asset size: `64200` bytes
- SHA-256: `2a39d1bf705b56b53f2514b5bb8012380606278989afabdc4f3c7424dd0f0367`
- Package file entries: `29`
- Included top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

## Accepted v0.5.4 governance and distribution state

- Accepted governance semantics from PR #18 are merged at `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Portable root `plugin.json` version `0.5.4` was integrated by PR #19 at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Repo-backed `engineering-governance-personal` marketplace was integrated by PR #20 at `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- ChatGPT Web Plugin is `0.5.4` with exactly three top-level Skills.
- Mac mini and MacBook Air are independently verified on one active `engineering-governance@engineering-governance-personal / 0.5.4` authority each.
- The 0.5.4 payload contains `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and the separate repository-host gate boundary.

## Current planning context

- Planning document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Current work package: Task 058 reusable Project Governance contract and template update.
- Current task: `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058`.
- Task branch: `codex/planning-doc-control-alignment-v055`.
- Draft PR: `#22` — open, draft, unmerged.

## Active development state

Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058` has completed source construction and V0 scenario verification and is waiting for independent Web audit.

Final source Delivery / Semantic HEAD for the audit is:

`eed269cab32ecdfb52da87627386bcc77a9e42c6`

The source candidate establishes:

- durable planning documents as optional long-lived design/plan authority, not a fourth control file;
- explicit Task-to-document work-package linkage with revision basis treated as provenance by default;
- Status as the current planning/project-position snapshot rather than detailed plan or history;
- a mandatory final Control Alignment Gate for state-changing handoff;
- conditional control writes with explicit `UPDATED` / `UNCHANGED` receipt results;
- strict read-only stale-control reporting without unauthorized mutation;
- preservation of v0.5.4 control-only drift, semantic evidence reuse, and separate live repository-host-gate semantics.

## V0 verification state

- Changed paths are limited to Task 058 controls, durable design, repository rule, Project Governance Skill/reference/template sources.
- `plugin.json` remains `0.5.4`.
- Exactly three top-level Skills remain.
- Acceptance scenarios A–G in the durable design document pass by direct rule inspection.
- No Plugin distribution/release mutation has occurred under Task 058.

## Active problems and blockers

No source-construction blocker is currently known. PR #22 must remain unmerged until independent Web audit accepts the source contract.

## Next intended milestone

Perform independent Web audit of PR #22. If accepted, merge Task 058 source first; only then authorize a separate Plugin `0.5.5` version/distribution/release task.

## Control alignment at current handoff

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Document alignment: `UNCHANGED`
- `CURRENT_STATUS.md`: `UPDATED` for the audit handoff/current milestone.
- `CURRENT_TASK.md`: `UPDATED` to `WAITING_FOR_INDEPENDENT_AUDIT` with PR #22 and frozen semantic source.
- Control alignment: `PASS`

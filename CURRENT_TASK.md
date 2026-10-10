# CURRENT TASK — v0.5 + Storage Affinity Integration and Clean Baseline

Task ID: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`

State: `READY_FOR_EXACT_HEAD_MERGE`

Mode: `INTEGRATED_SOURCE_AUDIT_ACCEPTED`

Authoritative branch: `main`

Integration branch: `codex/v0.5-storage-affinity-integration-v1`

## Owner-approved execution order

1. Integrate v0.5 Navigation Refresh + Follow-ups and Project Storage Affinity.
2. Audit the integrated source as a new exact candidate.
3. Merge only the audited integrated candidate to `main`.
4. After merge, classify and close terminal old PR/release/publisher branches that no longer carry unique active authority.
5. Preserve any branch with unique unresolved historical evidence until its disposition is explicit.
6. Finish with one clean authoritative `main` baseline before local Plugin installation/runtime behavior testing.

## Integrated candidate

`INTEGRATED_CANDIDATE_I1 = ee091fcdbad0e3edcec2b544067021068a0d54b9`

Start/control main for construction:

`467a92daa1bc6c43a7c874684a607c9a637a4dc9`

Inputs reconciled:

- v0.5 accepted frozen reusable A2: `ecadcf67bf00a5a82cd644cd822ad4d45a76a420`;
- Storage Affinity reusable implementation: `c250b9b081a93949f1d000165e64dcaa53610bdb`.

The old input branches are frozen/read-only inputs under this integration task and are not parallel writers.

## Integrated changed paths

Relative to the post-control integration base, exact I1 changes only:

- `AGENTS.md`
- `README.md`
- `docs/superpowers/plans/2026-10-09-v0.5.0-navigation-learning-findings-implementation.md`
- `docs/superpowers/specs/2026-10-09-navigation-learning-deferred-findings-v0.5.0-design.md`
- `plugin.json`
- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/references/refresh-policy.md`
- `skills/project-governance/SKILL.md`
- `skills/project-governance/assets/templates/AGENTS.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/workspace-lifecycle.md`

No root control file is part of I1.

## Integrated source audit

`INTEGRATED_SOURCE_AUDIT_I1 = PASS`

Findings:

- Critical: `0`
- Important: `0`

Fresh checks on exact I1 established:

1. `plugin.json` is `0.5.0`.
2. Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.
3. Global Router remains selection-only; its blob remains unchanged.
4. Non-overlapping Navigation/Follow-up files retain the accepted A2 contracts.
5. `project-governance/SKILL.md` and `development-flow.md` preserve both v0.5 and Storage Affinity semantics without contradictory ownership.
6. Storage Affinity retains canonical-root-first routing, project-local override, machine/runtime separation, ephemeral scratch allowance, and no universal host/volume rule.
7. Follow-ups remain non-blocking status memory only and never authorize repair.
8. Navigation refresh remains affected-only, no-churn for current routes, candidate-only in strict read-only mode, and historical snapshots cannot rewrite the current projection by themselves.
9. Root `AGENTS.md` scopes Web construction/local validation to Engineering-Governance only; Global Router is not broadened.
10. No fourth Skill/control file, Findings platform, storage subsystem, daemon, service, database, installer, or automatic remediation was introduced.
11. Maintainer Plan is explicitly marked historical where its old merge/release/test ordering was superseded by this task.
12. Live `main` was reverified at `467a92daa1bc6c43a7c874684a607c9a637a4dc9` after audit; no parallel drift occurred.

## Merge authorization

The user explicitly authorized this sequence: integrate first, then close old PR/branch debt, then test from the clean unique baseline.

Create an exact-head PR against `main` and merge only if:

- PR head equals the later control head whose only delta from I1 is root controls;
- live `main` remains `467a92daa1bc6c43a7c874684a607c9a637a4dc9` until merge;
- the control receipt proves `I1..B1` contains only `CURRENT_TASK.md` and `CURRENT_STATUS.md`.

After merge, do not release or run local Plugin V1 yet. Proceed directly to remote legacy branch/PR lifecycle closeout.

## Legacy branch closeout boundary

Safe deletion candidates after merge:

- branches fully contained in merged `main`;
- branches tied to already merged PRs;
- completed one-shot publisher branches whose release/tag/artifact evidence is durable elsewhere;
- superseded v0.5 design/implementation/storage branches once their reusable content is integrated into main and no unique unresolved evidence remains.

Do not delete a branch containing unique unresolved historical evidence. Classify it and retain explicitly if necessary.

## Final target

`EG_V0.5_INTEGRATED_MAIN_CLEAN_BASELINE_READY_FOR_INSTALL_TEST`

with exact merge SHA, remote branch inventory/dispositions, and no unresolved active parallel writer.

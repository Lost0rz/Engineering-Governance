# CURRENT TASK — v0.5 + Storage Affinity Integration and Clean Baseline

Task ID: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`

State: `AUTHORIZED_REMOTE_INTEGRATION`

Mode: `INTEGRATE_AUDIT_MERGE_THEN_LIFECYCLE_CLOSEOUT`

Authoritative branch: `main`

Integration branch: `codex/v0.5-storage-affinity-integration-v1`

## Objective

Create one authoritative Engineering-Governance v0.5 source baseline by integrating the already-audited Navigation Refresh + Follow-ups work with the already-audited Project Storage Affinity work on top of fresh `main`, reconcile their overlapping Project Governance surfaces, merge the integrated result to `main`, then close terminal legacy PR/release branches so the repository has one clean baseline before any local install/runtime behavior testing.

## Owner-approved execution order

1. Integrate v0.5 Navigation Refresh + Follow-ups and Project Storage Affinity first.
2. Audit the integrated source as a new candidate; prior branch audits are inputs, not substitutes for integrated-candidate audit.
3. Merge only the audited integrated candidate to `main`.
4. After merge, classify and close terminal old PR/release/publisher branches that no longer carry unique active authority.
5. Preserve any branch with unique unresolved historical evidence until its disposition is explicit.
6. Finish with one clean authoritative `main` baseline before local Plugin installation and real behavior testing.

## Inputs

- Fresh starting `main`: `d04bf63cefa7d48c843f0bccda0aabad3842c05f` before this task-control transition.
- v0.5 accepted frozen reusable candidate A2: `ecadcf67bf00a5a82cd644cd822ad4d45a76a420`.
- v0.5 implementation branch: `codex/navigation-learning-followups-v0.5.0-implementation`.
- Storage Affinity reusable implementation head: `c250b9b081a93949f1d000165e64dcaa53610bdb`.
- Storage Affinity branch: `codex/project-storage-affinity-v1`.

The v0.5 implementation branch and Storage Affinity branch are retained inputs, not parallel writers during integration. Do not mutate them while this integration task is active.

## Integration contract

Create `codex/v0.5-storage-affinity-integration-v1` from the fresh post-control `main` head.

Integrate the accepted reusable semantics from both inputs. Reconcile shared files deliberately rather than choosing one branch wholesale.

Known overlapping reusable surfaces include:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/development-flow.md`

The integrated result must preserve all of these semantics together:

### v0.5 Navigation + Follow-ups

- verified navigation corrections update only the affected accepted projection entry/fields;
- correct + freshness-current routes produce no write/churn;
- stale-but-same routes may refresh only evidence/freshness;
- unresolved replacements remain unknown/stale rather than guessed;
- historical/bounded snapshots do not rewrite the current projection without current-target evidence or explicit bounded mutation authority;
- strict read-only reports correction/Follow-up candidates without mutation;
- qualifying evidence-backed non-blocking adjacent issues are retained under `CURRENT_STATUS.md / Follow-ups` during normal state-changing status reconciliation;
- Follow-ups do not authorize repair; selected work must enter `CURRENT_TASK.md` before mutation;
- still-material Follow-ups survive unrelated status refresh and mere task selection.

### Project Storage Affinity

- resolve the canonical project root first;
- durable project-controlled development state follows the storage authority containing that canonical root by default;
- explicit project-local asset/path authority overrides the default;
- machine/runtime state remains a separate class and may stay machine-local;
- OS/tool-required ephemeral scratch may use system temp;
- unique/durable state must not be abandoned in unrelated temp/convenience locations at closure;
- no universal `/Volumes/Jack-Dev`, user-home, or Mac-mini rule;
- no mandatory storage manifest.

### Engineering-Governance repository-specific execution rule

Update root `AGENTS.md` only for this repository's durable execution split:

- Engineering-Governance Web/remote session owns reusable source construction, remote GitHub mutation, source audit, integration, and release preparation;
- local AI is used primarily for installed/runtime/behavior validation;
- reusable defects found locally return to the Web/remote Engineering-Governance flow for correction;
- this is repository-specific and must not be generalized to other projects or copied into Global Router.

## Version and routing

- Integrated Plugin version: `0.5.0`.
- Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.
- Global routing remains selection-only; do not add storage or Follow-up procedure to the managed global routing block.
- Do not create a fourth Skill, storage subsystem, Findings subsystem, daemon, service, database, installer, or automatic remediation runtime.

## Integrated source audit

This is a new candidate. Verify from its exact tree:

1. all v0.5 Navigation/Follow-up semantics remain intact;
2. all Storage Affinity semantics remain intact;
3. shared Project Governance files are coherent rather than duplicated/contradictory;
4. root `AGENTS.md` project-specific execution rule is correctly scoped;
5. `plugin.json` is exactly `0.5.0`;
6. exactly three top-level Skills remain;
7. Global Router is unchanged in responsibility and remains selection-only;
8. no prohibited hard-coded host/storage rule exists in reusable normative policy;
9. package payload remains `plugin.json + skills/**`;
10. changed scope contains no unrelated business-project/runtime/install mutation.

No local Plugin behavior test is authorized before the integrated baseline is merged and repository lifecycle closeout is complete.

## Merge gate

After integrated source audit passes:

- create/verify a PR against `main` or otherwise use an exact-head protected GitHub merge path;
- reverify live `main` before merge;
- merge only the exact audited integration head;
- verify post-merge `main` contains the exact integrated Plugin payload.

Do not publish a release yet.

## Legacy branch / PR closeout gate

After merge, classify remote non-main branches.

Safe cleanup candidates include branches whose commits are fully contained in `main`, merged-PR branches, and completed one-shot publisher branches whose release/tag/artifact evidence is already durable elsewhere.

Do not delete a branch merely because it is old. Preserve branches with unique unresolved historical evidence or still-active authority until their disposition is explicit.

The v0.5 design branch is expected to be superseded by the implementation/integrated history if no unique commits remain.

The target outcome is a clean remote repository baseline with `main` as the sole active development authority and only explicitly justified retained historical branches, if any.

## STOP conditions

STOP rather than improvise if:

- fresh `main` changes in a way that affects Plugin payload or this integration contract;
- either input branch has new reusable mutations beyond its audited candidate;
- integration loses one input's required semantics;
- a legacy branch contains unique work/evidence whose disposition is not established;
- exact integrated source identity cannot be proven before merge;
- cleanup would require deleting unresolved unique work.

## Out of scope until clean baseline

- local Plugin install/runtime V1;
- publication/release of v0.5.0;
- business-project mutation;
- changing the global installed `AGENTS.md` routing block;
- modifying installed Plugin cache/runtime.

## Final state

Success for this task is:

`EG_V0.5_INTEGRATED_MAIN_CLEAN_BASELINE_READY_FOR_INSTALL_TEST`

with exact integrated merge SHA, final remote branch inventory/dispositions, and no unresolved active parallel writer.

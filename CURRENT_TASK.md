# CURRENT TASK — EG-V01 Tooling Design

Task ID: `EG-V01-TOOLING-DESIGN-002`

State: `ACTIVE — LIFECYCLE CLEANUP / ARCHITECTURE DESIGN ONLY`

Mode: `TOOLING_FOUNDATION_DESIGN`

## Objective

Establish a clean post-v0.1 baseline, retire merged lifecycle residue safely, verify the reconciled entry-point documentation, and produce the first written architecture/design spec for a minimal reusable Bootstrap / Doctor / Audit tooling layer.

This is an **architectural design task**, not an implementation task.

## Accepted baseline

- Stable standard: `EngineeringGovernanceStandard` `0.1.0`.
- Stable closeout commit and required `v0.1.0` tag target: `738627a0caad330d277f60cfdaff5f153593135e`.
- PR #1: merged/closed.
- Merged task branch: `codex/eg-v01-reference-synthesis` at `96a3e2212bfa2ffcfcd31a64557f86380fa8d642`; lifecycle-complete but delete only after local safety proof.
- Accepted model: seven lifecycle layers, six cross-cutting axes, typed authorities, standalone profiles, orthogonal result/freshness/exception/decision semantics.
- Root `README.md` has already been reconciled on `main` to the accepted seven-layer model and correctly states the tooling is planned, not implemented.

## Gate 0 — local lifecycle cleanup and baseline

On the Mac mini canonical checkout:

1. fetch/prune and verify repository identity, branch, HEAD, working-tree state, worktrees, local branches, remote branches, and unique local-only commits;
2. fast-forward canonical `main` to the live remote control baseline;
3. prove the merged old task branch/worktree contains no unique unpushed work;
4. only then remove the old task worktree/local branch and delete remote `codex/eg-v01-reference-synthesis`;
5. verify no unexpected PR/worktree/branch lifecycle residue remains;
6. verify remote tag `v0.1.0` is absent, then create and push `v0.1.0` **only** at `738627a0caad330d277f60cfdaff5f153593135e`; STOP if the name exists at another target;
7. finish with one canonical clean checkout on `main` before creating the new design branch.

Never reset, force-delete, clean, stash, overwrite, or rebase unknown work to make cleanup pass.

## Gate 1 — create bounded design branch

After Gate 0 passes, create a fresh branch from current accepted `main`:

`codex/eg-v01-tooling-design`

If the branch already exists, inspect it and STOP on unexplained provenance rather than overwrite it.

## Gate 2 — verify entry-point baseline

On the task branch, verify root `README.md`:

- describes seven lifecycle layers;
- does not imply Bootstrap/Doctor/Audit already exist;
- remains navigational rather than becoming a second mutable control plane.

No README change is expected. If it differs from the verified remote baseline unexpectedly, STOP and report drift rather than silently rewriting it.

No unrelated cleanup/refactor is authorized.

## Gate 3 — architecture exploration

Read the accepted v0.1 contracts and compare at least these approaches:

1. **Skill-only:** reusable AI skill/procedure definitions, minimal/no deterministic executable core.
2. **Executable-core-first:** one local deterministic core/CLI with Bootstrap, Doctor and Audit commands; AI consumes its output.
3. **Hybrid:** one small deterministic core with thin AI skills/adapters for intent, judgment and review.

Evaluate each against:

- one canonical governance model shared by Bootstrap/Doctor/Audit;
- project-local/Git-native operation;
- no central database/service;
- no hidden background process;
- machine vs AI vs human review boundaries;
- cross-project portability;
- small-project overhead;
- offline/local operation where practical;
- evidence provenance and exact revisions;
- no governance tool becoming product/domain/runtime Authority;
- future extensibility without committing to MCP/enforcement now.

Recommend one approach with explicit trade-offs and YAGNI rationale. Do not choose a language/framework merely from preference; inspect the local environment and justify the smallest dependable implementation path.

## Gate 4 — required tooling semantics in the written design

The design must specify, at contract level:

### Shared core

- single canonical in-process/file model used by all three tools;
- stable identities/version pinning to `EngineeringGovernanceStandard 0.1.0`;
- authority routing, evidence, findings, freshness, exception and decision boundaries;
- deterministic vs AI/human judgment separation;
- output/report format and exit-code semantics conceptually, without implementing schemas yet.

### Bootstrap

- the only member of the trio allowed to propose/write repository governance setup;
- explicit target repository and preview/diff before writes;
- create missing governance artifacts only from an approved template/profile;
- never overwrite or reinterpret existing product/domain authorities silently;
- idempotent behavior and explicit conflict/STOP semantics;
- no automatic migration or remediation.

### Doctor

- read-only repository/control-plane health and drift check;
- verify repo identity, control files, task/status consistency, branch/PR/worktree lifecycle facts, declared standard/profile version and obvious stale authority/evidence pointers;
- no writes, repairs, branch changes, or hidden network mutations;
- fast/light enough for routine preflight.

### Audit

- read-only deeper evaluation against selected versioned checks/evidence;
- supports `MACHINE`, `AI_JUDGMENT`, `HUMAN`, `HYBRID` boundaries without presenting AI judgment as deterministic;
- records result separately from freshness/exception/project decision;
- produces findings/evidence references, never source-of-truth replacements;
- no enforcement or auto-remediation.

### Boundaries between the three

- shared model, no duplicate authority/state stores;
- Bootstrap writes setup only;
- Doctor diagnoses baseline/health only;
- Audit evaluates governance checks only;
- none owns product/domain/runtime facts.

## Gate 5 — written design artifact

Create:

`docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`

The written spec must include:

- user intent and success criteria;
- current accepted baseline;
- 2–3 approaches and recommendation;
- component boundaries and data flow;
- proposed repository layout;
- Bootstrap/Doctor/Audit responsibilities and non-responsibilities;
- write/read permissions and safety/STOP behavior;
- validation strategy and test levels for later implementation;
- migration/versioning approach;
- smallest first implementation slice;
- explicit deferred work;
- open questions that truly require user/product choice.

Perform a self-review for contradictions, over-design, duplicate authorities, hidden writers, unbounded scope, and conflict with v0.1.

## Gate 6 — handoff only, no implementation plan yet

Because this is architectural work, do **not** start implementation and do **not** write the detailed implementation plan before the written spec is reviewed by the user/Web.

When the spec is complete:

1. update `CURRENT_STATUS.md` with verified lifecycle cleanup/design state;
2. set this task to `WAITING_FOR_USER_SPEC_REVIEW`;
3. commit and push the design branch;
4. create a Draft PR if suitable;
5. verify remote head equals local head and the worktree is clean;
6. return the evidence receipt below.

## Explicitly forbidden in this task

- executable Bootstrap/Doctor/Audit implementation;
- CLI/source code or dependency manifests;
- machine-readable schema implementation;
- MCP;
- daemon/background/continuous service;
- enforcement or automatic remediation;
- pilot-repository modifications;
- unrelated refactor/cleanup;
- merging the design PR.

## Required receipt

```text
TASK_ID:
FINAL_STATE:

CONTROL_BASELINE_REMOTE_MAIN:
LOCAL_MAIN_AFTER_SYNC:
LOCAL_MAIN_REMOTE_MATCH:
MAIN_WORKING_TREE:

OLD_TASK_REMOTE_BRANCH_BEFORE:
OLD_TASK_UNIQUE_WORK_FOUND:
OLD_TASK_WORKTREE_REMOVED:
OLD_TASK_LOCAL_BRANCH_REMOVED:
OLD_TASK_REMOTE_BRANCH_REMOVED:

V0_1_TAG_CREATED:
V0_1_TAG_TARGET:
BASELINE_WORKTREE_COUNT:
BASELINE_OPEN_PRS:
BASELINE_CLEAN:

DESIGN_BRANCH:
DESIGN_HEAD:
REMOTE_DESIGN_HEAD:
LOCAL_REMOTE_MATCH:
DESIGN_WORKING_TREE:

README_BASELINE_VERIFIED:
DESIGN_SPEC:
APPROACH_RECOMMENDED:
BOOTSTRAP_CONTRACT_DEFINED:
DOCTOR_CONTRACT_DEFINED:
AUDIT_CONTRACT_DEFINED:
SHARED_MODEL_DEFINED:
IMPLEMENTATION_STARTED: NO

CHANGED_PATHS:
DRAFT_PR:
FINAL_STATE: WAITING_FOR_USER_SPEC_REVIEW | STOP
STOP_REASON:
```

STOP on unexplained drift, unknown local work, tag collision, branch provenance ambiguity, or any need to cross into executable implementation.

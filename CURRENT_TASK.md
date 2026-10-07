# CURRENT TASK — Phase A Skill Repository Skeleton Reset

Task ID: `EG-SKILLS-RESTRUCTURE-IMPL-009`

State: `AUTHORIZED_FOR_LOCAL_EXECUTION`

Mode: `IMPLEMENTATION`

## Objective

Execute Phase A of the accepted Engineering-Governance redesign: remove the retired live governance-runtime/research structure and establish the complete three-Skill repository skeleton with minimal valid Skill entrypoints, reference/template contracts, repository-level attribution metadata, and `V0` verification.

Do not perform later Skill enrichment in this task.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted design: `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`.
- Accepted implementation plan: `docs/superpowers/plans/2026-10-07-skill-repository-skeleton-reset-implementation-plan.md`.
- Plan creation commit: `82099ad7033d9bdc0aec6b7d880f157008157392`.
- Plan-review control baseline before this authorization: `4c91d767a98d34dc851c12532faf4fdf5551a373`.
- Authorized task branch: `codex/skill-repository-skeleton-reset`.
- Stable tag `v0.1.0` must continue to dereference to `738627a0caad330d277f60cfdaff5f153593135e`.
- The exact task-branch start SHA is the remote branch head created by Web from this authorization control commit. The local execution card supplies that SHA; mismatch is a STOP.

## Required execution method

- Read `AGENTS.md`, `CURRENT_STATUS.md`, this file, the accepted design, and the accepted implementation plan before editing.
- Use the existing canonical repository only as the source checkout; perform implementation in one fresh isolated worktree for the authorized task branch unless the local environment already provides an equivalent isolated task checkout.
- Execute the accepted implementation plan task-by-task. Do not re-plan or expand scope.
- Preserve task commits by the plan's boundaries so independent review can attribute changes.
- Push only the authorized task branch. Do not merge, rebase onto a newer control head, move tags, or modify unrelated branches.

## In scope

Exactly the Phase A work defined by the accepted plan:

1. enumerate and retire only the authorized obsolete live runtime/research/tooling paths;
2. rewrite `README.md` to the Skill-source identity and AI-adapted adoption model;
3. create `references/UPSTREAMS.md`, `references/LICENSE_NOTES.md`, and `examples/README.md`;
4. create exactly three Skill modules:
   - `skills/project-governance/`;
   - `skills/domain-navigation/`;
   - `skills/incident-doctor/`;
5. create every reference/template path locked by the plan with concise Phase A contracts;
6. preserve the stable Domain Map versus optional dynamic Repo Map distinction;
7. run the plan's `V0` checks;
8. record handoff evidence in this task file on the task branch and stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Out of scope

Do not:

- enrich the three Skills beyond Phase A contracts;
- add an installer or Bootstrap CLI;
- preserve or extend the old Doctor CLI/runtime as an active product;
- implement a Repo Map program;
- add executable navigation/diagnostic helpers;
- add a daemon, service, database, enforcement engine, automatic remediation, MCP prerequisite, or package/runtime dependency;
- copy upstream source code or long-form upstream text;
- create hypothetical validated examples;
- alter `v0.1.0`;
- merge the task branch.

## Risk and verification

Risk: `R0/R1 — repository layout/documentation migration with destructive live-tree deletion bounded by an exact manifest`.

Verification: `V0`.

Rationale: this slice introduces no runtime behavior, but deletion boundaries and repository identity must be exact. Run the plan's tree/frontmatter/path/tag/Git checks; do not run or recreate the retired Python runtime suite merely because it historically existed.

## Acceptance criteria

All Phase A acceptance criteria from the accepted plan must pass, including:

- full target skeleton exists;
- exactly three intended top-level Skill modules exist;
- previous Python runtime/tests and authorized legacy trees are absent from the live task branch;
- README states Skill-source / AI-adapted / no-installer behavior;
- Skill entrypoints have distinct valid triggers and boundaries;
- all control, Domain, and Incident templates exist;
- upstream/license metadata is truthful and reports no Phase A upstream code/text copying;
- no executable product/runtime surface or dependency manifest is introduced;
- `v0.1.0^{}` is unchanged;
- the task branch is pushed, clean, and local/remote heads match.

## STOP conditions

STOP immediately and report evidence without improvising if any of the following occurs:

- the remote authorized task-branch SHA or live remote `main` does not match the execution card at Gate 0;
- the canonical checkout is dirty or contains unpreserved local work;
- `git ls-files` shows an unexpected tracked path in or adjacent to the retirement set that the accepted plan does not authorize deleting;
- any task requires broadening deletion by guesswork;
- the stable tag target differs from `738627a0caad330d277f60cfdaff5f153593135e`;
- completing Phase A would require executable product code, a new dependency, installer behavior, or later-phase enrichment;
- a plan check fails for a reason not resolvable within the exact Phase A scope;
- control/remote head drifts during execution in a way that changes task authority.

## Handoff requirements

Before returning to Web:

- record start branch SHA and final task-branch SHA;
- record the exact retired roots/files and the three created Skill modules;
- summarize each `V0` command/result;
- record stable-tag target;
- record `git status --short`;
- record remote task-branch SHA and prove local/remote match;
- set task state to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
- commit and push that handoff update;
- do not merge.

## Current stop point

`AUTHORIZED_FOR_LOCAL_EXECUTION`

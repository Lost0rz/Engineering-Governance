# CURRENT TASK — Phase A Skill Repository Skeleton Reset

Task ID: `EG-SKILLS-RESTRUCTURE-IMPL-009`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

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

## Executor handoff — Phase A V0

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`. Implementation is complete; do not treat this executor report as acceptance or merge authorization.

### Branch and synchronization evidence

- `START_HEAD`: `954593b82a666bebf677636ce4f3cf08c07ceddd`.
- `PRE_HANDOFF_CONTENT_HEAD`: `68be12d41afc721311a06b973cc3fc3bb107a1bb`.
- `FINAL_HEAD`: this handoff-control commit; resolve its exact SHA from the authorized task branch HEAD and executor receipt.
- `REMOTE_HEAD`: verified after push to equal this handoff-control commit; exact SHA is in the executor receipt.
- `LOCAL_REMOTE_MATCH`: `PASS` after the handoff update was pushed and compared.
- `WORKING_TREE`: clean after the handoff commit/push; exact `git status --porcelain` result is in the executor receipt.
- Live `origin/main` remained `954593b82a666bebf677636ce4f3cf08c07ceddd` before handoff; no main change was made.

### Retirement manifest

`RETIREMENT_MANIFEST`: the exact `git ls-files` manifest contained 47 tracked paths, all under the authorized retirement roots or the three explicitly named legacy artifacts. Every listed path was retired; no adjacent or unexpected path was deleted.

```text
docs/governance/v0.1/README.md
docs/governance/v0.1/adversarial-review.md
docs/governance/v0.1/authority-model.md
docs/governance/v0.1/checks-evidence-findings.md
docs/governance/v0.1/exceptions-freshness-versioning.md
docs/governance/v0.1/lifecycle.md
docs/governance/v0.1/project-profile.md
docs/governance/v0.1/standard.md
docs/reality-checks/investdesk.md
docs/reference-audit/README.md
docs/reference-audit/allstar.md
docs/reference-audit/arc42.md
docs/reference-audit/backstage.md
docs/reference-audit/ddd-context-mapping.md
docs/reference-audit/madr.md
docs/reference-audit/opa-conftest.md
docs/reference-audit/opentelemetry.md
docs/reference-audit/scorecard.md
docs/reference-audit/synthesis.md
docs/superpowers/plans/2026-10-07-bootstrap-minimal-control-plane-implementation-plan.md
docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md
docs/superpowers/specs/2026-10-07-tooling-foundation-design.md
src/engineering_governance/__init__.py
src/engineering_governance/__main__.py
src/engineering_governance/control_reader.py
src/engineering_governance/doctor.py
src/engineering_governance/git_reader.py
src/engineering_governance/model.py
src/engineering_governance/report.py
tests/fixtures/doctor/inconsistent-task-id/AGENTS.md
tests/fixtures/doctor/inconsistent-task-id/CURRENT_STATUS.md
tests/fixtures/doctor/inconsistent-task-id/CURRENT_TASK.md
tests/fixtures/doctor/malformed-task/AGENTS.md
tests/fixtures/doctor/malformed-task/CURRENT_STATUS.md
tests/fixtures/doctor/malformed-task/CURRENT_TASK.md
tests/fixtures/doctor/pass/AGENTS.md
tests/fixtures/doctor/pass/CURRENT_STATUS.md
tests/fixtures/doctor/pass/CURRENT_TASK.md
tests/fixtures/doctor/unverified-missing-status/AGENTS.md
tests/fixtures/doctor/unverified-missing-status/CURRENT_TASK.md
tests/support.py
tests/test_cli.py
tests/test_control_reader.py
tests/test_doctor.py
tests/test_git_reader.py
tests/test_model.py
tests/test_report.py
```

`CREATED_SKILL_MODULES`:

- `skills/project-governance/`
- `skills/domain-navigation/`
- `skills/incident-doctor/`

Exactly these three top-level Skill directories exist. All planned reference, template, and `scripts/README.md` paths exist; local Markdown links in the Skill entrypoints resolve.

`V0_CHECK_RESULTS`:

- Task 1 retirement manifest and pre-change identity checks: `PASS`; 47 authorized tracked paths, no unexpected paths.
- Tasks 1–4 per-task path/frontmatter/content-boundary verifications: `PASS` after each task commit. Task 4's first check exposed a missing literal `retire` in its lifecycle wording; that wording was corrected within scope and the exact check then passed.
- Task 5 `find skills -mindepth 1 -maxdepth 1 -type d -print | sort`: `PASS`; exactly the three Skill directories above.
- Task 5 Python frontmatter verification: `PASS`; all three entrypoints have frontmatter, non-empty descriptions, and distinct expected names.
- Task 5 skeleton and retired-root checks: `PASS`; every locked path exists and `src`, `tests`, `docs/governance`, `docs/reality-checks`, and `docs/reference-audit` are absent.
- Task 5 executable-source scan: `PASS`; no `.py`, `.js`, `.ts`, `.sh`, `.rb`, `.go`, or `.rs` files under `skills/`, `references/`, or `examples/`.
- Task 5 dependency-manifest scan: `PASS`; no `pyproject.toml`, requirements file, `package.json`, `Cargo.toml`, or `go.mod` is tracked.
- Task 5 upstream/license checks: `PASS`; all four named upstream references exist and `LICENSE_NOTES.md` states no upstream code or long-form text was copied.
- Skill trigger and local path check: `PASS`; all three descriptions match the accepted plan and every relative Markdown link in each Skill entrypoint resolves.
- Task 1 README rejection-pattern and stable-tag checks: `PASS`; `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Live remote authority check before handoff: `PASS`; `origin/main` remained at the expected SHA, the task branch matched local HEAD, and the peeled stable tag matched its target.
- Historical Python runtime suite: not run, as required for V0 after retiring that runtime.

### Scope and provenance

- `STABLE_TAG_TARGET`: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- `UNEXPECTED_PATHS_FOUND`: none.
- `SCOPE_EXPANSION`: no.
- `UPSTREAM_CODE_COPIED`: no.
- `EXECUTABLE_RUNTIME_ADDED`: no.

### Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

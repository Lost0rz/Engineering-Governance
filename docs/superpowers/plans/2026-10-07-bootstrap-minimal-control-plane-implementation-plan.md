# Bootstrap Minimal Control Plane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the first directly usable Bootstrap capability: preview and explicitly confirmed creation of a minimal root-level governance control plane without overwriting, repairing, migrating, or inventing an active task.

**Architecture:** Reuse the existing local repository identity reader and CLI. Add one versioned in-code starter template (`minimal-control-plane.v1`) plus a small Bootstrap engine that renders three root controls, classifies each as `CREATE` or `NO_CHANGE`, computes an immutable preview-plan digest, and on apply recomputes the exact plan before any create-if-absent writes. The first slice requires a clean target repository so HEAD plus clean-state verification is the safe target-state boundary; dirty-target support is explicitly deferred rather than implementing a broad state-fingerprinting subsystem now.

**Tech Stack:** Python 3.11+, standard library only, Git local read-only probes, `unittest`, existing `engineering_governance` package and module CLI.

**Spec:** `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`

## Global Constraints

- Runtime floor remains Python 3.11+ and standard-library-only.
- Bootstrap is the only writer; Doctor remains read-only and unchanged.
- No network access, remote Git query, ref/branch/worktree mutation, migration, repair, enforcement, remediation, Audit, AI runtime, MCP, daemon, database, package installer, or third-party dependency.
- Target path is explicit. Repository identity must be established through the existing local Git reader.
- First-slice target must be clean at preview and apply. Dirty targets STOP instead of being fingerprinted or normalized.
- Approved template is exactly `minimal-control-plane.v1`; unsupported template versions STOP.
- Candidate paths are root-only: `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.
- Generic Bootstrap never creates an active task. The starter `CURRENT_TASK.md` is an explicit `NONE / NO_ACTIVE_TASK / IDLE` control.
- Existing exact candidate content is `NO_CHANGE`; any differing file, directory, symlink, or other candidate-path type is `CONFLICT / STOP` and is never overwritten.
- Preview is fully read-only. Apply requires the same named actor and an exact preview plan identity supplied through a separate `apply` command.
- Apply re-reads identity/state, re-renders, and recomputes the plan. Any mismatch STOPs before writes.
- Writes use create-if-absent semantics only. A concurrent appearance never gets overwritten.
- Command exits preserve the accepted semantics: `0` truthful preview/apply/NO_CHANGE; `2` unsafe/fatal STOP; `3` internal fatal.
- The stable `v0.1.0` tag must not move.

## First-slice public interface

```text
PYTHONPATH=src python3.11 -m engineering_governance bootstrap preview <target> \
  --template minimal-control-plane.v1 \
  --project-name <explicit-project-name> \
  --actor <explicit-human-actor>

PYTHONPATH=src python3.11 -m engineering_governance bootstrap apply <target> \
  --template minimal-control-plane.v1 \
  --project-name <same-project-name> \
  --actor <same-human-actor> \
  --confirm-plan sha256:<exact-preview-plan-digest>
```

The CLI does not persist a plan file. Preview emits one canonical JSON line containing the plan identity and entries. Apply emits one canonical JSON line describing the recomputed plan and created/no-change paths.

## Approved starter content semantics

`minimal-control-plane.v1` renders exactly three UTF-8 root files from an explicitly supplied project name. No repository name, domain authority, owner, branch, or active task is inferred.

`AGENTS.md` states only the durable starter rules: the project name, accepted `EngineeringGovernanceStandard 0.1.0`, `CURRENT_STATUS.md` as the current verified snapshot, `CURRENT_TASK.md` as the sole execution authorization, no work without an explicit active task, and `UNKNOWN` for unverified project facts.

`CURRENT_STATUS.md` identifies the supplied project name, standard `0.1.0`, `Active task: NONE`, and `State: BOOTSTRAPPED — NO_ACTIVE_TASK`; observation time remains `UNKNOWN` rather than being invented by Bootstrap.

`CURRENT_TASK.md` contains exactly one parseable task contract with `Task ID: NONE`, `State: NO_ACTIVE_TASK`, `Mode: IDLE`, and an explicit statement that no execution task is authorized. This makes a freshly bootstrapped repository Doctor-readable without fabricating product work.

## Review Focus

1. **Existing path ambiguity:** a symlink/directory/special file at any candidate path must STOP with no overwrite and no earlier speculative writes.
2. **Preview/apply drift:** HEAD change, dirty-state change, actor/project/template change, or candidate-path change between preview and apply must invalidate the confirmed plan before writes.
3. **Exact rerun idempotence:** three exact starter files must preview/apply as `NO_CHANGE` with exit `0` and zero writes.
4. **Concurrent create race:** if a candidate path appears after apply revalidation, create-if-absent must refuse overwrite; already-created authorized files may remain, and a later fresh preview must classify them `NO_CHANGE` rather than treating them as corruption.
5. **Path confinement:** rendered candidate paths must remain the exact three root basenames; traversal, nested output, or alternate template-controlled paths are impossible in this slice.

---

### Task 1: Bootstrap model, template, and clean-state probe

**Files:**
- Modify: `src/engineering_governance/model.py`
- Modify: `src/engineering_governance/git_reader.py`
- Create: `src/engineering_governance/bootstrap_templates.py`
- Create: `tests/test_bootstrap_templates.py`
- Modify: `tests/test_git_reader.py`

**Interfaces:**
- Consumes: existing `RepositoryIdentity`, `CommandResult`, `GitRunner`, `run_git_readonly()`, `read_repository()`.
- Produces: `BootstrapAction`, `BootstrapPlanEntry`, `BootstrapPlan`, `BootstrapApplyResult`; `render_minimal_control_plane(project_name: str) -> tuple[tuple[str, bytes], ...]`; `read_repository_clean(root: Path, *, git_runner: GitRunner) -> bool`.

- [ ] **Step 1: Write failing model/template tests**

Add tests that require:
- `minimal-control-plane.v1` renders exactly `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` in deterministic order;
- rendered bytes contain the explicitly supplied project name and standard `0.1.0`;
- `CURRENT_TASK.md` contains `Task ID: NONE`, `State: NO_ACTIVE_TASK`, and `Mode: IDLE`;
- `CURRENT_STATUS.md` references `NONE` so the existing Doctor consistency check can match it;
- the renderer rejects blank/control-character project names rather than inferring a value.

- [ ] **Step 2: Run focused tests and observe RED**

Run:
`PYTHONPATH=src python3.11 -m unittest tests.test_bootstrap_templates tests.test_git_reader -v`

Expected: new Bootstrap/template and clean-state tests fail because the interfaces are absent; existing Git-reader tests remain green.

- [ ] **Step 3: Add the minimal data model and approved template renderer**

Add immutable Bootstrap records to `model.py` and implement `render_minimal_control_plane(project_name: str)` in `bootstrap_templates.py`. Keep the starter content exactly within the semantics above; do not add a template registry or file-based packaging layer.

- [ ] **Step 4: Add one read-only clean-state Git probe**

Extend the local Git allowlist only for:
`git status --porcelain=v1 --untracked-files=all`

Implement `read_repository_clean(root, git_runner=...) -> bool`. Preserve `GIT_OPTIONAL_LOCKS=0`, timeouts, repository-selection environment rejection, and no remote operations.

- [ ] **Step 5: Run focused tests to GREEN**

Run the same focused command and require all tests pass.

- [ ] **Step 6: Commit Task 1**

Commit only the model/template/Git-reader/tests attributable to this task.

### Task 2: Read-only Bootstrap preview and plan identity

**Files:**
- Create: `src/engineering_governance/bootstrap.py`
- Create: `tests/test_bootstrap.py`

**Interfaces:**
- Consumes: Task 1 Bootstrap records, template renderer, `read_repository()`, and `read_repository_clean()`.
- Produces: `build_bootstrap_preview(target: Path, *, template_version: str, project_name: str, actor: str, git_runner: GitRunner, file_reader: Callable[[Path], bytes]) -> BootstrapPlan`; `serialize_bootstrap_plan(plan: BootstrapPlan) -> str`.

- [ ] **Step 1: Write failing preview tests**

Add tests for:
- clean repository with all three candidate paths absent -> three `CREATE` entries and one stable `sha256:` plan identity;
- exact pre-existing rendered content -> `NO_CHANGE` entries and no writes;
- mixed exact/absent -> deterministic `NO_CHANGE` + `CREATE` plan;
- differing regular file -> `CONFLICT / STOP`;
- candidate symlink/directory -> `CONFLICT / STOP`;
- dirty target -> STOP;
- unsupported template -> STOP;
- blank actor -> STOP;
- preview leaves working-tree files and Git metadata byte-for-byte unchanged.

- [ ] **Step 2: Run focused preview tests and observe RED**

Run:
`PYTHONPATH=src python3.11 -m unittest tests.test_bootstrap -v`

Expected: fail because Bootstrap preview is absent.

- [ ] **Step 3: Implement deterministic preview**

`build_bootstrap_preview()` must:
1. resolve the explicit repository with existing `read_repository()`;
2. require non-empty actor and clean target;
3. render the one approved template;
4. inspect only the three root candidate paths with `lstat`/`read_bytes`;
5. classify only exact content as `NO_CHANGE`, absence as `CREATE`, and every differing/ambiguous type as STOP;
6. compute a canonical plan digest over standard/template identity, canonical root, HEAD, branch/detached state, clean-state marker, project name, actor, ordered candidate paths/actions/rendered content digests and sizes.

Do not write files or persist the plan.

- [ ] **Step 4: Add Review Focus preview cases**

Pin path ambiguity, exact rerun idempotence, and root-only path confinement in focused tests.

- [ ] **Step 5: Run focused preview tests to GREEN**

Require all `tests.test_bootstrap` preview tests pass.

- [ ] **Step 6: Commit Task 2**

Commit only preview engine/tests.

### Task 3: Exact-plan apply with create-if-absent safety

**Files:**
- Modify: `src/engineering_governance/bootstrap.py`
- Modify: `tests/test_bootstrap.py`

**Interfaces:**
- Consumes: `build_bootstrap_preview()` and `BootstrapPlan` from Task 2.
- Produces: `apply_bootstrap(target: Path, *, template_version: str, project_name: str, actor: str, confirmed_plan_identity: str, git_runner: GitRunner, file_reader: Callable[[Path], bytes], create_exclusive: Callable[[Path, bytes], None]) -> BootstrapApplyResult`; `serialize_bootstrap_apply_result(result: BootstrapApplyResult) -> str`.

- [ ] **Step 1: Write failing apply tests**

Add tests that require:
- exact confirmed plan creates all three missing files and returns their paths;
- rerun after creation yields all `NO_CHANGE`, exit-success semantics, and zero writes;
- wrong plan identity STOPs before writes;
- changed actor/project/template STOPs because recomputed identity differs;
- HEAD or dirty-state drift STOPs before writes;
- candidate content/path type drift STOPs before writes;
- exclusive-create collision never overwrites the appeared file;
- simulated collision after one successful authorized create reports STOP without deleting or rewriting the already-created authorized file, and a fresh preview classifies that exact created file as `NO_CHANGE`.

- [ ] **Step 2: Run focused apply tests and observe RED**

Run:
`PYTHONPATH=src python3.11 -m unittest tests.test_bootstrap -v`

Expected: apply-specific tests fail because apply is absent.

- [ ] **Step 3: Implement revalidation and exclusive creation**

`apply_bootstrap()` recomputes the preview from the same explicit inputs, requires exact plan-identity equality, then creates only `CREATE` entries using an exclusive-create primitive equivalent to `os.open(path, O_WRONLY | O_CREAT | O_EXCL, 0o644)`. It never opens an existing candidate for writing and never rolls back by deleting authorized files already created before a later race STOP.

- [ ] **Step 4: Run focused apply tests to GREEN**

Require all Bootstrap engine tests pass.

- [ ] **Step 5: Commit Task 3**

Commit only apply engine/tests.

### Task 4: Bootstrap CLI, integration proof, and README

**Files:**
- Modify: `src/engineering_governance/__main__.py`
- Modify: `tests/test_cli.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: Task 2/3 preview/apply functions and serializers.
- Produces: public `bootstrap preview` and `bootstrap apply` module-CLI paths defined above.

- [ ] **Step 1: Write failing CLI tests**

Add subprocess-level tests for:
- preview emits exactly one JSON line, exit `0`, and no target mutation;
- apply with the exact preview digest creates only the three approved root controls and exits `0`;
- second preview/apply is `NO_CHANGE` and does not rewrite mtimes/content;
- missing/unsupported template, blank actor/project name, missing `--confirm-plan`, non-repository target, dirty target, conflict, and changed-plan conditions return command-level nonzero/STOP without unsafe writes;
- Doctor CLI behavior remains unchanged.

- [ ] **Step 2: Run focused CLI tests and observe RED**

Run:
`PYTHONPATH=src python3.11 -m unittest tests.test_cli -v`

Expected: new Bootstrap CLI cases fail because the subcommands are absent; Doctor CLI tests remain green.

- [ ] **Step 3: Wire only the approved CLI surface**

Extend stdlib `argparse` with `bootstrap preview` and `bootstrap apply`. Keep Doctor routing untouched. Map Bootstrap STOP/internal failures to the accepted `0/2/3` command semantics with bounded single-line stderr diagnostics and no traceback.

- [ ] **Step 4: Update README minimally**

Document both Bootstrap commands, the clean-target requirement, one approved template version, explicit actor/plan confirmation, and no-overwrite behavior. State that Audit remains unimplemented.

- [ ] **Step 5: Run focused CLI tests to GREEN**

Require all CLI tests pass.

- [ ] **Step 6: Run the full regression suite**

Run exactly:
`PYTHONPATH=src python3.11 -m unittest discover -s tests -v`

Require zero failures. Record the exact final test count; do not pre-normalize it to an expected number.

- [ ] **Step 7: Re-check write and scope boundaries**

Verify:
- no network/remote Git operation was added;
- no ref/branch/worktree mutation command is allowed;
- preview tests prove no filesystem/Git mutation;
- apply writes only the three approved root candidate paths and only via create-if-absent;
- no dependency/package/installer/framework file was added;
- `v0.1.0^{commit}` remains `738627a0caad330d277f60cfdaff5f153593135e`;
- Audit/AI/MCP/enforcement/migration remain absent.

- [ ] **Step 8: Commit Task 4 and prepare independent review handoff**

Push one authorized task branch, open a Draft PR, record RED/GREEN/full-suite evidence in `CURRENT_STATUS.md` and `CURRENT_TASK.md`, and stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`. Do not merge or clean the task worktree before independent Web review.

## Self-review result

- **Spec coverage:** The plan implements the accepted Bootstrap preview/approval/apply contract, `CREATE`/`NO_CHANGE`/conflict semantics, actor/plan binding, explicit target, create-if-absent behavior, offline/local scope, exit semantics, idempotence, and no-overwrite requirement. Audit/AI and migration remain deferred.
- **Deliberate first-slice restriction:** The design allows binding arbitrary index/worktree state; this plan instead requires a clean target at preview and apply. That is a stricter safe subset and avoids adding a broad dirty-state fingerprint subsystem before real usage proves it necessary.
- **Open design question resolved for this slice:** The starter artifact set is the existing three-file control plane, but the generic task file is explicitly idle (`NONE / NO_ACTIVE_TASK / IDLE`), so Bootstrap does not invent active work or authority.
- **Type/interface consistency:** Task 2 owns preview creation/serialization; Task 3 consumes that exact plan and owns apply; Task 4 only adapts those functions to CLI.
- **Proportion:** Four independently reviewable tasks produce one working vertical Bootstrap slice. No template registry, profile inheritance, installer, schema framework, remote integration, or diagnostic expansion is added.
# Doctor Foundation Implementation Plan

**Task:** `EG-V01-DOCTOR-FOUNDATION-PLAN-003`
**Plan state:** `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`
**Planning method:** `superpowers:writing-plans`
**Plan baseline:** `codex/eg-v01-tooling-design` at `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`
**Accepted standard:** `EngineeringGovernanceStandard 0.1.0`

## Goal

Implement one small, offline, read-only Doctor foundation after this plan is independently reviewed and a separate implementation task authorizes the work. The slice observes a local Git repository root and revision, reads the three root control files, checks a small deterministic relationship between the current task and status, and emits one immutable versioned base report to stdout.

This document is a plan only. It does not authorize or perform implementation.

## Architecture

Use a standard-library-only package with five small responsibilities:

1. `model.py` owns immutable shared records and result/freshness types.
2. `git_reader.py` observes the target root, Git common directory, HEAD, and symbolic branch using an allowlist of local read-only Git commands.
3. `control_reader.py` reads only root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`; it returns content identities and deterministic consistency observations without interpreting domain or product meaning.
4. `report.py` builds a frozen Doctor base report and its content identity using canonical JSON.
5. `doctor.py` coordinates readers, writes either one report to stdout or a bounded STOP diagnostic to stderr, and returns the command exit code.

There is no `__main__.py`, argument parser, console script, package manifest, or command installer in this slice. `run_doctor` is a directly callable library function whose streams and inputs are injected for focused tests. No module writes to the target or persists a report.

## Tech Stack

- macOS on Apple silicon; Python 3.11 or newer.
- Python standard library only, including `dataclasses`, `enum`, `hashlib`, `json`, `pathlib`, `subprocess`, `tempfile`, and `unittest`.
- Local Git executable for repository observation and synthetic test repository setup.
- Offline by default. Doctor must not invoke a network-capable Git command or read remote PR state.
- No database, cache, report store, daemon, or background process.

Any third-party runtime dependency discovered during implementation is a STOP requiring a separately reviewed task; it is not part of this plan.

## Spec path

Accepted design: [`docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`](../specs/2026-10-07-tooling-foundation-design.md), especially Sections 6, 10, 12, 13, 15, 16, 17, 18, and 19.

The slice preserves the Hybrid recommendation and `EngineeringGovernanceStandard 0.1.0`. Bootstrap, deeper Audit, and AI contribution execution remain unimplemented and outside this plan.

## Global Constraints

- Read only the explicit target. Do not write, repair, reformat, or normalize any target file.
- Do not call `fetch`, `pull`, `push`, `remote`, `ls-remote`, GitHub APIs, or any other network path. Do not change remotes, refs, branches, index, or worktrees.
- Do not infer project facts from missing controls, a detached HEAD, an unknown revision, or an unavailable value.
- Emit no persistent report or hidden state. A caller's shell redirection is outside the library's behavior.
- Do not add `pyproject.toml`, requirements files, schema files, CLI entry points, skills, templates, check registries, Bootstrap, deeper Audit, AIContribution composition, enforcement, CI gates, migration, remediation, or pilot changes.
- The only implementation files described below are future paths. This planning task must not create or modify `src/*`, `tests/*`, or `fixtures/*`.

## Review Focus

1. A non-repository or ambiguous target cannot establish trusted identity: emit no normal report, write a bounded STOP diagnostic, return `2`.
2. A missing root control is reportable evidence incompleteness: mark the affected evaluation `UNVERIFIED`, freshness `UNKNOWN`, record the missing path, emit the truthful report, and return `0`.
3. An existing but unreadable, invalid-UTF-8, non-regular, or structurally malformed required root control is fatal: emit no normal report and return `2`.
4. A detached HEAD is represented as `branch: null` and `detached: true`; it is not silently assigned a branch or treated as a fatal error.
5. An unborn repository may still have an identified root; report the revision as unknown and the identity evaluation as `UNVERIFIED` / `UNKNOWN`, with exit `0`.
6. A readable task/status identifier mismatch is a deterministic `FAIL` finding, not a command failure; the report is emitted and the exit code is `0`.
7. `UNVERIFIED` and unknown freshness must never be promoted to `PASS` by aggregation or serialization.
8. Fatal STOP must not be encoded as a normal evaluation result or serialized as a Doctor report.
9. A dirty target's tracked and untracked content, file modes, Git metadata, and index remain byte-for-byte unchanged after Doctor runs.
10. Refs and `git worktree list --porcelain` output are identical before and after a Doctor run, including when a linked worktree already exists.
11. The only Git subprocess arguments are the exact local read-only identity probes listed below. A prohibited command is rejected before subprocess execution; no network call is made.
12. Report serialization is stable for the same report value, independent of mapping insertion order; its identity is the SHA-256 digest of the canonical report payload without the identity field.
13. Control evidence contains paths and content digests, not copied control-file bodies. Missing, stale, or unknown values remain explicit limitations.

## Exact Future File Map

No paths in this section are created by the current planning task.

### Source files

- `src/engineering_governance/__init__.py` — package marker and intentionally small public exports.
- `src/engineering_governance/model.py` — frozen records, enums, and cross-module types.
- `src/engineering_governance/git_reader.py` — Git runner allowlist and local repository identity observation.
- `src/engineering_governance/control_reader.py` — root control-file reads, digests, and minimal consistency check.
- `src/engineering_governance/report.py` — immutable report construction and canonical JSON serialization.
- `src/engineering_governance/doctor.py` — orchestration, stdout/stderr behavior, and exit-code mapping.

### Test files

- `tests/support.py` — temporary Git repository builder and before/after mutation snapshots.
- `tests/test_model.py` — enum, frozen-record, and field invariant tests.
- `tests/test_git_reader.py` — repository root/HEAD/branch observations and Git command allowlist.
- `tests/test_control_reader.py` — present/missing/unreadable/malformed controls and consistency semantics.
- `tests/test_report.py` — report envelope, canonical JSON, digest, and immutable value behavior.
- `tests/test_doctor.py` — stdout/exit behavior, fixture matrix, and end-to-end read-only proof.

### Synthetic control fixtures

These are text fixtures, not committed Git repositories. `tests/support.py` copies a fixture into a temporary directory and initializes a local Git repository there; it removes the temporary repository after the test.

- `tests/fixtures/doctor/pass/AGENTS.md`
- `tests/fixtures/doctor/pass/CURRENT_STATUS.md`
- `tests/fixtures/doctor/pass/CURRENT_TASK.md`
- `tests/fixtures/doctor/unverified-missing-status/AGENTS.md`
- `tests/fixtures/doctor/unverified-missing-status/CURRENT_TASK.md` — deliberately no `CURRENT_STATUS.md`.
- `tests/fixtures/doctor/inconsistent-task-id/AGENTS.md`
- `tests/fixtures/doctor/inconsistent-task-id/CURRENT_STATUS.md`
- `tests/fixtures/doctor/inconsistent-task-id/CURRENT_TASK.md`
- `tests/fixtures/doctor/malformed-task/AGENTS.md`
- `tests/fixtures/doctor/malformed-task/CURRENT_STATUS.md`
- `tests/fixtures/doctor/malformed-task/CURRENT_TASK.md` — deliberately lacks the required unique task identity/state fields.

Unreadable-file behavior is tested through an injected reader raising `PermissionError`; this avoids permission-bit tests whose behavior differs under privileged macOS test users.

## Shared Types and Exact Interfaces

All cross-module values live in `model.py`. Use `@dataclass(frozen=True, slots=True)` and tuples for nested collections; do not expose mutable dictionaries as stored report state.

```python
class EvaluationResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNVERIFIED = "UNVERIFIED"
    NOT_APPLICABLE = "NOT_APPLICABLE"

class Freshness(str, Enum):
    CURRENT = "CURRENT"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"

class ControlState(str, Enum):
    PRESENT = "PRESENT"
    MISSING = "MISSING"

@dataclass(frozen=True, slots=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str

class DoctorStop(Exception):
    # Classified target/root-input failure; doctor.py maps this to exit 2.
    code: str
    safe_summary: str

    def __init__(self, code: str, safe_summary: str) -> None: ...

@dataclass(frozen=True, slots=True)
class RepositoryIdentity:
    root: str                 # canonical absolute Git top-level path
    git_common_dir: str       # canonical absolute common Git directory
    head: str | None          # full object ID, or None for an unborn repository
    branch: str | None        # symbolic branch, or None for detached HEAD
    detached: bool | None    # None only when HEAD cannot be resolved

@dataclass(frozen=True, slots=True)
class ControlFileObservation:
    path: str                 # one of the three root-relative control paths
    state: ControlState
    sha256: str | None        # digest of exact bytes; never include file body
    size_bytes: int | None

@dataclass(frozen=True, slots=True)
class Evaluation:
    check_id: str
    result: EvaluationResult
    freshness: Freshness
    evidence_paths: tuple[str, ...]
    limitations: tuple[str, ...]

@dataclass(frozen=True, slots=True)
class ControlSnapshot:
    files: tuple[ControlFileObservation, ...]  # fixed order: AGENTS, STATUS, TASK
    task_id: str | None       # None when CURRENT_TASK.md is missing
    task_state: str | None    # None when CURRENT_TASK.md is missing
    consistency: Evaluation
    presence: Evaluation

@dataclass(frozen=True, slots=True)
class DoctorReport:
    report_version: str
    tool_version: str
    standard_version: str
    observed_at: str
    target: RepositoryIdentity
    overall_result: EvaluationResult
    evaluations: tuple[Evaluation, ...]
    controls: tuple[ControlFileObservation, ...]
    limitations: tuple[str, ...]
    report_identity: str
```

Reader and report interfaces:

```python
GitRunner = Callable[[Path, tuple[str, ...], float], CommandResult]
FileReader = Callable[[Path], bytes]
Clock = Callable[[], datetime]

def run_git_readonly(
    cwd: Path, args: tuple[str, ...], timeout_seconds: float = 5.0
) -> CommandResult: ...

def read_repository(
    target: Path, *, git_runner: GitRunner
) -> RepositoryIdentity: ...

def read_controls(
    root: Path, *, file_reader: FileReader
) -> ControlSnapshot: ...

def build_doctor_report(
    target: RepositoryIdentity,
    controls: ControlSnapshot,
    observed_at: datetime,
) -> DoctorReport: ...

def serialize_report(report: DoctorReport) -> str: ...

def _report_payload(
    report: DoctorReport, *, include_identity: bool
) -> dict[str, object]: ...

def _canonical_json(payload: Mapping[str, object]) -> bytes: ...

def run_doctor(
    target: Path,
    *,
    stdout: TextIO,
    stderr: TextIO,
    git_runner: GitRunner,
    file_reader: FileReader,
    clock: Clock,
) -> int: ...
```

`run_doctor` is the library's testable invocation boundary, not a CLI entry point. The implementation task must supply real standard-library adapters from `subprocess.run`, `Path.read_bytes`, and an aware UTC clock; tests inject recording/failing adapters and fixed time. `run_git_readonly` accepts only these exact argument tuples: `("rev-parse", "--show-toplevel")`, `("rev-parse", "--git-common-dir")`, `("rev-parse", "--verify", "HEAD")`, and `("symbolic-ref", "--quiet", "--short", "HEAD")`. Reject every other tuple before launching a process. Invoke with `shell=False`, a bounded timeout, `GIT_OPTIONAL_LOCKS=0`, and `GIT_TERMINAL_PROMPT=0`. Do not read configured remotes.

## Frozen First-Slice Semantics

### Repository identity

Resolve the supplied target strictly to an existing directory, then ask local Git for the canonical top-level and common Git directory. The local identity is exactly those canonical paths plus the full HEAD object ID and symbolic branch observation. Do not treat an origin URL as identity and do not claim a globally unique repository identifier.

- A path that does not resolve to a directory, is outside a Git worktree, or cannot establish a trustworthy root is command-level fatal/unsafe STOP (`2`).
- A detached HEAD with a resolvable object ID is valid and is represented by `branch=None`, `detached=True`.
- An unborn or otherwise unresolvable HEAD with a known root is reportable as `head=None`; preserve its symbolic branch if Git reports one. Its identity evaluation is `UNVERIFIED` / `UNKNOWN`; exit `0`. Do not claim why the revision is unavailable.
- `symbolic-ref` exit `0` means a branch exists; exit `1` means detached only when HEAD exists. If HEAD cannot be verified and no symbolic branch exists, set `detached=None` rather than inferring a detached state. Failure to establish the root/common directory remains STOP (`2`).
- Do not call `git status`, because refreshing index state is unnecessary for this slice. Do not inspect/update refs or worktrees from Doctor.

### Control-file and consistency rules

Inspect exactly root-level `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`, in that fixed order.

- A missing file is an observed absence, not a parse failure. Its observation is `MISSING`, its dependent evaluation is `UNVERIFIED` / `UNKNOWN`, its path is recorded as a limitation, and the command returns `0` with a report.
- Check file type with read-only `lstat`; an existing symlink or non-regular control is a fatal root-input failure. An existing regular control that cannot be read, contains invalid UTF-8, or is blank is also fatal. Emit no normal report and return `2`.
- `CURRENT_TASK.md` must contain exactly one non-empty `Task ID:` line and exactly one non-empty `State:` line. Missing or duplicate fields are structurally malformed root input and return `2`. Do not interpret the task state value or infer task meaning.
- Parse those labels only at the start of a line after optional horizontal whitespace; trim the value and remove one surrounding pair of backticks when present. The task ID must be one non-whitespace token; the state may contain spaces. This is a narrow reader rule, not a general Markdown parser or machine-readable schema.
- When both `CURRENT_TASK.md` and `CURRENT_STATUS.md` are present, the exact parsed task ID must occur as a whole token in the status text. A mismatch or absent reference is a deterministic control-consistency `FAIL` with `CURRENT` freshness; it is still a truthful report and returns `0`.
- When `CURRENT_TASK.md` is missing, leave `task_id` and `task_state` as `None`; do not infer them from the status file. The dependent presence/consistency evaluations remain `UNVERIFIED` / `UNKNOWN`.
- `AGENTS.md` is checked for presence, regular-file type, UTF-8 readability, and non-blank content only. Do not interpret its prose as product policy.
- Use fixed evaluation IDs and order: `doctor.repository.identity`, `doctor.controls.presence`, `doctor.controls.task_status_consistency`. A present/readable set with a matching task reference yields `PASS` / `CURRENT` for applicable checks. Missing controls yield `UNVERIFIED` / `UNKNOWN`; a readable mismatch yields `FAIL` / `CURRENT` for consistency.
- `overall_result` uses only this fixed precedence: any `FAIL` → `FAIL`; otherwise any `UNVERIFIED` → `UNVERIFIED`; otherwise all `NOT_APPLICABLE` → `NOT_APPLICABLE`; otherwise `PASS`. Keep each per-check result in the report so the summary cannot hide unresolved evidence. This slice does not produce `NOT_APPLICABLE`.
- Freshness is `CURRENT` only for content read successfully during this invocation. This slice has no historical evidence baseline, so it does not claim `STALE`; unavailable or missing evidence is `UNKNOWN`.

### Report envelope and deterministic serialization

The report is a frozen in-memory `DoctorReport` serialized once to stdout as one UTF-8 JSON line. The envelope is fixed to:

- `report_version`: `"doctor-base.v1"`;
- `tool_version`: `"doctor-foundation/1"`, distinct from the standard version;
- `standard_version`: `"EngineeringGovernanceStandard 0.1.0"`;
- `observed_at`: timezone-aware UTC ISO-8601 with `Z` suffix;
- `target`: canonical root, Git common directory, full HEAD or `null`, branch or `null`, and `detached` as true, false, or null when unknown;
- `overall_result`: fixed-precedence summary of the per-check results;
- `evaluations`: fixed-order check IDs, result, freshness, evidence paths, and limitations;
- `controls`: fixed-order root paths, `PRESENT`/`MISSING`, byte size and SHA-256 digest or `null`;
- `limitations`: ordered report-level limitations; and
- `report_identity`: `sha256:<lowercase hex>`.

Canonical bytes are `json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")`. Calculate the digest over the complete payload without `report_identity`, then add the identity and serialize the final envelope by the same rule with one trailing newline. Keep list ordering explicit; do not include file bodies, host environment, remote URLs, or nondeterministic mapping order. `_report_payload` and `_canonical_json` are internal helpers so tests can verify mapping-order independence directly. Fix the injected clock in tests to prove byte-for-byte stable output and identity.

### Exit-code mapping

Exit codes classify command execution, not governance outcome:

| Code | Meaning | Output |
|---|---|---|
| `0` | A truthful report was produced, including `FAIL`, `UNVERIFIED`, unknown freshness, missing controls, detached HEAD, or an unborn-but-identified repository. | Exactly one base report line on stdout. |
| `2` | Target identity/root cannot be trusted, or a required present root control is unreadable, invalid, blank, symlinked/non-regular, or structurally malformed. | No normal report; one single-line `STOP:` diagnostic on stderr, capped at 256 characters and containing no file body. |
| `3` | An unexpected internal failure prevents a trustworthy report or STOP classification. | No normal report; one single-line `ERROR: INTERNAL_FATAL` diagnostic on stderr, capped at 256 characters with no traceback. |

No other exit code is used. Evidence gaps never become a nonzero enforcement gate. Fatal STOP is not represented as `FAIL`, `UNVERIFIED`, or a normal report.

## TDD Implementation Tasks

Every task below is one future implementation commit. For each task, first write its failing test, run the exact focused command and retain the specific RED evidence, make the smallest implementation change, rerun the same command and prove GREEN, run the listed focused/full verification, then commit. Do not skip RED by creating the implementation before the test. All commands below are future implementation instructions; none are run in this planning task.

### Task 1 — Shared immutable model and report identity

**Files:** `tests/test_model.py`, `tests/test_report.py`, then `src/engineering_governance/__init__.py`, `src/engineering_governance/model.py`, `src/engineering_governance/report.py`.

1. Write tests for enum values, frozen records/tuple fields, required report fields, UTC normalization, canonical key ordering, trailing newline, and the SHA-256 preimage rule. Include two equivalent payload constructions with different input mapping order and assert identical bytes and identity.
2. RED: run `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_model.py' -v` and `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_report.py' -v`; prove the tests fail because the planned model/report API is absent.
3. Implement only the frozen types, report builder, and canonical serializer from the signatures above.
4. GREEN: rerun both focused commands. Review that no mutable nested state or file body is retained.
5. Commit: `git add src/engineering_governance/__init__.py src/engineering_governance/model.py src/engineering_governance/report.py tests/test_model.py tests/test_report.py && git commit -m "feat(doctor): add immutable report model"`.

### Task 2 — Local repository identity reader

**Files:** `tests/support.py`, `tests/test_git_reader.py`, then `src/engineering_governance/git_reader.py`.

1. Write tests using a temporary synthetic Git repository for canonical root/common directory, full HEAD, symbolic branch, detached HEAD, unborn HEAD, non-repository target, and unreadable/unresolvable target. Add a recording Git runner assertion that `read_repository` requests only the four approved local probes.
2. RED: `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_git_reader.py' -v`; prove failing assertions identify missing observations and stop classification.
3. Implement `run_git_readonly` and `read_repository`; resolve Git-returned relative common-directory paths against the repository root and normalize paths without consulting remotes.
4. GREEN: rerun the focused command. Verify detached is represented, not repaired, and unborn HEAD is `UNVERIFIED`-eligible rather than a fabricated revision.
5. Commit: `git add src/engineering_governance/git_reader.py tests/support.py tests/test_git_reader.py && git commit -m "feat(doctor): observe local repository identity"`.

### Task 3 — Root control observations and basic consistency

**Files:** `tests/fixtures/doctor/{pass,unverified-missing-status,inconsistent-task-id,malformed-task}/*`, `tests/test_control_reader.py`, then `src/engineering_governance/control_reader.py`.

1. Write fixtures with three readable matching controls, a missing status file, a readable task/status ID mismatch, and a task file lacking the required unique ID/state fields. Write tests for exact file order, content digests without bodies, missing-file `UNVERIFIED`/`UNKNOWN`, mismatch `FAIL`/`CURRENT`, and fatal read/UTF-8/blank/non-regular/malformed cases using injected readers where needed.
2. RED: `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_control_reader.py' -v`; prove each behavior assertion fails against the absent reader.
3. Implement `read_controls` and the fixed line/token rules without adding a general Markdown parser or control schema.
4. GREEN: rerun the focused command. Confirm a missing file is reportable with exit-0-compatible state while malformed required input is a fatal exception consumed by the caller.
5. Commit: `git add src/engineering_governance/control_reader.py tests/fixtures/doctor tests/test_control_reader.py && git commit -m "feat(doctor): read control files deterministically"`.

### Task 4 — Doctor orchestration, stdout, and exit semantics

**Files:** `tests/test_doctor.py`, then `src/engineering_governance/doctor.py`.

1. Write tests for one-line report stdout and exit `0` on PASS, `FAIL`, `UNVERIFIED`/`UNKNOWN`, detached HEAD, and unborn HEAD; fatal target/control STOP returns `2` with no stdout report and a bounded stderr diagnostic; unexpected internal failure returns `3` with no normal report. Assert `UNVERIFIED` cannot aggregate to PASS.
2. RED: `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_doctor.py' -v`; prove the public invocation boundary and required exit behavior are missing.
3. Implement `run_doctor` as the direct library invocation; inject Git, file, and clock adapters; catch classified fatal failures separately from unexpected internal errors.
4. GREEN: rerun the focused command and then `PYTHONPATH=src python3.11 -m unittest discover -s tests -v` for the full current suite.
5. Commit: `git add src/engineering_governance/doctor.py tests/test_doctor.py && git commit -m "feat(doctor): emit report with stop semantics"`.

### Task 5 — Prove the no-mutation and offline boundary

**Files:** `tests/support.py`, `tests/test_git_reader.py`, `tests/test_doctor.py`, then the smallest required hardening in `src/engineering_governance/git_reader.py` or `src/engineering_governance/doctor.py`.

1. First add failing tests that call the Git adapter with `fetch`/`remote`/`ls-remote` and assert it is rejected before the fake process runner is invoked. Add end-to-end tests on a dirty temporary target (tracked modification plus untracked file) with an existing linked worktree. Snapshot file paths/types/modes/content digests, Git index/HEAD/config, refs, and `git worktree list --porcelain` before and after. Assert equality and assert the recorded Git command list contains only the approved local probes.
2. RED: run `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_git_reader.py' -v` and `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_doctor.py' -v`; retain the specific failure showing prohibited commands are not yet guarded or a mutation invariant is missing.
3. Add only the command allowlist enforcement or reader correction needed for those failures. Doctor must never call mutating commands; do not add a general sandbox or permission framework.
4. GREEN: rerun both focused commands, then `PYTHONPATH=src python3.11 -m unittest discover -s tests -v`. Review fixture teardown and confirm no repository outside the temporary test root is touched.
5. Commit: `git add src/engineering_governance/git_reader.py src/engineering_governance/doctor.py tests/support.py tests/test_git_reader.py tests/test_doctor.py && git commit -m "test(doctor): prove offline read-only behavior"`.

## Verification Commands for the Future Implementation

Run from the repository root on Python 3.11+:

```bash
PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_model.py' -v
PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_report.py' -v
PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_git_reader.py' -v
PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_control_reader.py' -v
PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_doctor.py' -v
PYTHONPATH=src python3.11 -m unittest discover -s tests -v
```

For each task, the first focused run is expected to fail for the newly specified behavior (RED); after the minimal implementation, the same focused command must pass (GREEN). Run the full suite after Tasks 4 and 5. No third-party test runner, package install, build backend, or network access is needed.

## Commit Boundaries

The future implementation commits are exactly the five task commits above, in order. Each commit contains its tests first in the task's execution sequence and the minimal implementation for that increment. Do not combine the whole slice into one commit, skip a failing test, add unrelated cleanup, or push implementation until a separate implementation task authorizes it. This plan task itself has only one plan document plus the two required control-plane files as its allowed changed paths.

## Writing-Plans Self-Review

- **Spec coverage:** Covers the accepted spec's shared in-memory model, read-only Doctor boundary, local/offline operation, truthful report, evidence gaps, fatal STOP, exit semantics, and no-mutation proof. Deferred capabilities remain out of scope.
- **Step granularity:** Five ordered commits each add a testable contract, show RED, make a minimal change, show GREEN, run applicable verification, and commit.
- **Type/interface consistency:** Shared records and exact reader/report/orchestration signatures are fixed in one `model.py` contract. `GitRunner`, `FileReader`, and `Clock` injection types line up across module boundaries; all nested report collections are immutable tuples.
- **Review Focus coverage:** Thirteen adversarial cases cover non-repository target, missing/unreadable/malformed controls, detached/unborn Git states, consistency mismatch, dirty target, refs/worktrees, offline command allowlist, truthful `UNVERIFIED`, fatal STOP separation, and deterministic report identity.
- **Proportion:** The plan is limited to one local Doctor slice, five source modules plus package marker, standard-library tests, and text fixtures. It adds no packaging, CLI, general parser, reusable enforcement framework, persistent state, or future command implementation.

**Implementation status:** Not started. This plan must receive implementation-plan review and a separate implementation authorization before any paths in its future file map are created.

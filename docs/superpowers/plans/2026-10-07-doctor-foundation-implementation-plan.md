# Doctor Foundation Implementation Plan

**Task:** `EG-V01-DOCTOR-FOUNDATION-PLAN-003`
**Plan state:** `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`
**Planning method:** `superpowers:writing-plans`
**Plan baseline:** `codex/eg-v01-tooling-design` at `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`
**Accepted standard:** `EngineeringGovernanceStandard 0.1.0`

## Goal

After independent review and a separate implementation authorization, build the smallest local read-only Doctor slice: observe a repository root and revision, inspect the three root control files, perform one deterministic task/status reference check, and emit an immutable versioned base report to stdout.

This document is a plan only. It does not authorize or perform implementation.

## Architecture

Use a standard-library-only package with five responsibilities:

1. `model.py` owns frozen shared records and result/freshness types.
2. `git_reader.py` observes the target root, Git common directory, HEAD, and symbolic branch through an allowlist of local read-only Git command tuples.
3. `control_reader.py` reads only root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`, returning content identities and deterministic consistency results.
4. `report.py` builds a frozen Doctor base report and its content identity using canonical JSON.
5. `doctor.py` coordinates the readers, writes one report to stdout or a bounded STOP diagnostic to stderr, and returns the command exit code.

There is no `__main__.py`, argument parser, console script, package manifest, or installer. `run_doctor` is a directly callable library function with injected streams and readers for tests. No module writes to the target or persists a report.

## Tech Stack

- macOS on Apple silicon; Python 3.11 or newer.
- Python standard library only: `dataclasses`, `enum`, `hashlib`, `json`, `pathlib`, `subprocess`, `tempfile`, `unittest`, and `unittest.mock`.
- Local Git executable for repository observation and synthetic test setup.
- Offline by default. Doctor does not invoke network-capable Git commands or query remote PR state.
- No database, cache, report store, daemon, or background process.

Any third-party runtime dependency discovered during implementation is a STOP requiring a separately reviewed task; it is not part of this plan.

## Spec path

Accepted design: [`docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`](../specs/2026-10-07-tooling-foundation-design.md), especially Sections 6, 10, 12, 13, 15, 16, 17, 18, and 19.

The slice preserves the Hybrid recommendation and `EngineeringGovernanceStandard 0.1.0`. Bootstrap, deeper Audit, and AI contribution execution remain outside this plan.

## Global Constraints

- Read only the explicit target. Do not write, repair, reformat, or normalize target files.
- Do not call `fetch`, `pull`, `push`, `remote`, `ls-remote`, GitHub APIs, or any network path. Do not change remotes, refs, branches, index, or worktrees.
- Do not infer project facts from missing controls, a detached HEAD, an unknown revision, or unavailable values.
- Emit no persistent report or hidden state. Caller shell redirection is outside the library's behavior.
- Do not add `pyproject.toml`, requirements files, schema files, CLI entry points, skills, templates, check registries, Bootstrap, deeper Audit, AIContribution composition, enforcement, CI gates, migration, remediation, or pilot changes.
- All `src/*`, `tests/*`, and `tests/fixtures/*` paths below are future implementation paths. This corrective may modify only this plan and the two control-plane files.

## Review Focus

1. A non-repository or ambiguous target cannot establish trusted identity: no normal report, bounded STOP diagnostic, exit `2`.
2. A missing root control is reportable incompleteness: affected evaluation `UNVERIFIED`, freshness `UNKNOWN`, limitation recorded, report emitted, exit `0`.
3. An existing unreadable, invalid-UTF-8, symlinked/non-regular, blank, or structurally malformed required root control is fatal: no normal report, exit `2`.
4. A resolvable detached HEAD is `branch=None`, `detached=True`; it is not assigned a branch or treated as fatal.
5. An unborn or otherwise unresolvable HEAD with a known root has `head=None`, identity `UNVERIFIED` / `UNKNOWN`, and exit `0`; the cause is not inferred.
6. A readable task/status ID mismatch is a deterministic `FAIL` finding and exit `0`.
7. `UNVERIFIED` and unknown freshness are never promoted to `PASS` by report aggregation or serialization.
8. Fatal STOP is never represented as a normal evaluation or serialized Doctor report.
9. Dirty tracked and untracked target content, file types/modes, Git metadata, and index are unchanged after Doctor.
10. Refs and `git worktree list --porcelain` are unchanged after Doctor, including when a linked worktree already exists.
11. Only the exact local Git identity probes below are permitted; prohibited tuples are rejected before subprocess execution.
12. The real Git subprocess adapter passes exact argv/cwd, `shell=False`, a bounded timeout, captured UTF-8 text streams, and a minimally augmented environment; adapter timeout becomes `DoctorStop`, then exit `2` without a report.
13. Equivalent report values serialize to the same canonical bytes and SHA-256 identity.
14. Evidence includes paths and content digests, not control-file bodies; missing/unknown values remain explicit limitations.

## Exact Future File Map

No paths in this section are created by this planning task.

### Source

- `src/engineering_governance/__init__.py` — package marker and small public exports.
- `src/engineering_governance/model.py` — frozen records, enums, and `DoctorStop`.
- `src/engineering_governance/git_reader.py` — Git command allowlist and local identity reader.
- `src/engineering_governance/control_reader.py` — root file reads, digests, task parsing, and consistency result.
- `src/engineering_governance/report.py` — immutable report construction and canonical JSON serialization.
- `src/engineering_governance/doctor.py` — orchestration, stdout/stderr behavior, and exit mapping.

### Tests

- `tests/support.py` — staged test support owned by the task that first needs each helper: Task 2 temporary Git repository setup, Task 3 fixture materialization, and Task 4 no-mutation snapshots. Task 2 must not prebuild the fixture or snapshot helpers.
- `tests/test_model.py` — shared type/result invariants.
- `tests/test_report.py` — immutable report, canonical bytes, and digest.
- `tests/test_git_reader.py` — local identity, detached/unborn states, and command allowlist.
- `tests/test_control_reader.py` — control-file outcomes and Task ID matching boundaries.
- `tests/test_doctor.py` — stdout/exit semantics and end-to-end no-mutation proof.

### Synthetic text fixtures

Fixtures contain control text only. Task 3's fixture helper copies them into a temporary directory; the local repository setup helper is owned by Task 2 and reused by later tests. Temporary `.git` data is not committed.

- `tests/fixtures/doctor/pass/AGENTS.md`
- `tests/fixtures/doctor/pass/CURRENT_STATUS.md`
- `tests/fixtures/doctor/pass/CURRENT_TASK.md`
- `tests/fixtures/doctor/unverified-missing-status/AGENTS.md`
- `tests/fixtures/doctor/unverified-missing-status/CURRENT_TASK.md` — no status file.
- `tests/fixtures/doctor/inconsistent-task-id/AGENTS.md`
- `tests/fixtures/doctor/inconsistent-task-id/CURRENT_STATUS.md`
- `tests/fixtures/doctor/inconsistent-task-id/CURRENT_TASK.md`
- `tests/fixtures/doctor/malformed-task/AGENTS.md`
- `tests/fixtures/doctor/malformed-task/CURRENT_STATUS.md`
- `tests/fixtures/doctor/malformed-task/CURRENT_TASK.md` — missing or duplicate required fields.

Inject a `FileReader` that raises `PermissionError` for unreadable-file tests; permission-bit behavior varies under privileged macOS test users.

### Test-support ownership and interfaces

`tests/support.py` is shared test infrastructure, but each helper is added only by the first task that needs it:

- Task 2 adds `initialize_temporary_git_repository(root: Path, *, initial_commit: bool) -> Path`, used by Git-reader tests to create committed, unborn, and detached local repositories. It does not materialize control fixtures or snapshot mutation state.
- Task 3 adds `materialize_doctor_fixture(name: str, destination: Path) -> Path`, used to copy one named synthetic control fixture into a temporary target before creating its local Git repository.
- Task 4 adds the frozen test-only `DoctorMutationSnapshot` record and `snapshot_doctor_mutation_state(root: Path, git_common_dir: Path) -> DoctorMutationSnapshot`. Its value covers target paths/types/modes/content digests, checkout Git metadata and index/config digests, the common-directory tree's paths/types/modes/content digests and refs, and `git worktree list --porcelain`. It is added alongside Task 4 tests before their RED run; it is not production code and is not prebuilt in Task 2.

Each later task may extend `tests/support.py` only for its own listed helper. Its Files and commit command must include the file whenever that task changes it.

## Shared Types and Exact Interfaces

Cross-module values live in `model.py`. Use `@dataclass(frozen=True, slots=True)` and tuples for nested collections; report state must not expose mutable nested values.

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
    code: str
    safe_summary: str
    def __init__(self, code: str, safe_summary: str) -> None: ...

@dataclass(frozen=True, slots=True)
class RepositoryIdentity:
    root: str
    git_common_dir: str
    head: str | None
    branch: str | None
    detached: bool | None

@dataclass(frozen=True, slots=True)
class ControlFileObservation:
    path: str
    state: ControlState
    sha256: str | None
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
    files: tuple[ControlFileObservation, ...]
    task_id: str | None
    task_state: str | None
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

Exact reader/report/orchestration signatures:

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

def _report_payload(
    report: DoctorReport, *, include_identity: bool
) -> dict[str, object]: ...

def _canonical_json(payload: Mapping[str, object]) -> bytes: ...

def serialize_report(report: DoctorReport) -> str: ...

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

`run_doctor` is a direct library invocation, not a CLI entry point. The implementation task supplies standard-library adapters from `subprocess.run`, `Path.read_bytes`, and an aware UTC clock; tests inject recording/failing adapters and fixed time. `run_git_readonly` accepts exactly these tuples and no others: `("rev-parse", "--show-toplevel")`, `("rev-parse", "--git-common-dir")`, `("rev-parse", "--verify", "HEAD")`, and `("symbolic-ref", "--quiet", "--short", "HEAD")`. Reject every unlisted tuple before starting a process. Invoke `subprocess.run(["git", *args], cwd=cwd, shell=False, timeout=timeout_seconds, check=False, capture_output=True, text=True, encoding="utf-8", errors="replace", env=...)`; use a fixed default timeout of `5.0` seconds and an environment copied from `os.environ` with only `GIT_OPTIONAL_LOCKS=0` and `GIT_TERMINAL_PROMPT=0` overlaid. Return `CommandResult(returncode, stdout, stderr)`. Convert `subprocess.TimeoutExpired` to `DoctorStop("GIT_PROBE_TIMEOUT", safe_summary)` without retry. This adapter timeout while establishing root/common-dir identity is command-level STOP (`2`), never `EvaluationResult.FAIL` or an `UNVERIFIED` report; Task 2 pins the adapter exception and Task 4 pins the final `run_doctor` exit/output mapping. No remote URL/name or network-capable argument is passed; never read configured remotes.

## Frozen First-Slice Semantics

### Repository identity

Resolve the supplied target strictly to an existing directory, then ask local Git for the canonical top-level and common Git directory. Resolve a relative common-directory result against the Git root. Identity consists only of these canonical paths, full HEAD object ID when resolvable, symbolic branch when present, and detached state when knowable. Do not treat an origin URL as identity.

- A target that is not a directory, is outside a Git worktree, or cannot establish a trusted root/common directory is a fatal STOP (`2`).
- A resolvable detached HEAD is `branch=None`, `detached=True`.
- An unresolvable HEAD with a known root is `head=None`; preserve a reported symbolic branch and use `detached=None` if detached state cannot be established. Its identity evaluation is `UNVERIFIED` / `UNKNOWN`, exit `0`. Do not infer why the revision is unavailable.
- A failed symbolic-ref probe with a valid HEAD means detached only for its documented no-symbolic-ref result (`1`). Any other symbolic-ref failure with a known root leaves `branch=None`, `detached=None`, identity `UNVERIFIED` / `UNKNOWN`, and exit `0`; it does not erase the known root. Failure to establish the root/common directory is STOP (`2`).
- Do not call `git status`; do not inspect or update refs/worktrees from Doctor.

### Control files and task/status consistency

Inspect only root `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`, in that order.

- Missing file: observation `MISSING`; dependent evaluation `UNVERIFIED` / `UNKNOWN`; record the path as a limitation; continue and return a report with exit `0`.
- Existing symlink, non-regular file, unreadable file, invalid UTF-8, or blank file: classified fatal root-input STOP, no report, exit `2`.
- `CURRENT_TASK.md` must have exactly one non-empty line whose first non-horizontal-space text is `Task ID:` and exactly one such line beginning `State:`. Labels are case-sensitive. Missing or duplicate fields are malformed root input and STOP (`2`). Trim values and remove one surrounding pair of backticks if present. The state is not interpreted.
- Task ID syntax is ASCII and exact: first character `[A-Za-z0-9]`; remaining characters may be `[A-Za-z0-9._/-]`. A nonempty value outside this grammar is malformed root input and STOP (`2`).
- For status matching, identifier characters are exactly ASCII letters, digits, dot `.`, underscore `_`, hyphen `-`, and slash `/`. Find a case-sensitive exact literal Task ID only if the preceding and following characters (when present) are not in that identifier-character set. Equivalent regex form: `(?<![A-Za-z0-9._/-])<re.escape(task_id)>(?![A-Za-z0-9._/-])`.
- Backticks, whitespace, colon, parentheses, and punctuation outside the identifier-character set are valid boundaries. Thus `TASK-1`, `` `TASK-1` ``, and `The active task is (TASK-1);` match; `TASK-10`, `XTASK-1`, `TASK-1-extra`, `TASK-1_extra`, and `TASK-1/child` do not match `TASK-1`.
- When task and status files are both present and readable but no exact bounded reference exists, consistency is `FAIL` / `CURRENT`; emit the truthful report and exit `0`. No match is not a fatal STOP.
- If the task file is missing, do not infer its ID/state from status; dependent consistency is `UNVERIFIED` / `UNKNOWN`.
- Fixed evaluation IDs/order: `doctor.repository.identity`, `doctor.controls.presence`, `doctor.controls.task_status_consistency`.
- Overall precedence: any `FAIL` → `FAIL`; else any `UNVERIFIED` → `UNVERIFIED`; else all `NOT_APPLICABLE` → `NOT_APPLICABLE`; otherwise `PASS`. Preserve per-check results. This slice does not emit `NOT_APPLICABLE` or `STALE`.
- Freshness `CURRENT` means the local input was successfully observed during this invocation; missing/unavailable evidence is `UNKNOWN`.

### Report and deterministic serialization

Emit one frozen `DoctorReport` as one UTF-8 JSON line on stdout. Fixed envelope fields:

- `report_version`: `"doctor-base.v1"`;
- `tool_version`: `"doctor-foundation/1"`;
- `standard_version`: `"EngineeringGovernanceStandard 0.1.0"`;
- `observed_at`: timezone-aware UTC ISO-8601 ending in `Z`;
- `target`: canonical root, Git common directory, full HEAD or `null`, branch or `null`, detached `true`/`false`/`null`;
- `overall_result`;
- `evaluations`: fixed check IDs, result, freshness, evidence paths, limitations;
- `controls`: fixed paths, `PRESENT`/`MISSING`, byte size and SHA-256 digest or `null`;
- ordered report `limitations`; and
- `report_identity`: `sha256:<lowercase hex>`.

Canonical bytes are `json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")`. Hash the complete payload without `report_identity`, then serialize the final payload with identity and exactly one trailing newline. Preserve list order; include no file body, environment snapshot, remote URL, or persistent state. Tests exercise `_canonical_json` directly for mapping-order independence and fix the injected clock for byte-stability.

### Exit semantics

| Code | Meaning | Output |
|---|---|---|
| `0` | A truthful report was produced, including `FAIL`, `UNVERIFIED`, unknown freshness, missing controls, detached HEAD, or unknown revision with a known root. | Exactly one base-report line on stdout. |
| `2` | Target/root identity is untrustworthy or a present required root control is unreadable, invalid, blank, symlinked/non-regular, or structurally malformed. | No report; one single-line `STOP:` diagnostic on stderr, at most 256 characters, with no file body. |
| `3` | An unexpected internal failure prevents a trustworthy report or STOP classification. | No report; one `ERROR: INTERNAL_FATAL` line on stderr, at most 256 characters and no traceback. |

Exit status classifies command execution, never governance outcome. Evidence gaps are not an enforcement gate. Fatal STOP is never encoded as an evaluation result.

## TDD Implementation Tasks

There are four implementation commits followed by one verification-only acceptance gate. For each implementation task, add its named tests before that task's implementation, run the focused command and retain the expected RED evidence, implement only the missing behavior, run the same command and prove GREEN, complete the task's listed verification, then commit. Test modules must import not-yet-implemented APIs inside each test or `setUp`, not at module import time, so unittest reports the exact named tests as RED. RED is caused by the new API/behavior being absent at that point in the sequence. No later task introduces tests for behavior already implemented earlier. Do not manufacture a defect to create RED.

### Task 1 — Shared immutable model and report identity

**Files:** `tests/test_model.py`, `tests/test_report.py`, then `src/engineering_governance/__init__.py`, `src/engineering_governance/model.py`, `src/engineering_governance/report.py`.

| Exact test name | Setup | Key assertions |
|---|---|---|
| `test_evaluation_enums_are_exact` | Import result, freshness, and control enums. | Values equal the frozen enum sets in Shared Types; no extra value is present. |
| `test_shared_records_are_frozen_and_collections_are_tuples` | Build an `Evaluation` with tuple fields. | Mutating a field raises `FrozenInstanceError`; nested collections cannot be appended to. |
| `test_canonical_json_is_stable_across_mapping_order` | Pass equivalent dictionaries with reversed insertion order to `_canonical_json`. | Returned bytes are identical and equal compact sorted-key UTF-8 JSON. |
| `test_report_identity_excludes_identity_field_from_digest` | Build a fixed-time report and remove identity from its payload. | Identity equals `"sha256:" + sha256(_canonical_json(payload_without_identity)).hexdigest()`. |
| `test_report_serialization_ends_with_one_newline` | Serialize one report. | Output ends in `\n` and not `\n\n`. |
| `test_overall_result_preserves_unverified` | Build evaluations with `PASS` and `UNVERIFIED`. | `overall_result` is `UNVERIFIED`, never `PASS`. |
| `test_overall_result_prefers_fail_to_unverified` | Build evaluations with `FAIL` and `UNVERIFIED`. | `overall_result` is `FAIL`; both per-check values remain present. |

**RED:** `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_model.py' -v` and `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_report.py' -v`. The tests fail because the package/model/report APIs and canonical serializer do not exist yet.

**Minimal implementation:** Add only the shared frozen records, enums, report builder, `_report_payload`, `_canonical_json`, and `serialize_report`.

**GREEN:** rerun both exact focused commands above. No test may be removed or weakened to obtain GREEN.

**Commit:** `git add src/engineering_governance/__init__.py src/engineering_governance/model.py src/engineering_governance/report.py tests/test_model.py tests/test_report.py && git commit -m "feat(doctor): add immutable report model"`.

### Task 2 — Local repository identity and Git command allowlist

**Files:** `tests/support.py` (add only `initialize_temporary_git_repository`), `tests/test_git_reader.py`, then `src/engineering_governance/git_reader.py`.

| Exact test name | Setup | Key assertions |
|---|---|---|
| `test_repository_identity_observes_root_common_dir_head_and_branch` | Temporary committed repo; query from a nested directory. | Root/common-dir are canonical absolute paths; HEAD is full object ID; branch is the observed symbolic branch. |
| `test_detached_head_has_no_inferred_branch` | Temporary repo checked out at a detached commit. | `branch is None`, `detached is True`, HEAD stays unchanged. |
| `test_unborn_head_is_unknown_without_claiming_reason` | Initialized repo with no commit. | Known root is retained; `head is None`; symbolic branch is preserved if present; `detached` is not falsely true. |
| `test_symbolic_ref_error_keeps_known_root_unverified` | Canned runner returns a non-1 symbolic-ref failure after valid root/common-dir results. | Root and HEAD remain; `branch is None`, `detached is None`; caller can report identity `UNVERIFIED` / `UNKNOWN`. |
| `test_non_repository_target_raises_doctor_stop` | Existing ordinary directory. | `read_repository` raises `DoctorStop`; no `RepositoryIdentity` is returned. |
| `test_reader_uses_only_exact_allowed_git_probe_tuples` | Inject a recording `GitRunner` with canned results. | Calls are exactly the four listed local tuples; no other argument tuple appears. |
| `test_fetch_tuple_is_rejected_before_subprocess` | Patch `git_reader.subprocess.run`; call with `("fetch", "--all")`. | `DoctorStop` is raised and mocked subprocess was not called. |
| `test_remote_tuple_is_rejected_before_subprocess` | Patch subprocess; call with `("remote", "-v")`. | `DoctorStop` is raised and mocked subprocess was not called. |
| `test_ls_remote_tuple_is_rejected_before_subprocess` | Patch subprocess; call with `("ls-remote", "origin")`. | `DoctorStop` is raised and mocked subprocess was not called. |
| `test_any_unlisted_git_tuple_is_rejected_before_subprocess` | Patch subprocess; call with `("push", "origin")` and `("status", "--short")`. | Each raises `DoctorStop`; subprocess remains uncalled. |
| `test_run_git_readonly_invokes_git_with_readonly_process_contract` | Patch `git_reader.subprocess.run` to return fixed stdout/stderr for `("rev-parse", "--show-toplevel")`; call `run_git_readonly` with a supplied `Path` and default timeout. | One call has argv exactly `["git", "rev-parse", "--show-toplevel"]` (no remote verb, remote name/URL, or network-capable argument), exact supplied `cwd`, `shell=False`, `timeout=5.0`, `check=False`, `capture_output=True`, `text=True`, `encoding="utf-8"`, `errors="replace"`; env equals a copy of `os.environ` with only `GIT_OPTIONAL_LOCKS=0` and `GIT_TERMINAL_PROMPT=0` overlaid; returned value equals `CommandResult(0, fixed_stdout, fixed_stderr)`. |
| `test_run_git_readonly_timeout_becomes_doctor_stop` | Patch `subprocess.run` to raise `subprocess.TimeoutExpired` for `("rev-parse", "--show-toplevel")`. | `run_git_readonly` raises `DoctorStop` with code `GIT_PROBE_TIMEOUT`; `subprocess.run` is called exactly once; there is no retry/backoff or fallback. |

**RED:** `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_git_reader.py' -v`. Task 2 first adds the Git-only temporary repository helper and all named tests. At this point Task 1 exists but `git_reader.py`, `run_git_readonly`, and the reader API do not; tests fail on those absent production APIs, not on test setup.

**Minimal implementation:** Implement `run_git_readonly` with the exact subprocess contract above, timeout-to-`DoctorStop` conversion, the four-tuple allowlist, and `read_repository`. All adapter and allowlist tests exist before this implementation; Task 5 adds no new Git behavior tests. Resolve Git-returned relative common-directory paths against the Git root. Do not read remotes.

**GREEN:** rerun the same focused command. Confirm prohibited tuples fail before subprocess and permitted probes remain local read-only commands.

**Commit:** `git add tests/support.py tests/test_git_reader.py src/engineering_governance/git_reader.py && git commit -m "feat(doctor): observe local repository identity"`.

### Task 3 — Control observations and exact Task ID matching

**Files:** `tests/support.py` (add only `materialize_doctor_fixture`), `tests/fixtures/doctor/{pass,unverified-missing-status,inconsistent-task-id,malformed-task}/*`, `tests/test_control_reader.py`, then `src/engineering_governance/control_reader.py`.

| Exact test name | Setup | Key assertions |
|---|---|---|
| `test_control_files_are_reported_in_fixed_order_with_digests` | Complete pass fixture. | Paths are AGENTS, STATUS, TASK in order; SHA-256 is over exact bytes; no body is returned. |
| `test_missing_status_is_unverified_unknown` | Fixture omits `CURRENT_STATUS.md`. | Status observation is `MISSING`; presence/consistency are `UNVERIFIED` / `UNKNOWN`; limitation names the path. |
| `test_unreadable_control_raises_doctor_stop` | Inject `FileReader` raising `PermissionError` for one present control. | `DoctorStop` is raised; no normal snapshot is returned. |
| `test_invalid_utf8_control_raises_doctor_stop` | Reader returns invalid UTF-8 bytes. | `DoctorStop` is raised; no replacement decoding occurs. |
| `test_blank_control_raises_doctor_stop` | Present control contains whitespace only. | `DoctorStop` is raised as malformed root input. |
| `test_symlink_control_raises_doctor_stop` | Root control path is a symlink. | `lstat` detects it and the reader raises `DoctorStop` without following it. |
| `test_non_regular_control_raises_doctor_stop` | Root control path is a directory. | `DoctorStop` is raised. |
| `test_missing_task_id_field_raises_doctor_stop` | Task fixture omits `Task ID:`. | `DoctorStop` is raised. |
| `test_duplicate_task_id_field_raises_doctor_stop` | Task fixture contains two `Task ID:` lines. | `DoctorStop` is raised. |
| `test_missing_task_state_field_raises_doctor_stop` | Task fixture omits `State:`. | `DoctorStop` is raised. |
| `test_invalid_task_id_syntax_raises_doctor_stop` | Task ID contains a non-ASCII or disallowed character. | `DoctorStop` is raised before status matching. |
| `test_task_id_exact_reference_matches` | Task ID `TASK-1`; status contains `TASK-1`. | Consistency is `PASS` / `CURRENT`. |
| `test_task_id_inside_backticks_matches` | Status contains `` `TASK-1` ``. | Consistency is `PASS` / `CURRENT`. |
| `test_task_id_in_ordinary_prose_matches` | Status says `The active task is (TASK-1);`. | Consistency is `PASS` / `CURRENT`; parentheses and semicolon are boundaries. |
| `test_task_id_prefix_collision_does_not_match` | Task ID `TASK-1`; status contains only `TASK-10`. | Consistency is `FAIL` / `CURRENT`. |
| `test_task_id_suffix_collision_does_not_match` | Status contains `TASK-1-extra`. | Consistency is `FAIL` / `CURRENT`; hyphen is an identifier character. |
| `test_task_id_embedded_identifier_does_not_match` | Status contains `XTASK-1`, `TASK-1_extra`, or `TASK-1/child`. | None matches `TASK-1`; consistency is `FAIL` / `CURRENT`. |
| `test_task_id_slash_and_dot_boundaries_are_identifier_characters` | Task ID `AREA/TASK.1`; status contains only `AREA/TASK.10` and `AREA/TASK.1/child`. | Neither collision matches; consistency is `FAIL` / `CURRENT`. |
| `test_missing_task_id_reference_is_consistency_fail` | Both files are readable; status omits the exact bounded ID. | Consistency is `FAIL` / `CURRENT`, not an exception or STOP. |

**RED:** `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_control_reader.py' -v`. Task 3 adds its fixture materializer and named tests before this run; Task 1 exists but `control_reader.py` and `read_controls` do not, so RED is caused by the absent production API rather than missing test support.

**Minimal implementation:** Implement the three-file read, fixed observation order, UTF-8/nonblank checks, task field parsing, and the exact ASCII boundary rule above. Do not add a Markdown parser or schema.

**GREEN:** rerun the same focused command. Verify `TASK-10`, `XTASK-1`, `TASK-1-extra`, `TASK-1_extra`, and `TASK-1/child` never match `TASK-1`.

**Commit:** `git add tests/support.py tests/fixtures/doctor tests/test_control_reader.py src/engineering_governance/control_reader.py && git commit -m "feat(doctor): read control files deterministically"`.

### Task 4 — Doctor orchestration and read-only acceptance tests

**Files:** `tests/support.py` (add only `DoctorMutationSnapshot` and `snapshot_doctor_mutation_state`), `tests/test_doctor.py`, then `src/engineering_governance/doctor.py`.

| Exact test name | Setup | Key assertions |
|---|---|---|
| `test_run_doctor_emits_one_pass_report_and_exit_zero` | Complete fixture, fixed clock, captured streams. | Exit `0`; stdout has one JSON line; overall `PASS`; stderr empty. |
| `test_run_doctor_emits_fail_report_and_exit_zero` | Task/status ID mismatch fixture. | Exit `0`; report includes consistency `FAIL`; no STOP diagnostic. |
| `test_run_doctor_emits_unverified_report_and_exit_zero` | Missing status fixture. | Exit `0`; report includes `UNVERIFIED` / `UNKNOWN`, never `PASS` for the missing-dependent check. |
| `test_unresolvable_head_emits_unverified_report_and_exit_zero` | Unborn repository fixture with readable controls. | Exit `0`; identity evaluation is `UNVERIFIED` / `UNKNOWN`; report has no fabricated revision. |
| `test_non_repository_returns_two_without_report` | Ordinary directory target. | Exit `2`; stdout empty; stderr starts `STOP:` and is at most 256 characters. |
| `test_malformed_root_returns_two_without_report` | Malformed task fixture. | Exit `2`; stdout empty; bounded `STOP:` diagnostic; no evaluation report. |
| `test_internal_failure_returns_three_without_report` | Inject an unexpected reader exception. | Exit `3`; stdout empty; stderr is bounded `ERROR: INTERNAL_FATAL` with no traceback. |
| `test_git_probe_timeout_returns_two_without_report` | Use Task 2's `run_git_readonly` as the injected Git runner and patch its `subprocess.run` to raise `TimeoutExpired` on the first root-identity probe. | `run_doctor` returns `2`; stdout is empty; stderr is one bounded `STOP:` diagnostic; no `DoctorReport` or `UNVERIFIED` evaluation is emitted; the adapter is called once. |
| `test_dirty_repository_content_and_git_metadata_are_unchanged` | Temporary repo with modified tracked file and untracked file; snapshot before run. | After `run_doctor`, paths/types/modes/content digests and `.git`/index/config bytes equal the before snapshot. |
| `test_linked_worktree_refs_and_index_are_unchanged` | Repo has a pre-existing linked worktree; snapshot refs and `git worktree list --porcelain`. | After `run_doctor`, refs, worktree listing, HEAD/index/config, and common-dir contents equal the before snapshot. |

**RED:** Add Task 4's snapshot helper and named tests before running `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_doctor.py' -v`. Tasks 1–3 and the support helper are available, but `doctor.py` / `run_doctor` do not exist; tests lazily import the API inside each test and RED is caused by absent `run_doctor`, including the timeout-mapping test, never by a missing support helper.

**Minimal implementation:** Implement `run_doctor`, inject Git/file/clock readers, build and serialize one report on success, map `DoctorStop` (including `GIT_PROBE_TIMEOUT` while establishing repository/root identity) to exit `2`, and map unexpected internal failures to exit `3`. No normal report is emitted on either stop path.

**GREEN:** rerun the same focused command, then run `PYTHONPATH=src python3.11 -m unittest discover -s tests -v`. The dirty-target and linked-worktree snapshot assertions are written before `run_doctor` and must pass with its minimal read-only implementation.

**Commit:** `git add tests/support.py tests/test_doctor.py src/engineering_governance/doctor.py && git commit -m "feat(doctor): emit read-only report with exit semantics"`.

### Task 5 — Verification-only acceptance gate

This is not an implementation task and creates no tests, source, or commit. It exists to collect the final first-slice acceptance evidence after Task 4.

1. Run `PYTHONPATH=src python3.11 -m unittest discover -s tests -v` and require all tests to pass.
2. Confirm the Task 4 before/after dirty-target and linked-worktree snapshots pass, including refs, worktree list, content, modes, Git metadata, and index.
3. Require the Task 2 adapter tests to prove the exact allowed argv, cwd, `shell=False`, timeout, environment flags/preserved `PATH` and `HOME`, captured deterministic text, `CommandResult`, and one-call timeout conversion; confirm no network path is present.
4. Inspect `git status --short` and the final diff. This gate cannot add or modify implementation files; any finding returns to a separately authorized corrective task.

**Acceptance result:** PASS only if all prior tasks are GREEN, the full suite passes, the read-only snapshots match, and the scoped diff contains only the planned first-slice files. Otherwise STOP and report the failing evidence. No artificial RED and no commit are assigned to this gate.

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

Tasks 1–4 run their exact focused command first for RED, then the same command for GREEN. Task 4 and the verification-only gate run the full suite. No third-party test runner, package install, build backend, or network access is required.

## Commit Boundaries

The four future implementation commits are exactly the Task 1–4 commits above, in order. Each includes its named tests before production implementation, genuine RED evidence, minimal implementation, GREEN evidence, and the listed verification. Test-only helpers needed to make a task's tests executable are added with that task's test setup before its RED run; the expected RED must identify the absent production API. In particular, Task 4's snapshots are not built in Task 2, and Task 4's RED is absent `run_doctor`. Task 5 is verification-only and has no commit. Do not combine unrelated cleanup, skip a failing test, or push implementation without a separate implementation authorization. This plan corrective may change only this plan and `CURRENT_STATUS.md` / `CURRENT_TASK.md`.

## Corrective Self-Review

1. **Exact file map:** Every source, test, and fixture path in the Future File Map appears in its owning Task Files block. `tests/support.py` is staged across Tasks 2–4 for only the helper first needed by that task.
2. **Commit coverage:** Each Task 1–4 commit command includes every path in its Files block, including `tests/support.py` in Tasks 2, 3, and 4. No task commits a helper it did not introduce or change.
3. **Support ownership:** Task 2 adds only its temporary Git repository initializer; Task 3 adds fixture materialization; Task 4 adds the snapshot record/helper. Task 2 does not prebuild Task 4 snapshot behavior.
4. **Genuine RED:** Each task's support setup is ready before its focused RED run, and each run fails on that task's absent production API. Task 4 specifically REDs on absent `run_doctor`, not missing snapshot support. No test is added after the behavior it asserts is implemented.
5. **Adapter test surface:** Task 2 has named tests for the real `run_git_readonly` subprocess call and timeout exception, in addition to the exact allowlist tests.
6. **Adapter assertions:** The subprocess test pins exact argv, no remote/network arguments, supplied cwd, `shell=False`, timeout `5.0`, `check=False`, captured UTF-8 text, exact environment copy plus the two Git flags, and `CommandResult` contents.
7. **Timeout classification:** The root identity probe timeout raises `DoctorStop("GIT_PROBE_TIMEOUT", ...)` once in Task 2. Task 4 verifies `run_doctor` returns `2` with no report or `UNVERIFIED` result; no retry/backoff/network fallback exists.
8. **Tasks and scope:** Four TDD implementation tasks and the verification-only Task 5 remain. The planned slice stays local/offline/read-only, Python 3.11+/stdlib-only, with the existing report and exit `0` / `2` / `3` contract.
9. **Interface/type consistency:** Shared frozen records, reader/report functions, injected adapters, `DoctorStop`, and staged support helper interfaces are defined once and match the owning task boundaries.
10. **Previously accepted Task ID rule:** Grammar, case sensitivity, exact literal matching, identifier characters, and boundary behavior remain pinned by exact, backtick, prose, prefix, suffix, embedded, and missing-reference tests.
11. **Proportion and spec coverage:** The plan covers the first slice described by spec Sections 6, 10, 12, 13, 15, 16, 17, 18, and 19. It adds no CLI, packaging, schema, general Markdown parser, persistent state, or future-command implementation.

**Implementation status:** Not started. This plan requires independent implementation-plan review and a separate implementation authorization before any future source, test, or fixture path is created.

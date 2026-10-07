from dataclasses import dataclass
from enum import Enum


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
    def __init__(self, code: str, safe_summary: str) -> None:
        self.code = code
        self.safe_summary = safe_summary
        super().__init__(safe_summary)


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

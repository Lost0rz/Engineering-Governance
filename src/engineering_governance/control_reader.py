import hashlib
import re
import stat
from pathlib import Path
from typing import Callable

from .model import (
    ControlFileObservation,
    ControlSnapshot,
    ControlState,
    DoctorStop,
    Evaluation,
    EvaluationResult,
    Freshness,
)


_CONTROL_NAMES = ("AGENTS.md", "CURRENT_STATUS.md", "CURRENT_TASK.md")
_TASK_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*", re.ASCII)
_STATUS_IDENTIFIER_CHARS = r"A-Za-z0-9._/-"
FileReader = Callable[[Path], bytes]


def _stop(code: str, summary: str) -> DoctorStop:
    return DoctorStop(code, summary)


def _parse_task_fields(text: str) -> tuple[str, str]:
    values: dict[str, list[str]] = {}
    for label in ("Task ID", "State"):
        pattern = re.compile(rf"^[ \t]*{re.escape(label)}:(.*)$", re.MULTILINE)
        values[label] = [match.group(1).strip() for match in pattern.finditer(text)]
        if len(values[label]) != 1 or not values[label][0]:
            raise _stop("MALFORMED_TASK_CONTROL", f"CURRENT_TASK.md needs exactly one non-empty {label} field")

    def normalized(value: str) -> str:
        if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
            return value[1:-1].strip()
        return value

    task_id = normalized(values["Task ID"][0])
    task_state = normalized(values["State"][0])
    if not task_id or not _TASK_ID_PATTERN.fullmatch(task_id):
        raise _stop("MALFORMED_TASK_CONTROL", "CURRENT_TASK.md has an invalid Task ID")
    if not task_state:
        raise _stop("MALFORMED_TASK_CONTROL", "CURRENT_TASK.md has an empty State")
    return task_id, task_state


def _contains_bounded_task_id(status_text: str, task_id: str) -> bool:
    pattern = re.compile(
        rf"(?<![{_STATUS_IDENTIFIER_CHARS}]){re.escape(task_id)}(?![{_STATUS_IDENTIFIER_CHARS}])",
        re.ASCII,
    )
    return pattern.search(status_text) is not None


def read_controls(
    root: Path, *, file_reader: FileReader
) -> ControlSnapshot:
    root = Path(root)
    observations: list[ControlFileObservation] = []
    text_by_name: dict[str, str] = {}
    missing_paths: list[str] = []

    for name in _CONTROL_NAMES:
        path = root / name
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            observations.append(
                ControlFileObservation(str(path), ControlState.MISSING, None, None)
            )
            missing_paths.append(str(path))
            continue
        except OSError as exc:
            raise _stop("UNREADABLE_ROOT_CONTROL", f"Cannot inspect root control {name}") from exc

        if not stat.S_ISREG(mode):
            raise _stop("INVALID_ROOT_CONTROL", f"Root control {name} is not a regular file")

        try:
            contents = file_reader(path)
        except OSError as exc:
            raise _stop("UNREADABLE_ROOT_CONTROL", f"Cannot read root control {name}") from exc

        try:
            text = contents.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise _stop("INVALID_ROOT_CONTROL", f"Root control {name} is not valid UTF-8") from exc
        if not text.strip():
            raise _stop("INVALID_ROOT_CONTROL", f"Root control {name} is blank")

        text_by_name[name] = text
        observations.append(
            ControlFileObservation(
                str(path),
                ControlState.PRESENT,
                hashlib.sha256(contents).hexdigest(),
                len(contents),
            )
        )

    presence_limitations = tuple(f"Missing control file: {path}" for path in missing_paths)
    presence = Evaluation(
        "doctor.controls.presence",
        EvaluationResult.UNVERIFIED if missing_paths else EvaluationResult.PASS,
        Freshness.UNKNOWN if missing_paths else Freshness.CURRENT,
        tuple(item.path for item in observations),
        presence_limitations,
    )

    task_id: str | None = None
    task_state: str | None = None
    consistency_missing = tuple(
        str(root / name)
        for name in ("CURRENT_TASK.md", "CURRENT_STATUS.md")
        if name not in text_by_name
    )
    if "CURRENT_TASK.md" in text_by_name:
        task_id, task_state = _parse_task_fields(text_by_name["CURRENT_TASK.md"])

    if consistency_missing:
        consistency = Evaluation(
            "doctor.controls.task_status_consistency",
            EvaluationResult.UNVERIFIED,
            Freshness.UNKNOWN,
            (str(root / "CURRENT_TASK.md"), str(root / "CURRENT_STATUS.md")),
            tuple(
                f"Missing control required for task/status consistency: {path}"
                for path in consistency_missing
            ),
        )
    else:
        assert task_id is not None
        matched = _contains_bounded_task_id(text_by_name["CURRENT_STATUS.md"], task_id)
        consistency = Evaluation(
            "doctor.controls.task_status_consistency",
            EvaluationResult.PASS if matched else EvaluationResult.FAIL,
            Freshness.CURRENT,
            (str(root / "CURRENT_TASK.md"), str(root / "CURRENT_STATUS.md")),
            () if matched else (f"CURRENT_STATUS.md does not reference task ID {task_id}",),
        )

    return ControlSnapshot(
        tuple(observations), task_id, task_state, consistency, presence
    )

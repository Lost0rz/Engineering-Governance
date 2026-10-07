from datetime import datetime
from pathlib import Path
from typing import Callable, TextIO

from .control_reader import FileReader, read_controls
from .git_reader import GitRunner, read_repository
from .model import DoctorStop
from .report import build_doctor_report, serialize_report


Clock = Callable[[], datetime]


def _write_bounded_line(stream: TextIO, message: str) -> None:
    single_line = " ".join(message.split())
    stream.write(single_line[:255] + "\n")


def run_doctor(
    target: Path,
    *,
    stdout: TextIO,
    stderr: TextIO,
    git_runner: GitRunner,
    file_reader: FileReader,
    clock: Clock,
) -> int:
    try:
        identity = read_repository(target, git_runner=git_runner)
        controls = read_controls(Path(identity.root), file_reader=file_reader)
        report = build_doctor_report(identity, controls, clock())
        stdout.write(serialize_report(report))
        return 0
    except DoctorStop as stop:
        _write_bounded_line(stderr, f"STOP: {stop.code} {stop.safe_summary}")
        return 2
    except Exception:
        _write_bounded_line(stderr, "ERROR: INTERNAL_FATAL")
        return 3

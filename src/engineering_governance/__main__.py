import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .doctor import run_doctor
from .git_reader import run_git_readonly


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="engineering_governance")
    commands = parser.add_subparsers(dest="command", required=True)
    doctor = commands.add_parser("doctor", help="inspect a local repository")
    doctor.add_argument("target", type=Path, help="repository path to inspect")
    arguments = parser.parse_args(argv)

    if arguments.command == "doctor":
        return run_doctor(
            arguments.target,
            stdout=sys.stdout,
            stderr=sys.stderr,
            git_runner=run_git_readonly,
            file_reader=Path.read_bytes,
            clock=lambda: datetime.now(timezone.utc),
        )

    parser.error("unsupported command")


if __name__ == "__main__":
    raise SystemExit(main())

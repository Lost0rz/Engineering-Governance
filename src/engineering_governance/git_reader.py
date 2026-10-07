import os
import re
import subprocess
from pathlib import Path
from typing import Callable

from .model import CommandResult, DoctorStop, RepositoryIdentity


GitRunner = Callable[[Path, tuple[str, ...], float], CommandResult]

_ALLOWED_GIT_ARGS = frozenset(
    {
        ("rev-parse", "--show-toplevel"),
        ("rev-parse", "--git-common-dir"),
        ("rev-parse", "--verify", "HEAD"),
        ("symbolic-ref", "--quiet", "--short", "HEAD"),
    }
)
_DEFAULT_TIMEOUT_SECONDS = 5.0
_FULL_OBJECT_ID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_REPOSITORY_SELECTION_ENV = ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR")


def _remove_output_terminator(value: str) -> str:
    return value[:-1] if value.endswith("\n") else value


def run_git_readonly(
    cwd: Path, args: tuple[str, ...], timeout_seconds: float = 5.0
) -> CommandResult:
    if args not in _ALLOWED_GIT_ARGS:
        raise DoctorStop(
            "GIT_COMMAND_NOT_ALLOWED",
            "Git probe is not in the local read-only allowlist.",
        )

    environment = os.environ.copy()
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    environment["GIT_TERMINAL_PROMPT"] = "0"
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=cwd,
            shell=False,
            timeout=timeout_seconds,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
        )
    except subprocess.TimeoutExpired:
        raise DoctorStop(
            "GIT_PROBE_TIMEOUT",
            "Local Git identity probe timed out.",
        ) from None

    return CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout or "",
        stderr=completed.stderr or "",
    )


def _resolved_path(raw_path: str, *, relative_to: Path, label: str) -> Path:
    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = relative_to / candidate
    try:
        return candidate.resolve(strict=True)
    except (OSError, RuntimeError):
        raise DoctorStop(
            "REPOSITORY_IDENTITY_UNAVAILABLE",
            f"Git did not provide a resolvable {label}.",
        ) from None


def read_repository(
    target: Path, *, git_runner: GitRunner
) -> RepositoryIdentity:
    try:
        resolved_target = target.resolve(strict=True)
    except (OSError, RuntimeError):
        raise DoctorStop(
            "TARGET_UNAVAILABLE",
            "The requested target directory cannot be resolved.",
        ) from None
    if not resolved_target.is_dir():
        raise DoctorStop(
            "TARGET_NOT_DIRECTORY",
            "The requested target is not a directory.",
        )
    if any(os.environ.get(name) for name in _REPOSITORY_SELECTION_ENV):
        raise DoctorStop(
            "GIT_ENVIRONMENT_UNTRUSTED",
            "Git repository selection environment is set.",
        )

    root_result = git_runner(
        resolved_target, ("rev-parse", "--show-toplevel"), _DEFAULT_TIMEOUT_SECONDS
    )
    root_text = _remove_output_terminator(root_result.stdout)
    if root_result.returncode != 0 or not root_text:
        raise DoctorStop(
            "REPOSITORY_ROOT_UNAVAILABLE",
            "A trusted Git repository root could not be established.",
        )
    root = _resolved_path(root_text, relative_to=resolved_target, label="repository root")
    if not root.is_dir():
        raise DoctorStop(
            "REPOSITORY_ROOT_UNAVAILABLE",
            "Git repository root is not a directory.",
        )
    common_result = git_runner(
        root, ("rev-parse", "--git-common-dir"), _DEFAULT_TIMEOUT_SECONDS
    )
    common_text = _remove_output_terminator(common_result.stdout)
    if common_result.returncode != 0 or not common_text:
        raise DoctorStop(
            "GIT_COMMON_DIR_UNAVAILABLE",
            "A trusted Git common directory could not be established.",
        )
    common_dir = _resolved_path(
        common_text, relative_to=root, label="Git common directory"
    )
    if not common_dir.is_dir():
        raise DoctorStop(
            "GIT_COMMON_DIR_UNAVAILABLE",
            "Git common directory is not a directory.",
        )

    head_result = git_runner(
        root,
        ("rev-parse", "--verify", "HEAD"),
        _DEFAULT_TIMEOUT_SECONDS,
    )
    head_text = head_result.stdout.strip()
    head = (
        head_text
        if head_result.returncode == 0 and _FULL_OBJECT_ID.fullmatch(head_text)
        else None
    )

    symbolic_result = git_runner(
        root,
        ("symbolic-ref", "--quiet", "--short", "HEAD"),
        _DEFAULT_TIMEOUT_SECONDS,
    )
    branch_text = symbolic_result.stdout.strip()
    if symbolic_result.returncode == 0 and branch_text:
        branch = branch_text
        detached: bool | None = False
    elif symbolic_result.returncode == 1:
        branch = None
        detached = True if head is not None else None
    else:
        branch = None
        detached = None

    return RepositoryIdentity(
        root=str(root),
        git_common_dir=str(common_dir),
        head=head,
        branch=branch,
        detached=detached,
    )

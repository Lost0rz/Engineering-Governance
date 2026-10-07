from dataclasses import dataclass
import hashlib
import os
import shutil
import stat
import subprocess
from pathlib import Path


def initialize_temporary_git_repository(
    root: Path, *, initial_commit: bool
) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "init", "--quiet"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    if initial_commit:
        (root / "README.md").write_text("temporary repository\n", encoding="utf-8")
        subprocess.run(
            ["git", "add", "README.md"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Doctor Tests",
                "-c",
                "user.email=doctor-tests@example.invalid",
                "commit",
                "--quiet",
                "-m",
                "initial fixture commit",
            ],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    return root.resolve()


def materialize_doctor_fixture(name: str, destination: Path) -> Path:
    source = Path(__file__).parent / "fixtures" / "doctor" / name
    shutil.copytree(source, destination, dirs_exist_ok=True)
    return destination.resolve()


@dataclass(frozen=True, slots=True)
class _MutationEntry:
    path: str
    kind: str
    mode: int
    sha256: str | None


@dataclass(frozen=True, slots=True)
class DoctorMutationSnapshot:
    target_root: str
    git_common_dir: str
    target_entries: tuple[_MutationEntry, ...]
    worktree_git_pointer: _MutationEntry
    checkout_git_metadata: tuple[_MutationEntry, ...]
    index_sha256: str | None
    config_sha256: str | None
    common_dir_entries: tuple[_MutationEntry, ...]
    refs: tuple[_MutationEntry, ...]
    worktree_list: str


def _mutation_entry(path: Path, *, relative_to: Path) -> _MutationEntry:
    metadata = path.lstat()
    mode = stat.S_IMODE(metadata.st_mode)
    relative_path = path.relative_to(relative_to).as_posix()
    if stat.S_ISLNK(metadata.st_mode):
        kind = "symlink"
        digest = hashlib.sha256(os.fsencode(os.readlink(path))).hexdigest()
    elif stat.S_ISDIR(metadata.st_mode):
        kind = "directory"
        digest = None
    elif stat.S_ISREG(metadata.st_mode):
        kind = "file"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
    else:
        kind = "other"
        digest = None
    return _MutationEntry(relative_path, kind, mode, digest)


def _mutation_tree(
    root: Path, *, exclude_root_git: bool = False
) -> tuple[_MutationEntry, ...]:
    entries: list[_MutationEntry] = []

    def walk(directory: Path) -> None:
        for child in sorted(directory.iterdir(), key=lambda item: item.name):
            if exclude_root_git and directory == root and child.name == ".git":
                continue
            entry = _mutation_entry(child, relative_to=root)
            entries.append(entry)
            if entry.kind == "directory":
                walk(child)

    walk(root)
    return tuple(entries)


def _worktree_git_dir(root: Path) -> Path:
    dot_git = root / ".git"
    if dot_git.is_dir():
        return dot_git.resolve()
    if not dot_git.is_file():
        raise AssertionError("temporary test repository has no .git metadata")
    pointer = dot_git.read_text(encoding="utf-8").strip()
    prefix = "gitdir: "
    if not pointer.startswith(prefix):
        raise AssertionError("temporary worktree has an invalid .git pointer")
    git_dir = Path(pointer[len(prefix) :])
    if not git_dir.is_absolute():
        git_dir = dot_git.parent / git_dir
    return git_dir.resolve()


def _digest_if_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_doctor_mutation_state(
    root: Path, git_common_dir: Path
) -> DoctorMutationSnapshot:
    root = root.resolve()
    git_common_dir = git_common_dir.resolve()
    worktree_git_dir = _worktree_git_dir(root)
    pointer = _mutation_entry(root / ".git", relative_to=root)
    common_entries = _mutation_tree(git_common_dir)
    environment = os.environ.copy()
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    environment["GIT_TERMINAL_PROMPT"] = "0"
    worktree_listing = subprocess.run(
        ["git", "worktree", "list", "--porcelain"],
        cwd=root,
        shell=False,
        timeout=10.0,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=environment,
    ).stdout
    refs = tuple(
        entry
        for entry in common_entries
        if entry.path == "packed-refs" or entry.path.startswith("refs/")
    )
    return DoctorMutationSnapshot(
        target_root=str(root),
        git_common_dir=str(git_common_dir),
        target_entries=_mutation_tree(root, exclude_root_git=True),
        worktree_git_pointer=pointer,
        checkout_git_metadata=_mutation_tree(worktree_git_dir),
        index_sha256=_digest_if_file(worktree_git_dir / "index"),
        config_sha256=_digest_if_file(git_common_dir / "config"),
        common_dir_entries=common_entries,
        refs=refs,
        worktree_list=worktree_listing,
    )

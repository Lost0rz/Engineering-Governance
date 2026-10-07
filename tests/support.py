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

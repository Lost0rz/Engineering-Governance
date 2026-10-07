import contextlib
import importlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from support import (
    initialize_temporary_git_repository,
    materialize_doctor_fixture,
    snapshot_doctor_mutation_state,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PROJECT_ROOT / "src"


class DoctorCliTests(unittest.TestCase):
    def _run_cli(self, *arguments):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(SOURCE_ROOT)
        for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR"):
            environment.pop(name, None)
        return subprocess.run(
            [sys.executable, "-m", "engineering_governance", *arguments],
            cwd=PROJECT_ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def _target(self, parent: Path) -> Path:
        root = materialize_doctor_fixture("pass", parent / "repository")
        initialize_temporary_git_repository(root, initial_commit=True)
        return root

    def _git_common_dir(self, root: Path) -> Path:
        result = subprocess.run(
            ["git", "rev-parse", "--git-common-dir"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        common_dir = Path(result.stdout.strip())
        if not common_dir.is_absolute():
            common_dir = root / common_dir
        return common_dir.resolve()

    def test_doctor_target_emits_existing_report_and_exits_zero(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = self._target(Path(temporary))
            completed = self._run_cli("doctor", str(target))

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        self.assertEqual(len(completed.stdout.splitlines()), 1)
        self.assertTrue(completed.stdout.endswith("\n"))
        report = json.loads(completed.stdout)
        self.assertEqual(report["target"]["root"], str(target.resolve()))
        self.assertEqual(report["overall_result"], "PASS")

    def test_non_repository_target_returns_stop_without_report(self):
        with tempfile.TemporaryDirectory() as temporary:
            completed = self._run_cli("doctor", temporary)

        self.assertEqual(completed.returncode, 2, completed.stderr)
        self.assertEqual(completed.stdout, "")
        self.assertTrue(completed.stderr.startswith("STOP:"))
        self.assertLessEqual(len(completed.stderr), 256)
        self.assertEqual(len(completed.stderr.splitlines()), 1)

    def test_usage_errors_do_not_invoke_doctor(self):
        try:
            cli = importlib.import_module("engineering_governance.__main__")
        except ImportError as exc:
            self.fail(f"CLI entry point is absent: {exc}")

        with patch.object(cli, "run_doctor") as run_doctor:
            for arguments in (("doctor",), ("audit", "/tmp/unused-target")):
                with self.subTest(arguments=arguments):
                    with contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as raised:
                            cli.main(list(arguments))
                    self.assertNotEqual(raised.exception.code, 0)

            run_doctor.assert_not_called()

    def test_cli_preserves_dirty_target_content_and_git_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = self._target(Path(temporary))
            (target / "README.md").write_text("local change\n", encoding="utf-8")
            (target / "untracked.txt").write_text("local evidence\n", encoding="utf-8")
            common_dir = self._git_common_dir(target)
            before = snapshot_doctor_mutation_state(target, common_dir)

            completed = self._run_cli("doctor", str(target))

            after = snapshot_doctor_mutation_state(target, common_dir)

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        self.assertEqual(len(completed.stdout.splitlines()), 1)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()

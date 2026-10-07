import io
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from support import (
    DoctorMutationSnapshot,
    initialize_temporary_git_repository,
    materialize_doctor_fixture,
    snapshot_doctor_mutation_state,
)


FIXED_TIME = datetime(2026, 10, 7, 12, 0, tzinfo=timezone.utc)


class DoctorTests(unittest.TestCase):
    def _api(self):
        try:
            from engineering_governance.doctor import run_doctor
            from engineering_governance.git_reader import run_git_readonly
        except ImportError as exc:
            self.fail(f"Doctor orchestration API is absent: {exc}")
        return run_doctor, run_git_readonly

    def _target(self, temporary, fixture="pass", *, initial_commit=True):
        root = materialize_doctor_fixture(fixture, Path(temporary) / "repo")
        initialize_temporary_git_repository(root, initial_commit=initial_commit)
        return root

    def _common_dir(self, root):
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

    def _run(self, run_doctor, git_runner, root):
        stdout = io.StringIO()
        stderr = io.StringIO()
        exit_code = run_doctor(
            root,
            stdout=stdout,
            stderr=stderr,
            git_runner=git_runner,
            file_reader=Path.read_bytes,
            clock=lambda: FIXED_TIME,
        )
        return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_run_doctor_emits_one_pass_report_and_exit_zero(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary)
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(output.splitlines()), 1)
        self.assertTrue(output.endswith("\n"))
        report = json.loads(output)
        self.assertEqual(report["overall_result"], "PASS")
        self.assertEqual(error, "")

    def test_run_doctor_emits_fail_report_and_exit_zero(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary, "inconsistent-task-id")
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        report = json.loads(output)
        consistency = next(
            item
            for item in report["evaluations"]
            if item["check_id"] == "doctor.controls.task_status_consistency"
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["overall_result"], "FAIL")
        self.assertEqual(consistency["result"], "FAIL")
        self.assertEqual(error, "")

    def test_run_doctor_emits_unverified_report_and_exit_zero(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary, "unverified-missing-status")
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        report = json.loads(output)
        presence = next(
            item
            for item in report["evaluations"]
            if item["check_id"] == "doctor.controls.presence"
        )
        consistency = next(
            item
            for item in report["evaluations"]
            if item["check_id"] == "doctor.controls.task_status_consistency"
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["overall_result"], "UNVERIFIED")
        self.assertEqual(presence["result"], "UNVERIFIED")
        self.assertEqual(consistency["result"], "UNVERIFIED")
        self.assertEqual(consistency["freshness"], "UNKNOWN")
        self.assertNotEqual(consistency["result"], "PASS")
        self.assertEqual(error, "")

    def test_unresolvable_head_emits_unverified_report_and_exit_zero(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary, initial_commit=False)
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        report = json.loads(output)
        identity = next(
            item
            for item in report["evaluations"]
            if item["check_id"] == "doctor.repository.identity"
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["target"]["head"], None)
        self.assertEqual(identity["result"], "UNVERIFIED")
        self.assertEqual(identity["freshness"], "UNKNOWN")
        self.assertEqual(error, "")

    def test_non_repository_returns_two_without_report(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        self.assertEqual(exit_code, 2)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("STOP:"))
        self.assertLessEqual(len(error), 256)
        self.assertEqual(len(error.splitlines()), 1)

    def test_malformed_root_returns_two_without_report(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary, "malformed-task")
            exit_code, output, error = self._run(run_doctor, git_runner, root)

        self.assertEqual(exit_code, 2)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("STOP:"))
        self.assertLessEqual(len(error), 256)
        self.assertEqual(len(error.splitlines()), 1)

    def test_internal_failure_returns_three_without_report(self):
        run_doctor, _ = self._api()

        def unexpected_git_failure(cwd, args, timeout):
            raise RuntimeError("unexpected injected failure")

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            exit_code, output, error = self._run(
                run_doctor, unexpected_git_failure, root
            )

        self.assertEqual(exit_code, 3)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("ERROR: INTERNAL_FATAL"))
        self.assertLessEqual(len(error), 256)
        self.assertNotIn("Traceback", error)

    def test_git_probe_timeout_returns_two_without_report(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary)
            with patch(
                "engineering_governance.git_reader.subprocess.run",
                side_effect=subprocess.TimeoutExpired(
                    ["git", "rev-parse", "--show-toplevel"], timeout=5.0
                ),
            ) as subprocess_run:
                exit_code, output, error = self._run(run_doctor, git_runner, root)

        subprocess_run.assert_called_once()
        self.assertEqual(exit_code, 2)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("STOP:"))
        self.assertLessEqual(len(error), 256)
        self.assertEqual(len(error.splitlines()), 1)
        self.assertNotIn("UNVERIFIED", error)

    def test_dirty_repository_content_and_git_metadata_are_unchanged(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._target(temporary)
            (root / "README.md").write_text("locally modified\n", encoding="utf-8")
            (root / "untracked.txt").write_text("untracked evidence\n", encoding="utf-8")
            common_dir = self._common_dir(root)
            before = snapshot_doctor_mutation_state(root, common_dir)

            exit_code, output, error = self._run(run_doctor, git_runner, root)
            after = snapshot_doctor_mutation_state(root, common_dir)

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(output.splitlines()), 1)
        self.assertEqual(error, "")
        self.assertIsInstance(before, DoctorMutationSnapshot)
        self.assertEqual(before, after)

    def test_linked_worktree_refs_and_index_are_unchanged(self):
        run_doctor, git_runner = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            temporary_path = Path(temporary)
            main_root = initialize_temporary_git_repository(
                temporary_path / "main", initial_commit=True
            )
            linked_root = temporary_path / "linked"
            subprocess.run(
                ["git", "worktree", "add", "--quiet", "-b", "linked-task", str(linked_root)],
                cwd=main_root,
                check=True,
                capture_output=True,
                text=True,
            )
            materialize_doctor_fixture("pass", linked_root)
            common_dir = self._common_dir(linked_root)
            before = snapshot_doctor_mutation_state(linked_root, common_dir)

            exit_code, output, error = self._run(run_doctor, git_runner, linked_root)
            after = snapshot_doctor_mutation_state(linked_root, common_dir)

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(output.splitlines()), 1)
        self.assertEqual(error, "")
        self.assertEqual(before.refs, after.refs)
        self.assertEqual(before.worktree_list, after.worktree_list)
        self.assertEqual(before.index_sha256, after.index_sha256)
        self.assertEqual(before.config_sha256, after.config_sha256)
        self.assertEqual(before.common_dir_entries, after.common_dir_entries)
        self.assertEqual(before, after)

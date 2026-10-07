import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from support import initialize_temporary_git_repository


class GitReaderTests(unittest.TestCase):
    def _api(self):
        try:
            from engineering_governance.git_reader import (
                read_repository,
                run_git_readonly,
            )
            from engineering_governance.model import CommandResult, DoctorStop
        except ImportError as exc:
            self.fail(f"Git reader API is absent: {exc}")
        return read_repository, run_git_readonly, CommandResult, DoctorStop

    def test_repository_identity_observes_root_common_dir_head_and_branch(self):
        read_repository, run_git_readonly, _, _ = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            root = initialize_temporary_git_repository(
                Path(temporary) / "repo", initial_commit=True
            )
            nested = root / "nested" / "directory"
            nested.mkdir(parents=True)

            identity = read_repository(nested, git_runner=run_git_readonly)

        self.assertEqual(identity.root, str(root.resolve()))
        self.assertEqual(identity.git_common_dir, str((root / ".git").resolve()))
        self.assertRegex(identity.head, r"\A[0-9a-f]{40,64}\Z")
        self.assertTrue(identity.branch)
        self.assertIs(identity.detached, False)

    def test_detached_head_has_no_inferred_branch(self):
        read_repository, run_git_readonly, _, _ = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            root = initialize_temporary_git_repository(
                Path(temporary) / "repo", initial_commit=True
            )
            subprocess.run(
                ["git", "checkout", "--quiet", "--detach", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            )
            head_before = subprocess.run(
                ["git", "rev-parse", "--verify", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            identity = read_repository(root, git_runner=run_git_readonly)

            head_after = subprocess.run(
                ["git", "rev-parse", "--verify", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

        self.assertIsNone(identity.branch)
        self.assertIs(identity.detached, True)
        self.assertEqual(identity.head, head_before)
        self.assertEqual(head_after, head_before)

    def test_unborn_head_is_unknown_without_claiming_reason(self):
        read_repository, run_git_readonly, _, _ = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            root = initialize_temporary_git_repository(
                Path(temporary) / "repo", initial_commit=False
            )

            identity = read_repository(root, git_runner=run_git_readonly)

        self.assertEqual(identity.root, str(root.resolve()))
        self.assertIsNone(identity.head)
        self.assertTrue(identity.branch)
        self.assertIs(identity.detached, False)

    def test_symbolic_ref_error_keeps_known_root_unverified(self):
        read_repository, _, CommandResult, _ = self._api()
        head = "0123456789abcdef0123456789abcdef01234567"

        with tempfile.TemporaryDirectory() as temporary:
            root = initialize_temporary_git_repository(
                Path(temporary) / "repo", initial_commit=True
            )

            def runner(cwd, args, timeout):
                if args == ("rev-parse", "--show-toplevel"):
                    return CommandResult(0, f"{root}\n", "")
                if args == ("rev-parse", "--git-common-dir"):
                    return CommandResult(0, ".git\n", "")
                if args == ("rev-parse", "--verify", "HEAD"):
                    return CommandResult(0, f"{head}\n", "")
                if args == ("symbolic-ref", "--quiet", "--short", "HEAD"):
                    return CommandResult(128, "", "symbolic ref unavailable")
                self.fail(f"unexpected Git tuple: {args!r}")

            identity = read_repository(root, git_runner=runner)

        self.assertEqual(identity.root, str(root))
        self.assertEqual(identity.head, head)
        self.assertIsNone(identity.branch)
        self.assertIsNone(identity.detached)

    def test_non_repository_target_raises_doctor_stop(self):
        read_repository, run_git_readonly, _, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            ordinary_directory = Path(temporary).resolve()
            with self.assertRaises(DoctorStop):
                read_repository(ordinary_directory, git_runner=run_git_readonly)

    def test_reader_uses_only_exact_allowed_git_probe_tuples(self):
        read_repository, _, CommandResult, _ = self._api()
        head = "0123456789abcdef0123456789abcdef01234567"

        with tempfile.TemporaryDirectory() as temporary:
            root = initialize_temporary_git_repository(
                Path(temporary) / "repo", initial_commit=True
            )
            calls = []

            def runner(cwd, args, timeout):
                calls.append(args)
                outputs = {
                    ("rev-parse", "--show-toplevel"): f"{root}\n",
                    ("rev-parse", "--git-common-dir"): ".git\n",
                    ("rev-parse", "--verify", "HEAD"): f"{head}\n",
                    ("symbolic-ref", "--quiet", "--short", "HEAD"): "main\n",
                }
                return CommandResult(0, outputs[args], "")

            read_repository(root, git_runner=runner)

        self.assertEqual(
            calls,
            [
                ("rev-parse", "--show-toplevel"),
                ("rev-parse", "--git-common-dir"),
                ("rev-parse", "--verify", "HEAD"),
                ("symbolic-ref", "--quiet", "--short", "HEAD"),
            ],
        )

    def test_fetch_tuple_is_rejected_before_subprocess(self):
        _, run_git_readonly, _, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            with patch(
                "engineering_governance.git_reader.subprocess.run"
            ) as subprocess_run:
                with self.assertRaises(DoctorStop):
                    run_git_readonly(Path(temporary), ("fetch", "--all"))

        subprocess_run.assert_not_called()

    def test_remote_tuple_is_rejected_before_subprocess(self):
        _, run_git_readonly, _, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            with patch(
                "engineering_governance.git_reader.subprocess.run"
            ) as subprocess_run:
                with self.assertRaises(DoctorStop):
                    run_git_readonly(Path(temporary), ("remote", "-v"))

        subprocess_run.assert_not_called()

    def test_ls_remote_tuple_is_rejected_before_subprocess(self):
        _, run_git_readonly, _, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            with patch(
                "engineering_governance.git_reader.subprocess.run"
            ) as subprocess_run:
                with self.assertRaises(DoctorStop):
                    run_git_readonly(Path(temporary), ("ls-remote", "origin"))

        subprocess_run.assert_not_called()

    def test_any_unlisted_git_tuple_is_rejected_before_subprocess(self):
        _, run_git_readonly, _, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            with patch(
                "engineering_governance.git_reader.subprocess.run"
            ) as subprocess_run:
                for args in (("push", "origin"), ("status", "--short")):
                    with self.subTest(args=args), self.assertRaises(DoctorStop):
                        run_git_readonly(Path(temporary), args)

        subprocess_run.assert_not_called()

    def test_run_git_readonly_invokes_git_with_readonly_process_contract(self):
        _, run_git_readonly, CommandResult, _ = self._api()
        cwd = Path("/tmp/doctor-target")
        args = ("rev-parse", "--show-toplevel")
        argv = ["git", *args]
        completed = subprocess.CompletedProcess(
            argv,
            0,
            stdout="/tmp/doctor-target\n",
            stderr="",
        )
        expected_env = os.environ.copy()
        expected_env["GIT_OPTIONAL_LOCKS"] = "0"
        expected_env["GIT_TERMINAL_PROMPT"] = "0"

        with patch(
            "engineering_governance.git_reader.subprocess.run",
            return_value=completed,
        ) as subprocess_run:
            result = run_git_readonly(cwd, args)

        subprocess_run.assert_called_once()
        call_args, call_kwargs = subprocess_run.call_args
        self.assertEqual(call_args, (argv,))
        self.assertEqual(
            call_kwargs,
            {
                "cwd": cwd,
                "shell": False,
                "timeout": 5.0,
                "check": False,
                "capture_output": True,
                "text": True,
                "encoding": "utf-8",
                "errors": "replace",
                "env": expected_env,
            },
        )
        self.assertEqual(result, CommandResult(0, "/tmp/doctor-target\n", ""))

    def test_run_git_readonly_timeout_becomes_doctor_stop(self):
        _, run_git_readonly, _, DoctorStop = self._api()
        args = ("rev-parse", "--show-toplevel")

        with tempfile.TemporaryDirectory() as temporary:
            with patch(
                "engineering_governance.git_reader.subprocess.run",
                side_effect=subprocess.TimeoutExpired(
                    ["git", *args], timeout=5.0
                ),
            ) as subprocess_run:
                with self.assertRaises(DoctorStop) as caught:
                    run_git_readonly(Path(temporary), args)

        self.assertEqual(caught.exception.code, "GIT_PROBE_TIMEOUT")
        subprocess_run.assert_called_once()

    def test_repository_selection_environment_overrides_stop_before_git_probe(self):
        read_repository, _, CommandResult, DoctorStop = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            target = base / "ordinary-target"
            target.mkdir()
            common_dir = base / "foreign-common"
            common_dir.mkdir()
            head = "0123456789abcdef0123456789abcdef01234567"
            calls = []

            def runner(cwd, args, timeout):
                calls.append(args)
                outputs = {
                    ("rev-parse", "--show-toplevel"): f"{target}\n",
                    ("rev-parse", "--git-common-dir"): f"{common_dir}\n",
                    ("rev-parse", "--verify", "HEAD"): f"{head}\n",
                    ("symbolic-ref", "--quiet", "--short", "HEAD"): "main\n",
                }
                return CommandResult(0, outputs[args], "")

            overrides = {
                "GIT_DIR": str(common_dir),
                "GIT_WORK_TREE": str(target),
                "GIT_COMMON_DIR": str(common_dir),
            }
            for name, value in overrides.items():
                with self.subTest(name=name):
                    calls.clear()
                    with patch.dict(os.environ, {name: value}):
                        with self.assertRaises(DoctorStop) as caught:
                            read_repository(target, git_runner=runner)
                    self.assertEqual(caught.exception.code, "GIT_ENVIRONMENT_UNTRUSTED")
                    self.assertEqual(calls, [])

    def test_git_common_dir_path_preserves_trailing_space(self):
        read_repository, _, CommandResult, _ = self._api()

        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = initialize_temporary_git_repository(
                base / "repository", initial_commit=True
            )
            common_dir = base / "common directory "
            common_dir.mkdir()
            head = "0123456789abcdef0123456789abcdef01234567"

            def runner(cwd, args, timeout):
                outputs = {
                    ("rev-parse", "--show-toplevel"): f"{root}\n",
                    ("rev-parse", "--git-common-dir"): f"{common_dir}\n",
                    ("rev-parse", "--verify", "HEAD"): f"{head}\n",
                    ("symbolic-ref", "--quiet", "--short", "HEAD"): "main\n",
                }
                return CommandResult(0, outputs[args], "")

            identity = read_repository(root, git_runner=runner)

        self.assertEqual(identity.git_common_dir, str(common_dir.resolve()))

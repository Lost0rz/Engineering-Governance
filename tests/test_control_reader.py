import hashlib
import tempfile
import unittest
from pathlib import Path

from support import materialize_doctor_fixture


class ControlReaderTests(unittest.TestCase):
    def _api(self):
        try:
            from engineering_governance.control_reader import read_controls
            from engineering_governance.model import (
                ControlState,
                EvaluationResult,
                Freshness,
                DoctorStop,
            )
        except ImportError as exc:
            self.fail(f"Control reader API is absent: {exc}")
        return read_controls, ControlState, EvaluationResult, Freshness, DoctorStop

    def _materialize(self, temporary, fixture="pass"):
        return materialize_doctor_fixture(fixture, Path(temporary) / "target")

    def test_control_files_are_reported_in_fixed_order_with_digests(self):
        read_controls, ControlState, _, _, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            snapshot = read_controls(root, file_reader=Path.read_bytes)
            expected_contents = {
                name: (root / name).read_bytes()
                for name in ("AGENTS.md", "CURRENT_STATUS.md", "CURRENT_TASK.md")
            }

        expected_names = ("AGENTS.md", "CURRENT_STATUS.md", "CURRENT_TASK.md")
        self.assertEqual(
            tuple(Path(item.path).name for item in snapshot.files), expected_names
        )
        self.assertEqual(
            tuple(item.path for item in snapshot.files),
            tuple(str(root / name) for name in expected_names),
        )
        for observation, name in zip(snapshot.files, expected_names):
            contents = expected_contents[name]
            self.assertIs(observation.state, ControlState.PRESENT)
            self.assertEqual(observation.sha256, hashlib.sha256(contents).hexdigest())
            self.assertEqual(observation.size_bytes, len(contents))
        self.assertFalse(hasattr(snapshot, "contents"))

    def test_missing_status_is_unverified_unknown(self):
        read_controls, ControlState, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary, "unverified-missing-status")
            snapshot = read_controls(root, file_reader=Path.read_bytes)

        status = next(item for item in snapshot.files if item.path.endswith("CURRENT_STATUS.md"))
        self.assertIs(status.state, ControlState.MISSING)
        for evaluation in (snapshot.presence, snapshot.consistency):
            self.assertIs(evaluation.result, EvaluationResult.UNVERIFIED)
            self.assertIs(evaluation.freshness, Freshness.UNKNOWN)
            self.assertTrue(any("CURRENT_STATUS.md" in item for item in evaluation.limitations))

    def test_unreadable_control_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)

            def unreadable(path):
                if path.name == "CURRENT_STATUS.md":
                    raise PermissionError("synthetic unreadable control")
                return path.read_bytes()

            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=unreadable)

    def test_invalid_utf8_control_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)

            def invalid_utf8(path):
                if path.name == "CURRENT_STATUS.md":
                    return b"\xff\xfe"
                return path.read_bytes()

            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=invalid_utf8)

    def test_blank_control_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "AGENTS.md").write_text(" \t\n", encoding="utf-8")
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_symlink_control_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            control = root / "AGENTS.md"
            control.unlink()
            control.symlink_to(root / "CURRENT_TASK.md")
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_non_regular_control_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            control = root / "AGENTS.md"
            control.unlink()
            control.mkdir()
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_missing_task_id_field_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary, "malformed-task")
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_duplicate_task_id_field_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            task = root / "CURRENT_TASK.md"
            task.write_text(
                "Task ID: TASK-1\nTask ID: TASK-2\nState: ACTIVE\n",
                encoding="utf-8",
            )
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_missing_task_state_field_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_TASK.md").write_text(
                "Task ID: TASK-1\n", encoding="utf-8"
            )
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_invalid_task_id_syntax_raises_doctor_stop(self):
        read_controls, _, _, _, DoctorStop = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_TASK.md").write_text(
                "Task ID: TÄSK-1\nState: ACTIVE\n", encoding="utf-8"
            )
            with self.assertRaises(DoctorStop):
                read_controls(root, file_reader=Path.read_bytes)

    def test_task_id_exact_reference_matches(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text("TASK-1\n", encoding="utf-8")
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.PASS)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_inside_backticks_matches(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text("`TASK-1`\n", encoding="utf-8")
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.PASS)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_in_ordinary_prose_matches(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text(
                "The active task is (TASK-1);\n", encoding="utf-8"
            )
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.PASS)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_prefix_collision_does_not_match(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text("TASK-10\n", encoding="utf-8")
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.FAIL)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_suffix_collision_does_not_match(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text(
                "TASK-1-extra\n", encoding="utf-8"
            )
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.FAIL)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_embedded_identifier_does_not_match(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text(
                "XTASK-1 TASK-1_extra TASK-1/child\n", encoding="utf-8"
            )
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.FAIL)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_task_id_slash_and_dot_boundaries_are_identifier_characters(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_TASK.md").write_text(
                "Task ID: AREA/TASK.1\nState: ACTIVE\n", encoding="utf-8"
            )
            (root / "CURRENT_STATUS.md").write_text(
                "AREA/TASK.10 AREA/TASK.1/child\n", encoding="utf-8"
            )
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.FAIL)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

    def test_missing_task_id_reference_is_consistency_fail(self):
        read_controls, _, EvaluationResult, Freshness, _ = self._api()
        with tempfile.TemporaryDirectory() as temporary:
            root = self._materialize(temporary)
            (root / "CURRENT_STATUS.md").write_text(
                "Readable status without task reference.\n", encoding="utf-8"
            )
            snapshot = read_controls(root, file_reader=Path.read_bytes)
        self.assertIs(snapshot.consistency.result, EvaluationResult.FAIL)
        self.assertIs(snapshot.consistency.freshness, Freshness.CURRENT)

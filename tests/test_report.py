import unittest
from datetime import datetime, timezone
from hashlib import sha256


class ReportTests(unittest.TestCase):
    def _report_api(self, case, *, presence_result="PASS", consistency_result="PASS"):
        try:
            from engineering_governance.model import (
                ControlSnapshot,
                Evaluation,
                EvaluationResult,
                Freshness,
                RepositoryIdentity,
            )
            from engineering_governance.report import (
                _canonical_json,
                _report_payload,
                build_doctor_report,
                serialize_report,
            )
        except ImportError as exc:
            case.fail(f"report/model API is absent: {exc}")

        target = RepositoryIdentity(
            root="/tmp/doctor-target",
            git_common_dir="/tmp/doctor-target/.git",
            head="0123456789abcdef0123456789abcdef01234567",
            branch="main",
            detached=False,
        )
        presence = Evaluation(
            check_id="doctor.controls.presence",
            result=EvaluationResult(presence_result),
            freshness=Freshness.CURRENT,
            evidence_paths=("AGENTS.md",),
            limitations=(),
        )
        consistency = Evaluation(
            check_id="doctor.controls.task_status_consistency",
            result=EvaluationResult(consistency_result),
            freshness=Freshness.CURRENT,
            evidence_paths=("CURRENT_TASK.md", "CURRENT_STATUS.md"),
            limitations=(),
        )
        controls = ControlSnapshot(
            files=(),
            task_id="TASK-1",
            task_state="ACTIVE",
            consistency=consistency,
            presence=presence,
        )
        report = build_doctor_report(
            target,
            controls,
            datetime(2026, 10, 7, 0, 0, tzinfo=timezone.utc),
        )
        return report, _canonical_json, _report_payload, serialize_report

    def test_canonical_json_is_stable_across_mapping_order(self):
        _, canonical_json, _, _ = self._report_api(self)

        first = {"z": "雪", "a": 1}
        second = {"a": 1, "z": "雪"}

        self.assertEqual(canonical_json(first), canonical_json(second))
        self.assertEqual(canonical_json(first), b'{"a":1,"z":"\xe9\x9b\xaa"}')

    def test_report_identity_excludes_identity_field_from_digest(self):
        report, canonical_json, report_payload, _ = self._report_api(self)

        payload_without_identity = report_payload(report, include_identity=False)
        expected = "sha256:" + sha256(canonical_json(payload_without_identity)).hexdigest()

        self.assertEqual(report.report_identity, expected)

    def test_report_serialization_ends_with_one_newline(self):
        report, _, _, serialize_report = self._report_api(self)

        serialized = serialize_report(report)

        self.assertTrue(serialized.endswith("\n"))
        self.assertFalse(serialized.endswith("\n\n"))

    def test_overall_result_preserves_unverified(self):
        report, _, _, _ = self._report_api(self, presence_result="UNVERIFIED")
        try:
            from engineering_governance.model import EvaluationResult
        except ImportError as exc:
            self.fail(f"model API is absent: {exc}")

        self.assertEqual(report.overall_result, EvaluationResult.UNVERIFIED)
        self.assertIn(
            EvaluationResult.UNVERIFIED,
            {evaluation.result for evaluation in report.evaluations},
        )

    def test_overall_result_prefers_fail_to_unverified(self):
        report, _, _, _ = self._report_api(
            self,
            presence_result="UNVERIFIED",
            consistency_result="FAIL",
        )
        try:
            from engineering_governance.model import EvaluationResult
        except ImportError as exc:
            self.fail(f"model API is absent: {exc}")

        self.assertEqual(report.overall_result, EvaluationResult.FAIL)
        self.assertIn(
            EvaluationResult.FAIL,
            {evaluation.result for evaluation in report.evaluations},
        )
        self.assertIn(
            EvaluationResult.UNVERIFIED,
            {evaluation.result for evaluation in report.evaluations},
        )

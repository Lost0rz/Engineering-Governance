import unittest
from dataclasses import FrozenInstanceError


class ModelTests(unittest.TestCase):
    def test_evaluation_enums_are_exact(self):
        try:
            from engineering_governance.model import (
                ControlState,
                EvaluationResult,
                Freshness,
            )
        except ImportError as exc:
            self.fail(f"model API is absent: {exc}")

        self.assertEqual(
            {member.value for member in EvaluationResult},
            {"PASS", "FAIL", "UNVERIFIED", "NOT_APPLICABLE"},
        )
        self.assertEqual(
            {member.value for member in Freshness},
            {"CURRENT", "STALE", "UNKNOWN"},
        )
        self.assertEqual(
            {member.value for member in ControlState},
            {"PRESENT", "MISSING"},
        )

    def test_shared_records_are_frozen_and_collections_are_tuples(self):
        try:
            from engineering_governance.model import (
                Evaluation,
                EvaluationResult,
                Freshness,
            )
        except ImportError as exc:
            self.fail(f"model API is absent: {exc}")

        evaluation = Evaluation(
            check_id="doctor.controls.presence",
            result=EvaluationResult.PASS,
            freshness=Freshness.CURRENT,
            evidence_paths=("AGENTS.md",),
            limitations=(),
        )

        with self.assertRaises(FrozenInstanceError):
            evaluation.check_id = "changed"
        with self.assertRaises(AttributeError):
            evaluation.evidence_paths.append("CURRENT_TASK.md")
        with self.assertRaises(AttributeError):
            evaluation.limitations.append("changed")

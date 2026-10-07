import json
from collections.abc import Mapping
from dataclasses import replace
from datetime import datetime, timezone
from hashlib import sha256

from .model import (
    ControlSnapshot,
    ControlState,
    DoctorReport,
    Evaluation,
    EvaluationResult,
    Freshness,
    RepositoryIdentity,
)


REPORT_VERSION = "doctor-base.v1"
TOOL_VERSION = "doctor-foundation/1"
STANDARD_VERSION = "EngineeringGovernanceStandard 0.1.0"


def _overall_result(evaluations: tuple[Evaluation, ...]) -> EvaluationResult:
    results = tuple(evaluation.result for evaluation in evaluations)
    if EvaluationResult.FAIL in results:
        return EvaluationResult.FAIL
    if EvaluationResult.UNVERIFIED in results:
        return EvaluationResult.UNVERIFIED
    if results and all(result is EvaluationResult.NOT_APPLICABLE for result in results):
        return EvaluationResult.NOT_APPLICABLE
    return EvaluationResult.PASS


def build_doctor_report(
    target: RepositoryIdentity,
    controls: ControlSnapshot,
    observed_at: datetime,
) -> DoctorReport:
    if observed_at.tzinfo is None or observed_at.utcoffset() is None:
        raise ValueError("observed_at must be timezone-aware")
    observed_utc = observed_at.astimezone(timezone.utc)
    observed_at_text = observed_utc.isoformat().replace("+00:00", "Z")

    identity_limitations: tuple[str, ...] = ()
    if target.head is None:
        identity_limitations = ("Git HEAD could not be resolved.",)
    elif target.detached is None:
        identity_limitations = ("Git branch or detached state could not be resolved.",)

    identity_evaluation = Evaluation(
        check_id="doctor.repository.identity",
        result=(
            EvaluationResult.UNVERIFIED
            if identity_limitations
            else EvaluationResult.PASS
        ),
        freshness=(Freshness.UNKNOWN if identity_limitations else Freshness.CURRENT),
        evidence_paths=(target.root, target.git_common_dir),
        limitations=identity_limitations,
    )
    evaluations = (
        identity_evaluation,
        controls.presence,
        controls.consistency,
    )
    limitations = tuple(
        dict.fromkeys(
            limitation
            for evaluation in evaluations
            for limitation in evaluation.limitations
        )
    )
    report_without_identity = DoctorReport(
        report_version=REPORT_VERSION,
        tool_version=TOOL_VERSION,
        standard_version=STANDARD_VERSION,
        observed_at=observed_at_text,
        target=target,
        overall_result=_overall_result(evaluations),
        evaluations=evaluations,
        controls=controls.files,
        limitations=limitations,
        report_identity="",
    )
    identity = "sha256:" + sha256(
        _canonical_json(_report_payload(report_without_identity, include_identity=False))
    ).hexdigest()
    return replace(report_without_identity, report_identity=identity)


def _report_payload(
    report: DoctorReport, *, include_identity: bool
) -> dict[str, object]:
    payload: dict[str, object] = {
        "report_version": report.report_version,
        "tool_version": report.tool_version,
        "standard_version": report.standard_version,
        "observed_at": report.observed_at,
        "target": {
            "root": report.target.root,
            "git_common_dir": report.target.git_common_dir,
            "head": report.target.head,
            "branch": report.target.branch,
            "detached": report.target.detached,
        },
        "overall_result": report.overall_result.value,
        "evaluations": [
            {
                "check_id": evaluation.check_id,
                "result": evaluation.result.value,
                "freshness": evaluation.freshness.value,
                "evidence_paths": list(evaluation.evidence_paths),
                "limitations": list(evaluation.limitations),
            }
            for evaluation in report.evaluations
        ],
        "controls": [
            {
                "path": control.path,
                "state": control.state.value,
                "size_bytes": control.size_bytes,
                "sha256": control.sha256,
            }
            for control in report.controls
        ],
        "limitations": list(report.limitations),
    }
    if include_identity:
        payload["report_identity"] = report.report_identity
    return payload


def _canonical_json(payload: Mapping[str, object]) -> bytes:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def serialize_report(report: DoctorReport) -> str:
    payload = _report_payload(report, include_identity=True)
    return _canonical_json(payload).decode("utf-8") + "\n"

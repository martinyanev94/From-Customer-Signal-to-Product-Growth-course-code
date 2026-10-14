from __future__ import annotations

from typing import Any

ALLOWED_METHODS = {
    "semi_structured_interview",
    "workflow_survey",
    "usage_signal",
}


def validate_program(program: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not program.get("decision"):
        errors.append("missing decision")
    participants = program.get("participants", {})
    if not participants.get("include"):
        errors.append("missing participant criteria")
    if not isinstance(participants.get("target_count"), int) or participants["target_count"] <= 0:
        errors.append("target_count must be a positive integer")
    methods = set(program.get("methods", []))
    if not methods:
        errors.append("missing research method")
    unknown_methods = methods - ALLOWED_METHODS
    if unknown_methods:
        errors.append("unsupported method: " + ", ".join(sorted(unknown_methods)))
    capture = program.get("capture", {})
    if capture.get("consent_status") not in {"pending", "granted", "declined"}:
        errors.append("consent_status must be pending, granted, or declined")
    if capture.get("recording_allowed") and capture.get("consent_status") != "granted":
        errors.append("recording requires granted consent")
    if not capture.get("pii_redacted"):
        errors.append("PII must be redacted")
    if not isinstance(capture.get("retention_days"), int) or capture["retention_days"] <= 0:
        errors.append("retention_days must be a positive integer")
    if not program.get("decision_owner"):
        errors.append("missing decision owner")
    return errors


def validate_insight(insight: dict[str, Any]) -> list[str]:
    required = ("participant_id", "workflow_stage", "observation", "evidence_ref", "confidence", "owner", "next_action")
    return [f"missing insight field: {field}" for field in required if not insight.get(field)]

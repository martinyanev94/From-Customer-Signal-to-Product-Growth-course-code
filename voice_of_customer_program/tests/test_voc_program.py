from voc_program import validate_insight, validate_program


def test_sample_program_is_valid():
    program = {
        "decision": "Reduce friction?",
        "participants": {"include": ["recent users"], "target_count": 4},
        "methods": ["semi_structured_interview"],
        "capture": {"consent_status": "pending", "recording_allowed": False, "pii_redacted": True, "retention_days": 90},
        "decision_owner": "product_manager",
    }
    assert validate_program(program) == []


def test_recording_requires_granted_consent():
    program = {
        "decision": "Reduce friction?",
        "participants": {"include": ["recent users"], "target_count": 4},
        "methods": ["semi_structured_interview"],
        "capture": {"consent_status": "pending", "recording_allowed": True, "pii_redacted": True, "retention_days": 90},
        "decision_owner": "product_manager",
    }
    assert "recording requires granted consent" in validate_program(program)


def test_insight_requires_evidence_and_owner():
    errors = validate_insight({"participant_id": "participant-004"})
    assert "missing insight field: evidence_ref" in errors
    assert "missing insight field: owner" in errors

from src.message_linter import lint_message


MESSAGE = {
    "audience": "operations leaders using spreadsheets for weekly reporting",
    "alternative": "manual spreadsheet consolidation",
    "outcome": "produce a weekly report in hours instead of days",
    "differentiator": "connects source systems and preserves an audit trail",
    "proof": "proof_registry.reporting_pilot_01",
    "objection": "implementation will take too much team time",
    "objection_response": "Start with one reporting workflow and review its source mapping.",
    "next_step": "Review the reporting workflow and audit trail",
    "text": "SignalDesk connects reporting sources so operations leaders can produce a weekly report in hours, with an audit trail.",
    "action": "Review the reporting workflow",
}


def test_complete_message_passes_all_checks():
    result = lint_message(MESSAGE)
    assert all(result["checks"].values())
    assert result["issues"] == []
    assert result["weakest"] is None


def test_missing_proof_identifies_credibility_as_weakest():
    incomplete = {**MESSAGE, "proof": ""}
    result = lint_message(incomplete)
    assert result["checks"]["credibility"] is False
    assert "missing:proof" in result["issues"]
    assert result["weakest"] == "credibility"


def test_repeated_alternative_does_not_count_as_differentiation():
    weak = {**MESSAGE, "differentiator": MESSAGE["alternative"]}
    result = lint_message(weak)
    assert result["checks"]["differentiation"] is False
    assert "differentiation:restates-alternative" in result["issues"]

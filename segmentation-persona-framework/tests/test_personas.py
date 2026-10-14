import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from personas import Persona, persona_report, signaldesk_persona, validate_persona


def test_signaldesk_persona_is_structurally_valid():
    assert validate_persona(signaldesk_persona) == []


def test_report_preserves_evidence_gaps_and_readiness():
    report = persona_report(signaldesk_persona)
    assert report["decision_ready"] is True
    assert len(report["evidence_gaps"]) == 2


def test_missing_evidence_reference_is_reported():
    incomplete = Persona(
        segment="Example segment",
        job_context="A real trigger and decision",
        functional_progress="A concrete functional outcome",
        emotional_progress="A concrete emotional outcome",
        constraints=["Time"],
        alternatives=["Manual work"],
        desired_outcomes=["A decision"],
    )
    assert "evidence_refs" in validate_persona(incomplete)
    assert persona_report(incomplete)["decision_ready"] is False

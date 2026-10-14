from dataclasses import dataclass, field
from typing import List


@dataclass
class Persona:
    segment: str
    job_context: str
    functional_progress: str
    emotional_progress: str
    constraints: List[str] = field(default_factory=list)
    alternatives: List[str] = field(default_factory=list)
    desired_outcomes: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)
    evidence_gaps: List[str] = field(default_factory=list)


def validate_persona(persona: Persona) -> List[str]:
    errors = []
    required = {
        "segment": persona.segment,
        "job_context": persona.job_context,
        "functional_progress": persona.functional_progress,
        "emotional_progress": persona.emotional_progress,
    }
    errors.extend(name for name, value in required.items() if not value.strip())
    if not persona.constraints:
        errors.append("constraints")
    if not persona.alternatives:
        errors.append("alternatives")
    if not persona.desired_outcomes:
        errors.append("desired_outcomes")
    if not persona.evidence_refs:
        errors.append("evidence_refs")
    return errors


def evidence_gaps(persona: Persona) -> List[str]:
    return list(persona.evidence_gaps)


def persona_report(persona: Persona) -> dict:
    structural_errors = validate_persona(persona)
    return {
        "structural_errors": structural_errors,
        "evidence_gaps": evidence_gaps(persona),
        "decision_ready": not structural_errors and bool(persona.evidence_refs),
    }


signaldesk_persona = Persona(
    segment="Evidence-driven product marketers",
    job_context=(
        "When scattered customer signals must become a roadmap recommendation, "
        "decide what deserves investment and defend it cross-functionally."
    ),
    functional_progress=(
        "Synthesize customer evidence into a prioritized, traceable recommendation."
    ),
    emotional_progress=(
        "Feel confident and credible when the recommendation is challenged."
    ),
    constraints=[
        "Limited time for synthesis",
        "Uneven evidence quality",
        "Multiple stakeholder priorities",
    ],
    alternatives=[
        "Spreadsheet and manual tagging",
        "Ad hoc team discussions",
        "Existing research or analytics tools",
    ],
    desired_outcomes=[
        "A ranked recommendation",
        "Evidence links preserved",
        "A decision the teams can act on",
    ],
    evidence_refs=[
        "insight-014",
        "interview-07",
        "roadmap-criterion-customer-evidence",
    ],
    evidence_gaps=[
        "Validate whether credibility is a recurring emotional need",
        "Compare manual synthesis with current alternatives",
    ],
)


if __name__ == "__main__":
    print(persona_report(signaldesk_persona))

from dataclasses import dataclass
from typing import List


@dataclass
class ResearchQuestion:
    question: str
    decision: str
    hypothesis: str
    evidence_required: List[str]


DECISION = (
    "Prioritize a support-workflow package for growing technology companies "
    "in the next planning cycle."
)

questions = [
    ResearchQuestion(
        question="Is fragmented support tracking a high-priority problem?",
        decision=DECISION,
        hypothesis="Teams with growing support volume will describe fragmented tracking as costly.",
        evidence_required=["customer interviews", "support-request themes"],
    ),
    ResearchQuestion(
        question="Do current alternatives leave a meaningful workflow gap?",
        decision=DECISION,
        hypothesis="Teams will report costly handoffs across support channels that alternatives do not resolve well.",
        evidence_required=["competitor documentation", "customer workaround examples"],
    ),
    ResearchQuestion(
        question="Can SignalDesk reach and serve this opportunity credibly?",
        decision=DECISION,
        hypothesis="The opportunity matches our target buyers and existing product strengths.",
        evidence_required=["buyer interviews", "channel evidence", "product capability review"],
    ),
]


def validate_plan(decision: str, items: List[ResearchQuestion]) -> List[str]:
    errors = []
    if not decision.strip():
        errors.append("decision is required")
    for index, item in enumerate(items, start=1):
        if len(item.question.strip()) < 15:
            errors.append(f"question {index} is too vague")
        if not item.hypothesis.strip():
            errors.append(f"question {index} needs a hypothesis")
        if not item.evidence_required:
            errors.append(f"question {index} needs evidence requirements")
    return errors


if __name__ == "__main__":
    errors = validate_plan(DECISION, questions)
    print("VALID" if not errors else "INVALID")
    for error in errors:
        print(f"- {error}")

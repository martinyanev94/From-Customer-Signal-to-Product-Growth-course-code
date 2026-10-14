from dataclasses import dataclass
from typing import List, Set


@dataclass
class Analyst:
    name: str
    firm: str
    relevance: str
    interaction: str


@dataclass
class Objective:
    objective_id: str
    outcome: str
    evidence_needed: List[str]


@dataclass
class FollowUp:
    action: str
    owner: str
    status: str
    evidence_status: str


def validate_plan(
    objective: Objective,
    analyst: Analyst,
    materials: Set[str],
) -> List[str]:
    errors: List[str] = []
    if not objective.outcome.strip():
        errors.append("objective needs an outcome")
    if not objective.evidence_needed:
        errors.append("objective needs evidence requirements")
    if not analyst.relevance.strip():
        errors.append("analyst relevance is missing")
    if not analyst.interaction.strip():
        errors.append("interaction type is missing")
    for item in objective.evidence_needed:
        if item not in materials:
            errors.append(f"missing briefing material: {item}")
    return errors


def build_sample_plan() -> tuple[Objective, Analyst, Set[str], FollowUp]:
    objective = Objective(
        objective_id="positioning-feedback",
        outcome="Test whether evidence-linked planning is clear to product teams",
        evidence_needed=[
            "core narrative",
            "customer outcome examples",
            "directional roadmap",
        ],
    )
    analyst = Analyst(
        name="Jordan Lee",
        firm="Northstar Research",
        relevance="Covers product planning workflows used by technology teams",
        interaction="briefing",
    )
    materials = {
        "core narrative",
        "customer outcome examples",
        "directional roadmap",
    }
    follow_up = FollowUp(
        action="Send evidence summary and record open product question",
        owner="Product marketing",
        status="pending",
        evidence_status="needs review",
    )
    return objective, analyst, materials, follow_up


if __name__ == "__main__":
    objective, analyst, materials, follow_up = build_sample_plan()
    errors = validate_plan(objective, analyst, materials)
    print("validation:", errors)
    print("follow-up:", follow_up.action)
    print("owner:", follow_up.owner)

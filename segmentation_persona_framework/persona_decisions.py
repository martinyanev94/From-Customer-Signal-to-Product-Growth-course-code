from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Persona:
    name: str
    job_context: str
    functional_progress: str
    emotional_progress: str
    evidence_refs: List[str]


maya = Persona(
    name="Maya",
    job_context="Weekly operations review",
    functional_progress="Reduce repetitive operational work",
    emotional_progress="Stay in control of changes",
    evidence_refs=["interview-07", "usage-pattern-03"],
)


def build_decisions(persona: Persona) -> List[Dict[str, object]]:
    return [
        {
            "lane": "product",
            "action": "Prioritize a guided automation flow",
            "need": persona.functional_progress,
            "evidence_check": "Completion without manual re-entry",
            "evidence_refs": ["interview-07", "usage-pattern-03"],
        },
        {
            "lane": "content",
            "action": "Create a five-minute setup demo",
            "need": persona.functional_progress,
            "evidence_check": "Demo viewers reach first successful setup",
            "evidence_refs": ["interview-07"],
        },
        {
            "lane": "channel",
            "action": "Test workflow-oriented search messaging",
            "need": persona.functional_progress,
            "evidence_check": "Qualified visits from workflow searches",
            "evidence_refs": ["usage-pattern-03"],
        },
        {
            "lane": "enablement",
            "action": "Add a control-and-review objection guide",
            "need": persona.emotional_progress,
            "evidence_check": "Sellers answer control objections consistently",
            "evidence_refs": ["interview-07"],
        },
    ]


REQUIRED_LANES = {"product", "content", "channel", "enablement"}


def validate_decisions(
    persona: Persona, decisions: List[Dict[str, object]]
) -> List[str]:
    errors: List[str] = []
    lanes = {item.get("lane") for item in decisions}
    missing_lanes = REQUIRED_LANES - lanes
    if missing_lanes:
        errors.append(f"missing lanes: {sorted(missing_lanes)}")

    for item in decisions:
        lane = str(item.get("lane", "unknown"))
        if not item.get("action"):
            errors.append(f"{lane} has no action")
        if not item.get("evidence_check"):
            errors.append(f"{lane} has no evidence check")
        if not item.get("evidence_refs"):
            errors.append(f"{lane} has an evidence gap")

    if len(persona.evidence_refs) < 2:
        errors.append("persona needs at least two evidence references")
    return errors


def main() -> None:
    decisions = build_decisions(maya)
    errors = validate_decisions(maya, decisions)
    print(f"persona: {maya.name}")
    print(f"decision rows: {len(decisions)}")
    print(f"validation: {'valid' if not errors else 'invalid'}")
    for error in errors:
        print(f"- {error}")


if __name__ == "__main__":
    main()

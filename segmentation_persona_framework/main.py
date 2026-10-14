from typing import Dict, List

Segment = Dict[str, str]

segments: List[Segment] = [
    {
        "name": "Incident Coordinators",
        "behavior": "assemble evidence during active incidents",
        "need": "fast, auditable handoff",
        "decision": "build incident handoff workflow",
        "evidence_status": "observed behavior; need to validate across accounts",
    },
    {
        "name": "Planning Leads",
        "behavior": "review work in weekly planning cycles",
        "need": "shared prioritization and alignment",
        "decision": "improve roadmap review and approval",
        "evidence_status": "observed behavior; need to validate decision authority",
    },
]


def is_actionably_distinct(left: Segment, right: Segment) -> bool:
    """Return whether the segment boundary could change an operating decision."""
    different_need = left["need"] != right["need"]
    different_decision = left["decision"] != right["decision"]
    return different_need or different_decision


def selection_rationale(items: List[Segment]) -> str:
    if len(items) < 2:
        raise ValueError("At least two candidate segments are required")

    left, right = items[0], items[1]
    distinct = is_actionably_distinct(left, right)
    action = "keep separate" if distinct else "merge"
    return (
        f"{action}: {left['name']} / {right['name']} | "
        f"needs: {left['need']} vs {right['need']} | "
        f"decisions: {left['decision']} vs {right['decision']}"
    )


if __name__ == "__main__":
    print(selection_rationale(segments))

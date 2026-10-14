from dataclasses import asdict, dataclass
import argparse
import json
from pathlib import Path
from typing import Optional

ROUTES = {
    "product": ("product lead", "Evaluate a guided first-import flow."),
    "marketing": ("marketing lead", "Test the onboarding message and proof."),
    "sales": ("sales enablement lead", "Add the objection to discovery guidance."),
    "customer_success": (
        "customer success lead",
        "Add an adoption check to the success playbook.",
    ),
}
VALID_CATEGORIES = set(ROUTES)


@dataclass
class Insight:
    insight_id: str
    evidence_ref: str
    theme: str
    unmet_need: str
    category: str
    owner: Optional[str] = None
    next_action: Optional[str] = None
    status: str = "new"


def load_insights(path: Path) -> list[Insight]:
    records = json.loads(path.read_text(encoding="utf-8"))
    return [Insight(**record) for record in records]


def route_insight(insight: Insight) -> Insight:
    route = ROUTES.get(insight.category)
    if route:
        insight.owner, insight.next_action = route
        insight.status = "routed"
    return insight


def validate_insight(insight: Insight) -> list[str]:
    errors = []
    if not insight.evidence_ref:
        errors.append("missing evidence_ref")
    if insight.category not in VALID_CATEGORIES:
        errors.append("uncategorized insight")
    if not insight.owner:
        errors.append("missing owner")
    if not insight.next_action:
        errors.append("missing next_action")
    return errors


def process(path: Path) -> dict[str, dict]:
    results = {}
    for insight in load_insights(path):
        routed = route_insight(insight)
        results[routed.insight_id] = {
            "record": asdict(routed),
            "errors": validate_insight(routed),
        }
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and route VoC insights")
    parser.add_argument("path", type=Path, help="Path to an insight JSON array")
    args = parser.parse_args()
    print(json.dumps(process(args.path), indent=2))


if __name__ == "__main__":
    main()

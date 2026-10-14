from dataclasses import dataclass
from typing import Literal

Confidence = Literal["high", "medium", "low"]


@dataclass(frozen=True)
class RoadmapItem:
    name: str
    score: float
    rationale: str
    customer_value: str
    confidence: Confidence
    horizon: str


def internal_view(item: RoadmapItem) -> str:
    return (
        f"{item.name}: score={item.score:.2f}; "
        f"confidence={item.confidence}; {item.rationale}"
    )


def external_view(item: RoadmapItem) -> str:
    return (
        f"{item.horizon}: exploring {item.name} — "
        f"{item.customer_value}. Confidence: {item.confidence}. "
        "Plans may change as we learn."
    )


def validate_views(item: RoadmapItem, internal: str, external: str) -> list[str]:
    errors: list[str] = []
    if item.name not in internal or item.name not in external:
        errors.append("initiative missing from a view")
    if item.customer_value not in external:
        errors.append("customer value missing externally")
    if f"{item.score:.2f}" in external:
        errors.append("internal score exposed externally")
    external_lower = external.lower()
    if "will ship" in external_lower or "guaranteed" in external_lower:
        errors.append("external promise detected")
    return errors


if __name__ == "__main__":
    item = RoadmapItem(
        name="self-serve onboarding",
        score=0.82,
        rationale="three interviews and funnel review indicate setup friction",
        customer_value="reduce first-session abandonment",
        confidence="medium",
        horizon="Near term",
    )
    internal = internal_view(item)
    external = external_view(item)
    print(internal)
    print(external)
    print("valid" if not validate_views(item, internal, external) else "invalid")

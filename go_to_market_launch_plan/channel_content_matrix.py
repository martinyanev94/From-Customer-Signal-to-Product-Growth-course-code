from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ChannelContentChoice:
    stage: str
    audience_behavior: str
    channel: str
    asset: str
    message: str
    cost: str
    learning_value: str


choices: List[ChannelContentChoice] = [
    ChannelContentChoice(
        "discover",
        "searches for practical guidance",
        "SEO guide",
        "Evidence-linked roadmap guide",
        "Trace evidence into a roadmap decision",
        "medium",
        "high",
    ),
    ChannelContentChoice(
        "evaluate",
        "needs proof and detailed answers",
        "direct demo",
        "Workflow demonstration",
        "See evidence move into prioritization",
        "high",
        "high",
    ),
    ChannelContentChoice(
        "adopt",
        "needs implementation confidence",
        "customer workshop",
        "First-decision setup workshop",
        "Reach a first roadmap decision with confidence",
        "medium",
        "high",
    ),
]


def validate_choices(items: List[ChannelContentChoice]) -> List[str]:
    errors: List[str] = []
    for index, item in enumerate(items):
        required = (
            item.stage,
            item.audience_behavior,
            item.channel,
            item.asset,
            item.message,
            item.cost,
            item.learning_value,
        )
        if not all(required):
            errors.append(f"choice {index} is incomplete")
    return errors


if __name__ == "__main__":
    errors = validate_choices(choices)
    print("valid" if not errors else errors)

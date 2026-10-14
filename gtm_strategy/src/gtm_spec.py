from dataclasses import dataclass


@dataclass(frozen=True)
class GTMSpec:
    product: str
    target_market: str
    launch_objective: str
    journey: list[dict]
    channels: list[dict]
    content: list[dict]
    measures: list[dict]


signaldesk_spec = GTMSpec(
    product="SignalDesk",
    target_market="Small technology teams with scattered customer evidence",
    launch_objective=(
        "Generate qualified evaluations and first evidence-linked "
        "roadmap decisions"
    ),
    journey=[
        {
            "stage": "discover",
            "job": "recognize the evidence problem",
            "signal": "qualified_visit",
        },
        {
            "stage": "evaluate",
            "job": "judge fit and value",
            "signal": "completed_evaluation",
        },
        {
            "stage": "adopt",
            "job": "reach a first roadmap decision",
            "signal": "first_roadmap_decision",
        },
        {
            "stage": "retain",
            "job": "repeat the evidence loop",
            "signal": "repeat_decision",
        },
    ],
    channels=[
        {
            "name": "expert newsletter",
            "job": "reach problem-aware teams",
            "stage": "discover",
        },
        {
            "name": "product-led evaluation",
            "job": "let teams judge workflow fit",
            "stage": "evaluate",
        },
        {
            "name": "direct onboarding",
            "job": "guide the first roadmap decision",
            "stage": "adopt",
        },
    ],
    content=[
        {
            "asset": "roadmap evidence guide",
            "job": "help teams name the problem",
            "stage": "discover",
        },
        {
            "asset": "worked evidence example",
            "job": "show how evidence becomes a decision",
            "stage": "evaluate",
        },
        {
            "asset": "onboarding checklist",
            "job": "support the first roadmap decision",
            "stage": "adopt",
        },
        {
            "asset": "review template",
            "job": "support repeated evidence-linked decisions",
            "stage": "retain",
        },
    ],
    measures=[
        {
            "name": "qualified_visit_rate",
            "stage": "discover",
            "outcome": "qualified_visit",
        },
        {
            "name": "evaluation_completion_rate",
            "stage": "evaluate",
            "outcome": "completed_evaluation",
        },
        {
            "name": "first_decision_rate",
            "stage": "adopt",
            "outcome": "first_roadmap_decision",
        },
        {
            "name": "repeat_decision_rate",
            "stage": "retain",
            "outcome": "repeat_decision",
        },
    ],
)


def validate_gtm(spec: GTMSpec) -> list[str]:
    """Check structural links in a GTM specification."""
    errors: list[str] = []
    stages = {item["stage"] for item in spec.journey}
    measured_stages = {item["stage"] for item in spec.measures}

    for required in ("discover", "evaluate", "adopt", "retain"):
        if required not in stages:
            errors.append(f"missing journey stage: {required}")

    for item in spec.channels:
        if item["stage"] not in stages:
            errors.append(f"channel has unknown stage: {item['stage']}")

    for item in spec.content:
        if item["stage"] not in stages:
            errors.append(f"content has unknown stage: {item['stage']}")

    if "adopt" not in measured_stages:
        errors.append("launch objective has no adoption measure")

    return errors


if __name__ == "__main__":
    print(validate_gtm(signaldesk_spec))

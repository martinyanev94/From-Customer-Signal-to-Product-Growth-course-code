from dataclasses import dataclass, field
from typing import List


PHASES = ("prepare", "release", "learn")


@dataclass
class LaunchItem:
    phase: str
    name: str
    owner: str
    dependency: str
    readiness_check: str
    risk_response: str
    communication: str


@dataclass
class LaunchPlan:
    objective: str
    items: List[LaunchItem] = field(default_factory=list)


@dataclass
class ReviewAction:
    signal: str
    interpretation: str
    owner: str
    next_action: str


def validate_plan(plan: LaunchPlan) -> List[str]:
    errors = []
    if not plan.objective.strip():
        errors.append("launch objective is required")
    if not plan.items:
        errors.append("at least one launch item is required")
    last_phase = -1
    for item in plan.items:
        if item.phase not in PHASES:
            errors.append(f"{item.name}: phase must be prepare, release, or learn")
        elif PHASES.index(item.phase) < last_phase:
            errors.append(f"{item.name}: phase order is invalid")
        else:
            last_phase = PHASES.index(item.phase)
        for field_name, value in (
            ("owner", item.owner),
            ("dependency", item.dependency),
            ("readiness check", item.readiness_check),
            ("risk response", item.risk_response),
            ("communication", item.communication),
        ):
            if not value.strip():
                errors.append(f"{item.name}: {field_name} is required")
    return errors


def add_review_action(actions: List[ReviewAction], action: ReviewAction) -> None:
    if not all((action.signal, action.interpretation, action.owner, action.next_action)):
        raise ValueError(
            "review actions require signal, interpretation, owner, and next action"
        )
    actions.append(action)


if __name__ == "__main__":
    plan = LaunchPlan(
        objective="Release the SignalDesk feedback workspace to the target beta cohort",
        items=[
            LaunchItem(
                phase="prepare",
                name="Enable support",
                owner="Customer Success",
                dependency="Tested onboarding flow",
                readiness_check="Support guide and escalation path approved",
                risk_response="Hold broad release and support the beta cohort manually",
                communication="Post readiness status in the launch channel",
            ),
            LaunchItem(
                phase="release",
                name="Publish launch message",
                owner="Product Marketing",
                dependency="Approved positioning and release scope",
                readiness_check="Audience, value claim, and availability are confirmed",
                risk_response="Delay announcement and correct the message",
                communication="Send the approved message to the beta cohort",
            ),
            LaunchItem(
                phase="learn",
                name="Review adoption signals",
                owner="Product Manager",
                dependency="Activation and feedback data available",
                readiness_check="Review meeting and metric snapshot are scheduled",
                risk_response="Run targeted customer interviews before changing spend",
                communication="Share findings and next action with all owners",
            ),
        ],
    )
    print(validate_plan(plan))

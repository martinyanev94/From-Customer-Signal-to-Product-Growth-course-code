from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Decision:
    name: str
    accountable: str
    consulted: List[str]
    informed: List[str]


@dataclass
class Commitment:
    owner: str
    output: str
    outcome: str
    status: str


@dataclass
class OperatingPlan:
    shared_outcome: str
    decisions: List[Decision]
    commitments: List[Commitment]


def validate_plan(plan: OperatingPlan) -> List[str]:
    errors: List[str] = []
    for decision in plan.decisions:
        if not decision.accountable:
            errors.append(f"{decision.name}: missing accountable role")
    for commitment_number, commitment in enumerate(plan.commitments, 1):
        for field_name in ("owner", "output", "outcome", "status"):
            if not getattr(commitment, field_name):
                errors.append(
                    f"commitment {commitment_number}: missing {field_name}"
                )
    if not plan.shared_outcome:
        errors.append("plan: missing shared outcome")
    return errors


def build_signaldesk_plan() -> OperatingPlan:
    return OperatingPlan(
        shared_outcome="Qualified teams reach a first roadmap decision quickly and understand SignalDesk's value.",
        decisions=[
            Decision(
                name="positioning",
                accountable="product_marketing",
                consulted=["sales", "customer_success"],
                informed=["product"],
            ),
            Decision(
                name="roadmap_scope",
                accountable="product",
                consulted=["sales", "customer_success"],
                informed=["executive_sponsor"],
            ),
            Decision(
                name="onboarding_response",
                accountable="customer_success",
                consulted=["product_marketing", "product"],
                informed=["sales"],
            ),
        ],
        commitments=[
            Commitment(
                owner="sales",
                output="Three recent evaluation objections",
                outcome="Faster qualified evaluation",
                status="open",
            ),
            Commitment(
                owner="customer_success",
                output="First-decision walkthrough",
                outcome="Faster qualified evaluation",
                status="open",
            ),
            Commitment(
                owner="product",
                output="Review of the two highest workflow frictions",
                outcome="Faster qualified evaluation",
                status="open",
            ),
            Commitment(
                owner="product_marketing",
                output="Evidence-linked executive brief",
                outcome="Faster qualified evaluation",
                status="open",
            ),
        ],
    )


def main() -> None:
    plan = build_signaldesk_plan()
    errors = validate_plan(plan)
    if errors:
        raise SystemExit("Invalid plan:\n- " + "\n- ".join(errors))
    print(f"Shared outcome: {plan.shared_outcome}")
    print(f"Decisions: {len(plan.decisions)}")
    print(f"Commitments: {len(plan.commitments)}")
    print("Validation: valid")


if __name__ == "__main__":
    main()

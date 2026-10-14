from dataclasses import dataclass


@dataclass
class EnablementCharter:
    audience: str
    buyer_stage: str
    seller_behavior: str
    training: list[str]
    resources: list[str]
    owner: str
    adoption_indicator: str
    outcome_indicator: str

    def validate(self) -> list[str]:
        required = {
            "audience": self.audience,
            "buyer_stage": self.buyer_stage,
            "seller_behavior": self.seller_behavior,
            "owner": self.owner,
            "adoption_indicator": self.adoption_indicator,
            "outcome_indicator": self.outcome_indicator,
        }
        errors = [
            f"{name} is required"
            for name, value in required.items()
            if not value.strip()
        ]
        if not self.training:
            errors.append("training must contain at least one item")
        if not self.resources:
            errors.append("resources must contain at least one item")
        return errors


def sample_charter() -> EnablementCharter:
    return EnablementCharter(
        audience="account executives",
        buyer_stage="evaluation",
        seller_behavior=(
            "Use approved proof to answer the value objection "
            "and record a next step."
        ),
        training=["objection-handling workshop", "demo practice"],
        resources=["evaluation proof card", "competitive response guide"],
        owner="product marketing with sales leadership",
        adoption_indicator="proof-card usage in evaluation opportunities",
        outcome_indicator=(
            "evaluation opportunities advancing to a qualified next step"
        ),
    )


def main() -> None:
    charter = sample_charter()
    print("Validation:", charter.validate())
    print("Target behavior:", charter.seller_behavior)
    print("Training:", ", ".join(charter.training))
    print("Resources:", ", ".join(charter.resources))


if __name__ == "__main__":
    main()

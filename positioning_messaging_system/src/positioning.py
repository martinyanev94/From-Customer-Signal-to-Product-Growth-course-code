from dataclasses import dataclass


@dataclass(frozen=True)
class PositioningCore:
    audience: str
    problem: str
    alternative: str
    differentiated_value: str
    proof: str
    category: str


def value_proposition(core: PositioningCore) -> str:
    return (
        f"For {core.audience}, {core.differentiated_value} "
        f"when {core.problem}; support: {core.proof}."
    )


def positioning_statement(core: PositioningCore) -> str:
    return (
        f"For {core.audience}, {core.category} that "
        f"{core.differentiated_value}. Unlike {core.alternative}, "
        f"it addresses {core.problem}."
    )


def validate(core: PositioningCore) -> list[str]:
    fields = {
        "audience": core.audience,
        "problem": core.problem,
        "alternative": core.alternative,
        "differentiated_value": core.differentiated_value,
        "proof": core.proof,
        "category": core.category,
    }
    return [
        f"{name} is required"
        for name, value in fields.items()
        if not value.strip()
    ]


core = PositioningCore(
    audience="product marketing teams coordinating roadmap decisions",
    problem="scattered customer evidence slows prioritization and alignment",
    alternative="spreadsheets, disconnected notes, and opinion-led meetings",
    differentiated_value="evidence-linked planning that turns research into defensible roadmap choices",
    proof="validated research records, a scored roadmap, and an evidence chain",
    category="evidence-linked product marketing workspace",
)


if __name__ == "__main__":
    print(value_proposition(core))
    print(positioning_statement(core))
    print(validate(core))

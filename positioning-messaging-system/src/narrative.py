from dataclasses import dataclass
from typing import Dict, List

REQUIRED_STEPS = ("problem", "change", "solution", "proof", "next_action")


@dataclass
class ProofRecord:
    claim_id: str
    evidence_ref: str
    description: str


@dataclass
class NarrativeStep:
    kind: str
    text: str
    proof_refs: List[str]


@dataclass
class StrategicNarrative:
    audience: str
    steps: List[NarrativeStep]
    proof_registry: Dict[str, ProofRecord]


def validate_narrative(narrative: StrategicNarrative) -> List[str]:
    errors: List[str] = []
    kinds = [step.kind for step in narrative.steps]

    if kinds != list(REQUIRED_STEPS):
        errors.append(
            "steps must follow problem, change, solution, proof, next_action"
        )

    if not narrative.audience.strip():
        errors.append("audience is empty")

    for step in narrative.steps:
        if step.kind not in REQUIRED_STEPS:
            errors.append(f"unknown step kind: {step.kind}")
        if not step.text.strip():
            errors.append(f"{step.kind} is empty")
        for ref in step.proof_refs:
            record = narrative.proof_registry.get(ref)
            if record is None or not record.claim_id or not record.evidence_ref:
                errors.append(f"unlinked proof reference: {ref}")

    proof_steps = [step for step in narrative.steps if step.kind == "proof"]
    if not proof_steps or not proof_steps[0].proof_refs:
        errors.append("proof step needs at least one proof reference")

    return errors


def build_signaldesk_narrative() -> StrategicNarrative:
    return StrategicNarrative(
        audience="product teams turning customer evidence into roadmap decisions",
        steps=[
            NarrativeStep(
                "problem",
                "Customer evidence is scattered, so decisions are hard to trace.",
                [],
            ),
            NarrativeStep(
                "change",
                "Teams can move from scattered feedback to an evidence-linked decision.",
                [],
            ),
            NarrativeStep(
                "solution",
                "SignalDesk records evidence, routes ownership, and preserves decision links.",
                [],
            ),
            NarrativeStep(
                "proof",
                "A validated differentiation record links the claim to customer evidence.",
                ["diff-017"],
            ),
            NarrativeStep(
                "next_action",
                "Review one active roadmap decision in an evidence session.",
                [],
            ),
        ],
        proof_registry={
            "diff-017": ProofRecord(
                "signaldesk-traceability",
                "differentiation-record",
                "Validated differentiation record linked to customer evidence",
            )
        },
    )


if __name__ == "__main__":
    narrative = build_signaldesk_narrative()
    errors = validate_narrative(narrative)
    print("valid" if not errors else "invalid")
    for error in errors:
        print(f"- {error}")

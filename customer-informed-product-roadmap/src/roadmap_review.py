from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class RoadmapCandidate:
    name: str
    segment: str
    persona_job: str
    evidence_refs: Tuple[str, ...]
    recommendation: str


def defend(candidate: RoadmapCandidate) -> str:
    if not candidate.evidence_refs:
        return f"{candidate.name}: insufficient evidence"
    return (
        f"{candidate.name} for {candidate.segment}: "
        f"{candidate.recommendation} "
        f"Evidence links: {len(candidate.evidence_refs)}"
    )


def validate_consistency(
    candidate: RoadmapCandidate,
    expected_segment: str,
    required_refs: Iterable[str],
) -> list[str]:
    errors: list[str] = []
    if candidate.segment != expected_segment:
        errors.append("candidate segment does not match the selected segment")
    missing = [ref for ref in required_refs if ref not in candidate.evidence_refs]
    if missing:
        errors.append(f"missing evidence links: {', '.join(missing)}")
    if not candidate.persona_job.strip():
        errors.append("persona job is empty")
    return errors


def main() -> None:
    candidate = RoadmapCandidate(
        name="Workflow evidence panel",
        segment="operations-led teams",
        persona_job="defend decisions during handoffs",
        evidence_refs=(
            "market:workflow",
            "voc:handoff-confidence",
            "persona:operations-lead",
        ),
        recommendation="Prioritize for the next planning horizon.",
    )
    print(defend(candidate))
    errors = validate_consistency(
        candidate,
        expected_segment="operations-led teams",
        required_refs=("market:workflow", "voc:handoff-confidence"),
    )
    print("Consistency check: PASS" if not errors else "Consistency check: FAIL")
    for error in errors:
        print(f"- {error}")


if __name__ == "__main__":
    main()

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Candidate:
    name: str
    customer_evidence: int
    market_opportunity: int
    strategic_fit: int
    adoption_risk: int


@dataclass(frozen=True)
class ScoredCandidate:
    name: str
    score: float
    customer_evidence: int
    market_opportunity: int
    strategic_fit: int
    adoption_risk: int


def _validate_rating(name: str, value: int) -> None:
    if not isinstance(value, int) or not 1 <= value <= 5:
        raise ValueError(f"{name} must be an integer from 1 through 5")


def score_candidate(candidate: Candidate) -> ScoredCandidate:
    ratings = {
        "customer_evidence": candidate.customer_evidence,
        "market_opportunity": candidate.market_opportunity,
        "strategic_fit": candidate.strategic_fit,
        "adoption_risk": candidate.adoption_risk,
    }
    for name, value in ratings.items():
        _validate_rating(name, value)

    adoption_readiness = 6 - candidate.adoption_risk
    score = (
        candidate.customer_evidence * 0.35
        + candidate.market_opportunity * 0.25
        + candidate.strategic_fit * 0.25
        + adoption_readiness * 0.15
    )
    return ScoredCandidate(
        name=candidate.name,
        score=round(score, 2),
        customer_evidence=candidate.customer_evidence,
        market_opportunity=candidate.market_opportunity,
        strategic_fit=candidate.strategic_fit,
        adoption_risk=candidate.adoption_risk,
    )


def rank_candidates(candidates: Iterable[Candidate]) -> List[ScoredCandidate]:
    return sorted(
        (score_candidate(candidate) for candidate in candidates),
        key=lambda candidate: candidate.score,
        reverse=True,
    )


if __name__ == "__main__":
    candidates = [
        Candidate("Guided onboarding", 5, 4, 5, 2),
        Candidate("Export audit trail", 4, 3, 4, 1),
        Candidate("Social sharing", 2, 5, 2, 4),
    ]
    for candidate in rank_candidates(candidates):
        print(f"{candidate.name}: {candidate.score}")

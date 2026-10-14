from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def synthesize_insights(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for observation in observations:
        code = observation["code"]
        grouped.setdefault(code, []).append(observation)

    insights = []
    for code, records in sorted(grouped.items()):
        insights.append(
            {
                "theme": code,
                "evidence_refs": [record["evidence_ref"] for record in records],
                "observation_count": len(records),
                "impacts": sorted({record["impact"] for record in records}),
            }
        )
    return insights


def build_differentiation(
    insight: dict[str, Any],
    unmet_need: str,
    differentiator: str,
    implications: list[str],
) -> dict[str, Any]:
    if not insight["evidence_refs"]:
        raise ValueError("differentiation needs evidence_refs")
    return {
        **insight,
        "unmet_need": unmet_need,
        "differentiator": differentiator,
        "business_implications": implications,
        "confidence": "hypothesis",
    }


def load_observations(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text())


def main() -> None:
    observations = load_observations(Path(__file__).with_name("sample_observations.json"))
    raw_insights = synthesize_insights(observations)
    decision_insight = {
        "theme": "decision_friction",
        "evidence_refs": [record["evidence_ref"] for record in observations],
        "observation_count": len(observations),
        "impacts": sorted({record["impact"] for record in observations}),
    }
    result = build_differentiation(
        decision_insight,
        "Teams need to identify and justify the next customer action without manually reconciling scattered signals.",
        "SignalDesk helps product teams move from scattered customer evidence to a prioritized, evidence-linked action.",
        ["time to agreed action", "evidence-linked action rate"],
    )
    print(json.dumps({"coded_insights": raw_insights, "differentiation": result}, indent=2))


if __name__ == "__main__":
    main()

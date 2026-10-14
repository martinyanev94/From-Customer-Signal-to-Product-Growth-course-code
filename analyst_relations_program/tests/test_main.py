from src.main import Analyst, Objective, validate_plan


def test_complete_plan_has_no_structural_errors():
    objective = Objective(
        objective_id="positioning-feedback",
        outcome="Test positioning clarity",
        evidence_needed=["core narrative", "customer outcome examples"],
    )
    analyst = Analyst(
        name="Jordan Lee",
        firm="Northstar Research",
        relevance="Covers product planning workflows",
        interaction="briefing",
    )

    assert validate_plan(
        objective,
        analyst,
        {"core narrative", "customer outcome examples"},
    ) == []


def test_missing_material_is_reported():
    objective = Objective(
        objective_id="roadmap-feedback",
        outcome="Test roadmap clarity",
        evidence_needed=["directional roadmap"],
    )
    analyst = Analyst(
        name="Jordan Lee",
        firm="Northstar Research",
        relevance="Covers product planning workflows",
        interaction="briefing",
    )

    assert validate_plan(objective, analyst, set()) == [
        "missing briefing material: directional roadmap"
    ]

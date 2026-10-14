import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from launch_plan import LaunchItem, LaunchPlan, ReviewAction, add_review_action, validate_plan


def valid_item():
    return LaunchItem(
        phase="prepare",
        name="Enable support",
        owner="Customer Success",
        dependency="Tested onboarding flow",
        readiness_check="Guide approved",
        risk_response="Hold broad release",
        communication="Post status",
    )


def test_valid_plan_has_no_structural_errors():
    plan = LaunchPlan("Release to the beta cohort", [valid_item()])
    assert validate_plan(plan) == []


def test_missing_owner_is_reported():
    item = valid_item()
    item.owner = ""
    errors = validate_plan(LaunchPlan("Release to beta", [item]))
    assert errors == ["Enable support: owner is required"]


def test_review_action_requires_next_action():
    actions = []
    try:
        add_review_action(actions, ReviewAction("low adoption", "unclear onboarding", "PM", ""))
    except ValueError as error:
        assert str(error) == "review actions require signal, interpretation, owner, and next action"
    else:
        raise AssertionError("expected ValueError")
    assert actions == []


def test_review_action_is_stored_when_complete():
    actions = []
    action = ReviewAction("low adoption", "unclear onboarding", "PM", "Test revised onboarding")
    add_review_action(actions, action)
    assert actions == [action]

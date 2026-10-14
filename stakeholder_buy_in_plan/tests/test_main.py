import unittest

from src.main import (
    Commitment,
    Decision,
    OperatingPlan,
    build_signaldesk_plan,
    validate_plan,
)


class OperatingPlanTests(unittest.TestCase):
    def test_example_plan_is_valid(self):
        self.assertEqual(validate_plan(build_signaldesk_plan()), [])

    def test_missing_accountable_role_is_reported(self):
        plan = OperatingPlan(
            shared_outcome="Reach a first roadmap decision",
            decisions=[Decision("roadmap_scope", "", [], [])],
            commitments=[],
        )
        self.assertIn(
            "roadmap_scope: missing accountable role",
            validate_plan(plan),
        )

    def test_missing_commitment_field_is_reported(self):
        plan = build_signaldesk_plan()
        plan.commitments.append(
            Commitment(
                owner="sales",
                output="",
                outcome="Faster evaluation",
                status="open",
            )
        )
        self.assertIn(
            "commitment 5: missing output",
            validate_plan(plan),
        )


if __name__ == "__main__":
    unittest.main()

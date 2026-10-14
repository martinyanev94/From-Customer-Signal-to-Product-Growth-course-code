import unittest

from src.research_plan import DECISION, ResearchQuestion, questions, validate_plan


class ResearchPlanTests(unittest.TestCase):
    def test_example_plan_is_valid(self):
        self.assertEqual(validate_plan(DECISION, questions), [])

    def test_missing_evidence_is_reported(self):
        incomplete = [
            ResearchQuestion(
                question="Is the problem important to buyers?",
                decision=DECISION,
                hypothesis="Buyers will describe the problem as costly.",
                evidence_required=[],
            )
        ]
        self.assertEqual(
            validate_plan(DECISION, incomplete),
            ["question 1 needs evidence requirements"],
        )

    def test_vague_question_is_reported(self):
        vague = [
            ResearchQuestion(
                question="What?",
                decision=DECISION,
                hypothesis="The answer will affect the decision.",
                evidence_required=["interviews"],
            )
        ]
        self.assertEqual(
            validate_plan(DECISION, vague),
            ["question 1 is too vague"],
        )


if __name__ == "__main__":
    unittest.main()

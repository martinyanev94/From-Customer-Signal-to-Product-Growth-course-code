import unittest

from src.narrative import (
    REQUIRED_STEPS,
    build_signaldesk_narrative,
    validate_narrative,
)


class NarrativeTests(unittest.TestCase):
    def test_example_has_required_sequence_and_valid_proof(self):
        narrative = build_signaldesk_narrative()

        self.assertEqual(
            [step.kind for step in narrative.steps], list(REQUIRED_STEPS)
        )
        self.assertEqual(validate_narrative(narrative), [])

    def test_missing_proof_reference_is_reported(self):
        narrative = build_signaldesk_narrative()
        narrative.steps[3].proof_refs = ["diff-999"]

        errors = validate_narrative(narrative)

        self.assertIn("unlinked proof reference: diff-999", errors)

    def test_missing_proof_step_does_not_crash(self):
        narrative = build_signaldesk_narrative()
        narrative.steps = narrative.steps[:3]

        errors = validate_narrative(narrative)

        self.assertIn("proof step needs at least one proof reference", errors)

    def test_wrong_order_is_reported(self):
        narrative = build_signaldesk_narrative()
        narrative.steps[0], narrative.steps[1] = (
            narrative.steps[1],
            narrative.steps[0],
        )

        errors = validate_narrative(narrative)

        self.assertIn(
            "steps must follow problem, change, solution, proof, next_action",
            errors,
        )


if __name__ == "__main__":
    unittest.main()

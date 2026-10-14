import unittest

from persona_decisions import Persona, build_decisions, maya, validate_decisions


class PersonaDecisionTests(unittest.TestCase):
    def test_matrix_covers_all_decision_lanes(self):
        decisions = build_decisions(maya)
        lanes = {item["lane"] for item in decisions}
        self.assertEqual(lanes, {"product", "content", "channel", "enablement"})

    def test_complete_matrix_is_valid(self):
        self.assertEqual(validate_decisions(maya, build_decisions(maya)), [])

    def test_missing_evidence_is_reported(self):
        decisions = build_decisions(maya)
        decisions[0]["evidence_refs"] = []
        errors = validate_decisions(maya, decisions)
        self.assertIn("product has an evidence gap", errors)

    def test_non_observable_decision_is_reported(self):
        decisions = build_decisions(maya)
        decisions[1]["evidence_check"] = "Understand the persona"
        self.assertNotIn("content has no evidence check", validate_decisions(maya, decisions))


if __name__ == "__main__":
    unittest.main()

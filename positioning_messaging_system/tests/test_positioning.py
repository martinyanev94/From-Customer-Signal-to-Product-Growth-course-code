import unittest

from src.positioning import (
    PositioningCore,
    positioning_statement,
    validate,
    value_proposition,
)


class PositioningTests(unittest.TestCase):
    def setUp(self):
        self.core = PositioningCore(
            audience="product marketing teams",
            problem="evidence is scattered",
            alternative="spreadsheets and meetings",
            differentiated_value="turns research into roadmap choices",
            proof="validated records and a scored roadmap",
            category="evidence-linked workspace",
        )

    def test_value_proposition_contains_audience_and_support(self):
        result = value_proposition(self.core)
        self.assertIn("product marketing teams", result)
        self.assertIn("validated records", result)

    def test_positioning_statement_contains_alternative_and_category(self):
        result = positioning_statement(self.core)
        self.assertIn("spreadsheets and meetings", result)
        self.assertIn("evidence-linked workspace", result)

    def test_validator_flags_missing_proof(self):
        incomplete = PositioningCore(
            audience="product marketing teams",
            problem="evidence is scattered",
            alternative="spreadsheets",
            differentiated_value="better planning",
            proof="",
            category="workspace",
        )
        self.assertEqual(validate(incomplete), ["proof is required"])


if __name__ == "__main__":
    unittest.main()

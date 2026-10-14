import unittest

from main import build_differentiation, synthesize_insights


class InsightSynthesisTests(unittest.TestCase):
    def setUp(self):
        self.observations = [
            {"evidence_ref": "A", "code": "effort", "impact": "slow"},
            {"evidence_ref": "B", "code": "effort", "impact": "rework"},
            {"evidence_ref": "C", "code": "visibility", "impact": "unclear"},
        ]

    def test_groups_codes_and_preserves_evidence(self):
        insights = synthesize_insights(self.observations)
        effort = next(item for item in insights if item["theme"] == "effort")
        self.assertEqual(effort["observation_count"], 2)
        self.assertEqual(effort["evidence_refs"], ["A", "B"])

    def test_differentiation_is_marked_as_hypothesis(self):
        insight = synthesize_insights(self.observations)[0]
        result = build_differentiation(insight, "need", "promise", ["metric"])
        self.assertEqual(result["confidence"], "hypothesis")

    def test_missing_evidence_is_rejected(self):
        with self.assertRaises(ValueError):
            build_differentiation({"evidence_refs": []}, "need", "promise", ["metric"])


if __name__ == "__main__":
    unittest.main()

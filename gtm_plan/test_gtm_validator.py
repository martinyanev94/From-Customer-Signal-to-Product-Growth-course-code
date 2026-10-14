import json
import unittest
from pathlib import Path

from gtm_validator import validate_plan


class GtmValidatorTests(unittest.TestCase):
    def test_sample_plan_prioritizes_readiness_then_coverage(self):
        plan = json.loads(Path("sample_plan.json").read_text())
        findings = validate_plan(plan)
        self.assertEqual(findings[0]["severity"], "critical")
        self.assertIn("Sales training", findings[0]["message"])
        self.assertTrue(any("retain" in item["message"] for item in findings))

    def test_complete_plan_has_no_findings(self):
        plan = {
            "target_market": "Product teams",
            "journey_stages": ["discover", "adopt"],
            "channels": [{"stages": ["discover", "adopt"]}],
            "content": [{"stage": "discover"}, {"stage": "adopt"}],
            "metrics": [{"stage": "adopt", "kind": "adoption"}],
            "launch_items": [{"name": "Release", "owner": "Product", "readiness_check": "QA approved"}]
        }
        self.assertEqual(validate_plan(plan), [])


if __name__ == "__main__":
    unittest.main()

import unittest

from main import audit_asset, average_sales_cycle, conversion_rate


class EnablementAuditTests(unittest.TestCase):
    def test_usage_without_behavior_requires_practice(self):
        result = audit_asset({"asset_key": "guide", "owner": "Product Marketing", "uses": 42, "behavior_events": 0, "stage_coverage": 1})
        self.assertEqual(result.status, "adoption_without_behavior")

    def test_missing_owner_blocks_action(self):
        result = audit_asset({"asset_key": "guide", "owner": "", "uses": 42, "behavior_events": 2, "stage_coverage": 1})
        self.assertEqual(result.status, "blocked")

    def test_metrics_use_explicit_formulas(self):
        self.assertEqual(conversion_rate(20, 50), 40.0)
        self.assertEqual(average_sales_cycle([30, 45, 60, 50, 35]), 44.0)

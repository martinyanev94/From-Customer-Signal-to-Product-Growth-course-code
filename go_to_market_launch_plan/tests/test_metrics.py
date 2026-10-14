import unittest

from src.metrics import METRICS, SNAPSHOT, build_report, optimization_triggers


class MetricModelTests(unittest.TestCase):
    def test_report_marks_values_below_increase_targets_for_review(self):
        report = build_report(METRICS, SNAPSHOT)
        statuses = {row["metric_id"]: row["status"] for row in report}
        self.assertEqual(statuses["qualified_evaluations"], "on_track")
        self.assertEqual(statuses["activated_accounts"], "review")
        self.assertEqual(statuses["retained_accounts"], "review")
        self.assertEqual(statuses["segment_arr"], "review")

    def test_adoption_trigger_is_stage_specific(self):
        report = build_report(METRICS, SNAPSHOT)
        triggers = dict(optimization_triggers(report))
        self.assertEqual(triggers["activated_accounts"], "inspect evaluation-to-setup handoff")

    def test_improving_adoption_removes_its_trigger(self):
        snapshot = dict(SNAPSHOT)
        snapshot["activated_accounts"] = 21
        report = build_report(METRICS, snapshot)
        trigger_ids = {metric_id for metric_id, _ in optimization_triggers(report)}
        self.assertNotIn("activated_accounts", trigger_ids)


if __name__ == "__main__":
    unittest.main()

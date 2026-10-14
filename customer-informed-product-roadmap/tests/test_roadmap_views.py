import unittest

from src.roadmap_views import (
    RoadmapItem,
    external_view,
    internal_view,
    validate_views,
)


class RoadmapViewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.item = RoadmapItem(
            name="self-serve onboarding",
            score=0.82,
            rationale="setup evidence supports the priority",
            customer_value="reduce first-session abandonment",
            confidence="medium",
            horizon="Near term",
        )

    def test_internal_view_keeps_decision_detail(self) -> None:
        result = internal_view(self.item)
        self.assertIn("0.82", result)
        self.assertIn(self.item.rationale, result)

    def test_external_view_keeps_value_without_score(self) -> None:
        result = external_view(self.item)
        self.assertIn(self.item.customer_value, result)
        self.assertIn("medium", result)
        self.assertNotIn("0.82", result)
        self.assertNotIn("will ship", result.lower())

    def test_consistent_views_are_valid(self) -> None:
        errors = validate_views(
            self.item,
            internal_view(self.item),
            external_view(self.item),
        )
        self.assertEqual(errors, [])

    def test_external_promise_is_rejected(self) -> None:
        errors = validate_views(
            self.item,
            internal_view(self.item),
            "Q3 will ship self-serve onboarding; guaranteed.",
        )
        self.assertIn("external promise detected", errors)


if __name__ == "__main__":
    unittest.main()

import unittest

from src.roadmap_review import RoadmapCandidate, defend, validate_consistency


class RoadmapReviewTests(unittest.TestCase):
    def test_defense_includes_traceability_count(self):
        candidate = RoadmapCandidate(
            "Workflow evidence panel",
            "operations-led teams",
            "defend decisions during handoffs",
            ("market:workflow", "voc:handoff-confidence"),
            "Prioritize for the next planning horizon.",
        )
        result = defend(candidate)
        self.assertIn("Evidence links: 2", result)

    def test_missing_required_reference_is_reported(self):
        candidate = RoadmapCandidate(
            "Advanced export",
            "operations-led teams",
            "prepare reusable reports",
            ("market:workflow",),
            "Keep in discovery.",
        )
        errors = validate_consistency(
            candidate,
            "operations-led teams",
            ("market:workflow", "voc:handoff-confidence"),
        )
        self.assertIn("missing evidence links: voc:handoff-confidence", errors)


if __name__ == "__main__":
    unittest.main()

import unittest

from src.roadmap_scoring import Candidate, rank_candidates, score_candidate


class RoadmapScoringTests(unittest.TestCase):
    def test_guided_onboarding_score(self):
        candidate = Candidate("Guided onboarding", 5, 4, 5, 2)
        self.assertEqual(score_candidate(candidate).score, 4.6)

    def test_rank_orders_candidates_by_score(self):
        candidates = [
            Candidate("Social sharing", 2, 5, 2, 4),
            Candidate("Guided onboarding", 5, 4, 5, 2),
            Candidate("Export audit trail", 4, 3, 4, 1),
        ]
        self.assertEqual(
            [item.name for item in rank_candidates(candidates)],
            ["Guided onboarding", "Export audit trail", "Social sharing"],
        )

    def test_invalid_rating_is_rejected(self):
        with self.assertRaises(ValueError):
            score_candidate(Candidate("Bad input", 6, 3, 3, 2))


if __name__ == "__main__":
    unittest.main()

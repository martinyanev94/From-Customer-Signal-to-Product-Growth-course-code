import unittest

from main import is_actionably_distinct, selection_rationale, segments


class SegmentTest(unittest.TestCase):
    def test_different_need_is_actionably_distinct(self):
        self.assertTrue(is_actionably_distinct(segments[0], segments[1]))

    def test_same_need_and_decision_can_merge(self):
        first = dict(segments[0])
        second = dict(segments[0], name="Another Incident Team")
        self.assertFalse(is_actionably_distinct(first, second))

    def test_rationale_names_the_action(self):
        rationale = selection_rationale(segments)
        self.assertTrue(rationale.startswith("keep separate:"))


if __name__ == "__main__":
    unittest.main()

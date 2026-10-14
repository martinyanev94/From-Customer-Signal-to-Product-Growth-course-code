import unittest

from channel_content_matrix import choices, validate_choices


class ChannelContentMatrixTests(unittest.TestCase):
    def test_running_example_is_complete(self):
        self.assertEqual(validate_choices(choices), [])

    def test_missing_message_is_rejected(self):
        incomplete = [choices[0].__class__(
            choices[0].stage,
            choices[0].audience_behavior,
            choices[0].channel,
            choices[0].asset,
            "",
            choices[0].cost,
            choices[0].learning_value,
        )]
        self.assertEqual(validate_choices(incomplete), ["choice 0 is incomplete"])


if __name__ == "__main__":
    unittest.main()

import unittest

from messaging import Message, PositioningCore, render_message, validate_message

class MessagingTests(unittest.TestCase):
    def setUp(self):
        self.core = PositioningCore(
            audience="product marketing leaders",
            problem="scattered customer feedback",
            claim="turn scattered customer signals into evidence-linked decisions",
            alternative="scattered notes and manually routed feedback",
            proof=["Each insight keeps its evidence reference, owner, and next action"],
            next_action="Map an active insight to an owner",
        )

    def test_all_channels_preserve_core(self):
        for channel in ("website", "sales", "launch_email", "success_handoff"):
            message = render_message(self.core, channel)
            self.assertEqual(validate_message(self.core, message), [])

    def test_missing_proof_is_detected(self):
        message = Message("website", self.core.audience, f"{self.core.claim}. Each insight keeps an owner. Map an active insight to an owner.")
        self.assertIn("missing proof", validate_message(self.core, message))

    def test_action_must_be_last(self):
        message = Message("sales", self.core.audience, f"{self.core.claim}. {self.core.proof[0]}. Which active insight still has no owner? Extra claim.")
        self.assertIn("action must end message", validate_message(self.core, message))

if __name__ == "__main__":
    unittest.main()

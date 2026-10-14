from dataclasses import dataclass
from typing import Sequence

CHANNELS = {"website", "sales", "launch_email", "success_handoff"}
CHANNEL_ACTIONS = {
    "website": "Map an active insight to an owner.",
    "sales": "Which active insight still has no owner?",
    "launch_email": "Map your first active insight to an owner.",
    "success_handoff": "Map the first active insight to an owner during onboarding.",
}

@dataclass(frozen=True)
class PositioningCore:
    audience: str
    problem: str
    claim: str
    alternative: str
    proof: Sequence[str]
    next_action: str

@dataclass(frozen=True)
class Message:
    channel: str
    audience: str
    text: str

def render_message(core: PositioningCore, channel: str) -> Message:
    if channel not in CHANNELS:
        raise ValueError(f"Unsupported channel: {channel}")
    proof = core.proof[0]
    action = CHANNEL_ACTIONS[channel]
    text = f"{core.claim}. {proof}. {action}"
    return Message(channel, core.audience, text)

def validate_message(core: PositioningCore, message: Message) -> list[str]:
    errors: list[str] = []
    if message.channel not in CHANNELS:
        errors.append("unsupported channel")
    if not message.audience.strip():
        errors.append("missing audience field")
    text = message.text.casefold()
    if core.claim.casefold() not in text:
        errors.append("core claim drifted")
    proof = core.proof[0].casefold()
    if proof not in text:
        errors.append("missing proof")
    action = CHANNEL_ACTIONS[message.channel].casefold()
    if not text.rstrip().endswith(action):
        errors.append("action must end message")
    return errors

if __name__ == "__main__":
    core = PositioningCore(
        audience="product marketing leaders",
        problem="scattered customer feedback",
        claim="turn scattered customer signals into evidence-linked decisions",
        alternative="scattered notes and manually routed feedback",
        proof=["Each insight keeps its evidence reference, owner, and next action"],
        next_action="Map an active insight to an owner",
    )
    for channel in ("website", "sales", "launch_email", "success_handoff"):
        message = render_message(core, channel)
        print(f"[{message.channel}] {message.text}")
        print("valid:", validate_message(core, message) == [])

import json
from pathlib import Path

VALID_LANES = {"inbound", "outbound"}


def validate_brief(path):
    brief = json.loads(Path(path).read_text())
    for lane in VALID_LANES:
        if lane not in brief:
            raise ValueError(f"Missing lane: {lane}")

    stakeholders = brief.get("stakeholders", [])
    invalid = [
        stakeholder["name"]
        for stakeholder in stakeholders
        if stakeholder.get("lane") not in VALID_LANES
    ]
    if invalid:
        raise ValueError(f"Invalid stakeholder lanes: {invalid}")

    return f"Valid brief: {len(stakeholders)} stakeholders across {len(VALID_LANES)} lanes"


if __name__ == "__main__":
    print(validate_brief("brief.json"))

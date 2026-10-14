import json
from pathlib import Path

from catalog import search, validate


ROOT = Path(__file__).parent.parent
records = json.loads((ROOT / "data" / "collateral.json").read_text())

errors = validate(records)
if errors:
    raise SystemExit("Validation errors:\n" + "\n".join(errors))

matches = search(
    records,
    stage="consideration",
    use_case="answer_manual_reporting_objection",
)

for record in matches:
    print(f"{record['title']} | v{record['version']} | owner: {record['owner']}")
    print(f"Next action: {record['next_action']}")

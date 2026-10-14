from __future__ import annotations

REQUIRED_FIELDS = (
    "stage",
    "audience",
    "use_case",
    "owner",
    "version",
    "next_action",
)


def search(records, *, stage=None, audience=None, use_case=None):
    matches = records
    for field, value in (
        ("stage", stage),
        ("audience", audience),
        ("use_case", use_case),
    ):
        if value:
            matches = [record for record in matches if record[field] == value]
    return [record for record in matches if record.get("status") == "current"]


def validate(records):
    errors = []
    for record in records:
        missing = [field for field in REQUIRED_FIELDS if not record.get(field)]
        if missing:
            errors.append(f"{record['id']}: missing {', '.join(missing)}")

    current_keys = [record["asset_key"] for record in records if record.get("status") == "current"]
    duplicates = sorted({key for key in current_keys if current_keys.count(key) > 1})
    errors.extend(f"{key}: duplicate current versions" for key in duplicates)
    return errors

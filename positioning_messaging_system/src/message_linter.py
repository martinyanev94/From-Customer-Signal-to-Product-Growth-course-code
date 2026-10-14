from __future__ import annotations

from typing import Any

REQUIRED_FIELDS = (
    "audience",
    "alternative",
    "outcome",
    "differentiator",
    "proof",
    "objection",
    "objection_response",
    "next_step",
    "text",
    "action",
)


def lint_message(message: dict[str, Any]) -> dict[str, Any]:
    """Return structural quality checks for one messaging record.

    This validates planning completeness. It does not verify whether claims or
    proof are factually true.
    """
    issues: list[str] = []
    for field in REQUIRED_FIELDS:
        value = message.get(field, "")
        if not isinstance(value, str) or not value.strip():
            issues.append(f"missing:{field}")

    text = message.get("text", "")
    if isinstance(text, str) and text and len(text.split()) > 30:
        issues.append("clarity:too-long")

    alternative = message.get("alternative", "")
    differentiator = message.get("differentiator", "")
    if (
        isinstance(alternative, str)
        and isinstance(differentiator, str)
        and alternative.strip().lower() == differentiator.strip().lower()
    ):
        issues.append("differentiation:restates-alternative")

    checks = {
        "relevance": bool(message.get("audience") and message.get("outcome")),
        "differentiation": bool(
            message.get("alternative") and message.get("differentiator")
        ) and "differentiation:restates-alternative" not in issues,
        "credibility": bool(message.get("proof")),
        "clarity": bool(message.get("text")) and "clarity:too-long" not in issues,
        "objection_handling": bool(
            message.get("objection")
            and message.get("objection_response")
            and message.get("next_step")
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "checks": checks,
        "issues": issues,
        "weakest": failed[0] if failed else None,
    }

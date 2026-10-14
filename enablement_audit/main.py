from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class AssetAudit:
    asset_key: str
    status: str
    next_action: str


def audit_asset(asset: dict[str, Any]) -> AssetAudit:
    if not asset.get("owner"):
        return AssetAudit(asset["asset_key"], "blocked", "Assign an owner")
    if asset.get("uses", 0) > 0 and asset.get("behavior_events", 0) == 0:
        return AssetAudit(asset["asset_key"], "adoption_without_behavior", "Add guided practice and capture seller behavior")
    if asset.get("stage_coverage", 0) == 0:
        return AssetAudit(asset["asset_key"], "coverage_gap", "Map the asset to a buyer stage")
    return AssetAudit(asset["asset_key"], "ready_for_review", "Compare outcome indicators")


def conversion_rate(won: int, pursued: int) -> float:
    if pursued <= 0:
        raise ValueError("pursued opportunities must be positive")
    return won / pursued * 100


def average_sales_cycle(days_to_close: list[int]) -> float:
    if not days_to_close:
        raise ValueError("at least one closed deal is required")
    return sum(days_to_close) / len(days_to_close)

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class MetricDefinition:
    metric_id: str
    stage: str
    kind: str
    definition: str
    target: float
    direction: str
    source: str


METRICS = [
    MetricDefinition("qualified_evaluations", "evaluate", "leading", "target accounts that request a workspace demo", 40, "increase", "campaign_crm"),
    MetricDefinition("activated_accounts", "adopt", "adoption", "target accounts that complete workspace setup", 20, "increase", "product_events"),
    MetricDefinition("retained_accounts", "retain", "retention", "activated accounts active after 30 days", 16, "increase", "product_events"),
    MetricDefinition("segment_arr", "revenue", "outcome", "recurring revenue from the target segment", 12000, "increase", "billing"),
]

SNAPSHOT = {
    "qualified_evaluations": 52,
    "activated_accounts": 18,
    "retained_accounts": 13,
    "segment_arr": 9600,
}


def build_report(definitions: List[MetricDefinition], snapshot: Dict[str, float]) -> List[Dict[str, object]]:
    rows = []
    for metric in definitions:
        if metric.metric_id not in snapshot:
            raise KeyError(f"Missing snapshot value: {metric.metric_id}")
        actual = snapshot[metric.metric_id]
        if metric.direction == "increase":
            passed = actual >= metric.target
        elif metric.direction == "decrease":
            passed = actual <= metric.target
        else:
            raise ValueError(f"Unsupported direction: {metric.direction}")
        rows.append({"metric_id": metric.metric_id, "stage": metric.stage, "kind": metric.kind, "actual": actual, "target": metric.target, "status": "on_track" if passed else "review"})
    return rows


def optimization_triggers(report: List[Dict[str, object]]) -> List[Tuple[str, str]]:
    triggers = []
    for row in report:
        if row["status"] != "review":
            continue
        stage = row["stage"]
        if stage == "adopt":
            action = "inspect evaluation-to-setup handoff"
        elif stage == "retain":
            action = "inspect product friction and support"
        elif stage == "revenue":
            action = "inspect pricing, expansion, and segment volume"
        else:
            action = "inspect the stage-specific tactic"
        triggers.append((str(row["metric_id"]), action))
    return triggers


def format_report(report: List[Dict[str, object]]) -> str:
    lines = ["metric\tstage\tactual\ttarget\tstatus"]
    for row in report:
        lines.append(f"{row['metric_id']}\t{row['stage']}\t{row['actual']}\t{row['target']}\t{row['status']}")
    return "\n".join(lines)


if __name__ == "__main__":
    report = build_report(METRICS, SNAPSHOT)
    print(format_report(report))
    print("\noptimization triggers")
    for metric_id, action in optimization_triggers(report):
        print(f"- {metric_id}: {action}")

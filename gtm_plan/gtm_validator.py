import json
import sys
from pathlib import Path

SEVERITY = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def issue(severity, message, action):
    return {"severity": severity, "message": message, "action": action}


def validate_plan(plan):
    findings = []
    stages = set(plan.get("journey_stages", []))
    channels = plan.get("channels", [])
    content = plan.get("content", [])
    metrics = plan.get("metrics", [])
    launch_items = plan.get("launch_items", [])

    if not plan.get("target_market"):
        findings.append(issue("critical", "Target market is missing", "Define the priority market before launch."))

    for stage in sorted(stages):
        if not any(stage in channel.get("stages", []) for channel in channels):
            findings.append(issue("high", f"No channel serves {stage}", f"Assign a channel to the {stage} stage."))
        if not any(item.get("stage") == stage for item in content):
            findings.append(issue("high", f"No content serves {stage}", f"Create a content item with a job for {stage}."))

    for metric in metrics:
        if not metric.get("stage") or not metric.get("kind"):
            findings.append(issue("high", "Metric is missing stage or kind", "Complete the metric dictionary entry."))
        if metric.get("kind") == "revenue" and not metric.get("outcome"):
            findings.append(issue("high", "Revenue metric has no outcome", "Connect revenue to an explicit business outcome."))

    for item in launch_items:
        if not item.get("owner") or not item.get("readiness_check"):
            findings.append(issue("critical", f"Launch item is not ready: {item.get('name', 'unnamed')}", "Assign an owner and define a verifiable readiness check."))

    return sorted(findings, key=lambda finding: (SEVERITY[finding["severity"]], finding["message"]))


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python gtm_validator.py plan.json")
    plan = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(validate_plan(plan), indent=2))


if __name__ == "__main__":
    main()

# Launch plan project

This small Python project models a phased launch plan and its post-launch review loop.

Run the example:

```bash
python src/launch_plan.py
```

Run the tests with pytest installed:

```bash
python -m pytest
```

The validator checks the objective, phase order, and required coordination fields. It does not prove that a readiness claim, metric interpretation, or customer conclusion is true.

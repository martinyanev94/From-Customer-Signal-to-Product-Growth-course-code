# Analyst Relations Program

This small Python project models an analyst relations plan for a product marketing team.
It validates planning structure: objectives need outcomes and evidence requirements,
analysts need relevance and an interaction type, briefing materials need to cover the
objective, and follow-up records retain ownership and status.

The validator does not prove that an analyst is truly relevant or that a customer claim
is true. Those require human review and evidence.

## Run

From the `analyst_relations_program` directory:

```bash
python -m src.main
python -m unittest discover -s tests
```

# GTM consistency validator

Run the validator against the sample plan:

```text
python gtm_validator.py sample_plan.json
```

Run the tests:

```text
python -m unittest -v
```

The validator checks structural links across target market, journey stages, channels, content, metrics, and launch readiness. A passing result does not prove customer truth or channel performance; those still require evidence and review.

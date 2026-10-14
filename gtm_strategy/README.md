# GTM strategy specification

This small Python project stores and validates the SignalDesk go-to-market specification.

## Run the validator

From this directory, run:

```bash
python -m src.gtm_spec
```

Expected output for the included specification:

```text
[]
```

## Run the tests

With pytest installed, run:

```bash
python -m pytest
```

The validator checks structural links between journey stages, channels, content, and measures. It does not establish whether customer claims are true or whether a metric reflects real value.

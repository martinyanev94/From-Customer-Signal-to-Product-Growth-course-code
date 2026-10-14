# Positioning messaging system

This standard-library Python example renders one positioning core into four channel-specific messages. It preserves the exact claim and proof record while selecting a channel-specific action, then validates structural consistency and action placement.

The validator does not prove customer truth or semantic claim accuracy; those require human review.

## Run

From this directory:

```bash
python messaging.py
python -m unittest -v
```

"""
compute_delta.py — Compute deltas between two weekly state snapshots.

This is executable Python. The routine imports and calls compute_delta()
to produce the Phase 5 delta summary.

Usage:
    import json
    from scripts.compute_delta import compute_delta

    with open("state/latest.json") as f:
        previous = json.load(f)

    current = { ... }  # new state dict from this week's analysis
    delta = compute_delta(previous, current)
"""

import json
import sys
from typing import Any


# Numeric fields to diff between weekly states
NUMERIC_FIELDS = [
    "acute_load_7d",
    "chronic_load_28d",
    "distance_from_peak_pct",
    "hrv_7d_avg",
    "rhr_7d_avg",
    "sleep_hours_7d_avg",
    "weight_kg_7d_avg",
    "sessions_completed",
]


def compute_delta(previous: dict, current: dict) -> dict:
    """Compute field-level deltas between two state snapshots.

    Returns a dict with:
      - field_deltas: {field: {before, after, delta, pct_change}}
      - situational_context_changed: bool
      - previous_context: str
      - current_context: str
    """
    field_deltas = {}

    for field in NUMERIC_FIELDS:
        before = previous.get(field)
        after = current.get(field)

        if before is None or after is None:
            field_deltas[field] = {
                "before": before,
                "after": after,
                "delta": None,
                "pct_change": None,
            }
            continue

        try:
            before_f = float(before)
            after_f = float(after)
        except (TypeError, ValueError):
            field_deltas[field] = {
                "before": before,
                "after": after,
                "delta": None,
                "pct_change": None,
            }
            continue

        delta = round(after_f - before_f, 2)
        pct_change = round(delta / before_f * 100, 2) if before_f != 0 else None

        field_deltas[field] = {
            "before": before_f,
            "after": after_f,
            "delta": delta,
            "pct_change": pct_change,
        }

    prev_context = previous.get("situational_context", "")
    curr_context = current.get("situational_context", "")

    return {
        "field_deltas": field_deltas,
        "situational_context_changed": prev_context != curr_context,
        "previous_context": prev_context,
        "current_context": curr_context,
    }


def format_delta_summary(delta: dict) -> str:
    """Format the delta dict into a human-readable summary."""
    lines = []
    for field, values in delta["field_deltas"].items():
        before = values["before"]
        after = values["after"]
        d = values["delta"]
        pct = values["pct_change"]

        if d is None:
            lines.append(f"  {field}: {before} → {after} (no delta)")
        else:
            sign = "+" if d >= 0 else ""
            pct_str = f" ({sign}{pct}%)" if pct is not None else ""
            lines.append(f"  {field}: {before} → {after} ({sign}{d}{pct_str})")

    summary = "Field deltas:\n" + "\n".join(lines)

    if delta["situational_context_changed"]:
        summary += (
            f"\n\nSituational context changed:"
            f"\n  Before: {delta['previous_context']}"
            f"\n  After:  {delta['current_context']}"
        )
    else:
        summary += "\n\nSituational context: unchanged"

    return summary


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compute_delta.py <previous.json> <current.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        previous = json.load(f)
    with open(sys.argv[2]) as f:
        current = json.load(f)

    delta = compute_delta(previous, current)
    print(format_delta_summary(delta))

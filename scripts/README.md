# Scripts

## Executable Python

- **`compute_delta.py`** — Real Python module. Computes field-level deltas between two weekly state snapshots (`state/latest.json` → new state). Used by the routine in Phase 5. Can also be run from the command line:
  ```
  python scripts/compute_delta.py state/latest.json /tmp/new_state.json
  ```

## Documentation-only files

These files document the SQL and logic the routine executes directly via MCP connectors (`biometrics:query`, `baby mcp:query`). They exist so the logic is reviewable and version-controlled in one place, but they are **not** run as Python scripts.

- **`compute_historical_peak.py`** — Documents the SQL and methodology for computing the historical peak fitness state (`state/historical-peak.json`). The actual computation is performed interactively in a Claude Code session during bootstrap.

- **`fetch_weekly_snapshot.py`** — Documents the exact SQL queries run each week to pull the data snapshot across all core tables (Strava, Garmin, Withings, nutrition, labs, cognitive, cohabitant). The routine executes these via MCP, not by running this file.

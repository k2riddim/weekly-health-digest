---
name: digest-pipeline
description: Orchestrates the 6-phase weekly health digest pipeline. Invoke to re-anchor execution if the routine drifts.
---

# Digest Pipeline — Phase Orchestrator

This skill defines the 6 mandatory phases of the weekly health digest. Each phase must complete with real tool calls before advancing. The canonical definitions live in `CLAUDE.md`; this skill exists as a re-anchoring checkpoint.

## Phase 0 — Recover previous state

1. Read `state/latest.json` → `LAST_STATE`
2. Read `state/historical-peak.json` → `HISTORICAL_PEAK`
3. Read `protocols/thresholds.yaml` → `T` (parse all threshold values)
4. If `LAST_STATE.bootstrap === true`, flag Phase 5 as first-real-delta mode

**Gate:** All three files parsed. If `latest.json` is missing, abort with pipeline error.

## Phase 1 — Snapshot the week (broad pass)

Define `W` = ISO week ending yesterday (Saturday).

Query all core tables via `biometrics:query` and `baby mcp:query`. Do NOT interpret — just collect raw numbers.

Required data pulls:
- `strava_activities` for W (training executed)
- `training_load_daily` for W + 14 prior days (ACWR computation)
- `readiness_daily` for W
- `garmin_health` for W (wearable vitals)
- `withings_measurements` last 28d, filter `weight_kg > T.data_quality.weight_kg_floor`
- `oh_daily_nutrition_summary` for W
- `cognitive_sessions` for W
- `oh_observations` since W_start - 30d (labs, only if new data)
- Baby MCP: night wakings and sleep fragmentation for W

**Gate:** At least training + wearable + body comp data present. If core tables empty for `T.data_quality.abort_if_no_data_days`+ days, emit warning.

## Phase 2 — Triage + situational reassessment

1. Re-evaluate `situational_context` from `LAST_STATE`. State which signals confirm or contradict it.
2. Identify top 3 signals for deep-dive. For each: list competing hypotheses, rank them, name tables to query.
3. Check all deviation thresholds from `T.deviation_thresholds`.
4. If nothing abnormal → declare "maintenance mode" explicitly.

**Gate:** Triage document produced with ranked signals.

## Phase 3 — Deep dive

For each top signal from Phase 2:
1. State hypothesis and falsification criterion BEFORE querying
2. Run SQL that tests the hypothesis — every claim must touch ≥2 tables
3. Compare against personal 90-day baseline, not just population ranges
4. Load the relevant research module from `.claude/skills/research-modules/` before writing interpretation
5. Produce one data-anchored paragraph per domain

If a signal warrants a standalone study: invoke `.claude/skills/investigation` to scaffold files under `investigations/`.

**Gate:** Each signal has a falsifiable conclusion or explicit "data-limited" declaration.

## Phase 4 — Build W+1 training plan

Invoke `.claude/skills/training-planner` with inputs:
- `LAST_STATE`, current week load/readiness, `HISTORICAL_PEAK`
- `situational_context` (updated from Phase 2)
- `T.training` and `T.session_planning` thresholds

Receive 3–5 session specs. Create Google Calendar events in French. Check for conflicts first.

**Gate:** Calendar events created. Session specs recorded.

## Phase 5 — Delta vs last week

Run `scripts/compute_delta.py` for numeric field diffs.

Compute:
- Completion rate (fuzzy match planned vs actual: date + type + duration ±25%)
- Recommendation follow-through (pass/fail/unmeasurable)
- Markers-to-watch resolution (resolved/worsened/flat)
- Distance-from-peak (chronic_load_28d as % of HISTORICAL_PEAK, WoW delta in pp)
- Situational context drift narrative

If chronic_load_28d exceeds HISTORICAL_PEAK → update `state/historical-peak.json`.

**Gate:** Delta summary produced. If bootstrap mode, label accordingly.

## Phase 6 — Persist + deliver

1. Write `state/latest.json` with full new state
2. Copy to `state/history/YYYY-WW.json`
3. Write `digests/YYYY-WW.md` in the canonical digest format
4. Update `state/historical-peak.json` if beaten
5. Git add, commit on `claude/week-YYYY-WW`, push
6. Open PR using `.github/pull_request_template.md`
7. Create Gmail draft: subject `[HEALTH-DIGEST] Week YYYY-WW`, body = digest markdown

**Gate:** PR URL obtained. Gmail draft created. All artifacts committed.

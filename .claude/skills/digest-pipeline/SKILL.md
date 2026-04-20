---
name: digest-pipeline
description: Orchestrates the 6-phase daily health digest pipeline. Invoke to re-anchor execution if the routine drifts.
---

# Digest Pipeline — Phase Orchestrator

This skill defines the 6 mandatory phases of the daily health digest. Each phase must complete with real tool calls before advancing. The canonical definitions live in `CLAUDE.md`; this skill exists as a re-anchoring checkpoint.

## Phase 0 — Recover previous state

1. Read `state/latest.json` → `LAST_STATE`
2. Read `state/historical-peak.json` → `HISTORICAL_PEAK`
3. Read `protocols/thresholds.yaml` → `T` (parse all threshold values)
4. If `LAST_STATE.bootstrap === true`, flag Phase 5 as first-real-delta mode

**Gate:** All three files parsed. If `latest.json` is missing, abort with pipeline error.

## Phase 1 — Snapshot today + rolling context

Define `D` = yesterday (most recent complete day). Context window = last 7 days ending at `D`. Planning horizon = 7 days starting today.

Query all core tables via `biometrics:query` and `baby mcp:query`. Read Google Calendar for the planning horizon. Do NOT interpret — just collect raw numbers.

Required data pulls:
- `strava_activities` where `start_date >= D - 7 days` (did yesterday's planned session execute?)
- `training_load_daily` from `D - 14` through `D` (ACWR continuity)
- `readiness_daily` from `D - 7` through `D`
- `garmin_health` from `D - 7` through `D`
- `withings_measurements` last 28d, filter `weight_kg > T.data_quality.weight_kg_floor`
- `oh_daily_nutrition_summary` from `D - 7` through `D`
- `cognitive_sessions` from `D - 7` through `D`
- `oh_observations` since max(`LAST_STATE.as_of_date`, `D - 30`) — only surface if new
- Baby MCP: night wakings and sleep fragmentation from `D - 7` through `D`
- Google Calendar: list events from today through `today + 7`
  - Extract `no_train_days` = dates whose event summary or description matches `sur site` (case-insensitive)
  - Extract existing training events Claude created in prior runs (match on title convention / event id stored in `LAST_STATE.plan_7d_ahead`)

**Gate:** Training load, readiness, wearable, and calendar data present. If core tables empty for `T.data_quality.abort_if_no_data_days`+ days, emit warning.

## Phase 2 — Triage + situational reassessment

1. Re-evaluate `situational_context` from `LAST_STATE`. State which signals from the last 24–48h confirm or contradict it.
2. **Plan adherence check**: for each session in `LAST_STATE.plan_7d_ahead` with date ≤ yesterday, did it execute? Match `strava_activities` by date ± 1 day, type, and duration ± 25%.
   - Executed → mark done
   - Missed on a "sur site" day → legitimate
   - Missed on a free day → flag reason (readiness? choice? data gap?)
3. Identify up to 3 signals for deep-dive. For each: list competing hypotheses, rank them, name tables to query.
4. Check all deviation thresholds from `T.deviation_thresholds`.
5. If nothing abnormal → declare "maintenance — stay the course" explicitly.

**Gate:** Triage document produced with ranked signals and plan-adherence verdict.

## Phase 3 — Deep dive (only when warranted)

Skip this phase on quiet days. Only execute if Phase 2 identified ≥1 signal.

For each top signal:
1. State hypothesis and falsification criterion BEFORE querying
2. Run SQL that tests the hypothesis — every claim must touch ≥2 tables
3. Compare against personal 90-day baseline, not just population ranges
4. Load the relevant research module from `.claude/skills/research-modules/` before writing interpretation
5. Produce one data-anchored paragraph per domain

If a signal warrants a standalone study: invoke `.claude/skills/investigation` to scaffold files under `investigations/YYYY-MM-DD-<slug>/`.

**Gate:** Each signal has a falsifiable conclusion or explicit "data-limited" declaration. On quiet days, state "no deep-dives today".

## Phase 4 — Replan the rolling 7-day training window

Invoke `.claude/skills/training-planner` with inputs:
- `LAST_STATE`, today's load/readiness, `HISTORICAL_PEAK`
- `situational_context` (updated from Phase 2)
- `T.training` and `T.session_planning` thresholds
- `no_train_days` list from Phase 1
- Existing training Calendar events in the horizon (from Phase 1)

Planner outputs a full 7-day rolling plan. For each day:
- Existing event that still fits → leave untouched
- Existing event that no longer fits → update (shift time/intensity) or delete
- Day needs a session but has no event → create one
- Day blocked by "sur site" or rest-required → no event

**Gate:** Calendar state matches the new plan. `plan_7d_ahead` field populated.

## Phase 5 — Delta vs yesterday (and rolling 7d)

Run `scripts/compute_delta.py` for numeric field diffs.

Compute:
- Plan adherence (yesterday's session executed?)
- Recommendation follow-through (pass/fail/unmeasurable per prior recommendation)
- Markers-to-watch resolution (resolved/worsened/flat since yesterday)
- Rolling 7d vs prior rolling 7d shifts: acute_load_7d, HRV 7d avg, RHR 7d avg, sleep hours 7d avg
- Distance-from-peak (chronic_load_28d as % of HISTORICAL_PEAK, day-over-day delta in pp)
- Situational context drift narrative

If chronic_load_28d exceeds HISTORICAL_PEAK → update `state/historical-peak.json`.

**Gate:** Delta summary produced. If bootstrap mode, label accordingly.

## Phase 6 — Persist + deliver

1. Write `state/latest.json` with full new state (schema in CLAUDE.md)
2. Copy to `state/history/YYYY-MM-DD.json`
3. Write `digests/YYYY-MM-DD.md` in the canonical daily-digest format
4. Update `state/historical-peak.json` if beaten
5. Git add, commit on `claude/day-YYYY-MM-DD`, push
6. Open PR using `.github/pull_request_template.md`
7. Send Telegram message via the `telegram` MCP connector:
   - French, compact (≤ ~600 characters so it fits a phone notification)
   - Contains: headline, today's session (or rest/sur-site), HRV/RHR/sleep snapshot, top P0 recommendation, PR link

**Gate:** PR URL obtained. Telegram message sent. All artifacts committed.

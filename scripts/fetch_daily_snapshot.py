"""
fetch_daily_snapshot.py — Documentation of daily data snapshot queries

This file documents the exact SQL queries the routine runs each day via
biometrics:query and baby mcp:query, plus the Google Calendar lookups.
The routine executes these directly through MCP connectors, not by running
this Python file. Having the queries in one reviewable place ensures the
logic is auditable and version-controlled.

Date variables:
- D          = yesterday (most recent complete day of data)
- D_minus_7  = D - 7 days (rolling context window start)
- D_minus_14 = D - 14 days (ACWR lookback)
- today      = current date at run time
- horizon    = today + 7 days (planning window end)
"""

# =============================================================================
# 1. Training executed (rolling 7d) — strava_activities
# =============================================================================
#
# Purpose: check if yesterday's planned session executed; compute trailing load.
#
# SQL:
#   SELECT
#     id, name, sport_type, start_date, start_date_local,
#     distance, moving_time,
#     average_heart_rate, max_heart_rate,
#     suffer_score, training_load
#   FROM strava_activities
#   WHERE start_date >= '{D_minus_7}' AND start_date <= '{D}'::date + INTERVAL '1 day'
#   ORDER BY start_date;

# =============================================================================
# 2. Load & readiness — training_load_daily (D - 14 through D)
# =============================================================================
#
# SQL:
#   SELECT
#     date, daily_load, acute_load_7d, chronic_load_28d, training_status
#   FROM training_load_daily
#   WHERE date >= '{D_minus_14}' AND date <= '{D}'
#   ORDER BY date;

# =============================================================================
# 3. Readiness — readiness_daily (D - 7 through D)
# =============================================================================
#
# SQL:
#   SELECT
#     date, hrv_overnight_avg, hrv_7d_avg, hrv_baseline_low, hrv_baseline_high,
#     rhr, rhr_7d_avg, sleep_hours, sleep_score,
#     weight_kg, readiness_flag, readiness_notes, training_status
#   FROM readiness_daily
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;

# =============================================================================
# 4. Wearable vitals — garmin_health (D - 7 through D, today's upload prioritised)
# =============================================================================
#
# SQL:
#   SELECT
#     date, resting_heart_rate, hrv_score, hrv_weekly_avg,
#     sleep_score, sleep_hours, deep_sleep_minutes, rem_sleep_minutes,
#     body_battery, training_readiness, stress_score,
#     skin_temperature_c, vo2max_running, vo2max_cycling
#   FROM garmin_health
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;

# =============================================================================
# 5. Body composition — withings_measurements (last 28d)
# =============================================================================
#
# SQL:
#   SELECT
#     date, weight_kg, fat_mass_kg, fat_free_mass_kg,
#     fat_ratio_percent, muscle_mass_kg, bone_mass_kg
#   FROM withings_measurements
#   WHERE date >= '{D}'::date - INTERVAL '28 days'
#     AND weight_kg > {T.data_quality.weight_kg_floor}
#   ORDER BY date;

# =============================================================================
# 6. Nutrition — oh_daily_nutrition_summary (rolling 7d)
# =============================================================================
#
# SQL (introspect columns first if schema unknown):
#   SELECT column_name, data_type
#   FROM information_schema.columns
#   WHERE table_name = 'oh_daily_nutrition_summary';
#
# Then:
#   SELECT *
#   FROM oh_daily_nutrition_summary
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;

# =============================================================================
# 7. Cognitive — cognitive_sessions (rolling 7d)
# =============================================================================
#
# SQL:
#   SELECT *
#   FROM cognitive_sessions
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;

# =============================================================================
# 8. Labs — oh_observations (only if new since LAST_STATE.as_of_date)
# =============================================================================
#
# SQL:
#   SELECT
#     observation_name, value, unit, reference_range, effective_datetime
#   FROM oh_observations
#   WHERE effective_datetime > '{LAST_STATE.as_of_date}'::timestamp
#   ORDER BY effective_datetime DESC;

# =============================================================================
# 9. Cohabitant — baby MCP queries (rolling 7d)
# =============================================================================
#
# Via baby mcp:query:
#   SELECT * FROM may_sleep
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;
#
#   SELECT * FROM may_feedings
#   WHERE date >= '{D_minus_7}' AND date <= '{D}'
#   ORDER BY date;
#
#   SELECT * FROM owlet_sleep_sessions
#   WHERE start_time >= '{D_minus_7}' AND start_time <= '{D}'::date + INTERVAL '1 day'
#   ORDER BY start_time;
#
#   SELECT * FROM napper_logs
#   WHERE start_time >= '{D_minus_7}' AND start_time <= '{D}'::date + INTERVAL '1 day'
#     AND category IN ('NIGHT_WAKING', 'WOKE_UP', 'BED_TIME')
#   ORDER BY start_time;

# =============================================================================
# 10. Google Calendar — planning horizon + "sur site" detection
# =============================================================================
#
# Via Google Calendar MCP, list events from today through today + 7 days.
# For each event, check whether summary or description contains "sur site"
# (case-insensitive). Collect:
#   - no_train_days: set of dates blocked by a "sur site" event
#   - existing_training_events: events whose id matches any
#     LAST_STATE.plan_7d_ahead[*].calendar_event_id (these are Claude-created
#     training events that may need updating or deletion)
#   - other_events: meetings and personal events that constrain session timing
#     (a training slot must not collide with an existing meeting)

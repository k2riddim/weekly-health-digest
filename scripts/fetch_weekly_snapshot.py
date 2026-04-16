"""
fetch_weekly_snapshot.py — Documentation of weekly data snapshot queries

This file documents the exact SQL queries the routine runs each week via
biometrics:query and baby mcp:query. The routine executes these directly
through MCP connectors, not by running this Python file. Having the SQL
in one reviewable place ensures the logic is auditable and version-controlled.

In all queries below, W_start and W_end refer to the ISO week boundaries
(Monday 00:00 to Sunday 23:59) ending yesterday.
"""

# =============================================================================
# 1. Training executed — strava_activities
# =============================================================================
#
# SQL:
#   SELECT
#     id, name, sport_type, start_date,
#     distance, moving_time, elapsed_time,
#     total_elevation_gain,
#     average_heartrate, max_heartrate,
#     average_speed, suffer_score
#   FROM strava_activities
#   WHERE start_date >= '{W_start}' AND start_date < '{W_end}'
#   ORDER BY start_date;

# =============================================================================
# 2. Load & readiness — training_load_daily (W + prior 14d for ACWR)
# =============================================================================
#
# SQL:
#   SELECT
#     calendar_date,
#     acute_load_7d, chronic_load_28d,
#     acwr, load_status
#   FROM training_load_daily
#   WHERE calendar_date >= '{W_start}'::date - INTERVAL '14 days'
#     AND calendar_date <= '{W_end}'::date
#   ORDER BY calendar_date;

# =============================================================================
# 3. Readiness — readiness_daily
# =============================================================================
#
# SQL:
#   SELECT *
#   FROM readiness_daily
#   WHERE calendar_date >= '{W_start}' AND calendar_date <= '{W_end}'
#   ORDER BY calendar_date;

# =============================================================================
# 4. Wearable vitals — garmin_health
# =============================================================================
#
# SQL:
#   SELECT
#     calendar_date,
#     resting_heart_rate, avg_heart_rate_variability,
#     sleep_score, sleep_duration_hours,
#     body_battery_highest, body_battery_lowest,
#     stress_avg, respiration_avg,
#     skin_temp_deviation_celsius
#   FROM garmin_health
#   WHERE calendar_date >= '{W_start}' AND calendar_date <= '{W_end}'
#   ORDER BY calendar_date;

# =============================================================================
# 5. Body composition — withings_measurements (last 28d)
# =============================================================================
#
# SQL:
#   SELECT
#     date, weight_kg, fat_mass_kg, fat_free_mass_kg,
#     fat_ratio_pct, muscle_mass_kg, bone_mass_kg
#   FROM withings_measurements
#   WHERE date >= '{W_start}'::date - INTERVAL '28 days'
#     AND weight_kg > {T.data_quality.weight_kg_floor}
#   ORDER BY date;

# =============================================================================
# 6. Nutrition — oh_daily_nutrition_summary
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
#   WHERE date >= '{W_start}' AND date <= '{W_end}'
#   ORDER BY date;

# =============================================================================
# 7. Cognitive — cognitive_sessions
# =============================================================================
#
# SQL:
#   SELECT *
#   FROM cognitive_sessions
#   WHERE date >= '{W_start}' AND date <= '{W_end}'
#   ORDER BY date;

# =============================================================================
# 8. Labs — oh_observations (last 30d, only if new data)
# =============================================================================
#
# SQL:
#   SELECT
#     observation_name, value, unit, reference_range,
#     effective_datetime
#   FROM oh_observations
#   WHERE effective_datetime >= '{W_start}'::date - INTERVAL '30 days'
#   ORDER BY effective_datetime DESC;

# =============================================================================
# 9. Cohabitant — baby MCP queries
# =============================================================================
#
# Night wakings (via baby mcp:query):
#   SELECT *
#   FROM may_sleep
#   WHERE date >= '{W_start}' AND date <= '{W_end}'
#   ORDER BY date;
#
# Feedings:
#   SELECT *
#   FROM may_feedings
#   WHERE date >= '{W_start}' AND date <= '{W_end}'
#   ORDER BY date;
#
# Owlet sleep sessions (for fragmentation analysis):
#   SELECT *
#   FROM owlet_sleep_sessions
#   WHERE start_time >= '{W_start}' AND start_time < '{W_end}'
#   ORDER BY start_time;

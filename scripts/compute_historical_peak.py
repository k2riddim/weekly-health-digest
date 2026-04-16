"""
compute_historical_peak.py — Documentation of historical peak computation

This file documents the logic and SQL used to compute the historical peak
fitness state stored in state/historical-peak.json. The actual bootstrap
computation is performed interactively via biometrics:query in a Claude Code
session, not by running this script.

The historical peak represents Benjamin's best sustained training period,
used as the "north star" for the weekly digest's distance-from-peak metric.
"""

# =============================================================================
# Step 1: Find the peak 90-day rolling average of chronic_load_28d
# =============================================================================
#
# This identifies the year/period when sustained fitness was highest.
#
# SQL:
#   SELECT
#     calendar_date,
#     chronic_load_28d,
#     AVG(chronic_load_28d) OVER (
#       ORDER BY calendar_date
#       ROWS BETWEEN 89 PRECEDING AND CURRENT ROW
#     ) AS rolling_90d_avg
#   FROM training_load_daily
#   WHERE chronic_load_28d IS NOT NULL
#   ORDER BY rolling_90d_avg DESC NULLS LAST
#   LIMIT 1;
#
# This gives us the date at the center of the peak sustained training block.

# =============================================================================
# Step 2: Query activity mix for the peak year
# =============================================================================
#
# Using the year identified in Step 1, pull the activity distribution:
#
# SQL:
#   SELECT
#     sport_type,
#     COUNT(*) AS session_count,
#     ROUND(AVG(distance / 1000.0), 1) AS avg_distance_km,
#     ROUND(AVG(moving_time / 60.0), 0) AS avg_duration_min,
#     ROUND(SUM(distance / 1000.0), 0) AS total_distance_km
#   FROM strava_activities
#   WHERE EXTRACT(YEAR FROM start_date) = <peak_year>
#   GROUP BY sport_type
#   ORDER BY session_count DESC;

# =============================================================================
# Step 3: Weekly volume for the peak year
# =============================================================================
#
# SQL:
#   SELECT
#     sport_type,
#     ROUND(AVG(weekly_km), 1) AS avg_weekly_km
#   FROM (
#     SELECT
#       sport_type,
#       DATE_TRUNC('week', start_date) AS week,
#       SUM(distance / 1000.0) AS weekly_km
#     FROM strava_activities
#     WHERE EXTRACT(YEAR FROM start_date) = <peak_year>
#     GROUP BY sport_type, DATE_TRUNC('week', start_date)
#   ) sub
#   GROUP BY sport_type;

# =============================================================================
# Step 4: Dominant HR zones for the peak year
# =============================================================================
#
# SQL:
#   SELECT
#     sport_type,
#     ROUND(AVG(average_heartrate), 0) AS avg_hr,
#     ROUND(AVG(max_heartrate), 0) AS avg_max_hr
#   FROM strava_activities
#   WHERE EXTRACT(YEAR FROM start_date) = <peak_year>
#     AND average_heartrate IS NOT NULL
#   GROUP BY sport_type
#   ORDER BY COUNT(*) DESC;
#
# Map average HR to zone using protocols/zones.md thresholds.

# =============================================================================
# Output schema: state/historical-peak.json
# =============================================================================
#
# {
#   "computed_at": "ISO datetime",
#   "year": N,
#   "chronic_load_28d_avg": N,
#   "chronic_load_28d_peak": N,
#   "activity_mix": {"Run": pct, "Ride": pct, ...},
#   "weekly_volume_km": {"Run": N, "Ride": N},
#   "typical_session_minutes": {"Run": N, "Ride": N},
#   "dominant_hr_zones": {"Run": "Z2-Z3", "Ride": "Z2"},
#   "hallmark": "free-text one-liner describing that year's training identity"
# }

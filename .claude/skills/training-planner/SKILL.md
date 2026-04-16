---
name: training-planner
description: Builds the W+1 training plan (3–5 sessions) respecting ACWR band, ramp cap, and current readiness. Creates Google Calendar events in French.
---

# Training Planner

Given the week's analysis, produce 3–5 session specifications for W+1 that respect physiological load constraints and current-life situational factors.

## Inputs required

- `LAST_STATE` — previous week's state from `state/latest.json`
- Current week's `acute_load_7d` and `chronic_load_28d` from Phase 1 data
- `HISTORICAL_PEAK` from `state/historical-peak.json`
- `situational_context` — updated in Phase 2
- `T.training` — thresholds from `protocols/thresholds.yaml`:
  - `acwr_lower_bound`, `acwr_upper_bound`
  - `weekly_acute_ramp_cap`
  - `deload_multiplier`
  - `return_from_layoff_acute_to_chronic_threshold`
- `T.session_planning` — `min_sessions_per_week`, `max_sessions_per_week`, `horizon_days`

## Load constraints checklist

Before generating sessions, verify each constraint:

- [ ] **Ramp cap**: Next week target acute ≤ this week acute × `T.training.weekly_acute_ramp_cap`
- [ ] **ACWR band**: Projected ACWR (next_acute / chronic_load_28d) within `[acwr_lower_bound, acwr_upper_bound]`
- [ ] **Rebuild mode**: If acute/chronic < `return_from_layoff_acute_to_chronic_threshold`, bias toward aerobic base (Z1–Z2), lower volume
- [ ] **Red flags**: If HRV/sleep/illness signals flagged in Phase 2–3, apply `deload_multiplier` to this week's acute
- [ ] **Illness signals**: Rest + light aerobic only, no intensity
- [ ] **Session count**: Between `min_sessions_per_week` and `max_sessions_per_week`

## Calendar conflict check

Before creating any events:

1. Call `gcal_list_events` for W+1 (Monday through Sunday)
2. Identify time slots that are already occupied
3. Place training sessions in free slots, preferring:
   - Morning slots for intensity sessions
   - Consistent timing with prior weeks when possible
   - Adequate recovery between hard sessions (≥48h)

## Session specification format

Each session must include:
- **Day and time**: specific slot, avoiding conflicts
- **French title**: e.g., "Course Z2 — Base aérobie"
- **Duration**: in minutes
- **Target HR zone**: from `protocols/zones.md`
- **Target load contribution**: estimated load units
- **One-line rationale**: why this session, in context of the week plan
- **Tired-day fallback**: what to do instead if feeling flat (e.g., "Réduire à 30min Z1 marche")

## Activity type selection

Draw from the activity mix in `HISTORICAL_PEAK.activity_mix` for guidance, but adapt to current capacity:
- Rebuild phases: predominantly Run Z2 and Ride Z2
- Maintenance: mix per historical preference
- Peak approach: introduce Z3–Z4 intervals per 80/20 principle

## Output

Return a list of 3–5 session objects:
```json
[
  {
    "day": "Monday",
    "time": "07:30",
    "type": "Run",
    "title_fr": "Course Z2 — Base aérobie",
    "duration_min": 45,
    "target_zone": "Z2",
    "target_load": 85,
    "rationale": "...",
    "fallback": "Réduire à 30min Z1 marche"
  }
]
```

Create each as a Google Calendar event with:
- Title: the French title
- Duration: as specified
- Description: zone target, load target, rationale, and fallback instruction — all in French

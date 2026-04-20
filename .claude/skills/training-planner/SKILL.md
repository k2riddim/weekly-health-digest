---
name: training-planner
description: Replans a rolling 7-day training window every day. Respects ACWR band, ramp cap, readiness, and "sur site" calendar blocks. Creates/updates/deletes Google Calendar events in French.
---

# Training Planner — Daily Rolling Replanner

Given today's analysis, produce a full 7-day training plan (today → today+6) and reconcile it with existing Google Calendar training events. The plan is rebuilt daily but touched minimally — preserve what still fits, only change what must change.

## Inputs required

- `LAST_STATE` — previous day's state from `state/latest.json`, including `plan_7d_ahead` with `calendar_event_id` for each event Claude created previously
- Today's `acute_load_7d` and `chronic_load_28d` from Phase 1 data
- `HISTORICAL_PEAK` from `state/historical-peak.json`
- `situational_context` — updated in Phase 2
- `T.training` — thresholds from `protocols/thresholds.yaml`:
  - `acwr_lower_bound`, `acwr_upper_bound`
  - `weekly_acute_ramp_cap`
  - `deload_multiplier`
  - `return_from_layoff_acute_to_chronic_threshold`
- `T.session_planning` — `min_sessions_per_week`, `max_sessions_per_week`, `horizon_days`
- `no_train_days` — list of dates (YYYY-MM-DD) where Google Calendar shows a "sur site" event. **Training is forbidden on these days.**
- `existing_events` — list of Calendar events in the horizon that Claude created before (matched via `calendar_event_id`)

## "Sur site" constraint

An event whose summary or description contains `sur site` (case-insensitive match on the Calendar event) marks a day as on-site at work. Benjamin cannot train that day.

Logic:
1. Before proposing any session, cross-check the target date against `no_train_days`.
2. If there is already a training event Claude created for a day that has since become a `no_train_day`, **delete** that event and mark the day `blocked` in `plan_7d_ahead`.
3. Never create a new training event on a `no_train_day`.

## Load constraints checklist

Before generating sessions, verify each constraint:

- [ ] **Ramp cap**: Projected next-7-day acute load ≤ trailing acute × `T.training.weekly_acute_ramp_cap`
- [ ] **ACWR band**: Projected ACWR (next_acute / chronic_load_28d) within `[acwr_lower_bound, acwr_upper_bound]`
- [ ] **Rebuild mode**: If acute/chronic < `return_from_layoff_acute_to_chronic_threshold`, bias toward aerobic base (Z1–Z2), lower volume
- [ ] **Red flags**: If HRV/sleep/illness signals flagged in Phase 2–3, apply `deload_multiplier` to today's planned load
- [ ] **Illness signals**: Rest + light aerobic only, no intensity
- [ ] **Session count**: Between `min_sessions_per_week` and `max_sessions_per_week` across the 7-day window, adjusted for `no_train_days` (fewer available days → fewer sessions, not higher density)
- [ ] **Recovery spacing**: ≥48h between hard (Z4/Z5) sessions; ≥24h between moderate (Z3) sessions and any intensity
- [ ] **No training on `no_train_days`**

## Calendar reconciliation — minimize churn

For each day in the 7-day horizon, compare the new plan to the existing Calendar event (if any):

| Existing event | New plan | Action |
|---------------|---------|--------|
| None | Session proposed | **CREATE** new Calendar event |
| Exists, still fits | Same session | **LEAVE** untouched (do not re-create) |
| Exists | Different session (type / intensity / duration change) | **UPDATE** the event |
| Exists | Day now blocked (`sur site` appeared) or rest required | **DELETE** the event |
| Exists | No plan for the day (e.g., removed due to deload) | **DELETE** the event |

**Always** re-read Google Calendar at Phase 1 before making changes — do not assume `LAST_STATE.plan_7d_ahead` matches current Calendar state.

## Session specification format

Each session in `plan_7d_ahead` must include:
- **Date** (YYYY-MM-DD) and **time** (HH:MM)
- **French title**: e.g., "Course Z2 — Base aérobie"
- **Duration**: in minutes
- **Target HR zone**: from `protocols/zones.md`
- **Target load contribution**: estimated load units
- **Rationale**: why this session, in context of the week plan
- **Tired-day fallback**: what to do instead if feeling flat (e.g., "Réduire à 30min Z1 marche")
- **Calendar event id**: assigned after create/update
- **Status**: `planned` | `blocked` | `rest`

## Activity type selection

Draw from the activity mix in `HISTORICAL_PEAK.activity_mix` for guidance, but adapt to current capacity:
- Rebuild phases: predominantly Run Z2 and Ride Z2
- Maintenance: mix per historical preference
- Peak approach: introduce Z3–Z4 intervals per 80/20 principle

## Output

Return a `plan_7d_ahead` list (one entry per day, including blocked/rest days):

```json
[
  {
    "date": "2026-04-17",
    "day": "Friday",
    "time": "07:30",
    "type": "Run",
    "title_fr": "Course Z2 — Base aérobie",
    "duration_min": 45,
    "target_zone": "Z2",
    "target_load": 85,
    "rationale": "...",
    "fallback": "Réduire à 30min Z1 marche",
    "calendar_event_id": "evt_abc123",
    "status": "planned"
  },
  {
    "date": "2026-04-18",
    "day": "Saturday",
    "status": "blocked",
    "reason": "sur site"
  },
  {
    "date": "2026-04-19",
    "day": "Sunday",
    "status": "rest",
    "reason": "recovery spacing after Friday intensity"
  }
]
```

Apply Calendar actions per the reconciliation table above. Record `calendar_event_id` for each created or updated event. Record the chosen actions in the digest so Benjamin can see what moved.

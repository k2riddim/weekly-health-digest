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
- `recent_runs` — the completed runs from the last ~3 weeks (date, distance, duration, avg HR, any reported pain), used to anchor prescribed run length (see checklist).
- `heat_forecast` — per-day feels-like temperature for the planning horizon (from Phase 1), used with `T.heat` and `protocols/heat.md`.
- `PROFILE.medications` and `T.glp1` — from `protocols/health-profile.md` / `protocols/thresholds.yaml`. While a GLP-1 agonist is active the planner must: keep a strength stimulus in the window, add fuelling / hydration lines to every event, respect the post-injection window when known, and refuse any readiness gate expressed as a pre-medication RHR/HRV absolute.

## Mandatory reads when the return-to-running protocol is active

If Benjamin is in a running comeback, **read `protocols/return-to-running.md` before planning** (it is the super-important override). For any outdoor session, **read `protocols/heat.md`** and apply the `T.heat` bands. These are not optional — the comeback and heat rules override the generic defaults below.

## "Sur site" constraint

An event whose summary or description contains `sur site` (case-insensitive match on the Calendar event) marks a day as on-site at work. Benjamin cannot train that day.

Logic:
1. Before proposing any session, cross-check the target date against `no_train_days`.
2. If there is already a training event Claude created for a day that has since become a `no_train_day`, **delete** that event and mark the day `blocked` in `plan_7d_ahead`.
3. Never create a new training event on a `no_train_day`.

## Load constraints checklist

Before generating sessions, verify each constraint:

- [ ] **Ramp cap**: Projected next-7-day acute load ≤ trailing acute × `T.training.weekly_acute_ramp_cap`. **When the return-to-running protocol is active, use `T.training.comeback_weekly_acute_ramp_cap` (+15%) instead** — the layoff-depressed chronic base tolerates faster early progression.
- [ ] **ACWR band**: Projected ACWR (next_acute / chronic_load_28d) within `[acwr_lower_bound, acwr_upper_bound]`. **When the return-to-running protocol is active, use `comeback_acwr_upper_bound` (1.50) as the upper bound** — the general 1.30 ceiling is too tight while chronic load is still rebuilding.
- [ ] **Rebuild mode**: If acute/chronic < `return_from_layoff_acute_to_chronic_threshold`, bias toward aerobic base (Z1–Z2). Volume should still progress and single runs should get longer — bias aerobic ≠ stay short. Extend the long run (easy Z1–Z2) as tissue feedback allows; do not treat a longer easy run as a red-flag load spike.
- [ ] **Run length anchored to demonstrated tolerance**: Set the easy-run floor to the longest run in `recent_runs` that was completed without pain and followed by clean recovery. **Never prescribe below that without a specific current recovery/injury reason.** Progress the long run from that anchor by ≤ ~1 km / ~10 min per step. If recent runs consistently overshot the prescribed target and were tolerated well, the target was too low → **raise it**, do not clamp it. **Do not** use GPS turnaround alarms, forced cutoffs, or "STRICT MAX" caps to enforce an artificially low target — those are only legitimate in a genuine red-flag context (post-injury, illness, red recovery markers). See `return-to-running.md` §4F.
- [ ] **Heat**: For each outdoor session, take the `heat_forecast` feels-like value at the planned start hour, apply the `T.heat` post-heatwave modifier if triggered, and classify per `protocols/heat.md`. **First lever is timing** (move to the coolest hour), then duration reduction, then indoor substitution or rest. In the Red band, no outdoor running — substitute indoor or rest. Do not encode heat as a blanket "−20% if >36°C"; that threshold is far too permissive for this athlete.
- [ ] **Red flags**: If HRV/sleep/illness signals flagged in Phase 2–3, apply `deload_multiplier` to today's planned load
- [ ] **Illness signals**: Rest + light aerobic only, no intensity
- [ ] **GLP-1 lens (while `T.glp1.active`)**: (a) RHR/HRV drift inside `T.glp1.rhr_expected_shift_bpm_*` vs the post-initiation baseline, with no second signal, is **not** a red flag and does not trigger the deload multiplier or a "porte deload"; (b) ≥ `T.glp1.strength_sessions_per_week_min` resistance session per rolling week (lean-mass preservation — bodyweight / gym / "Renfo" counts); (c) every event description carries the fuelling line (last solid meal ≥ `T.glp1.pre_run_meal_gap_hours_min` h before; small, frequent carbs beyond `T.glp1.session_duration_min_requiring_fuel` min; explicit pre-hydration when heat band ≥ Yellow); (d) if `T.glp1.injection_weekday` is known, do not place the long run or any Z3+ work inside the `post_injection_side_effect_window_days` window — schedule easy work or rest there; (e) a session moved or softened for GI side effects is recorded as "déplacée — effet secondaire GI", never as a silent skip.
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
- **Fuelling / hydration line** (while `T.glp1.active`): e.g., "Dernier repas solide ≥ 3 h avant ; 500 ml d'eau + électrolytes avant le départ ; gel ou boisson glucidique toutes les 20–25 min au-delà de 75 min" — GI side-effect days: "séance déplacée, pas sautée"
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

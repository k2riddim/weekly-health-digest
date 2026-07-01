---
name: calendar-strava-sync
description: Reconciles past Google Calendar training events against actual Strava execution (done / skipped / custom / unplanned), and keeps Strava activity metadata (name, description, commute flag) clean. Runs standalone, multiple times a day, independent of the once-daily digest pipeline.
---

# Calendar ↔ Strava Sync

Two independent jobs. Both are housekeeping on live external state (Google Calendar, Strava via the `biometrics` MCP) — not part of `state/latest.json`. Nothing here is persisted to the repo except this convention doc; there is nothing to commit on a normal run unless the convention itself changes.

## Job 1 — Tag past calendar events with execution status

Scope: calendar events in the recent past (rolling window — reuse the digest pipeline's 7-day context window unless told otherwise) whose summary/description represents a planned training session (created by the training-planner skill, or manually by Benjamin).

For each such past event, look up Strava activities within date ±1 day and compare type/duration/distance to the plan:

| Situation | Title prefix | Color family |
|---|---|---|
| Matching Strava activity, close to plan (type, distance/duration within ~25%, target zone respected) | `✅ done \| <emoji> <original title>` | green, shaded by suffer score (below) |
| Matching Strava activity, but materially different (distance/duration/HR/timing deviates from plan) | `✅ custom session done \| <emoji> <what was actually done>` | green/blue/orange, shaded by suffer score (below) |
| No matching Strava activity, day not blocked, no stated reason | `⏭️ skipped \| <original title>` | Graphite (`colorId: 8`) |
| No matching Strava activity, explicit reason known (weather abort, illness, rescheduled) | `❌ ANNULÉ — <original title> (<reason>)` | Graphite (`colorId: 8`) |
| Strava activity with no corresponding calendar event at all | **create** a new event, title `✅ done \| <emoji> <descriptive title>`, colored per suffer score | green, shaded by suffer score |

Commute rides get the same treatment as any other session (they normally land in the low-suffer green band). Always include commute activities in the review — don't skip them because they're not "training" in the athletic sense.

Each updated/created event's **description** should read as: `<Strava link/id> — <km · duration · avg/max HR · elevation · suffer>` plus one line on any deviation from plan. This is a private calendar description, so HRV/ACWR/readiness/weight context is fine here (unlike the public Strava description in Job 2).

### Suffer-score color formula (data-driven, no hardcoded cutoffs)

At the start of the run, compute personal terciles/percentile from trailing 120 days:

```sql
select
  percentile_cont(0.33) within group (order by suffer_score) as p33,
  percentile_cont(0.66) within group (order by suffer_score) as p66,
  percentile_cont(0.90) within group (order by suffer_score) as p90
from strava_activities
where start_date >= now() - interval '120 days' and suffer_score is not null;
```

Then, for the activity being tagged:

- **Executed as planned** (green family — Calendar only offers two true greens):
  - `suffer_score < p33` → `colorId: 2` (Sage, light green)
  - `suffer_score >= p33` → `colorId: 10` (Basil, dark green) — add a 🔥 to the title if `suffer_score >= p90` (no third green shade available)
- **Custom / deviated session** (distinct family so it's visually separable from a clean "as planned" execution):
  - `suffer_score < p66` → `colorId: 2` (Sage)
  - `p66 <= suffer_score < p90` → `colorId: 7` (Peacock)
  - `suffer_score >= p90` → `colorId: 6` (Tangerine)
- **Skipped / cancelled**: always `colorId: 8` (Graphite) — no suffer score exists since nothing happened.

Recompute the percentiles every run; never hardcode an absolute suffer-score number in a prompt or event description.

**Minimize churn.** This formula is applied prospectively, to events not yet tagged. Do not retag or recolor an event that was already tagged by a prior run just because the exact color would differ under a refined formula — that just generates noise on Benjamin's calendar for no benefit. (An audit on 2026-07-01 found a couple of early instances where "custom, suffer ≥ p90" landed on Peacock instead of Tangerine — left as-is for this reason.)

## Job 2 — Label & document Strava activities

Runs over the same recent window. Two independent sub-steps per activity:

### a) Rename — only if the name is still a Strava default

Only touch `name` when it matches an unedited Strava auto-generated title, e.g. `Morning Run`, `Sortie en vélo électrique le matin`, `Sortie gravel le matin`, `Trajet du soir`, or the English/French auto-title equivalents. If the name already carries any custom content (distance, protocol reference, run number, free text), leave it untouched — do not "improve" a name a human already chose.

Detecting "default" reliably: query `select name, count(*) from strava_activities group by name order by count(*) desc` — a name repeated verbatim across many dates with no distinguishing detail (no distance, no date-specific context) is almost always an unedited default template. A name that's unique or contains numbers/places/protocol references is edited.

New name convention (French), matching what's already in use:
- Runs: `Retour running — Run #N — X,X km <zone>` (append a location suffix if notable, e.g. `(Forêt de Chantilly)`)
- E-bike commute: `Trajet domicile → bureau — vélo électrique` / `Trajet bureau → domicile — vélo électrique`
- Unplanned/free e-bike: `Balade matinale/soirée/locale — vélo électrique`
- Gravel/road rides: short descriptive French title reflecting what happened

### b) Description — only if none is set

Check `raw_data->>'description'` on `strava_activities` (or the `strava_response.description` returned by `update_strava_activity`). If null/empty, add one; if already set, leave it alone — never overwrite an existing description.

Content: distance/duration/HR/elevation/suffer line, plus one short line of context (terrain, weather, protocol deviation from plan). This description is **public on Strava** — keep it to training facts only.

**Never include in a Strava description:** body weight or body-composition numbers, fitness/weight-loss objectives or target dates, HRV/ACWR/training-readiness/body-battery figures, lab or medical information, or anything about private life. Those are fine in the *Calendar* event description (Job 1) but not here.

### c) Commute flag

Always set/confirm `commute: true` on activities that are clearly a home↔work e-bike trip, regardless of whether the name/description needed touching. Don't skip commute-flag verification just because the name was already custom.

## Scope note

This is ongoing hygiene, not a historical backfill. Process the recent rolling window each run (mirrors the digest pipeline's `D-7`..`D` context window). A one-off bulk cleanup of years of historical default-named activities is a separate, explicitly-requested task — don't attempt it opportunistically as part of a routine run.

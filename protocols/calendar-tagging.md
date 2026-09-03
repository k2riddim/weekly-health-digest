# Calendar & Strava Tagging Convention

Reference for the standalone "review calendar + label Strava" routine (runs 3x/day, separate
from the daily health digest). Not read by the digest pipeline. Written down because the
convention had drifted slightly across manual runs before this file existed — this is the
canonical version going forward.

## Scope of each pass

Review window: the trailing ~5-7 days plus today. For each day in the window:
- Match `strava_activities` against existing Google Calendar training events for that day.
- Tag the Calendar event's color + title prefix based on the match outcome (below).
- Create a Calendar event for any unplanned Strava activity (including commutes) that has none.
- **Idempotency**: an event whose title already carries a status prefix (✅ / ⏭️ / 🟢 / ❌) is
  left alone unless new Strava data now contradicts it (e.g. a "skipped" session that a
  later-arriving activity now shows was actually done — retag it then). Never re-churn an
  already-correct tag; this keeps the calendar stable across 3 runs/day.
- A "skipped" tag applied before the full grace window has elapsed should say so in the
  description (see template) so a later pass knows to re-check rather than treat it as final.

## Status prefixes (prepended to the existing/base title)

| Situation | Prefix | colorId base |
|---|---|---|
| Activity executed, matches the planned session (type/time/effort roughly as planned) | `✅ done \| ` | suffer-score gradient (below) |
| Activity executed but differs materially from the plan (different type, time, or distance) | `🟢 custom done \| ` | suffer-score gradient (below) |
| Planned session never executed (no matching Strava activity by review time) | `⏭️ skipped \| ` | `8` (Graphite) always |
| Planned session proactively invalidated ahead of time (heat abort, deload gate not crossed, etc. — decided by the training planner, not a no-show) | `❌ annulé \| ` or `❌ annulé (reason) \| ` | `11` (Tomato) |
| Unplanned Strava activity with no corresponding event → new event created | `✅ done \| ` (or `🚌 ` prefix for a commute) | suffer-score gradient |

Activity-type emoji follow the prefix: 🏃 run, 🚴 bike, 🚌 commute (any commute-flagged ride,
regardless of sport), 🏊 swim, 🚶 walk/active recovery.

## Suffer-score → colorId gradient (done / custom done only)

`suffer_score` from `strava_activities`. Skipped and annulé ignore this table (fixed colors above).

| suffer_score | colorId | Google color name |
|---|---|---|
| < 5 | `2` | Sage (palest green) |
| 5–15 | `10` | Basil (green) |
| 15–35 | `5` | Banana (yellow) |
| 35–50 | `6` | Tangerine (orange) |
| 50–70 | `4` | Flamingo (pink-red) |
| ≥ 70 | `11` | Tomato (red) |

## Description templates (Calendar event, French)

**Done / custom done** (activity happened):
```
<What happened> — Strava #<activity_id>
<distance> km · <duration> min · FC moy <hr> bpm · FC max <hr_max> bpm · D+ <elev> m · Charge <load> · Suffer <suffer>

<one line on how it relates to the plan, or "Séance non planifiée..." if unplanned>
```

**Skipped** (retag over the original plan description, keep the plan below a separator):
```
Retagué le <DD/MM> — Revue calendrier post-exécution (routine 3x/jour). Séance non exécutée — aucune
activité Strava enregistrée à l'heure de la revue (<HHhMM> Paris), soit environ <X>h<YY> après la fin
du créneau prévu (<start>-<end>). Sera re-vérifié et corrigé automatiquement si une activité Strava
apparaît lors du prochain passage.

---
<original plan description, unchanged>
```

## Strava activity labeling (separate task, same pass)

- **Rename** only if the current name is still an unedited Strava default (e.g. "Morning Run",
  "Sortie en vélo électrique le soir/matin/après-midi"). Leave any name that already looks
  human-edited untouched, even if it wasn't renamed by this routine.
- **Description**: add one only if none exists yet (check `raw_data->>'description'`). Public
  training info only — distance/duration/HR/elevation/suffer/load, plan deviation, route notes.
  Never weight, body composition, fitness objectives, lab/medical data, or other private-life
  details.
- **Commute flag**: always set `commute: true` on trajet domicile↔bureau rides, regardless of
  whether the name/description needed touching.
- **Timezone**: `strava_activities.start_date` is UTC; `start_date_local` is already Paris local
  (matches `date -u` + 2h in CEST, +1h in CET). Google Calendar events default to Europe/Paris
  when `timeZone` is passed explicitly — always pass it. Cross-check both before matching an
  activity to a calendar slot; a naive UTC-vs-local mismatch is the most common source of
  mis-tagged "skipped" events.

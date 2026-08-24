# Calendar tagging & Strava labeling — recurring routine (3x/day)

Governs the ad hoc "review calendar events" + "label & document Strava
activities" scheduled task (distinct from the daily digest pipeline in
CLAUDE.md — this runs 3x/day and only touches Google Calendar event
titles/colors/descriptions and Strava activity names/descriptions, never
`state/latest.json`). Documented here so the convention stays consistent
across runs instead of being re-derived from scratch each time.

## Scope each run

1. Pull Strava activities for roughly the last 10-14 days (`strava_activities`,
   `start_date_local >=` a lookback window) and Google Calendar events over
   the same window through today.
2. Cross-reference: every Strava activity should have a corresponding Calendar
   event; every past (start time already elapsed) planned Calendar event
   should be reconciled against Strava.
3. **Idempotency**: an event whose description already contains
   `Strava #<activity_id>` for the matching activity is already tagged — skip
   it unless the underlying Strava data changed materially (e.g. a
   previously-missing activity now exists, or a commute flag was corrected).
   Never re-tag today's still-future planned session as skipped — only judge
   sessions whose scheduled end time has already passed.

## Calendar event title convention

Prefix (status marker) + activity-type emoji + description, e.g.:
`✅ done | 🏃 Run #29 — 7,04 km matin (Bois de Vincennes, suffer 51)`

Status prefixes:
- `✅ done` — planned session executed materially as planned (type/distance
  in the right ballpark).
- `✅ custom session done` — something was executed that day but diverged
  from the plan (different distance/type/timing) — activity happened, just
  not per spec.
- `⏭️ skipped` — no matching Strava activity found by review time, more than
  ~3-4h after the planned slot ended. Provisional: re-checked and corrected
  automatically on the next pass if an activity later appears.
- `❌ annulé (raison)` — deliberately cancelled ahead of time for a stated
  reason (heat protocol, illness, etc.), not just "no data yet".
- Unplanned/added activities (no prior Calendar event): create a new event,
  title `✅ done | <emoji> <description>`, and note in the description that
  it was "ajouté a posteriori suite à la revue Strava (routine 3x/jour)".

Activity-type emoji: 🏃 Run, 🚌 Trajet (commute), 🚴 Vélo (non-commute ride),
🏊 Baignade/Swim, 🥾 Hike/Walk, 🏋️ Workout — pick the closest match.

## Color convention (colorId)

**Every color choice is driven by `suffer_score`** of the underlying
activity, except the two non-execution states:

| State | colorId | Name |
|---|---|---|
| Skipped (no data yet, provisional) | 8 | Graphite (gray) |
| Cancelled deliberately | 11 | Tomato (red) |
| Executed, suffer 0-5 | 2 | Sage (pastel green) |
| Executed, suffer 6-10 | 10 | Basil (deep green) |
| Executed, suffer 11-25 | 5 | Banana (yellow) |
| Executed, suffer 26-60 | 4 | Flamingo (coral/pink) |
| Executed, suffer 61+ | 11 | Tomato (red) |

This gradient applies identically whether the title says `done` or
`custom session done` — status is conveyed by title text only; color always
encodes effort. Commutes rarely exceed suffer ~10 so in practice they land on
Sage or Basil.

## Commutes

Commute rides must appear on the Calendar even though they're not part of
the training plan — create an event if missing, same tagging/color scheme as
above. If `strava_activities.commute` looks wrong given the time-of-day/
distance (e.g. a home↔office-shaped ride not flagged as commute), correct
the flag via `update_strava_activity` and note the correction in the
Calendar event description.

## Timezone

`strava_activities.start_date` is UTC; `start_date_local` is already
Europe/Paris local time — use `start_date_local` directly, don't re-offset
it. When calling Calendar tools pass explicit `+02:00` (CEST, summer) /
`+01:00` (CET, winter) offsets or `timeZone: "Europe/Paris"` — never assume
UTC.

## Strava activity labeling (separate task, same run)

- **Name**: only rename if the current name is an unedited Strava default
  (e.g. "Morning Run", "Sortie en vélo électrique le soir", "Evening Ride").
  If it already looks hand-edited (custom title, run number, distance in the
  name), leave it untouched — this holds even for the description step
  below.
- **Description**: add one if none is set (`raw_data->>'description' IS
  NULL`). French, factual, public-safe: distance, duration, avg/max HR,
  elevation gain, suffer score, and — when relevant — a one-line note on
  deviation from the planned session (distance vs target, timing shift).
  Never include weight, body composition, fitness objectives/targets, medical
  info, or private-life details — those stay in the Calendar description and
  `state/latest.json`, not on Strava (semi-public platform).
  Always set/confirm the `commute` flag for commute rides.

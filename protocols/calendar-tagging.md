# Calendar tagging — Strava ↔ Google Calendar review (3x/day routine)

Reference for the recurring "review calendar events" + "label & document Strava
activities" task. Not part of the daily-digest 6-phase pipeline — this runs
independently, up to 3x/day, purely to keep Calendar and Strava in sync with
what actually happened.

## Timezone rule

Always match on `strava_activities.start_date_local` (already Paris local,
naive timestamp) against Calendar event times interpreted in `Europe/Paris`.
Never compare `start_date` (UTC) directly to a Calendar local time — that is
the recurring off-by-2h bug to avoid.

## Title prefixes

- `✅ done` — activity executed and matches the planned session (type/time/effort close enough).
- `🟢/🟡/🟠/🔴 custom done` — an activity was executed that day but differs from
  the plan (unplanned session, swapped discipline, different distance/time).
  The emoji color must match the suffer-score band below.
- `⏭️ skipped` — planned session, no matching Strava activity found at review
  time. Always gray regardless of anything else.
- `❌ annulé` — the planned session was explicitly invalidated (deload gate,
  readiness gate, injury) and won't be attempted at all, as opposed to simply
  "not done yet by review time".

## Color scale — driven by `suffer_score` (Google Calendar `colorId`)

Applies to every **executed** activity (`✅ done` and `🟢/🟡/🟠/🔴 custom done`).
Not executed → always Graphite regardless of any other factor.

| suffer_score        | colorId | Name      | Emoji |
|----------------------|---------|-----------|-------|
| < 20                 | 2       | Sage      | 🟢    |
| 20 – 39               | 5       | Banana    | 🟡    |
| 40 – 59               | 6       | Tangerine | 🟠    |
| ≥ 60                  | 11      | Tomato    | 🔴    |
| n/a — not executed    | 8       | Graphite  | (⏭️)  |
| n/a — cancelled       | 11      | Tomato    | (❌)  |

Commutes get the same suffer-based color as any other activity (they just
tend to land in the Sage band, suffer ~5-10).

## Retag notes

When flipping a session to `⏭️ skipped` because no Strava activity has landed
yet, prepend (not append) a short French note to the existing description:
date of the retag, time gap since the planned end, and that it will be
re-checked automatically. Keep the original plan body below a `---`
separator — never delete it, so the next pass can see what was actually
prescribed.

## Strava activity hygiene (name + description)

- Rename only if the current name is still a Strava/vendor default
  ("Morning Run", "Sortie en vélo électrique le soir", …). Leave any
  name that already looks edited, even if it wasn't edited by this routine.
- Add a description only if none is set. Keep it public-safe: distance,
  duration, HR, elevation, suffer score, and a one-line protocol/deviation
  note. Never put weight, medication, training objectives, or private-life
  details in a Strava description — that goes in the Calendar event
  description instead, which is private.
- Always set `commute: true` on identifiable home↔office e-bike legs, even
  when the default name was already replaced by a prior pass.

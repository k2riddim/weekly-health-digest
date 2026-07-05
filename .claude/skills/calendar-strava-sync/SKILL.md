---
name: calendar-strava-sync
description: Reconciles Google Calendar training events against actual Strava activity, tags status by color + title prefix (suffer-score-driven), adds unplanned/commute sessions, and labels/documents Strava activities. Runs each pipeline pass, not just once daily.
---

# Calendar ↔ Strava Sync

Two independent jobs, both idempotent (safe to re-run every pass without reprocessing already-tagged items).

## Job A — Reconcile Calendar against Strava

### Review window

Look back from `D` (yesterday, or today once an activity has actually landed) far enough to catch anything untouched — in practice: every Calendar training event in the last ~7–10 days whose `summary` does **not already start with** one of the status prefixes below. Already-prefixed events are considered processed; skip them unless a new Strava activity appears that changes the verdict (e.g. a day previously tagged `skipped` gets a late-synced activity).

### Matching

For each unprocessed past Calendar training event (type Run/Ride/EBikeRide session, weigh-ins and "Sur site" markers are not training events and are never touched):

1. Look for Strava activities on the same calendar date, matching sport family (Run ↔ Run/TrailRun, Ride ↔ Ride/EBikeRide/GravelRide).
2. **Match found, metrics broadly consistent with the plan** (duration/distance within ~20%, no explicit cap violated) → **done**.
3. **Match found, but materially different** (distance/duration deviates beyond plan tolerance, an explicit cap like "NE PAS DÉPASSER X km" was breached, or the activity landed on a different day than planned) → **custom session done**.
4. **No matching activity and the date has fully passed** → **skipped**.

### Status → title prefix + color

| Status | Title prefix | `colorId` |
|---|---|---|
| Done as planned | `✅ done \| ` | suffer-score band (below) |
| Custom session done (something happened, differs from plan) | `✅ custom session done \| ` | suffer-score band (below) |
| Skipped (nothing logged) | `⏭️ skipped \| ` | `8` (Graphite/gray) always |
| Pre-emptively cancelled (called off ahead of the date, e.g. by the training-planner on a heat/illness signal) | `❌ ANNULÉ — ` | `8` (Graphite/gray) |

Keep the rest of the original title after the prefix. Prepend a short factual note to the description (Strava id, distance/time/HR/suffer, one line on plan deviation) above a `---` separator, then keep the original planned-session description below it (label it `[Plan initial]`) so the rationale history isn't lost.

### Suffer-score → color band (for done / custom session done only)

Google Calendar's palette only offers two usable greens plus an escalation color — use suffer_score as the intensity axis:

| `suffer_score` | `colorId` | Meaning |
|---|---|---|
| `< 15` | `2` (Sage, pastel green) | easy / recovery-level effort |
| `15 – 39` | `6` (Tangerine) | moderate-to-hard effort |
| `>= 40` | `11` (Tomato) | very hard / outlier effort — flag for review |

Commute rides are almost always `< 15` → Sage. A skipped/cancelled event never gets a suffer-based color — it's always Graphite regardless, because no effort happened.

### Unplanned activities & commutes

If a Strava activity in the window has no corresponding Calendar event at all (not just unmatched-but-processed — genuinely no event that day for that type), **create** one:
- Title: `✅ done | 🏃/🚴/🚌 <short description> (non planifié)` — use 🚌 for commute rides, 🏃 for runs, 🚴 for other rides.
- Time: match the Strava activity's actual start/end time.
- Color: suffer-score band above.
- Description: `Strava #<activity_id>` + stats line, one line noting it wasn't on the plan.

Commute activities (`commute = true` in `strava_activities`, or renamed as such per Job B) must always have a Calendar entry — they represent real time/load even though they're not "training" in the structured-plan sense.

## Job B — Label & document Strava activities

Runs over the same window, independent of Job A's matching.

### B1 — Rename, only if the name is still Strava's auto-generated default

Strava auto-generates names like `Morning Run`, `Afternoon Ride`, `Evening Run`, or the French equivalents (`Course à pied le matin`, `Sortie vélo le soir`, `Sortie en vélo électrique le soir`, `Sortie gravel le matin`). These carry no specific information (no distance, no run/session number, no location, no protocol reference) — **rename** these to match the established convention, e.g. `Retour running — Run #N — X km Z2 (location, note)` for structured comeback runs, or a plain descriptive title for anything else.

If the name has already been edited by a prior pass or by hand (contains a run number, distance, location, or any custom text) — **leave it alone**, even when doing the description/commute updates below.

### B2 — Description (applies regardless of whether the name was touched)

Add a description **only if none is currently set** (`raw_data->>'description'` is null/empty). Include: Strava activity id, distance/duration/HR/suffer, and any protocol deviation (e.g. planned cap exceeded, session moved to a different day). Never include weight, body composition, fitness goals/targets, medical or symptom information, or other private-life details — those stay in the private digest/state files only.

### B3 — Commute tagging

Always set `commute = true` via `update_strava_activity` for any activity that is a home↔office trip (already `true` for most e-bike commutes synced from Strava's own detection, but fix it if Strava missed one — e.g. a manually-logged commute or a mislabeled Ride).

## Idempotency notes

- Job A: an event whose title already starts with `✅`, `⏭️`, or `❌` is treated as done unless new Strava data contradicts it.
- Job B: a name is only touched if it still matches the generic auto-generated pattern; a description is only added if empty. Never overwrite a human-authored description.

# Daily Health Digest

An autonomous daily health analysis system powered by Claude Code Routines. Every morning, Claude clones this repo, pulls fresh biometric data, checks the week's calendar for "sur site" blocks, replans the rolling 7-day training window, delivers a digest via Telegram, and commits everything as a reviewable PR.

## How the Routine works

The system executes a **6-phase pipeline** on every daily run:

| Phase | Name | What happens |
|-------|------|-------------|
| 0 | Recover state | Reads `state/latest.json`, `state/historical-peak.json`, and `protocols/thresholds.yaml` |
| 1 | Snapshot | Pulls last 7 days of data from all connectors; reads Google Calendar for today + 7 days ahead; identifies `no_train_days` (events containing "sur site") |
| 2 | Triage | Reassesses situational context, checks whether yesterday's planned session executed, identifies any signals, checks deviation thresholds |
| 3 | Deep dive | Only when warranted — tests hypotheses with SQL across multiple tables, loads research modules |
| 4 | Replan 7d | Builds the rolling 7-day plan; reconciles with existing Calendar events (leave / update / delete / create); respects `no_train_days` |
| 5 | Delta | Computes day-over-day changes, plan adherence, distance from historical peak |
| 6 | Persist + deliver | Commits artifacts on a `claude/day-YYYY-MM-DD` branch, opens a PR, sends a Telegram message |

### Calendar-aware training

Before scheduling any training session, the routine reads the next 7 days of Google Calendar events. Any day whose event summary or description contains **"sur site"** (case-insensitive) is treated as a day Benjamin is on-site at work and cannot train — no session is scheduled, and any existing Claude-created training event on that day is deleted.

### Rolling replan, minimal churn

The plan is rebuilt every day, but Calendar changes are minimized:
- Existing training events that still fit → untouched
- Existing events that no longer fit (readiness drop, newly-discovered "sur site") → updated or deleted
- New slots that open up → new events created

This keeps Benjamin's calendar stable while adapting to fresh data.

### Where state lives

- **`state/latest.json`** — canonical current state, overwritten each day
- **`state/historical-peak.json`** — best sustained training period, updated only if beaten
- **`state/history/YYYY-MM-DD.json`** — append-only daily archive
- **`digests/YYYY-MM-DD.md`** — human-readable daily reports
- **`investigations/`** — standalone deep-dive analyses when signals warrant extended study

### What gets committed daily

Each run creates a branch `claude/day-YYYY-MM-DD` containing:
- Updated `state/latest.json`
- Archived `state/history/YYYY-MM-DD.json`
- Human-readable `digests/YYYY-MM-DD.md`
- Any investigation files under `investigations/`
- Updated `state/historical-peak.json` (only if a new peak is reached)

## Setup: creating the Routine

1. Go to [claude.ai/code/routines](https://claude.ai/code/routines)
2. Click **New routine**
3. Configure:
   - **Name**: `Daily Health Digest`
   - **Prompt**:
     ```
     Execute the daily health digest as specified in CLAUDE.md. Commit all artifacts on a `claude/day-YYYY-MM-DD` branch and open a PR. Send a Telegram summary to Benjamin. Update Google Calendar training events for the next 7 days, respecting any "sur site" blocks.
     ```
   - **Repository**: `weekly-health-digest`
   - **Connectors**: enable all four:
     - `biometrics` (mcp.chrz.dev)
     - `baby mcp` (baby.chrz.dev)
     - `Google Calendar`
     - `telegram`
   - **Schedule**: Daily, e.g. 06:30 Europe/Paris (so Benjamin gets the digest before morning sessions start)
4. Click **Save**

The Routine clones this repo's default branch (main) at the start of every run. `CLAUDE.md` is auto-loaded as the routine prompt.

## Reviewing daily runs

1. **Check Telegram** — a compact French summary arrives on your phone: headline, today's session (or rest / "sur site" note), readiness metrics, top recommendation, PR link.
2. **Review the PR** — each day's full analysis lands as a pull request on the `claude/day-YYYY-MM-DD` branch.
   - The PR body is auto-populated from `.github/pull_request_template.md`.
   - Review the delta summary, plan adherence, recommendations, and training plan.
3. **Merge or close** — merge to archive the day's state on main; close to discard.
4. **Calendar events** — training sessions appear in Google Calendar in French.
   - To reject a planned session: delete the calendar event (the next day's run will see it's gone and won't recreate it unless conditions change).
   - To block a day from training: add an event with "sur site" in the title or description. The next run will remove any training event scheduled for that day.
   - Each event includes a tired-day fallback in the description.

## Evolving the system

### Add a research module

Create a new `.md` file in `.claude/skills/research-modules/` with the topic brief. Reference it in `CLAUDE.md` under the "Research modules" section so the routine knows when to load it.

### Reset historical peak

After a new fitness test or if the stored peak no longer represents a meaningful target:
1. Edit `state/historical-peak.json` directly, or
2. Delete it and re-run the bootstrap computation from a Claude Code session

### Tune thresholds

Edit `protocols/thresholds.yaml`. All population-level invariants (ACWR band, ramp cap, sigma cutoffs, deload rules) are read from this file at the start of every run. Changes take effect on the next scheduled execution.

### Update HR zones

Edit `protocols/zones.md` after a field test (30-min time trial, graded exercise test, or similar). The routine references these zones when prescribing training sessions.

### Change the "sur site" keyword

The `sur site` match is defined in the Phase 1 calendar section of `CLAUDE.md` and in the training-planner skill. Update both locations (case-insensitive substring match) if the convention changes.

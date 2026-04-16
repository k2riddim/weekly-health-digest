# Weekly Health Digest

An autonomous weekly health analysis system powered by Claude Code Routines. Every Sunday at 20:00 (Paris time), Claude clones this repo, pulls a week of biometric data from connected sources, analyses trends, plans next week's training, schedules calendar events, and delivers a digest to your inbox — all committed as a reviewable PR.

## How the Routine works

The system executes a **6-phase pipeline** on every run:

| Phase | Name | What happens |
|-------|------|-------------|
| 0 | Recover state | Reads `state/latest.json`, `state/historical-peak.json`, and `protocols/thresholds.yaml` |
| 1 | Snapshot | Pulls raw data from all connectors (Strava, Garmin, Withings, nutrition, labs, cognitive, cohabitant) |
| 2 | Triage | Reassesses situational context, identifies top signals, checks deviation thresholds |
| 3 | Deep dive | Tests hypotheses with SQL queries across multiple tables, loads research modules |
| 4 | Training plan | Builds 3–5 sessions for W+1 respecting ACWR band, ramp cap, and readiness; creates Google Calendar events |
| 5 | Delta | Computes week-over-week changes, tracks recommendation follow-through, measures distance from historical peak |
| 6 | Persist + deliver | Commits all artifacts on a `claude/week-YYYY-WW` branch, opens a PR, creates a Gmail draft |

### Where state lives

- **`state/latest.json`** — canonical current state, overwritten each week
- **`state/historical-peak.json`** — best sustained training period, updated only if beaten
- **`state/history/YYYY-WW.json`** — append-only weekly archive
- **`digests/YYYY-WW.md`** — human-readable weekly reports
- **`investigations/`** — standalone deep-dive analyses when signals warrant extended study

### What gets committed weekly

Each run creates a branch `claude/week-YYYY-WW` containing:
- Updated `state/latest.json`
- Archived `state/history/YYYY-WW.json`
- Human-readable `digests/YYYY-WW.md`
- Any investigation files under `investigations/`
- Updated `state/historical-peak.json` (only if a new peak is reached)

## Setup: creating the Routine

1. Go to [claude.ai/code/routines](https://claude.ai/code/routines)
2. Click **New routine**
3. Configure:
   - **Name**: `Weekly Health Digest`
   - **Prompt**:
     ```
     Execute the weekly health digest as specified in CLAUDE.md. Commit all artifacts on a `claude/week-YYYY-WW` branch and open a PR. Create a Gmail draft for mobile reading. Create Google Calendar events for W+1.
     ```
   - **Repository**: `weekly-health-digest`
   - **Connectors**: enable all four:
     - `biometrics` (mcp.chrz.dev)
     - `baby mcp` (baby.chrz.dev)
     - `Gmail`
     - `Google Calendar`
   - **Schedule**: Weekly, Sunday 20:00 Europe/Paris
4. Click **Save**

The Routine clones this repo's default branch (main) at the start of every run. `CLAUDE.md` is auto-loaded as the routine prompt.

## Reviewing weekly runs

1. **Check your email** — a Gmail draft with subject `[HEALTH-DIGEST] Week YYYY-WW` is created for mobile reading
2. **Review the PR** — each week's analysis lands as a pull request on the `claude/week-YYYY-WW` branch
   - The PR body is auto-populated from `.github/pull_request_template.md`
   - Review the delta summary, recommendations, and training plan
3. **Merge or close** — merge to archive the week's state on main; close to discard
4. **Calendar events** — training sessions are created in Google Calendar in French
   - To reject a planned session: simply delete the calendar event
   - Each event includes a tired-day fallback in the description

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

### Add an investigation template

The investigation skill (`.claude/skills/investigation/SKILL.md`) handles scaffolding automatically. To trigger one manually, note the pattern in the skill file and create the directory structure under `investigations/`.

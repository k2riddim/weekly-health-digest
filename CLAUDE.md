# Daily Health Digest — Routine Prompt

Auto-loaded by Claude Code on every run of the daily-digest Routine. Contains the complete self-contained logic for one daily run.

## Context

Benjamin is a male endurance athlete based in Paris with longitudinal data across Strava, Garmin, Withings, labs, chess, nutrition, and cohabitant metrics. Everything about his current situation must be re-discovered from data each day. This prompt contains no hardcoded numbers, no life-phase assumptions, and no training templates — they evolve with him. With the exception of the super important  return to running protocol you must always check and apply if the user is returning to running.

## Target

Intelligent progression toward the best sustainable fitness Benjamin has historically demonstrated (`state/historical-peak.json`), respecting current-life constraints inferred daily. The rolling 7-day training plan is **replanned every day** based on: yesterday's execution, today's readiness, upcoming calendar constraints, and trailing load trajectory. Never prescribe a ramp that raises acute 7-day load >10% week-over-week. No hero weeks.

## Language

Analytical report in **English**. Calendar event titles and descriptions, Telegram message body in **French**.

## Connectors and data

- `biometrics` MCP (`mcp.chrz.dev`) — full biometric database with ~60 biomarkers, 923+ days Garmin, 998+ Withings, 2,364+ Strava activities, chess, nutrition. Use `biometrics:query` for read-only SQL. Introspect unfamiliar tables via `information_schema.columns` before querying.
- `baby mcp` (`baby.chrz.dev`) — cohabitant sleep + feeding + vitals. Tables: `owlet_vitals`, `owlet_sleep_sessions`, `may_feedings`, `may_sleep`, `may_diapers`, `may_weights`, `may_heights`, `may_cranial`.
- `Google Calendar` — for reading existing events (critical for training-day constraints) and creating/updating training events. **An event whose summary or description contains "sur site" means Benjamin is working on-site that day and cannot train.**
- `Telegram` — for delivering the daily digest to mobile.

## Memory

- **Primary state**: `state/latest.json` (committed each day). Read at the start of Phase 0, overwritten at the end of Phase 6.
- **Historical peak**: `state/historical-peak.json`. Stable. Only update if the current 28-day chronic load exceeds the stored peak — then write a new version.
- **Archive**: `state/history/YYYY-MM-DD.json` — append-only copy of each day's state.
- **Human digest**: `digests/YYYY-MM-DD.md`.
- **Phone delivery**: Telegram message, body = compact version of the daily digest (French).

## Thresholds

Load `protocols/thresholds.yaml` at the start of every run. All population-level invariants (ACWR band, ramp cap, sigma cutoffs, deload multiplier, illness triggers) come from there. Never hardcode them in this prompt.

## Research modules

When a signal surfaces that warrants deeper interpretation, `read_file` the matching module in `.claude/skills/research-modules/` before writing the recommendation:
- HRV anomalies → `hrv-interpretation.md`
- Load / readiness questions → `training-load-theory.md`
- Lab abnormalities → `labs-optimal-ranges.md`
- Sleep disruption → `sleep-fragmentation.md`
- Post-layoff rebuild → `endurance-rebuild.md`

## EXECUTION — 6 mandatory phases

Complete all 6. Each requires real tool calls, not assumptions. Between phases, state your hypotheses explicitly before the next query.

### Phase 0 — Recover previous state

1. `cat state/latest.json` → parse into `LAST_STATE`.
2. `cat state/historical-peak.json` → parse into `HISTORICAL_PEAK`.
3. `cat protocols/thresholds.yaml` → parse into `T`.
4. If `LAST_STATE.bootstrap === true`, note that Phase 5 is the first real delta (compare today to the bootstrap snapshot, labelled as such).

### Phase 1 — Snapshot today + rolling context (broad pass)

Define `D` = yesterday (most recent complete day of data). Define the **context window** = last 7 days ending at `D`. Define the **planning horizon** = 7 days starting today.

Pull raw numbers via `biometrics:query`, `baby mcp:query`, and `Google Calendar`. Do not interpret yet.

Minimum coverage:
- **Training executed** — `strava_activities` where `start_date >= D - 7 days`. Look specifically at whether yesterday's planned session (from `LAST_STATE.plan_7d_ahead`) was executed.
- **Load & readiness** — `training_load_daily` for `D - 14` through `D` (ACWR continuity). `readiness_daily` for `D - 7` through `D`.
- **Wearable** — `garmin_health` for `D - 7` through `D` (focus on today/yesterday).
- **Body composition** — `withings_measurements` last 28d, filter `weight_kg > T.data_quality.weight_kg_floor`.
- **Nutrition** — `oh_daily_nutrition_summary` for `D - 7` through `D`.
- **Cognitive** — `cognitive_sessions` for `D - 7` through `D`.
- **Labs** — `oh_observations` `effective_datetime >= D - 30` (only surface if new data landed since `LAST_STATE.as_of_date`).
- **Cohabitant** — `baby mcp:query` for night wakings / sleep fragmentation for `D - 7` through `D`.
- **Calendar — upcoming 7 days** — list all events via `Google Calendar` for today through `today + 7`. Extract `no_train_days` = any date whose event summary or description matches `sur site` (case-insensitive). These are blocked for training.
- **Calendar — yesterday** — to cross-check: did a "sur site" event yesterday prevent training, or did Benjamin skip for another reason?

### Phase 2 — Triage + situational reassessment

Produce an internal triage:
1. **Reassess `situational_context`** inherited from `LAST_STATE`. Does the last 24–48h contradict it? State the signals that update it. Daily updates are incremental — the context rarely flips, but drifts.
2. **Plan adherence check** — did yesterday's planned session (if any) execute? Was it skipped for a "sur site" event (legitimate), for readiness reasons (conditional), or silently (flag)?
3. **Top 1–3 signals worth deep-diving**. For each: competing hypotheses ranked, tables to query. On a quiet day, zero deep-dives is the correct answer.
4. If nothing is abnormal → explicit "maintenance — stay the course".

Deep-dive triggers (from `T.deviation_thresholds`):
- Any marker >`T.deviation_thresholds.personal_sigma_dive`σ from its personal 90-day baseline **today**
- ACWR outside `[T.training.acwr_lower_bound, T.training.acwr_upper_bound]`
- HRV 7d avg below `hrv_baseline_low` for ≥`T.deviation_thresholds.hrv_below_baseline_days` consecutive days
- Sleep hours <6h on ≥`T.deviation_thresholds.sleep_low_nights_per_week` nights across the last 7, or sleep score drop >`T.deviation_thresholds.sleep_score_drop_pct` for ≥2 consecutive nights
- Skin temperature deviation >`T.deviation_thresholds.skin_temp_spike_celsius`°C for ≥2 consecutive nights
- Weight trend reversing sign over `T.deviation_thresholds.weight_trend_reversal_window_days` days
- Any new lab value outside reference range

### Phase 3 — Deep dive (only when warranted)

For each top signal from Phase 2, run the SQL that tests the hypotheses. Keep going until you have a falsifiable answer or are explicitly data-limited.

**Rules:**
- **Hypothesis before query.** State expected result; name what would falsify it.
- **Every claim touches ≥2 tables.**
- **Compare against personal baseline**, not just population reference ranges.
- Load the relevant research module (`.claude/skills/research-modules/*.md`) before writing the interpretive paragraph.
- If the topic needs new clinical info, use `web_search`.

One data-anchored paragraph per domain dove into. On days with no signals, skip this phase entirely and state so.

**Spawn an investigation** (via `.claude/skills/investigation`) if the signal is: (a) strong enough to warrant a standalone study, (b) requires chart-based analysis, (c) is novel vs prior days. The investigation skill handles file scaffolding under `investigations/YYYY-MM-DD-<slug>/`.

### Phase 4 — Replan the rolling 7-day training window

Invoke `.claude/skills/training-planner`. Inputs: `LAST_STATE`, today's load/readiness, `HISTORICAL_PEAK`, `situational_context`, `T.training`, `T.session_planning`, the `no_train_days` list from Phase 1, the list of existing Calendar training events within the horizon.

The planner produces a **full rolling 7-day plan** (today → today + 6). Because this runs daily:
- If an existing Calendar training event still fits the updated plan → leave it.
- If it no longer fits (e.g., readiness has dropped, or a newly-discovered "sur site" event blocks the day) → **update or delete** the Calendar event.
- If a new slot opens up → create a new Calendar event.

Planner constraints:
- Next 7-day projected acute load ≤ `T.training.weekly_acute_ramp_cap` × trailing acute
- If acute/chronic < `T.training.return_from_layoff_acute_to_chronic_threshold` → rebuild mode, bias aerobic
- Red flags → deload today to `T.training.deload_multiplier` × normal
- Illness signals → rest + light aerobic only
- Projected ACWR in `[T.training.acwr_lower_bound, T.training.acwr_upper_bound]`
- **Respect `no_train_days`**: never schedule a session on a "sur site" day
- Respect `T.session_planning.min_sessions_per_week` and `max_sessions_per_week` across the rolling window, adjusted for blocked days

Each new or updated event must have: French title, duration, target HR zone, target load, one-line rationale, tired-day fallback.

### Phase 5 — Delta vs yesterday (and rolling 7d)

Compute using `scripts/compute_delta.py`:
- **Plan adherence** — was yesterday's planned session executed? Was any unplanned activity logged?
- **Recommendation follow-through** — pass/fail/unmeasurable per `LAST_STATE.recommendations`
- **Markers-to-watch resolution** — resolved/worsened/flat since yesterday
- **Rolling 7d vs previous rolling 7d** — shift in acute_load_7d, HRV 7d avg, RHR 7d avg, sleep hours 7d avg
- **Distance-from-peak** — current chronic_load_28d as % of `HISTORICAL_PEAK.chronic_load_28d_avg`, day-over-day delta in pp
- **Situational context drift**

If today's chronic_load_28d exceeds `HISTORICAL_PEAK.chronic_load_28d_avg` → update `state/historical-peak.json` with new values.

### Phase 6 — Persist + deliver

**Commit artifacts on branch `claude/day-YYYY-MM-DD`:**
1. Write `state/latest.json` (full new state, schema below).
2. Copy that state to `state/history/YYYY-MM-DD.json`.
3. Write the human digest to `digests/YYYY-MM-DD.md` (format below).
4. If historical peak changed, rewrite `state/historical-peak.json`.
5. If an investigation was spawned, its files are already under `investigations/`.
6. `git add` all; `git commit -m "Day YYYY-MM-DD: <one-line headline>"`; push to `claude/day-YYYY-MM-DD`.
7. Open a PR via GitHub CLI or equivalent, using `.github/pull_request_template.md`.

**Telegram delivery** via the `telegram` MCP connector. Send a compact French message containing:
- Headline (1 line)
- Today's planned session (or rest / "sur site" block)
- Key readiness metrics (HRV, RHR, sleep)
- Top recommendation (P0)
- PR link

The full digest stays in the repo; Telegram is a push notification summary.

## Digest format

```markdown
# Daily Health Digest — <YYYY-MM-DD> (<weekday>)

## 1. Headline
One sentence: readiness today, load trajectory, dominant situational factor, today's training status (planned / rest / blocked).

## 2. Delta vs yesterday
- Yesterday's plan: [executed / skipped — reason / no session scheduled]
- Rolling 7d acute load: A → B (±Δ)
- Rolling 7d HRV avg: A → B (±Δ)
- Rolling 7d sleep: A → B (±Δ)
- Distance from peak: P% (±Δpp vs yesterday)
- Situational context: [unchanged / updated because ...]

## 3. Today's readout
### Readiness snapshot
### Training & load (trailing 7d)
### Sleep & recovery (last night + trend)
### Body composition (if new reading today)
### Nutrition (if logged)
### Cognitive (if session today)
### Labs (only if new data)
### Cohabitant signals (only if they materially drove tonight's recovery)

## 4. Top 1–3 prioritised recommendations
1. **[P0]** action — rationale, evidence class [RCT | guideline | consensus | preliminary], measurable outcome for tomorrow/this week
2. **[P1]** ...
3. **[P2]** ...

## 5. Rolling 7-day training plan
- Target acute load: N
- Blocked days (sur site): [list]
- Sessions (Google Calendar):
  1. <date> <weekday> <time> — <French title> — <zone/load> — [status: existing / created / updated / deleted]
  ...
- Deload trigger: ...

## 6. GP conversation seeds (only if relevant)
Natural observations Benjamin could mention at his next visit, not test requests.

## 7. Investigations opened today
(Link to `investigations/YYYY-MM-DD-<slug>/` directories. Omit section if none.)
```

## state/latest.json schema

```json
{
  "as_of_date": "YYYY-MM-DD",
  "bootstrap": false,
  "situational_context": "free-text, re-evaluated today",
  "acute_load_7d": N,
  "chronic_load_28d": N,
  "distance_from_peak_pct": N,
  "hrv_7d_avg": N,
  "rhr_7d_avg": N,
  "sleep_hours_7d_avg": N,
  "weight_kg_7d_avg": N,
  "last_session": {
    "date": "YYYY-MM-DD",
    "type": "...",
    "duration_min": N,
    "training_load": N
  },
  "plan_7d_ahead": [
    {"date": "YYYY-MM-DD", "day": "...", "time": "...", "type": "...", "duration_min": N, "target_load": N, "calendar_event_id": "...", "status": "planned|blocked|rest"}
  ],
  "no_train_days": ["YYYY-MM-DD"],
  "recommendations": [
    {"priority": "P0", "text": "...", "measurable": "...", "evidence_class": "..."}
  ],
  "markers_to_watch": [
    {"marker": "...", "threshold": "...", "reason": "..."}
  ],
  "investigations_opened": ["YYYY-MM-DD-<slug>"],
  "pr_url": "https://github.com/..."
}
```

## Standing rules

1. **Think hard.** Never write a recommendation without querying its supporting data first.
2. **Evidence class on every recommendation.**
3. **Never diagnose.** Use "consistent with", "warrants discussion with GP".
4. **GP diplomacy.** Frame test suggestions as observations Benjamin could naturally mention.
5. **Unit discipline.** km, min, kg, bpm; training load unitless.
6. **State data limitations explicitly.** Do not fabricate.
7. **Abort check.** If core tables have no data for the last `T.data_quality.abort_if_no_data_days` days, note pipeline issue at top and produce qualitative sections from what exists.
8. **Bootstrap path.** If `LAST_STATE` is missing or explicitly marked `bootstrap: true`, Phase 5 says so; otherwise proceed normally.
9. **Calendar authority.** Never schedule training on a `no_train_days` date. Always re-read Calendar at Phase 1 — a "sur site" event added since yesterday overrides any existing training event for that day.
10. **Daily cadence discipline.** Replanning is cumulative, not from scratch — preserve upcoming events that still fit; only touch what must change. Reducing event churn keeps Benjamin's calendar stable.

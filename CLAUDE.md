# Weekly Health Digest — Routine Prompt

Auto-loaded by Claude Code on every run of the weekly-digest Routine. Contains the complete self-contained logic for one weekly run.

## Context

Benjamin is a male endurance athlete based in Paris with longitudinal data across Strava, Garmin, Withings, labs, chess, nutrition, and cohabitant metrics. Everything about his current situation must be re-discovered from data each week. This prompt contains no hardcoded numbers, no life-phase assumptions, and no training templates — they evolve with him.

## Target

Intelligent progression toward the best sustainable fitness Benjamin has historically demonstrated (`state/historical-peak.json`), respecting current-life constraints inferred weekly. Never prescribe a ramp that raises acute 7-day load >10% week-over-week. No hero weeks.

## Language

Analytical report in **English**. Calendar event titles and descriptions in **French**.

## Connectors and data

- `biometrics` MCP (`mcp.chrz.dev`) — full biometric database with ~60 biomarkers, 923+ days Garmin, 998+ Withings, 2,364+ Strava activities, chess, nutrition. Use `biometrics:query` for read-only SQL. Introspect unfamiliar tables via `information_schema.columns` before querying.
- `baby mcp` (`baby.chrz.dev`) — cohabitant sleep + feeding + vitals. Tables: `owlet_vitals`, `owlet_sleep_sessions`, `may_feedings`, `may_sleep`, `may_diapers`, `may_weights`, `may_heights`, `may_cranial`.
- `Gmail` — for creating the digest draft.
- `Google Calendar` — for reading existing W+1 events and creating new ones.

## Memory

- **Primary state**: `state/latest.json` (committed each week). Read at the start of Phase 0, overwritten at the end of Phase 6.
- **Historical peak**: `state/historical-peak.json`. Stable. Only update if this week's chronic_load_28d avg exceeds the stored peak — then write a new version.
- **Archive**: `state/history/YYYY-WW.json` — append-only copy of each week's state.
- **Human digest**: `digests/YYYY-WW.md`.
- **Phone delivery**: Gmail draft with subject `[HEALTH-DIGEST] Week YYYY-WW`, body = the markdown digest.

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
4. If `LAST_STATE.bootstrap === true`, note that Phase 5 is the first real delta (compare this week to the bootstrap snapshot, labelled as such).

### Phase 1 — Snapshot the week (broad pass)

Define `W` = ISO week ending yesterday. Pull raw numbers via `biometrics:query` and `baby mcp:query`. Do not interpret yet.

Minimum coverage:
- **Training executed** — `strava_activities` in W
- **Load & readiness** — `training_load_daily` (W + prior 14d for ACWR), `readiness_daily` (W)
- **Wearable** — `garmin_health` (W)
- **Body composition** — `withings_measurements` last 28d, filter `weight_kg > T.data_quality.weight_kg_floor`
- **Nutrition** — `oh_daily_nutrition_summary` for W (introspect columns first if unsure)
- **Cognitive** — `cognitive_sessions` for W
- **Labs** — `oh_observations` `effective_datetime >= W_start - 30` (only surface if new data landed)
- **Cohabitant** — `baby mcp:query` for night wakings / sleep fragmentation in W

### Phase 2 — Triage + situational reassessment

Produce an internal triage:
1. **Reassess `situational_context`** inherited from `LAST_STATE`. Does this week's data contradict it? State the signals that update it.
2. **Top 3 signals worth deep-diving**. For each: competing hypotheses ranked, tables to query.
3. If nothing is abnormal → explicit "maintenance mode".

Deep-dive triggers (from `T.deviation_thresholds`):
- Any marker >`T.deviation_thresholds.personal_sigma_dive`σ from its personal 90-day baseline
- ACWR outside `[T.training.acwr_lower_bound, T.training.acwr_upper_bound]`
- HRV 7d avg below `hrv_baseline_low` for ≥`T.deviation_thresholds.hrv_below_baseline_days` consecutive days
- Sleep hours <6h on ≥`T.deviation_thresholds.sleep_low_nights_per_week` nights, or sleep score drop >`T.deviation_thresholds.sleep_score_drop_pct` for ≥2 consecutive nights
- Skin temperature deviation >`T.deviation_thresholds.skin_temp_spike_celsius`°C for ≥2 consecutive nights
- Weight trend reversing sign over `T.deviation_thresholds.weight_trend_reversal_window_days` days
- Any new lab value outside reference range

### Phase 3 — Deep dive

For each top signal, run the SQL that tests the hypotheses. Keep going until you have a falsifiable answer or are explicitly data-limited.

**Rules:**
- **Hypothesis before query.** State expected result; name what would falsify it.
- **Every claim touches ≥2 tables.**
- **Compare against personal baseline**, not just population reference ranges.
- Load the relevant research module (`.claude/skills/research-modules/*.md`) before writing the interpretive paragraph.
- If the topic needs new clinical info, use `web_search`.

One data-anchored paragraph per domain dove into.

**Spawn an investigation** (via `.claude/skills/investigation`) if the signal is: (a) strong enough to warrant a standalone study, (b) requires chart-based analysis, (c) is novel vs prior weeks. The investigation skill handles file scaffolding under `investigations/YYYY-WW-<slug>/`.

### Phase 4 — Build W+1 training plan

Invoke `.claude/skills/training-planner`. Inputs: `LAST_STATE`, this week's load/readiness, `HISTORICAL_PEAK`, `situational_context`, `T.training`, `T.session_planning`.

Planner outputs 3–5 session specs respecting:
- Next week acute load ≤ this week acute × `T.training.weekly_acute_ramp_cap`
- If acute/chronic < `T.training.return_from_layoff_acute_to_chronic_threshold` → rebuild mode, bias aerobic
- Red flags → deload to `T.training.deload_multiplier` × this week acute
- Illness signals → rest + light aerobic only
- Projected ACWR in `[T.training.acwr_lower_bound, T.training.acwr_upper_bound]`

Before creating events, call `Google Calendar:gcal_list_events` for W+1 to avoid conflicts. Each event: French title, duration, target HR zone, target load, one-line rationale, tired-day fallback.

### Phase 5 — Delta vs last week

Compute using `scripts/compute_delta.py`:
- **Completion rate** of last week's planned sessions (fuzzy match date + activity_type + duration ±25%)
- **Recommendation follow-through** — pass/fail/unmeasurable per prior recommendation
- **Markers-to-watch resolution** — resolved/worsened/flat
- **Distance-from-peak** — current chronic_load_28d as % of `HISTORICAL_PEAK.chronic_load_28d_avg`, with WoW delta in pp
- **Situational context drift**

If this week's chronic_load_28d_avg exceeds `HISTORICAL_PEAK.chronic_load_28d_avg` → update `state/historical-peak.json` with new values.

### Phase 6 — Persist + deliver

**Commit artifacts on branch `claude/week-YYYY-WW`:**
1. Write `state/latest.json` (full new state, schema below).
2. Copy that state to `state/history/YYYY-WW.json`.
3. Write the human digest to `digests/YYYY-WW.md` (format below).
4. If historical peak changed, rewrite `state/historical-peak.json`.
5. If an investigation was spawned, its files are already under `investigations/`.
6. `git add` all; `git commit -m "Week YYYY-WW: <one-line headline>"`; push to `claude/week-YYYY-WW`.
7. Open a PR via GitHub CLI or equivalent, using `.github/pull_request_template.md`.

**Gmail draft** for mobile reading: subject `[HEALTH-DIGEST] Week YYYY-WW`, body = the markdown digest.

## Digest format

```markdown
# Weekly Health Digest — Week <ISO-week> (<start> → <end>)

## 1. Headline
One sentence: load trajectory, recovery status, dominant situational factor.

## 2. Delta vs last week
- Completed: X/Y scheduled sessions
- Chronic load 28d: A → B (±Δ), % of historical peak: P% (WoW ±Δpp)
- Markers moved: ...
- Markers flat: ...
- Situational context: [unchanged / updated because ...]

## 3. Domain readout
### Training & load
### Sleep & recovery
### Body composition
### Nutrition
### Cognitive
### Labs (only if new data)
### Cohabitant signals (only if they materially drove this week's patterns)

## 4. Top 3 prioritised recommendations
1. **[P0]** action — rationale, evidence class [RCT | guideline | consensus | preliminary], measurable outcome for next week
2. **[P1]** ...
3. **[P2]** ...

## 5. W+1 training plan
- Target acute load: N
- Sessions (created in Google Calendar):
  1. <day> <time> — <title> — <zone/load>
  ...
- Deload trigger: ...

## 6. GP conversation seeds (only if relevant)
Natural observations Benjamin could mention at his next visit, not test requests.

## 7. Investigations opened this week
(Link to `investigations/YYYY-WW-<slug>/` directories. Omit section if none.)
```

## state/latest.json schema

```json
{
  "week_ending": "YYYY-MM-DD",
  "bootstrap": false,
  "situational_context": "free-text, re-evaluated this week",
  "acute_load_7d": N,
  "chronic_load_28d": N,
  "distance_from_peak_pct": N,
  "hrv_7d_avg": N,
  "rhr_7d_avg": N,
  "sleep_hours_7d_avg": N,
  "weight_kg_7d_avg": N,
  "sessions_completed": N,
  "sessions_scheduled_next_week": [
    {"day": "...", "time": "...", "type": "...", "duration_min": N, "target_load": N}
  ],
  "recommendations": [
    {"priority": "P0", "text": "...", "measurable": "...", "evidence_class": "..."}
  ],
  "markers_to_watch": [
    {"marker": "...", "threshold": "...", "reason": "..."}
  ],
  "investigations_opened": ["YYYY-WW-<slug>"],
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

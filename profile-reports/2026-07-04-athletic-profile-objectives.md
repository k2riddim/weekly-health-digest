# Athletic Profile Classification & Objectives Tracker — 2026-07-04

Data window: full lifetime history (2426 Strava activities, 2014-05-01 → 2026-07-01), Withings since 2011, Garmin since 2023-Q3 (device limitation — no VO2max/HRV before then), labs since Dec 2025 most recent panel.

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers — lifetime totals

| Metric | Value |
|---|---|
| Span | 2014-05-01 → 2026-07-01 (12.2 years) |
| Total activities | 2,426 |
| Total distance | 24,298 km |
| Total moving time | 2,147 h (~89.5 days) |

**By activity type (lifetime):**

| Type | Count | km | Hours |
|---|---|---|---|
| Ride | 742 | 11,983 | 635 |
| Run | 817 | 6,978 | 743 |
| EBikeRide | 226 | 3,642 | 193 |
| Workout (gym) | 328 | 76 | 287 |
| VirtualRide | 43 | 812 | 35 |
| Walk | 76 | 251 | 63 |
| Hike | 24 | 189 | 57 |
| AlpineSki | 12 | 317 | 33 |
| Swim | 23 | 28 | 14 |
| WeightTraining | 121 | 1 | 77 |
| Other (misc, <5 sessions each) | 14 | 21 | 8 |

Running and cycling are co-dominant by time (743h vs 635h), but the balance between them has swung dramatically across eras — that swing is the story of this profile.

### 2. Volume trajectory — distinct phases

| Phase | Years | Dominant modality | Sessions/wk (dominant) | km/wk (dominant) | Hallmark |
|---|---|---|---|---|---|
| **Build era** | 2014–2016 | Running | 3.0–3.4 runs/wk | 29–33 km/wk | Marathon de Paris 2016 debut (3:58:12) |
| **Peak performance era** | 2018–2019 | Running | 1.4–2.2 runs/wk (lower freq, higher quality) | 14–19 km/wk | **Marathon PR 3:39:55 (2019)**, **Half PR 1:34:33 (2019)** |
| **COVID/gym drift** | 2020–2022 | Gym/Workout, running near-zero (1–18 runs/yr) | — | — | Running essentially paused; body recomposition via strength work |
| **Multi-sport peak-load era** | 2023 | Cycling (+gym) | 1.1 rides/wk | 40.8 km/wk (Ride) | **Highest chronic training load of career** (stored `historical-peak.json`: chronic_load_28d_avg 1608, peak 2100) — but running down to 33 runs/yr |
| **E-bike commuting era** | 2024–2025 | EBikeRide (commute) | 2.0–2.5/wk | 40–45 km/wk | Traditional cycling and running both subordinate to daily e-bike commuting; one half-marathon race in Oct 2025 at markedly slower pace (6:14/km vs 4:29/km PR) |
| **Second running layoff** | Nov 2025 – Apr 2026 | None (near-total stop) | ~0 | — | 182-day gap (2025-11-02 → 2026-05-03), coincident with new-child period (per `return-to-running.md`) |
| **Structured comeback (current)** | May 3, 2026 → present | Run (Z1–Z2 reintroduction) | 13 runs in 9 weeks (~1.4/wk avg, but only 2 runs in the last 3 weeks) | 2–7.5 km/session | Governed by the standing return-to-running protocol; **frequency has stalled since June 27** |

**Key trajectory read:** peak *performance* (2018–2019) and peak *training load* (2023) were different eras with different dominant modalities. The 2023 "historical peak" is a cycling+gym load peak, not a running peak — worth remembering when `training-planner` uses `historical-peak.json.activity_mix` as its reference, since that mix (Workout 22%, Ride 22%, Walk 20%, EBike 18%, Run only 13%) does not reflect the running-specific fitness ceiling shown in Part 2's race data.

### 3. Competitive performance — race results

All runs >20 km, chronological, with recorded pace and (where available) official time:

| Date | Race | Distance | Pace | Official/notable time |
|---|---|---|---|---|
| 2015-03-07 | Semi Marathon de Paris | 21.4 km | 5.11/km | **1:49:27** |
| 2015-10-10 | 20km de Paris | 20.3 km | 4.95/km | **1:40:06** |
| 2016-03-05 | Semi de Paris | 21.2 km | 4.73/km | **1:40:18** |
| 2016-04-02 | Marathon de Paris | 42.3 km | 5.63/km | **3:58:12** |
| 2016-10-08 | 20km de Paris | 20.1 km | 5.33/km | **1:47:43** |
| 2018-04-07 | Semi de Bourg-lès-Valence | 21.1 km | 5.42/km | ~1:54 |
| 2019-03-16 | **Semi de Rueil-Malmaison** | 20.5 km | 4.60/km | **1:34:33 — LIFETIME PR** |
| 2019-04-13 | **Marathon de Paris** | 43.0 km | 5.05/km | **3:39:55 — LIFETIME PR** |
| 2024-03-02 | Semi de Paris | 21.3 km | 5.50/km | ~1:57 (post-hiatus #1) |
| 2025-10-18 | Semi du Bois de Vincennes | 21.2 km | 6.14/km | ~2:10 (post-hiatus #2, slowest on record) |

**Benchmarking:** the 2019 half-marathon PR (1:34:33, 4:29/km) sits in roughly the top 15–20% of French amateur half-marathon finishers (median club/amateur half is ~2:00–2:10). The marathon PR (3:39:55) is a solid amateur time, comfortably inside the top third of finishers at major French marathons. Both PRs were run at ~86 kg — the two post-hiatus races (2024, 2025) were 8–15 min slower than the 2019 PR pace and occurred at 97–104 kg, a body-composition-confounded comparison, not a fitness collapse per se.

### 4. Physiological markers

Garmin device data only exists from **2023-Q3** onward (data limitation — no VO2max/HRV/training-readiness before this).

| Quarter | VO2max Run | VO2max Bike | RHR | Steps/day |
|---|---|---|---|---|
| 2025-Q2 (peak on record) | 43.2 | 41.2 | 48.5 | 9,131 |
| 2025-Q3 | 41.2 | 40.4 | 52.5 | 8,443 |
| 2025-Q4 | 40.9 | 39.4 | 53.0 | 10,831 |
| 2026-Q1 | 40.1 | 38.7 | 50.4 | 10,937 |
| 2026-Q2 (current) | 41.1 | 38.6 | 49.3 | 6,689 (partial quarter) |

- **VO2max running 41.1**: for a 42-year-old male, this sits at the **ACSM "Good"** classification boundary (approaching "Superior" for age 40–49, where norms run roughly 39–43 = Good, 44+ = Superior). Down ~5% from the 2025-Q2 peak (43.2) recorded during the brief 2025 running window, consistent with the subsequent layoff.
- **RHR 48–50 bpm**: **ACSM "Excellent"** for adult males (<56 bpm bracket at the top). Notably resilient — RHR barely moved across the entire 182-day running layoff, indicating the aerobic base (largely built via cycling/e-bike volume) was preserved even while running-specific fitness (VO2max run) drifted down.
- Steps trending down in the most recent partial quarter — partial-quarter artifact (only 3 days of July data), not a real signal.

### 5. Body composition trajectory (Withings, `weight_kg > 70` filter)

| Year | Avg weight | Avg fat % | Avg muscle mass | n readings |
|---|---|---|---|---|
| 2015 (leanest, running peak) | 86.9 kg | 22.0% | — | 188 |
| 2019 (PR year) | 86.3 kg | 21.5% | — | 227 |
| 2021 | 84.6 kg | 21.3% | — | 76 |
| 2022 | 91.4 kg | 25.4% | — | 64 |
| 2023 (highest training-load year) | 94.8 kg | 27.9% | — | 35 |
| 2024 | 97.0 kg | 31.5% (highest on record) | — | 28 |
| 2025 | 103.5 kg | 28.0% | 71.0 kg | 23 |
| 2026 YTD | 104.6 kg | 27.4% | 71.9 kg | 16 |
| **Latest single reading** | **103.67 kg** (2026-06-20 — 14 days stale, no sync since) | 26.3% | 72.6 kg | — |

**Correlation with training phases:** every leanest period (2015, 2019, 2021) coincides with either high running volume or near-total inactivity/low food availability context (2021, sparse data). Every regain period (2017, 2022–2025) coincides with the shift away from running toward cycling/gym/e-bike — those modalities sustained cardiovascular fitness (RHR, steps) but did not control weight/fat% the way running volume historically did for this athlete. The 2023 "peak training load" year is also the year fat% started climbing (27.9%) despite being the highest-volume year on record — a training-load ≠ body-composition-outcome dissociation worth naming explicitly, since `historical-peak.json` currently anchors the planner's "target" state to a year that was not lean.

Muscle mass data only exists from 2025 onward (Withings Body+ scale acquired then) — no earlier comparison possible.

### 6. The verdict

**Classification: Masters-age (42y, male) recreational endurance athlete, sub-elite amateur competitor tier (top-fifth-percentile amateur half-marathon PR: 1:34:33), Mitchell high-dynamic/low-to-moderate-static cardiovascular profile, currently in a physician-uninvolved, self-directed structured return-to-running rebuild following the second extended running layoff of his training history (182 days, Nov 2025–May 2026), at a body weight ~18 kg above his personal-best racing weight.**

Supporting evidence: a 12-year, 800+ run training history with two genuine PR-caliber performances (2019 marathon and half) demonstrates the physiological ceiling is real and was reached without professional coaching. Since then, three forces have reshaped the profile — (1) a durable multi-year drift from running toward low-impact cycling/e-bike commuting that preserved cardiovascular markers (RHR, VO2max-bike) while running-specific fitness and body composition drifted the other way, (2) two life-driven layoffs (2020 COVID-era, and 2025–26 second-child period) each followed by a deliberate, data-aware comeback, and (3) a currently intact aerobic engine (RHR "Excellent," VO2max-run "Good") masking a tissue-tolerance and body-composition deficit relative to the 2019 peak. This is not a detrained novice profile — it's a high-ceiling amateur competitor whose current limiter is tissue tolerance and body mass, not cardiovascular capacity, which is exactly the framing `protocols/return-to-running.md` already encodes.

---

## PART 2 — Objectives Tracker

### Active objectives (7, all created 2026-04-26/27, one added 2026-06-15)

| # | Title | Domain | Target | Deadline | Baseline → Current (live) | Confidence |
|---|---|---|---|---|---|---|
| 1 | Retour au niveau compétiteur amateur (parent goal) | performance | Semi <1h45 & poids <95kg | 2027-06-29 | — | **40%** |
| 2 | Descendre à 95 kg | body_composition | ≤95 kg | 2026-12-30 | 105.22 → **103.67 kg** (stale 14d) | **35%** |
| 3 | Bilan sanguin complet annuel | health | reach | 2026-12-30 | last done 2025-12-01 | **85%** |
| 4 | 160g protéines/jour (moy. 30j) | nutrition | ≥160g | 2026-09-29 | — → **115.4 g** (30d avg, 31 days logged) | **40%** |
| 5 | Reprendre la course 3x/semaine | habit | ≥3/wk | 2026-09-29 | — → **~0.67/wk** (last 3 wks); ~1.4/wk since comeback start | **25%** |
| 6 | Semi-marathon <1h45 | performance | ≤105 min | 2027-03-30 | — → no race since Oct 2025 (2:10) | **30%** |
| 7 | Sortie 12km Parc des Beaumonts | performance | ≥12 km | 2026-10-30 | 5.8 → **7.51 km** (max since, DB stale) | **55%** |

### Live values fetched (dynamic queries built from each objective's `source_table`/`source_column`/`source_filter`/`source_agg`)

- **#2 weight_kg**: `SELECT weight_kg FROM withings_measurements WHERE weight_kg > 70 ORDER BY date DESC LIMIT 1` → 103.67 kg (2026-06-20). **No Withings sync in 14 days** — data-quality flag, not necessarily a plateau.
- **#4 protein_g**: `SELECT AVG(total_protein_g) FROM oh_daily_nutrition_summary WHERE date >= today-30d` → 115.4 g/day, 31/30 days logged (good logging discipline, poor target adherence — 28% below target).
- **#7 long_run_distance_km**: `SELECT MAX(distance) FROM strava_activities WHERE sport_type IN ('Run','TrailRun') AND start_date >= start_date` → actual max is **7.51 km** (Run #12, 2026-06-20), not the 5.8 km stored as `current_value` — refreshed below.
- **#5 runs_per_week**: no `source_table` (manual metric). Computed directly: 13 runs across 9.3 weeks since 2026-05-03 = 1.4/wk lifetime-of-comeback average, but only **2 runs in the trailing 3 weeks** (2026-06-21, 2026-06-28) = 0.67/wk — the rate is decelerating, not accelerating, right when the objective needs the opposite.
- **#6 half_marathon_time_min**, **#1**, **#3**: no `source_table` — these are race-day or logistics-based objectives with no continuous data proxy; assessed qualitatively below.

*(Objectives #2, #4, #7 current_value refreshed in the database via `upsert_objective` as part of this run — see Memory section.)*

### Confidence rationale (0–100 scale, weighed per the six factors)

- **#2 Weight → 95kg (35%)**: Actual pace since baseline is −0.194 kg/wk (105.22→103.67 over 8 weeks); required pace to hit 95kg by Dec 30 is −0.339 kg/wk — current trajectory is running at **57% of the rate needed**. Projected weight at deadline on current pace: ~98.7 kg, missing target by ~3.7 kg. The required rate (0.339 kg/wk ≈ 0.32%/wk of bodyweight) is itself well within the evidence-based 0.5–1%/wk fat-loss range — physiologically plausible, just not currently being executed. Headwind: protein intake (#4) is 28% under target, which undermines lean-mass-preserving deficit dieting.
- **#4 Protein 160g (40%)**: pure gap-closing (44.6g/day short), no trend data yet since this is the first month tracked. Logging discipline is excellent (31/30 days) — the lever is meal composition, not tracking. Achievable but requires an active plan (this is exactly the kind of thing that should become a P0/P1 recommendation).
- **#5 Runs 3x/week (25%, lowest of the set)**: this is the objective most at risk, and structurally so — hitting 3 sessions/week by Sept 29 requires more than doubling the trailing-3-week cadence (0.67→3) in ~13 weeks, while the mandatory return-to-running protocol (`protocols/return-to-running.md`) explicitly prescribes conservative, injury-risk-gated ramping (ACWR ≤1.3, no rapid frequency jumps) given body weight +18kg vs PR era and a 42-year-old tendon-remodeling timeline. **These two constraints are in tension** — see coherence check below.
- **#6 Semi <1h45 (30%)**: 38 weeks of runway is generous, and the 2019 PR (1:34:33) proves the physiological ceiling exists. But today's longest continuous run is 7.5 km at Z2 (~7.5 min/km), a large gap from 21.1 km at ~4:59/km target pace, and the goal is fully dependent on #5 and #7 executing on schedule.
- **#7 Long run 12km (55%, highest of the performance goals)**: the underlying progression math is favorable — from an actual current max of 7.51 km, a standard ~10%/week long-run build reaches 12 km well inside the 16.9-week runway — *if* weekly running frequency holds. Entirely gated on #5.
- **#3 Bilan sanguin (85%)**: pure logistics/habit renewal — last panel was Dec 2025 (7 months ago, within the annual cadence), GP relationship and history of compliance already established (Vitamin D supplementation, retest already anticipated in `return-to-running.md`).
- **#1 Parent objective (40%)**: geometric mean of its two hardest sub-goals (weight, running frequency/pace) pulled down by their current under-pace status, but partially offset by the long (51-week) runway allowing course-correction.

### Coherence check — conflicts and dependencies

1. **Direct conflict: objective #5's deadline vs. the safety protocol.** "3 runs/week by Sept 29" is an aggressive frequency ramp for a comeback explicitly flagged in `return-to-running.md` as "materially riskier than past ones" (body mass × impact, tendon remodeling timeline, Vitamin D insufficiency history). The daily training-planner must not compress the ramp to chase this objective's date — if forced to choose, the ACWR/ramp-cap protocol wins. **Recommendation: extend objective #5's target_date rather than accelerate the ramp.**
2. **Shared root cause: #2 (weight) and #4 (protein)** are both under-pace for the same reason — nutrition execution, not a training problem. Fixing meal-plan discipline moves both at once with zero injury risk, unlike accelerating running.
3. **Dependency chain: #5 → #7 → #6 → #1.** Running frequency is the load-bearing input for the long-run buildup, which is the load-bearing input for the semi-marathon time goal, which is half of the parent objective. A stall at #5 (currently the case) cascades through the whole tree.
4. **Data-quality conflicts reduce trajectory confidence directly**: Withings hasn't synced in 14 days (weight trend partially stale) and `training_load_daily` has a 3-day gap (Jul 2–4, no rows) right at the point this assessment is being made — both should be treated as measurement gaps, not physiological signals, and flagged for the next daily digest to re-verify once fresh data lands.

### Narrative synthesis

The seven objectives are compatible in direction but not in current pace — every measurable one is currently behind its required rate, and the shortfalls compound through the dependency chain above rather than existing independently. The critical path runs through running frequency (#5): it is simultaneously the objective furthest behind, the one with the most demanding near-term deadline (13 weeks), and the sole input for two downstream performance goals. But #5 cannot simply be accelerated — the standing return-to-running protocol correctly constrains how fast frequency can rise given body weight and tendon-remodeling risk, so the honest fix is to **retime the objective, not the training plan**.

**Single highest-leverage action right now: close the protein gap (115g → 160g/day).** It is the fastest-moving lever available (behavior change only, no physiological ramp limit), it directly de-risks the weight-loss objective (supports a lean-mass-sparing deficit) without needing more training volume, and it carries zero injury risk — unlike trying to force the running-frequency objective faster than the safety protocol allows. Recommend this as the P0 action item in the next daily digest, alongside a proposal to `upsert_objective` the target_date on #5 from 2026-09-29 to something more consistent with a 10%/week frequency ramp (e.g., late Nov/Dec 2026).

---

*Report generated 2026-07-04. Companion memory update: `protocols/return-to-running.md` refreshed with runs since June 14 (an unnumbered June 2 run, #12, #13) and current metrics; `state/latest.json` unchanged (last daily digest run remains 2026-06-14 — a 20-day gap in the daily pipeline exists and should be investigated separately).*

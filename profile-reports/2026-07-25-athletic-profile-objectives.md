# Athletic Profile & Objectives Tracker — 2026-07-25

Weekly deep-dive. Part 1 classifies Benjamin's lifetime athletic profile from raw data. Part 2 refreshes every active objective against live queries and reassesses confidence.

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers — lifetime totals

- **2,438 activities** logged, **2014-05-01 → 2026-07-23** (12.2 years span)
- **24,412 km**, **2,156 hours** total moving time across all activity types
- Full type breakdown:

| Type | Count | km | Hours |
|---|---:|---:|---:|
| Run | 823 | 7,014 | 748 |
| Ride | 742 | 11,983 | 635 |
| Workout | 328 | 76 | 287 |
| EBikeRide | 230 | 3,719 | 197 |
| WeightTraining | 121 | 1 | 77 |
| Walk | 76 | 251 | 63 |
| VirtualRide | 43 | 812 | 35 |
| Swim | 25 | 29 | 14 |
| Hike | 24 | 189 | 57 |
| AlpineSki | 12 | 317 | 33 |
| Other (Crossfit, StairStepper, Rowing, Surfing, Snowshoe, Yoga, SUP) | 13 | 21 | 8 |

Cycling (Ride+EBike+Virtual) is the largest lifetime km total (16,514 km); running is the largest lifetime *hour* investment when weighted by intensity/frequency of structured blocks (748h across 823 sessions, avg ~55min/session).

### 2. Volume trajectory — distinct phases (Run+Ride, excludes EBikeRide commuting)

| Year | Sessions/wk | Hours/wk | Dominant mode | Note |
|---|---:|---:|---|---|
| 2014 | 4.9 | 3.0 | Ride+Run balanced | Baseline year |
| 2015 | 4.4 | 3.8 | Run (1,692km) | First half-marathon block |
| 2016 | 5.5 | 4.6 | Run (1,506km) + Ride | **Volume peak** — Paris Marathon 3:58:12 |
| 2017 | 4.0 | 3.1 | Ride (1,812km) | Cycling-focus year, running drops off |
| 2018 | 4.1 | 3.7 | Run + Workout | Trail racing (Marcelly, +1,480m) |
| 2019 | 4.4 | 3.4 | Run (733km) | **Performance peak** — Marathon PR 3:39:55, Half PR 1:34:33 |
| 2020 | 2.9 | 2.7 | Ride | Covid disruption, running collapses (13 runs/yr) |
| 2021 | 1.3 | 1.6 | Ride | **Trough** |
| 2022 | 1.6 | 2.6 | Ride | Cycling-only, essentially no running (1 run/yr) |
| 2023 | 4.1 | 4.2 | Ride (2,123km) | Rebuild, cycling-led — **historical chronic-load peak (2,100)** stored in `state/historical-peak.json` |
| 2024 | 2.9 | 2.9 | Ride + Run | Comeback race (Semi de Paris, 1:57:00) |
| 2025 | 1.6 | 1.6 | Run + Ride | Paternity transition begins; comeback race slows further (2:10:30) |
| 2026 YTD (7mo) | 0.7 | 0.4 | Run | **Lowest structured volume on record** — but this undercounts: E-bike commuting (13 rides/198km logged separately) is the de facto daily-movement modality, and the return-to-running protocol (active since 2026-05-03) is intentionally low-volume by design, not a collapse |

Two clear performance eras separated by an 8-year climb-and-fall: **2015-2019 build** (culminating in lifetime PRs) → **2020-2023 disruption/cycling pivot** → **2024-2026 postpartum rebuild**, currently mid-rebuild.

### 3. Competitive performance — race results

All official halfs/marathons + long training runs ≥20km:

| Date | Race | Distance | Time | Pace/km | HR avg |
|---|---|---:|---:|---:|---:|
| 2015-03-07 | Semi Marathon de Paris | 21.39 km | 1:49:27 | 5:07 | 176 |
| 2015-10-10 | 20km de Paris | 20.25 km | 1:40:06 | 4:57 | 179 |
| 2016-04-02 | **Marathon de Paris** | 42.34 km | 3:58:12 | 5:38 | 172 |
| 2016-10-08 | 20km de Paris | 20.10 km | 1:47:43 | 5:20 | 169 |
| 2017-10-21 | Trail du Haut Planet | 24.51 km | 2:58:00 | 7:16 (+525m) | 174 |
| 2018-04-07 | Semi Bourg-lès-Valence | 21.09 km | 1:54:24 | 5:26 | 186 |
| 2018-10-04 | Pointe de Marcelly (mountain) | 21.64 km | 3:49:12 | 10:35 (+1,480m) | 171 |
| **2019-03-16** | **Semi de Rueil-Malmaison — LIFETIME PR** | 20.54 km | **1:34:33** | **4:36** | 177 |
| **2019-04-13** | **Marathon de Paris — LIFETIME PR** | 42.99 km | **3:39:55** | **5:05** | 172 |
| 2024-03-02 | Semi de Paris (comeback) | 21.27 km | 1:57:00 | 5:30 | 165 |
| 2025-10-18 | Semi Bois de Vincennes (comeback) | 21.24 km | 2:10:30 | 6:08 | 169 |

**Benchmark context**: 1:34:33 for a half marathon places Benjamin in the sub-1:35 tier — competitive amateur territory in French club racing (roughly top 10-15% of half-marathon finishers nationally, "grand public performant" tier per FFA amateur benchmarks). The 3:39:55 marathon similarly sits in the solid-amateur band (~top 20-25% of marathon finishers). Both PRs were set within a 4-week window in March-April 2019 at age 35, the clear competitive apex of the dataset.

The two comeback halves (2024, 2025) show a **34% pace slowdown** vs the 2019 PR (4:36/km → 6:08/km) — consistent with the ~18kg weight gain and multi-year training gap, not a loss of aerobic engine (see VO2max below).

### 4. Physiological markers

- **VO2max running**: quarterly trajectory — 2025Q2 peak 42.2 → 2025Q4/2026Q1-Q2 trough 39.4-41.2 (pregnancy/newborn low-activity window) → **2026Q3 recovering to 41.6, most recent single readings flat at 42**. For a 42-year-old male (DOB 1983-09-25), VO2max ≈ 42 ml/kg/min sits in the **"Good"** ACSM age/sex percentile band (roughly 70th-80th percentile vs untrained population norms for 40-49yo men) — notably strong given current body mass.
- **Resting heart rate**: quarterly avg improving steadily — 2026Q1 53.0 → 2026Q3 48.8, most recent daily readings 47-49 bpm. This is at or near the *best* RHR recorded in the dataset (2025Q3 low was 48.5) — a genuinely excellent cardiovascular marker, ACSM-wise consistent with "Excellent" classification for age.
- **Steps**: 2026 daily avg ~10,800/day (Q1-Q3), among the highest in the dataset — high non-exercise daily activity (NEAT) is being maintained despite low structured-session volume, plausibly driven by e-bike commuting + parenting logistics.

### 5. Body composition trajectory

| Year | Avg weight | Avg fat% | Note |
|---|---:|---:|---|
| 2011 | 102.3 kg | 32.1% | Earliest data |
| 2015 | 86.9 kg | 22.0% | **Leanest recorded**, precedes 2016 marathon |
| 2019 | 86.3 kg | 21.5% | Second-leanest, coincides with both lifetime PRs |
| 2021 | 84.6 kg | 21.3% | Covid-era low-volume but still lean |
| 2024 | 97.0 kg | **31.5%** (highest fat% on record) | Regain accelerating |
| 2025 | 103.5 kg | 28.0% | Muscle mass tracking begins (71.0 kg) |
| 2026 YTD | 104.6 kg | 27.4% | **Heaviest weight on record**, but fat% and muscle mass both improved slightly vs 2024 |

Weight and fat% track training volume almost exactly inverse: every high-volume running year (2015, 2016, 2019) is a body-composition trough; every low-volume year (2017 cycling-only, 2021-2024 disruption) is a body-composition peak. 2026 breaks the pattern slightly — weight is at an all-time high but fat% and muscle mass are both nudging in the right direction, consistent with the current recomposition/comeback effort gaining early traction even though the scale hasn't caught up (and the scale itself hasn't been used in over a month — see Part 2).

### 6. The verdict

**Master-age (42y) recreational endurance athlete, post-peak, mid-rebuild.** Benjamin demonstrated genuine competitive-amateur ability in 2019 (sub-1:35 half, sub-3:40 marathon — both in the top quartile of French amateur finishers), built over a disciplined 2015-2019 progression. A multi-year disruption (2020 Covid, 2021-2023 cycling-only pivot, 2024-2026 new-parenthood transition) produced substantial detraining and an ~18kg weight regain, with 2026 marking the heaviest recorded bodyweight (BMI ≈ 33.0, technically class-I obese by BMI alone, though partly muscular given 71.9kg lean mass). Critically, the physiological engine has **not** decayed to match: VO2max (42 ml/kg/min) and RHR (47-49 bpm) both sit in "Good-to-Excellent" ACSM bands for his age and are actively trending upward this quarter. This is the classic post-layoff pattern — cardiovascular fitness returns faster than body composition and running economy — and it means the current return-to-running comeback is working physiologically even though the scale and race times haven't caught up yet. Per Mitchell's classification, running/cycling training is high-dynamic, low-to-moderate-static — appropriate and low-risk given the preserved cardiovascular base, contingent on managing joint/tendon load at current bodyweight during the ramp (per `protocols/return-to-running.md`).

---

## PART 2 — Objectives Tracker

### Step 1-3: Live values, progress, trajectory (queried 2026-07-25)

| # | Objective | Baseline | Current (live) | Target | Progress | Trajectory |
|---|---|---:|---:|---:|---:|---|
| 1 | Global comeback (rollup) | — | — | Semi <1h45, poids <95kg | — | Rollup of #2/#5/#7 |
| 2 | Poids → 95 kg | 105.22 kg | **103.67 kg** (Withings, **35 days stale**, no reading since 2026-06-20) | 95 kg by 2026-12-30 | 15.2% of delta closed | Pace 0.197 kg/wk vs 0.287 kg/wk required — under-pace, unchanged since last cycle |
| 3 | Bilan sanguin annuel | — | Last panel 2025-12-01 (7.8mo ago) | Full panel by 2026-12-30 | On track for annual cadence | Vitamin D-specific retest ("due ~July 2026") is now **at the end of its due window with zero action taken** |
| 4 | Protéines 160g/j | 115.4 g (30d avg) | **54.6 g** (30d avg) / **112.9 g** on the 15 days actually logged | 160 g by 2026-09-29 | Regressed vs baseline on raw avg | **Logging has been completely dark for 16 consecutive days (2026-07-09 → 2026-07-24)** — worse than the 9-day gap flagged last cycle. On days he does log, intake is flat vs baseline (~113g vs 115g) — still a disengagement problem, not a diet collapse, but the gap is now widening, not closing |
| 5 | Semi < 1h45 | — | No race in window | 105 min by 2027-03-30 | Gated by #6, #7 | No change; historical precedent strong (1:34:33 PR) |
| 6 | Sortie longue 12 km (Beaumonts) | 5.8 km | **8.03 km** (max since 2026-06-14, unchanged since 2026-07-14) | 12 km by 2026-10-30 | 35.9% of delta closed | **Plateaued this week** — 3 runs since the 7/14 peak (7.05, 5.01, 6.07 km) all came in below it; no new max, but all three sit comfortably above the old 5.8km baseline and even the prior 7.51km plateau, so tolerance is being consolidated rather than lost |
| 7 | Course 3x/semaine | — | **2 runs** in trailing 7d (2026-07-18→24: runs on 7/19, 7/22) | 3/wk by 2026-09-29 | Below target | **2nd consecutive week at exactly 2 runs/wk** (prior window 7/11-7/17 also logged 2) — first sign of a stabilizing floor, still one session short of target every week so far |
| 8 | FTP Zwift 200W | 150W | — | 200W | — | **Abandoned** 2026-06-15, no change |

Supporting load context: ACWR currently ~1.31 (2026-07-23), inside the comeback ceiling of 1.50. Weekly training load has been volatile (36→29→60→32→144→82 over the last 6 weeks) — the 144 spike (week of 7/12) is the week that produced the new 8.03km long-run max; the current week has settled back toward baseline.

### Step 4 — Coherence across objectives

- **#7 (running frequency) remains the critical-path bottleneck** gating both #6 (long run) and #5 (half marathon). It has now held flat at 2/wk for two straight weeks — better than the volatile 0-3/wk swings of the prior month, but still short of 3/wk. No physiological reason for the gap (ACWR mid-band, RHR/VO2max both improving) — this continues to look behavioral/scheduling, not capacity-limited.
- **#2 (weight) and #4 (protein) share a measurement problem, not just a shared root cause.** Both objectives depend on manual logging (Withings weigh-ins, nutrition entries) that has gone dark simultaneously — no weigh-in in 35 days, no nutrition log in 16 days. This is now a *general self-tracking disengagement* pattern spanning two domains at once, distinct from the training domain (Strava/Garmin, which sync automatically and show no such gap). Worth naming explicitly: the objectives most dependent on manual daily input are the ones stalling; the ones fed by passive wearables are the ones showing real progress.
- **#3 (bloodwork)'s Vitamin D sub-component is now overdue**, not just trending that way — this is a distinct, low-effort action (single retest) that's fully decoupled from the training/nutrition thread and could be resolved independently this week.
- **#8 (FTP) being abandoned removes cycling-load competition** for training time, which should in theory make #7's 3x/week target easier, not harder — the frequency shortfall isn't a competing-priorities problem.

### Step 5 — Confidence scores (0-100, probability of hitting target_date)

| Objective | Confidence | Δ vs 2026-07-18 | Key driver |
|---|---:|---:|---|
| #1 Global rollup | **24%** | −3pp | Weight and protein both regressed on measurement; running frequency stabilizing offsets partially |
| #2 Weight 95kg | **20%** | −5pp | No new data point in 35 days; pace-vs-required gap unchanged but now more stale, and staleness itself is evidence against the trajectory |
| #3 Bloodwork annual | **45%** | −10pp | Annual cadence itself fine, but the Vit-D retest window has now closed with no booking |
| #4 Protein 160g | **10%** | −8pp | 16-day unbroken logging gap, no signs of resuming; even the "it's just a logging gap" read is getting harder to sustain the longer it persists |
| #5 Semi <1h45 | **25%** | unchanged | Fully gated by #6/#7; no new evidence either way this week |
| #6 Long run 12km | **35%** | −3pp | Plateaued at 8.03km for the second straight week; direction still positive (3 runs above old baseline) but no fresh ground gained |
| #7 Running 3x/wk | **26%** | +2pp | Two consecutive weeks at 2/wk is the first stabilization signal in the dataset — small but real |
| #8 FTP (abandoned) | n/a | — | Abandoned, excluded |

**Confidence methodology**: trajectory momentum (weighted heaviest for #2/#4 given data staleness), rate sufficiency vs required pace, dependency satisfaction (#5/#6/#7 chain), physiological plausibility (weight-loss pace of 0.2-0.3 kg/wk is well within the evidence-based 0.5-1%/bodyweight/wk band — the shortfall is engagement, not an unsafe target), and historical precedent (strong for the half marathon given the 2019 PR; unproven for sustained 3x/wk running given no prior comeback has held that cadence for more than 2 consecutive weeks in this dataset).

### Narrative synthesis

The physiological story and the behavioral story have diverged further this cycle. VO2max and RHR are both improving — the comeback is working at the level that matters most for long-term health and eventual race capacity. But every objective that depends on Benjamin manually logging something (the scale, the food diary) has gone quiet at the same time, while the one modality with automatic tracking (running, via Strava/Garmin) shows the first genuine stabilization signal in the whole rebuild — two straight weeks at 2 runs/week.

**Critical path is unchanged: running frequency (#7).** It gates the long run (#6) and the half marathon (#5), and it's now the strongest-trending objective in the whole set even though it's still short of target. The **single highest-leverage action** this week is not a new intervention — it's protecting the two-week streak: get a third run in before the week resets, ideally short and easy, to convert "stabilized at 2" into "stabilized at 3." Everything else (the stalled scale, the dark nutrition log, the overdue Vit-D retest) is real but lower-leverage and, notably, all three are *measurement* problems rather than *outcome* problems — they can be closed with a single weigh-in, a single day of logging, and a single phone call to book bloodwork, none of which compete with training time or fatigue budget.

Timelines remain broadly realistic relative to each other: the half-marathon target (2027-03-30) has the most runway and is appropriately the most gated; the nearer-term nutrition/frequency targets (2026-09-29) are the ones showing strain, which is expected for habit-formation goals with tight windows. No objective needs its target_date moved yet — the pattern is engagement variance, not an infeasible plan.

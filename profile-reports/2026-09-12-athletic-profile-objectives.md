# Athletic Profile Classification & Objectives Tracker — 2026-09-12

*Weekly deep-dive pass (separate from the daily digest). Data pulled live via `biometrics:query` on 2026-09-12. Standing medical context: Benjamin has been on **Wegovy (semaglutide) 0.25 mg weekly** since 2026-08-12 (day 31 today) — see `protocols/health-profile.md`. Every RHR/HRV/weight/intake reading below is read through that lens before being called abnormal.*

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers (lifetime, Strava, 2014-05-01 → 2026-09-07)

| Metric | Value |
|---|---|
| Total activities | 2,477 |
| Total distance | 24,909.6 km |
| Total moving time | 2,187.3 h (~91.1 days) |
| Span | 12.4 years |

**Activity type distribution (all-time):**

| Type | n | km | hours |
|---|---|---|---|
| Run | 838 | 7,099.5 | 757.8 |
| Ride | 742 | 11,982.7 | 635.1 |
| Workout (gym/HIIT) | 328 | 76.3 | 286.9 |
| EBikeRide (commute, excluded from training load) | 253 | 4,131.5 | 218.0 |
| WeightTraining | 121 | 0.5 | 77.3 |
| Walk | 76 | 251.0 | 63.1 |
| VirtualRide | 43 | 811.9 | 34.7 |
| Swim | 26 | 29.3 | 14.5 |
| Hike | 24 | 189.2 | 56.7 |
| AlpineSki | 12 | 317.0 | 33.0 |
| Other (Crossfit, StairStepper, Rowing, Surfing, Snowshoe, Yoga, SUP) | 9 | 20.7 | 8.8 |

A cycling-and-running dual-sport athlete for most of the record, with a meaningful strength/gym habit (449 combined Workout+WeightTraining sessions, 364 h) that has nearly disappeared since 2020.

### 2. Volume trajectory — distinct training phases

| Phase | Window | Sessions/wk | Hours/wk | Character |
|---|---|---|---|---|
| Early build | 2014-05 → 2016-12 | **5.57** | 4.32 | Highest lifetime volume; run+ride base building |
| Marathon peak | 2017-02 → 2019-12 | 4.49 | 3.66 | Both marathon PRs and the half-marathon PR fall here |
| COVID trough | 2020-02 → 2021-12 | 2.25 | 2.31 | Sharp drop; also the leanest body-composition years (84.6 kg avg 2021) |
| Low-volume plateau | 2022-07 → 2024-12 | 3.47 | 3.91 | Volume partly recovers (cycling-led) but weight climbs every year (91→94.8→97.0 kg) |
| Pre-comeback trough | 2025-01 → 2026-04 | **1.47** | 1.37 | Deepest lifetime trough — coincides with new-parenthood (Léonie born 2026-01-09) and the weight plateau (101-107 kg) that triggered the Wegovy consult |
| **Running comeback (current)** | 2026-04-26 → present | 2.15 | 1.35 | Return-to-running protocol active; volume is *running*-led this time (unlike every prior phase) but total weekly hours are still below the pre-comeback trough |

**Reading this trajectory today (2026-09-12):** the comeback phase's session count looks like an improvement over the immediate pre-comeback trough, but total training hours/week have not actually recovered — sessions are shorter than historic norms, and the most recent week (Sep 7-12) sits at **1 run**, against an objective target of 3/wk and a historic peak-era norm of 4.5-5.6 sessions/wk across all disciplines. This is a rebuild from the deepest point in the 12-year record, not a return to a recent baseline.

### 3. Competitive performance

**Official races (chronological):**

| Date | Race | Distance | Time | Pace |
|---|---|---|---|---|
| 2015-03-08 | Semi Marathon de Paris | 21.1 km | 1:49:27 | 5:11/km |
| 2015-10-11 | 20 km de Paris | 20.1 km | 1:40:06 | 4:57/km |
| 2016-03-06 | Semi de Paris | 21.1 km | 1:40:18 | 4:44/km |
| 2016-04-03 | Marathon de Paris | 42.3 km | 3:58:12 | 5:38/km |
| 2016-10-09 | 20 km de Paris | 20.1 km | 1:47:43 | 5:22/km |
| 2016-02-07 | 10 km de Vincennes (PR) | 9.9 km | 44:42 | 4:30/km |
| 2018-04-08 | Semi de Bourg-lès-Valence | 21.1 km | 1:54:22 | 5:25/km |
| 2019-03-17 | **Semi de Rueil-Malmaison — PR** | 20.5 km (GPS) | **1:34:33** | **4:36/km** |
| 2019-04-14 | **Marathon de Paris — PR** | 43.0 km | **3:39:55** | **5:05/km** |
| 2024-03-03 | Semi de Paris | 21.3 km | 1:56:59 | 5:30/km |
| 2025-10-19 | Semi du Bois de Vincennes | 21.2 km | 2:10:27 | 6:08/km |

Also on record: 2 completed marathons, 6 half-marathons overall (per `lifetime_prs.all_halfs`), several ultra-distance charity events (No Finish Line, 2×20-25 km), and 2 mountain trail races (Trail du Haut Planet ×2, Pointe de Marcelly with 1,480 m D+ — the lifetime elevation-gain PR for a run).

**Long training runs** (not races, "SL" = sortie longue) cluster in two marathon-build blocks: Nov 2015-Mar 2016 (7 runs, 20.8-26.1 km) and Feb-Mar 2019 (4 runs, 22.2-26.4 km), both immediately preceding a marathon PR — a consistent, reproducible build pattern.

**Benchmarking:**
- Half-marathon PR **1:34:33** (2019) is a genuinely strong amateur time. French median male half-marathon finish is ~1:55-2:00; sub-1:35 sits roughly in the **top 5-10% of half-marathon finishers nationally** — solidly "compétiteur amateur" / sub-elite club-runner territory, not merely "finisher."
- Marathon PR **3:39:55** (2019) is a solid recreational-competitive time (~top 30-35% of male finishers; French median ~4:15-4:30).
- The 2024 and 2025 half-marathon results (1:56:59, 2:10:27) show a **~25-35 min regression** from the 2019 PR, tracking the parallel weight/detraining trend below — the fitness is not gone, but the current comeback is rebuilding from well below the demonstrated ceiling.

### 4. Physiological markers (Garmin, quarterly)

| Quarter | VO2max run | VO2max bike | RHR | Steps/day |
|---|---|---|---|---|
| 2025 Q2 | 42.2 | 40.3 | 50.3 | 10,389 |
| 2025 Q3 (peak) | **43.2** | 41.2 | **48.5** | 9,131 |
| 2025 Q4 | 41.2 | 40.4 | 52.5 | 8,443 |
| 2026 Q1 | 40.9 | 39.4 | 53.0 | 10,831 |
| 2026 Q2 (nadir) | 40.1 | 38.7 | 50.4 | 10,937 |
| 2026 Q3 (current, incl. GLP-1 period) | 42.2 | 40.5 | 50.9 | 10,711 |

- **VO2max running 42.2 ml/kg/min** (ACSM norms, male 40-49) classifies as **"Good"**, roughly the 70th-80th percentile for age/sex — despite the body-composition trend below, cardiorespiratory fitness has been substantially preserved and is currently *recovering* (Q2→Q3 2026 rebound tracks the running-comeback restart).
- **RHR** sits at 50-53 bpm on the quarterly average (masks the current 51-58 bpm daily range, elevated by the GLP-1 class effect since Aug 12 plus a resolving cold, see Part 2). A resting HR in the high-40s/low-50s for a 42-year-old male is itself "good" by ACSM standards (<60 bpm average population; <50 good/excellent for a non-elite).
- **Daily steps** roughly doubled from the 2023-2024 range (5,600-8,400/day) to 9,000-11,000/day from 2025 onward — likely reflects e-bike-commute-adjacent activity and new-parent daily movement, independent of structured training.

### 5. Body composition trajectory

| Year | Avg weight (kg) | Avg fat % | Avg muscle (kg, tracked from 2025) |
|---|---|---|---|
| 2021 (leanest) | **84.6** | **21.3** | — |
| 2022 | 91.4 | 25.4 | — |
| 2023 | 94.8 | 27.9 | — |
| 2024 | 97.0 | 31.5 | — |
| 2025 | 103.5 | 28.0 | 71.0 |
| 2026 (YTD avg) | 103.9 | 27.0 | 71.9 |
| **Current (2026-09-01)** | **101.15** | n/a (no fresh composition split since Aug 11) | n/a |

Weight and fat% move in lockstep with the volume trajectory: the 2021 low (84.6 kg) sits inside the marathon-fit COVID-trough years; the climb to 103.5-103.9 kg (2025-2026) is the plateau documented in `health-profile.md` that triggered Wegovy initiation. Since initiation (Aug 12), weight has moved from 100.68 kg (Aug 11, pre-drug) → 101.15 kg (Sep 1) — essentially flat, **slower** than the GLP-1-expected 0.5-1.0%/week loss band (see Part 2, objective 218d1c78) and with no fresh fat/muscle split in a month to check the lean-mass-loss risk directly.

### 6. The verdict

**Detrained sub-elite masters endurance athlete undergoing medically-supervised, weight-management-driven re-training.** Historical performance data (half-marathon 1:34:33, marathon 3:39:55, both 2019, both in the top third-to-tenth percentile of French amateur fields) place the demonstrated athletic ceiling well above "recreational jogger" — this is a rider/runner with a genuine competitive training history (Mitchell classification: predominantly high-dynamic, low-to-moderate-static endurance sport — running and road cycling). Two trend lines have since diverged: **cardiorespiratory fitness has been substantially preserved** (VO2max 42.2 ml/kg/min = ACSM "Good", ~75th percentile for age/sex, currently rebounding) while **body composition has not** (BMI ≈ 33, ACSM/WHO Class I obesity, following 15 months of weight-cycling plateau). This "fit-but-fat" discordance is precisely the profile Wegovy was prescribed for, and the running comeback since 2026-04-26 is real (running-led for the first time in the 12-year record) but is currently executing at roughly a third of the historic peak-era session volume and well below its own 3-runs/week target — see Part 2 for why.

---

## PART 2 — Objectives Tracker (live refresh, 2026-09-12)

### Step 1-2 — Active objectives & live current values

| ID | Objective | Live value | Target | Direction | Target date |
|---|---|---|---|---|---|
| a1bde447 | Reprendre la course 3x/semaine | **1 run** (this week, Mon-today) | ≥3/wk | at_least | 2026-09-29 |
| 49829c29 | Protéines ≥160 g/j (avg) | **43.1 g** (30d avg) | ≥160 g | at_least | 2026-09-29 |
| 218d1c78 | Descendre à 95 kg | **101.15 kg** (stale, last reading 2026-09-01) | ≤95 kg | at_most | 2026-12-30 |
| 9b982443 | Sortie 12 km Beaumonts | **10.5 km** max (unchanged, Run #20, 2026-07-25) | ≥12 km | at_least | 2026-10-30 |
| 42361937 | Bilan sanguin annuel | no new labs since 2025-12-04 (286 days) | — | reach | 2026-12-30 |
| 96910249 | Semi < 1h45 | no qualifying attempt | ≤105 min | at_most | 2027-03-30 |
| a0000000 | Retour niveau compétiteur (semi<1h45, poids<95kg) | rollup of the above | — | reach | 2027-06-29 |

### Step 3 — Progress & trajectory, objective by objective

**a1bde447 — 3 runs/week.** Only 2 runs logged since the last refresh (2026-09-05): 7.28 km on Sep 7 and 5.00 km on Sep 7 (the Sep-04 entry in the raw pull is a UTC date-boundary artifact of the same run). The current week (Mon Sep 7 → today) stands at **1/3**, with **zero runs Sep 8-11** — but this gap now has an *identified, legitimate* cause: a symptom-log entry **"Gros rhume" (bad cold), started 2026-09-08, severity 6/10, still active** — a genuine second signal (illness) independent of the GLP-1 lens, and per protocol this is a "rest + light aerobic only" period, not a silent skip. Garmin corroborates: RHR spiked to 57-58 bpm and body battery crashed to 20-21 on Sep 8-9 (well beyond the GLP-1-expected band), then recovered sharply on Sep 11 (RHR 51, HRV 34, sleep 8.7 h/score 94, body battery 61) — consistent with a resolving viral illness rather than a deepening recovery deficit. **Trajectory:** flat-to-slightly-worse in raw adherence, but the underlying autonomic-recovery capacity looks intact once the illness is accounted for.

**49829c29 — Protein ≥160 g/day.** The 30-day rolling average has fallen further, to **43.1 g/day** (from 70.4 g last week, from 74.0 g the week before — third consecutive week of decline). Root cause is unambiguous this week: `oh_nutrition_intakes` shows **zero rows of any kind** (not just zero-value rows) for every day from **2026-08-23 through 2026-09-11 — 20 consecutive days**, up from the 12-day streak flagged on Sep 5. The last real logged days were Aug 20-22 (112-142 g/day, i.e., capability is not the issue). Because there are literally no intake rows (not merely zero macros), this is best read as **Benjamin having stopped logging**, not necessarily zero intake — but at 20 days with no visibility at all, on an appetite-suppressing medication, the length of the blackout is itself the concerning signal regardless of true intake. **Trajectory: worst-trending objective in the set, now 4 straight refreshes of a worsening blackout.**

**218d1c78 — Weight to 95 kg.** No new Withings reading since 2026-09-01 (11 days stale) — 101.15 kg. Demonstrated pace since the 2026-04-26 baseline (105.22 kg) is **-0.205 kg/wk** over 139 days; the pace required over the 109 days remaining to 2026-12-30 is **-0.391 kg/wk** — the gap has widened again. Notably, this demonstrated pace is *below* even the low end of the GLP-1-expected loss band (0.5-1.0%/wk of bodyweight ≈ -0.5 to -1.0 kg/wk at this bodyweight) — i.e., **the medication is under-delivering relative to its own expected effect**, not overshooting it. Plausible explanations, none confirmed: (a) still at the 0.25 mg starter dose with the Sep 9 step to 0.5 mg unconfirmed either way (no injection log exists in `oh_supplement_logs` at all — a standing known-unknown), (b) the resolving cold (fluid shifts), (c) compensatory eating outside the 20-day logging blackout that the data cannot see. No fat/muscle split since Aug 11 to check the lean-mass-share-of-loss flag directly.

**9b982443 — 12 km Beaumonts.** Max long run still 10.5 km, now **7 full weeks without an attempt above it** (was 6 weeks last refresh) — the longest stall since this objective opened. Directly downstream of a1bde447: the deferred attempt week has not yet been rescheduled. 6.9 weeks remain to 2026-10-30.

**42361937 — Annual blood panel.** Still no action; 286 days since the last panel, Vitamin D retest (27 ng/mL, insufficient) now ~10 weeks past its informal due date. 109 days of runway remain — numerically adequate but this is the 4th straight refresh of pure inaction on a zero-training-cost item.

**96910249 — Semi < 1h45.** Fully gated by 9b982443 and a1bde447; no independent movement. 6.5 months of runway remains, which is the main thing keeping this from being urgent.

### Step 4 — Coherence across objectives

No objectives point in conflicting directions. The dependency chain is unchanged and, if anything, more clearly evidenced this week: **a1bde447 (run frequency) → 9b982443 (long-run distance) → 96910249 (semi time) → a0000000 (root)**, with **49829c29 (protein)** sitting outside that chain but plausibly gating the HRV/RHR recovery that in turn gates a1bde447 — the same cross-domain read as last week, now with a longer (20 vs. 12 day) blackout to point to. The genuine new information this week is **exculpatory, not incriminating**: the Sep 8-9 RHR/body-battery spike that would otherwise look like worsening overload has an identified, resolving cause (a cold), and the Sep 11 rebound (best readiness numbers in three weeks) suggests the underlying recovery machinery is intact once the confound clears. The system correctly did not schedule hard training through it.

### Step 5 — Confidence scores (0-100, probability of hitting target_date)

| Objective | Confidence | Δ vs 2026-09-05 | Key driver |
|---|---|---|---|
| a1bde447 — 3 runs/wk | **12%** | ↓ from 16% | 17 days left, needs to ~triple current pace; illness explains but doesn't reverse the miss |
| 49829c29 — Protein 160 g/kg | **3%** | ↓ from 5% | 20-day zero-log streak, worst-trending objective for the 4th straight week |
| 218d1c78 — 95 kg | **22%** | ↓ from 28% | Demonstrated pace now below even the low end of the GLP-1-expected band |
| 9b982443 — 12 km Beaumonts | **15%** | ↓ from 20% | 7th week stalled at 10.5 km, 6.9 weeks of runway left |
| 42361937 — Blood panel | **20%** | ↓ from 24% | 4th refresh of inaction, runway still adequate |
| 96910249 — Semi <1h45 | **8%** | ↓ from 10% | Fully gated; long runway (6.5 mo) is the main cushion |
| **a0000000 — Root objective** | **14%** | ↓ from 17% | Weighted down by protein/weight/long-run stalls, partly offset by the illness explanation removing one false alarm |

**Confidence-factor notes:**
- *Historical precedent* is the strongest tailwind across the board — a 1:34:33 half and 3:39:55 marathon are proof this athlete can execute a structured build; the gap right now is adherence and fuelling, not physiological ceiling.
- *Physiological plausibility*: current weight-loss rate (-0.205 kg/wk) is itself plausible/safe, but it is **not on track** to reach 95 kg by the target date without either a dose step or closing the fuelling gap.
- *Contextual headwinds*: an active respiratory illness (new this week), a 20-day nutrition-logging blackout (worsening), Benjamin's return to work today (2026-09-12, congé ended Sep 11) removing the extra daytime flexibility of the past two weeks, and an unconfirmed GLP-1 dose-step window (Sep 9) that adds noise to any RHR/weight reading right now.
- *Contextual tailwind*: VO2max running rebounded to 42.2-42.3 this quarter (best since 2025 Q3), and the one run logged this week (Sep 7, 5.00 km) showed no HR-at-pace drift.

### Narrative synthesis — critical path and highest-leverage action

The objectives remain mutually compatible and the timelines are not yet unrealistic relative to each other (the root objective's 2027-06-29 date and the semi objective's 2027-03-30 date both still have 6+ months of runway), but **every measurable sub-objective weakened again this week**, for the second straight refresh. The single highest-leverage, zero-training-cost action is unchanged from last week and now more urgent: **restart protein logging today.** Two things make this the critical path rather than just one more flagged item: (1) it is the one lever fully within Benjamin's control regardless of illness, work schedule, or medication timing, and (2) a 20-day blind spot on an appetite-suppressing drug is a genuine athletic and safety risk (lean-mass loss, under-fuelling a running rebuild) independent of whatever the true intake actually was. Recommended trigger, as before: **3 consecutive days logged ≥120 g protein** should be the cue to re-run the HRV/RHR deload-gate check, rather than waiting on HRV/RHR alone to normalize. Second-priority action: confirm whether the Sep 9 dose step to 0.5 mg happened — it changes how every RHR/weight reading from here should be read, and it is currently unconfirmed in both directions.

# Weekly Athletic Profile & Objectives Refresh — 2026-08-15

*Benjamin, 42, M, Paris. Weekly deep-dive combining (1) a full lifetime athletic profile classification from Strava/Withings/Garmin, and (2) a live objectives-tracker pass against the `objectives` table. Previous refresh: 2026-08-08 (report not persisted to git that cycle — continuity carried via `objectives.notes`, restored here).*

## Executive synthesis

Benjamin is a **masters-age (42) recreational endurance athlete with a demonstrated competitive-amateur running ceiling** (half-marathon PR 1:34:33, marathon PR 3:39:55, both age 35, 2019) who is roughly **1.5 years into recovering from a 2020–2024 volume collapse and weight/fat-percentage regain**, with cardiovascular fitness (VO2max "Good" band, RHR "Athlete" band) holding up materially better than body composition (BMI ≈31.8, near the 12-year record's least-favorable point). The rebuild is underway, not stalled or complete.

On the objectives side, this week is a **single external event (Saint-Malo travel, Aug 11–15) denting three of the four nodes on the critical path** to the master "return to competitor" rollup — running-frequency streak broke after 4 clean weeks, and the Beaumonts long-run progression missed its second consecutive staged session. Weight-loss trajectory continues to strengthen (now essentially on pace) and is the one clear bright spot. The protein-logging objective remains the worst-scoring item in the whole set by a wide margin — a zero-cost, zero-training-load, purely behavioral fix, and now flagged as a genuine risk to lean mass given the concurrent calorie deficit.

**Highest-leverage action this week:** get a run in before the travel window closes (protects 3 of 7 objectives simultaneously via the dependency graph); independently, close the protein-logging gap (worst-scoring objective, zero recovery cost, capability already demonstrated).

---

# PART 1 — Athletic Profile Classification

## Raw numbers

*All figures pulled directly from `strava_activities`, `withings_measurements`, `garmin_health`, `lifetime_prs`, `fitness_assessments`, and `oh_user_profile`. Units per source: `strava_activities.distance` in km, `moving_time`/`duration` in minutes.*

**Lifetime (2014-05-01 → 2026-08-13, ~12.3 years of continuous Strava logging):**
- **2,460 activities**, **24,684.7 km**, **2,173.4 hours** (≈ 90.6 full days of moving time)
- Height 178 cm, DOB 1983-09-25 (age 42), sex male, blood type O- (`oh_user_profile`)

**Activity-type distribution (full history):**

| Type | n | km | hours | span |
|---|---|---|---|---|
| Run | 831 | 7,062.9 | 753.4 | 2014-05 → 2026-08 |
| Ride | 742 | 11,982.7 | 635.1 | 2014-05 → 2026-05 |
| EBikeRide | 243 | 3,943.3 | 208.6 | 2022-09 → 2026-08 |
| Workout | 328 | 76.3 | 286.9 | 2018-03 → 2026-01 |
| Walk | 76 | 251.0 | 63.1 | 2014-08 → 2023-08 |
| VirtualRide | 43 | 811.9 | 34.7 | 2018-10 → 2026-04 |
| Hike | 24 | 189.2 | 56.7 | 2015-05 → 2025-08 |
| AlpineSki | 12 | 317.0 | 33.0 | 2022-12 → 2024-02 |
| WeightTraining | 121 | 0.5 | 77.3 | 2018-03 → 2026-01 |
| Swim | 26 | 29.3 | 14.5 | 2022-09 → 2026-08 |
| Crossfit, Surfing, Snowshoe, StandUpPaddling, Rowing, Yoga, StairStepper | ~13 total | ~21 | ~9 | scattered |

By raw hours, Run (753.4h) is the single largest bucket, narrowly ahead of Ride (635.1h); combined cycling-family volume (Ride + EBikeRide + VirtualRide = 878.4h) edges out running when e-biking is included — a distinction that matters for the verdict since e-bike riding is a materially lower training stimulus than road cycling or running.

## Volume trajectory

Coverage-adjusted sessions/week and hours/week (against actual first/last activity date per year, not calendar-year length):

| Year | Coverage | Sessions/wk | Hours/wk | km/wk | Dominant mode |
|---|---|---|---|---|---|
| 2014 | May–Dec | 7.29 | 4.54 | 54.5 | Ride (159) + Run (93) |
| 2015 | full | 4.41 | 3.82 | 38.8 | **Run** (179 act., 174.8h) |
| 2016 | full | 5.47 | 4.57 | 52.2 | Run (157, 156.2h) ≈ Ride (127, 78.8h) |
| 2017 | full | 4.01 | 3.13 | 41.3 | Ride (158, 114.0h) |
| 2018 | full | 4.10 | 3.70 | 20.5 | Run (116, 106.4h) + strength (86.3h) |
| 2019 | full | 4.43 | 3.38 | 16.9 | Run (71, 74.2h) + Workout (62.7h) |
| 2020 | full | 2.89 | 2.70 | 20.6 | Workout (74.7h) — running collapses (13, 12.6h) |
| 2021 | full | **1.30** | **1.61** | 23.8 | **trough** — Ride 42.8h, Run only 15.6h |
| 2022 | Jul–Dec | 3.78 | 5.88 | 54.6 | Ride (40.8h); running nearly absent (1 act.) |
| 2023 | full | 4.97 | 4.49 | 54.2 | Ride (92.9h) + rebuilding base |
| 2024 | full | 2.89 | 2.89 | 47.9 | mixed — VirtualRide, ski, some Run return (32) |
| 2025 | full | 3.87 | 3.87 | 64.9 | **EBikeRide dominates** (118, 118.6h) |
| 2026 (YTD, to Aug 13) | 32.1wk | 3.67 | 2.99 | 50.8 | EBikeRide (67.2h) + rebuilding Run (27, 17.5h) |

Three distinct phases:

1. **Peak endurance-running phase (≈2015–2019).** Structured "SL" long-run progressions, marathon-pace blocks, racing every season. 2016 was the highest structured-hours year (238.9h total, Run 156.2h alone). This phase produced every running PR he currently holds.
2. **Detraining/trough (≈2020–2022).** 2021 is the clear nadir: 1.30 sessions/wk, 1.61 h/wk, running down to 18 activities/142.9 km for the entire year; 2022 logged just 1 run (12.1 km).
3. **Cycling-led partial rebuild → current running comeback (≈2023–2026).** Volume hours recover but composition shifts to Ride/EBikeRide. From late 2025 into 2026, running count picks back up (45 runs in 2025, 27 YTD 2026) alongside large EBikeRide volume that inflates raw hours without equivalent running-specific fitness. Matches Benjamin's own 2025-12-17 `fitness_assessments` goals: `["weight_loss","endurance","strength","general_fitness","comeback","stress_relief"]`, injuries field `"obese"`.

**Data-quality caveat**: the "Other" bucket conflates EBikeRide, Workout, Walk, Hike, WeightTraining across eras (Workout/strength dominant 2018–2021; EBikeRide dominant 2025–2026) — decomposed explicitly above so 2025/2026 volume isn't misread as equivalent-quality rebound to the 2015–2019 running base.

## Competitive performance

`activity_type = 'Run' AND distance > 20 km`, cross-referenced against `lifetime_prs`. Races flagged where the name states an official/net time or is a named public event; long training runs ("SL", "sortie longue") flagged as training.

| Date | Event / name | Dist (km) | Time | Pace (min/km) | Avg HR | Flag |
|---|---|---|---|---|---|---|
| 2015-03-07 | Semi Marathon de Paris (officiel 1:49:27) | 21.39 | 1:49:12 | 5:11 | 176 | **Race** |
| 2015-10-10 | 20km de Paris 2015 (officiel 1:40:06) | 20.25 | 1:40:12 | 4:57 | 179 | **Race** |
| 2016-03-05 | Semi de Paris (réel 1:40:18) | 21.21 | 1:40:18 | 4:44 | 172 | **Race** |
| 2016-04-02 | **Marathon de Paris (3:58:12)** | 42.34 | 3:58:18 | 5:38 | 172 | **Race** |
| 2016-10-08 | 20km de Paris (1:47:43) | 20.10 | 1:47:12 | 5:20 | 169 | **Race** |
| 2017-10-21 | Trail du Haut Planet | 24.51 | 2:58:00 | 7:16 | 174 | **Race** (524.7m D+) |
| 2018-04-07 | Semi marathon de Bourg-lès-Valence | 21.09 | 1:54:24 | 5:25 | 186 | **Race** |
| 2018-10-04 | Pointe de Marcelly | 21.64 | 3:49:12 | 10:35 | 171 | Mountain outing, 1,479.8m D+ (`lifetime_prs.highest_elevation_run`) |
| 2018-10-20 | Trail du haut planet (annual repeat) | 24.35 | 2:33:00 | 6:17 | 175 | **Race** |
| 2019-03-16 | **Semi de Rueil-Malmaison — PR 1:34:33** | 20.54 | 1:34:30 | 4:36 | 177 | **Race**, current half-marathon PR |
| 2019-04-13 | **Marathon de Paris — PR 3:39:55** | 42.99 | 3:37:04 | 5:03 | 173 | **Race**, current marathon PR |
| 2024-03-02 | Semi de Paris 2024 | 21.27 | 1:57:00 | 5:30 | 165 | **Race** — 22.5 min slower than 2019 PR |
| 2025-10-18 | Semi-marathon du Bois de Vincennes | 21.24 | 2:10:30 | 6:08 | 169 | **Race** — slowest recorded half, coincides with Q4-2025 weight/VO2max low point |

Confirmed current PRs (`lifetime_prs`): 5K 29:23 (2014-07-10), 10K 44:42 (2016-02-06), half marathon 1:34:33 (2019-03-16), marathon 3:39:55 (2019-04-13), longest run 42.99 km.

**Benchmarking** (general amateur/age-graded reference points, not a certified ranking): a 1:34:33 half marathon (4:29/km) sits comfortably in the top ~5–10% of finishers at a mass-participation French road race (median commonly cited ~1:50–2:00). A 3:39:55 marathon (5:12/km) is roughly top ~15–25% (median commonly cited ~4:15–4:30). The 44:42 10K and 29:23 5K are internally consistent with that pacing — a genuinely well-rounded, race-fit amateur profile in 2014–2019. The two most recent races (2024, 2025) are 20–36 minutes slower than the 2019 peak over the same/similar distance, directly reflecting the detraining/weight-gain years.

## Physiological markers

`garmin_health` only has data from **2023-09-30 onward** — no wearable trail for the 2015–2019 peak era; the trend below covers only the most recent ~3 years.

| Year-Q | VO2max running | VO2max cycling | RHR (bpm) | Avg steps/day |
|---|---|---|---|---|
| 2024 Q4 | n/a | n/a | n/a | **5,633 (low point)** |
| 2025 Q2 | 42.19 | 40.25 | 50.3 | 10,389 |
| 2025 Q3 | **43.17 (peak)** | **41.23 (peak)** | **48.5 (best)** | 9,131 |
| 2025 Q4 | 41.18 | 40.35 | 52.5 | 8,443 |
| 2026 Q1 | 40.90 | 39.39 | 53.0 | 10,831 |
| 2026 Q2 | **40.05 (low)** | 38.73 | 50.4 | 10,937 |
| 2026 Q3 (partial) | 42.04 | 38.97 | 49.3 | 10,621 |

Cross-checked against `fitness_assessments` (2025-12-17): VO2max running 40.9, cycling 40, RHR 51, HRV avg 35, readiness 91, `fitness_score 49.5/100` — sits right at the Q4-2025/Q1-2026 dip, corroborating it as real, not noise.

**Context (ACSM-style generic norms, men 40–49)**: Poor <36.7, Fair 36.7–40.4, Good 40.5–44.1, Excellent 44.2–51.4. Benjamin's tracked range (40.05–43.17) sits in the **"Good" band throughout**, brushing Good/Excellent at its 2025-Q3 best and Fair/Good at its 2026-Q2 worst. RHR (48–53 bpm every quarter) is consistently in the **"Athlete/Excellent"** bracket and didn't degrade nearly as much as VO2max during the dip — cardiac efficiency has stayed strong even through the body-composition setback. Steps show the same pattern: low at 2024 Q4 (5,633/day), sustained recovery to ~9,000–11,000/day from 2025 Q2 onward.

## Body composition trajectory

`withings_measurements`, filtered `weight_kg > 70`.

| Year | n | Avg weight (kg) | Avg fat % |
|---|---|---|---|
| 2015 | 188 | 86.90 (near career-low) | 21.98 (career-low) |
| 2019 | 227 | **86.34 (career-low weight)** | 21.48 |
| 2021 | 76 | 84.60 (annual low, sparse) | 21.34 |
| 2024 | 28 (low n) | 96.99 | 31.54 |
| 2025 | 23 (low n) | 103.48 | 28.02 |
| 2026 (YTD) | 19 (low n) | 104.08 | 26.98 |

**Correlation with training**: clean inverse relationship. Weight/fat% bottom out exactly during the two peak running years bracketing the 2019 marathon PR. The 2021 trough is followed almost immediately by the steepest weight regain in the dataset — quarterly low 81.55 kg (2021 Q1) → quarterly high 105.54 kg (2026 Q1), **+23.99 kg (+29.4%) over five years** — matching the running collapse and pivot to lower-impact cycling. Fat% follows the same arc: 21.34% (2021) → 31.54% (2024, "obese" by ACE ≥25% boundary for men) → 26.98% YTD 2026. Most recent readings (2026-08-02: 102.01 kg/25.2%; 08-04: 101.16 kg/25.8%; 08-11: 100.68 kg/25.9%) show an active downward trend in the last two weeks. Current weight (100.68 kg) is nearly back to the earliest-recorded 2011 baseline (102.28 kg avg) — over a decade of training has not yet produced durable body-composition gains relative to the start of the record, though the 2015–2019 trough shows it clearly can. At 178 cm, current BMI ≈ **31.8 (Obese Class I, WHO/CDC)**; 2015 low computes to BMI ≈26.9 (Overweight). BMI is blunt for a muscular endurance athlete (muscle mass ~71–72 kg per 2025–2026 readings), but the fat% trend corroborates the same story more granularly.

## The verdict

**Classification: a masters-age (42, M) recreationally-trained endurance athlete of demonstrated competitive-amateur running caliber (career-best half marathon 1:34:33, marathon 3:39:55, both age 35), currently in an active post-detraining reconditioning phase following a multi-year (≈2020–2024) volume collapse and weight/fat-percentage regain, with cardiovascular fitness markers holding up better than body composition.**

- **ACSM physical-activity classification**: current volume (2026 YTD: 3.67 sessions/wk, 2.99 h/wk, ~50.8 km/wk incl. e-bike) clears the ACSM/WHO minimum aerobic guideline (≥150 min/wk moderate or ≥75 min/wk vigorous) with margin — "**meets/exceeds public-health aerobic guidelines, regularly active**." Not yet back to the "highly trained competitive endurance athlete" tier of 2015–2019 (4–5+ h/wk structured running plus regular racing) — that tier is the explicit rebuild target per his own Dec-2025 self-assessment goals.
- **ACSM cardiorespiratory-fitness classification** (VO2max, men 40–49): consistently **"Good"**, brushing "Excellent" at 2025-Q3 best (43.17), briefly toward "Fair" at 2026-Q2 worst (40.05), recovering (42.04, mid-Q3 2026). RHR (48–53 bpm) sits in **"Athlete/Excellent"** throughout, decoupled from the weight/VO2max dip.
- **Mitchell classification** (dominant sport type): largest single-mode volume is **running (753.4h, Class IC — low static/high dynamic)**, with **road cycling as a strong secondary mode (635.1h, Class IIIC — moderate-high static/high dynamic** given trunk/arm-bracing). Together: a mixed high-dynamic, low-to-moderate-static endurance athlete profile — built for sustained aerobic output, not strength/power (WeightTraining/Workout only ~364h combined across 12 years).
- **Net read**: an athlete who has already proven a competitive-amateur running ceiling and retains "Good"-band VO2max plus elite-adjacent RHR, but whose body composition (BMI ~31.8, fat% ~26–27%) is at its least favorable point in the 12-year record outside the earliest 2011 baseline, and whose recent race times are 20+ minutes off peak. The most recent 3–6 months (rising run count, falling weight, recovering VO2max/steps) show the rebuild is underway, not stalled.

### Data-quality notes
- `garmin_health` has zero rows before 2023-09-30 — no VO2max/RHR trail for the 2015–2019 peak era.
- Withings sampling density varies enormously by year (10–227 readings/year); years with n<30 are directionally reliable but individually noisier.
- `muscle_mass_kg` null in all Withings records before 2025.
- Race-vs-training-run flags on the >20km list are inferred from activity names/patterns, not an authoritative race calendar.

---

# PART 2 — Objectives Tracker

## Live status (this refresh, 2026-08-15)

| Objective | Domain | Priority | Target | Live value | Progress | Trajectory | Confidence | Δ vs 08-08 |
|---|---|---|---|---|---|---|---|---|
| Protéines ≥160g/j | nutrition | high | 160 g/day (avg_30d) | 40.78 g (30d incl. zero-days); 122.35 g avg on the 10 logged days | -167% (literal metric) | Stalled/regressing — 3rd blackout-relog-blackout cycle | **15** | +7 |
| Reprendre la course 3x/sem | habit | high | ≥3 runs/wk | 1 run this ISO week (Run #27, 4.23km, 8/12) | 33% this week | Regressing this week (travel-driven); 100% trailing 4-wk hit-rate | **40** | -15 |
| Descendre à 95 kg | body_composition | high | ≤95 kg | 100.68 kg (Withings, 8/11) | 44.4% | Ahead/on track — pace 0.395 kg/wk (7.6wk) & 0.297 kg/wk (full baseline) both ≥ required 0.290 kg/wk | **48** | +3 |
| Bilan sanguin complet annuel | health | high | panel done | No new labs since 2025-12-01; Vitamin D retest still not done (6+ wks overdue) | n/a | On track (annual cadence); sub-item slipping | **35** | -5 |
| Sortie 12 km Beaumonts | performance | medium | ≥12 km | 10.5 km (Run #20, 7/25, unchanged) | 75.8% | Weakening — SL progression missed twice (#26 -35% vs target; #29 not attempted) | **47** | -10 |
| Semi-marathon <1h45 | performance | medium | ≤105 min | no race scheduled | n/a | Stalled — fully gated | **20** | -5 |
| Retour compétiteur amateur (rollup) | performance | high | semi<1h45 & <95kg | rollup of above | mixed | Net slightly negative this cycle | **28** | -3 |

*Live-value computation notes: protein = `AVG(total_protein_g)` over `oh_daily_nutrition_summary`, 7/16–8/15, 10/30 days logged, with an explicit fresh zero-day on 8/14 breaking the prior 10-day relog streak. Weight = latest `withings_measurements.weight_kg>70` row (8/11); fat% trend 26.8%→25.2%→25.8%→25.9% (6/6→8/11), roughly flat/slightly improving — recent weight drop doesn't read as pure water/muscle loss. Long-run = `MAX(distance)` on Run/TrailRun since block start 6/14, unchanged since 7/25. Running frequency = manual weekly count from `strava_activities` (no source_table configured on this objective). Training-load context: `training_load_daily` chronic_load_28d declining 29.25→24.74, `training_status` → "Detraining" over 8/4–8/13; `garmin_health` RHR drifting 49→55 bpm over the same window while HRV holds flat/BALANCED at 35–37 — consistent with travel suppressing training/recovery mildly, not illness.*

## Coherence across objectives

**Dependency graph**: rollup (`a0000000`) ← weight (`218d1c78`), running-frequency (`a1bde447`, gates the running leg), long-run (`9b982443`), semi (`96910249`, fully gated by frequency + long-run). Bloodwork (`42361937`) is structurally independent.

**Critical path**: running-frequency → long-run → semi → rollup. Running frequency is the single most load-bearing node, and it's the objective that just broke its live streak.

**Conflicts / competing constraints**:
1. **Time/recovery budget**: the Saint-Malo trip (8/11–15+) is the proximate cause of both misses this week — one external constraint eating into two objectives on the critical path simultaneously.
2. **Fat-loss vs. training-volume**: weight-loss pace (0.29–0.40 kg/wk, ~0.3–0.4%/wk of ~101kg) sits safely under the 0.5–1%/wk evidence-based ceiling, and fat% is trending down in parallel with weight, not flat — reassuring, not alarming.
3. **Protein × weight-loss cross-domain risk**: a calorie deficit combined with repeated full-zero protein-logging days (average only 122g even on logged days vs. the 160g/1.6g·kg⁻¹ target) is the textbook setup for lean-mass loss during a cut. Fat% holding steady is mildly reassuring but not conclusive — a genuine coherence risk between the protein and weight objectives, not just a logging-habit nuisance.
4. **Bloodwork** competes with nothing but its own sub-item (Vitamin D retest) is the clearest example of a zero-cost/no-deadline task quietly slipping.

## Confidence rationale (0–100)

- **Protein (15, ↑7)**: demonstrated 10-day capability (avg 122g/day when logged, several days ≥150g) is a real positive, but a third blackout cycle (fresh zero 8/14) means the habit isn't yet stable. Target (1.6 g/kg) is fully realistic — this is 100% behavioral.
- **Running 3x/wk (40, ↓15)**: four consecutive weeks at target (W29–W32) was a genuine habit as of 8/8; W33 broke it with 1 day left to recover, travel-driven not physiological (HRV stable, no illness signal). Historical precedent of recovering after travel gaps keeps this from scoring lower.
- **Weight ≤95kg (48, ↑3)**: trailing pace now slightly exceeds required pace on two lookback windows — genuine trajectory improvement. Tempered by a 4-day Withings gap and a rate that's within, not comfortably above, the evidence-based band.
- **Bilan sanguin (35, ↓5)**: annual-panel time budget still fine (137 days left), but Vitamin D sub-item has sat untouched 6+ weeks past its informal due date with zero new observations — concrete slippage risk.
- **Beaumonts 12km (47, ↓10)**: the arithmetic gap (1.5km, 0.14km/wk required) is trivial in isolation — the downgrade is plan-adherence: two consecutive under-executed/missed SL sessions erode the staged progression and compress buffer before the early-Sept attempt window.
- **Semi <1h45 (20, ↓5)**: fully gated by two objectives that both had a net-negative week; still no race scheduled with 7.5 months runway. 2019 PR (1:34:33) remains a strong tailwind if the gating objectives recover.
- **Rollup (28, ↓3)**: weighted mix of a strengthening leg (weight) and a freshly weakened gating dependency (running frequency). Net slightly negative.

**Physiological plausibility**: weight-loss rate (0.3–0.4%/wk) is within/conservative vs. the 0.5–1%/wk range. Protein target (1.6 g/kg) is standard for an endurance athlete his size. The 12km long-run target implies a 14% total-distance increase over ~7 remaining weeks — normal endurance-rebuild progression, not a hero jump. No objective in the set has a physiologically unrealistic implied rate; every shortfall identified is behavioral/logistical, not adaptation-rate-limited.

## Narrative synthesis

The seven objectives are mostly compatible but share exactly one finite resource this week: time and routine, consumed by the Saint-Malo trip. That single external event is the proximate cause of the two worst pieces of fresh news — the running-frequency streak breaking after four clean weeks, and the long-run objective's SL rung going unexecuted for the second week running. Both sit on the same critical path, so one travel week has simultaneously dented three of the four objectives feeding the master rollup. This is a timing/scheduling issue, not a physiological one: HRV is flat and the RHR drift (49→55 bpm) is mild and travel-shaped, not an illness or overtraining signal.

Separately, there is a quieter but structurally more important cross-domain risk: the calorie deficit driving the (currently ahead-of-pace) weight objective is running in parallel with a protein-logging pattern that undershoots the 160g target even on its best days and hits zero on its worst. Stable fat% is a reassuring proxy but not proof lean mass is protected — this is the one place where two active objectives could be quietly working against each other rather than just competing for a calendar slot.

The bloodwork objective is the outlier: fully decoupled from training/weight, technically still on its annual cadence, but its one sub-task (Vitamin D retest) is the clearest example in the whole set of a zero-cost item slipping purely from lack of a trigger.

**Single highest-leverage action right now**: get a run in on Sunday 8/16 before the trip ends — the cheapest available intervention (one session) with the largest downstream effect, since running-frequency is the one node whose failure this week is dragging down three other confidence scores through the dependency graph. Close behind it, and entirely independent of the travel constraint: close the protein-logging gap — worst-scoring objective in the set, zero recovery cost, and its own demonstrated 10-day capability (122g/day average when logged) shows the fix is adherence, not physiology or time.

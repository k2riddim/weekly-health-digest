# Weekly Athletic Profile & Objectives Review — 2026-07-11

## Data note (system health)

No daily-digest run appears to have ever persisted to this repository: `state/history/` and `digests/` are empty, and `state/latest.json` is frozen at `as_of_date: 2026-06-14` (27 days stale) despite the objectives table itself carrying live refreshes through 2026-07-04. The Google Calendar / daily replanning pipeline described in `CLAUDE.md` therefore has **no confirmed committed output** — either it isn't running on schedule or its Phase 6 commit step is failing. Recommend checking the daily-digest automation/scheduler directly; this weekly review cannot substitute for it (no rolling 7-day calendar plan, no daily deltas).

---

# PART 1 — Athletic Profile Classification

## 1. Raw numbers (lifetime, 2014-05-01 → 2026-07-08, ~12.2 years)

- **2,431 activities**, **24,380 km**, **2,152 hours** (~90 days of continuous training time)
- Top modalities by distance: Ride 11,983 km (742 acts, 635 h) · Run 6,984 km (818 acts, 744 h) · EBikeRide 3,719 km (230 acts, 197 h, commuting) · VirtualRide 812 km (43 acts) · Workout 328 acts / 287 h (gym, no distance) · WeightTraining 121 acts / 77 h · Walk 251 km (76 acts) · Hike 189 km · Swim 28 km (23 acts) · AlpineSki 317 km (12 acts)
- Age 42 (b. 1983-09-25), male, 178 cm, blood type O-.

## 2. Volume trajectory — distinct phases

| Phase | Years | Sessions/wk | Hours/wk | Character |
|---|---|---|---|---|
| A — Marathon build #1 | 2015–2016 | 4.4–5.5 | 3.8–4.5 | Run-dominant (179 runs/1,692 km in 2015 alone); culminates in marathon debut |
| B — Cycling pivot | 2017 | ~3.1 (Ride 158 acts) | ~2.5 | Run collapses to 46 acts/300 km; road cycling volume peaks (1,812 km) |
| C — Marathon build #2 / lifetime peak fitness | 2018–2019 | 4.0–4.4 | 3.2–3.4 | Run + WeightTraining + Workout combined; produces both lifetime PRs |
| D — COVID / gym-only | 2020–2021 | ~2.5–3.5 | ~1.5–2.0 | Running nearly disappears (13–18 acts/yr); home Workout dominant |
| E — Recreational multisport, historical chronic-load peak | 2022–2023 | ~4.1 | ~4.2 | Cycling-led (2023: 56 rides/2,123 km, 38 km avg) + Walk/Workout/Swim mix; this is the year stored in `state/historical-peak.json` (chronic_load_28d_peak = 2,100) |
| F — Decline / post-paternity trough | 2024–2025 | ~1.5–2.0 | ~1.3–1.6 | Run 32–45 acts/yr only; weight climbs from ~91 kg (2022) to 103.5 kg avg (2025); half marathon Oct 2025 run at 2:10:30 (6:08/km) — a 36-min regression vs. the 2019 PR pace |
| G — Return-to-running comeback (active) | May 2026 → present | ~1.15 structured + e-bike commuting | ~0.7 h structured/wk (+ ~2.1 h/wk e-bike commuting, 1,068 km YTD) | 14 runs since 2026-05-02, distances 1.25–7.51 km, HR-capped Z1-Z2 rebuild under `protocols/return-to-running.md` |

The 2023 "historical peak" was a **cycling-and-diversification** peak, not a running peak — Benjamin's best *running-specific* fitness was Phase C (2018–2019), not the chronologically-stored `historical-peak.json` reference year. Worth keeping distinct when interpreting "% of peak" in the daily digest: it measures aggregate training-load capacity, not running readiness.

## 3. Competitive performance

| Date | Race | Distance | Time | Pace | Note |
|---|---|---|---|---|---|
| 2015-03-07 | Semi Marathon de Paris | 21.1 km | 1:49:27 | 5:11/km | |
| 2015-10-10 | 20 km de Paris | 20.0 km | 1:40:06 | 5:00/km | |
| 2016-04-02 | Marathon de Paris (debut) | 42.2 km | 3:58:12 | 5:38/km | |
| 2016-10-08 | 20 km de Paris | 20.0 km | 1:47:43 | 5:23/km | |
| 2018-04-07 | Semi de Bourg-lès-Valence | 21.1 km | ~1:54:24 | 5:25/km | HR 185.7 avg — near-maximal effort |
| **2019-03-16** | **Semi de Rueil-Malmaison** | **21.1 km** | **1:34:33** | **4:29/km** | **Lifetime half-marathon PR** |
| **2019-04-13** | **Marathon de Paris (PR)** | **42.2 km** | **3:39:55** | **5:06/km** | **Lifetime marathon PR** |
| 2024-03-02 | Semi de Paris | 21.1 km | 1:57:00 | 5:30/km | Post-2019 fitness already receding |
| 2025-10-18 | Semi-marathon Bois de Vincennes | 21.1 km | 2:10:30 | 6:08/km | Trough-era result, +36 min vs. PR |

**Benchmarking**: 1:34:33 for a half marathon is competitive-amateur territory in France — roughly top 5–10% of finishers in typical open road races (club-runner pace, ~4:29/km sustained). 3:39:55 for a marathon is comfortably sub-4:00 and above the median amateur finisher. Both PRs stand from the 2018–2019 build; nothing since has come close. **The current objective — half marathon sub-1:45 (105 min) — is ~11 minutes slower than Benjamin's demonstrated 2019 ceiling**, meaning it is a return-to-form target, not a stretch target, contingent on rebuilding the aerobic base and losing the ~18 kg gained since 2021.

## 4. Physiological markers (quarterly)

| Metric | 2025 Q2 | 2025 Q3 | 2025 Q4 | 2026 Q1 | 2026 Q2 | 2026 Q3 (partial) |
|---|---|---|---|---|---|---|
| VO2max running | 42.2 | 43.2 | 41.2 | 40.9 | 40.1 | 41.4 |
| VO2max cycling | 40.3 | 41.2 | 40.4 | 39.4 | 38.7 | 38.6 |
| RHR | 50.3 | 48.5 | 52.5 | 53.0 | 50.4 | 49.5 |
| Steps/day | 10,389 | 9,131 | 8,443 | 10,831 | 10,937 | 9,384 |

At age 42, VO2max running of ~40–41 ml/kg/min sits at the **Fair–Good boundary** on ACSM age-graded norms for men 40–49 (Fair 38.5–41.6, Good 41.7–45.3) — a step below the "Good" band and well below what his historical performances imply for his 2019 self. It bottomed in 2026 Q2 (40.1, coincident with peak body weight) and is now recovering (41.4 Q3) alongside the running comeback. RHR (48–53 bpm) sits at the **Excellent–Good boundary** and never fully deconditioned — a favorable sign, since cardiac/autonomic fitness is historically the slower marker to lose and the faster one to reconstitute. Daily steps (9,000–11,000) reflect a genuinely active lifestyle (e-bike commuting) independent of structured training, a solid NEAT floor to rebuild on.

**Mitchell classification**: running and cycling are High Dynamic / Low-to-Moderate Static components (Class IIIA–IIIC depending on intensity) — a favorable, low structural/pressor-risk profile for continued endurance loading.

## 5. Body composition trajectory

Weight and fat% by year (Withings, weight_kg > 70 filter):

| Year | Avg weight (kg) | Avg fat % |
|---|---|---|
| 2015 (lean low) | 86.9 | 22.0 |
| 2019 (2nd marathon PR) | 86.3 | 21.5 |
| 2021 (lifetime lean low) | 84.6 | 21.3 |
| 2022 | 91.4 | 25.4 |
| 2023 | 94.8 | 27.9 |
| 2024 | 97.0 | 31.5 |
| 2025 | 103.5 | 28.0 |
| 2026 YTD | 104.6 | 27.4 |

Body composition tracks training volume almost 1:1 — every low-volume phase (2017, 2020–2021 excepted since 2021 is the lean outlier from sustained cycling, 2022–2025) corresponds to a weight/fat% increase, and every high-run-volume phase (2015, 2018–2019) corresponds to the leanest readings. The ~+20 kg swing from 2021 (84.6 kg) to the 2025/26 average (~104 kg) is the single largest driver of both the VO2max regression and the half-marathon pace regression — this is a body-composition story as much as a training-load story. Latest reading (2026-06-20): 103.67 kg, 26.3% fat — down 1.5 kg from the comeback baseline (105.22 kg, late April), the first sustained downtrend since 2021.

## 6. The verdict

**Master's-age (42) recreational endurance athlete in an active, structured post-layoff/post-paternity rebuild, with a demonstrated competitive-amateur ceiling (sub-1:35 half marathon, sub-3:40 marathon, both 2018–2019) that current fitness sits well below.** Cardiorespiratory fitness (VO2max ~40–41 ml/kg/min) currently classifies as **Fair-to-Good** per ACSM age-graded norms — below his historical implied ceiling — while resting cardiac fitness (RHR 48–52 bpm, Excellent-Good) has been comparatively well-preserved, indicating the deficit is more body-composition- and volume-driven than a loss of trained cardiac capacity. Mitchell classification places his sports (running/cycling) in the low-risk High-Dynamic category, supporting continued progressive endurance loading. He is 9 weeks into a deliberately conservative return-to-running protocol (14 sessions, 1.25–7.51 km, HR-capped Z1-Z2) layered on an e-bike-commute aerobic base — physiologically on track (ACWR currently ~1.10, mid-band, well under the comeback ceiling of 1.5) but **behaviorally inconsistent**, with running frequency decelerating rather than accelerating over the past three weeks (see Part 2).

---

# PART 2 — Objectives Tracker

## Active objectives — live status (refreshed 2026-07-11)

| # | Objective | Baseline | Current (live) | Target | Progress | Confidence |
|---|---|---|---|---|---|---|
| 1 | Reprendre la course 3x/semaine (habit) | — | **1.0 runs/wk** (rolling 4wk: 6/13,6/20,6/27,7/4) — but **0 runs in the trailing 7 days**, last session 2026-07-04 | 3/wk by 2026-09-29 | 33% of target rate | **18%** |
| 2 | Courir jusqu'au Parc des Beaumonts (12 km) | 5.8 km | **7.51 km** (max since 6/15, unchanged 3 weeks — last 3 runs: 7.51 → 3.48 → 6.00 km) | 12 km by 2026-10-30 | 27.6% | **30%** |
| 3 | Descendre à 95 kg | 105.22 kg | **103.67 kg** (stale — no Withings sync in 21 days) | 95 kg by 2026-12-30 | 15.4% of Δ | **30%** |
| 4 | Semi-marathon < 1h45 | — | no recent race | 105 min by 2027-03-30 | n/a | **25%** |
| 5 | 160 g protéines/jour (30d avg) | 115.4 g (7/4) | **107.6 g** — moving *away* from target | 160 g by 2026-09-29 | -14.9pp regression | **20%** |
| 6 | Bilan sanguin complet annuel | — | last full panel 2025-12-01 (7 mo ago); Vitamin D retest specifically due ~2026-07 per prior state, not yet scheduled | by 2026-12-30 | on track for annual cadence, Vit-D component overdue | **65%** |
| 7 | Retour au niveau compétiteur (global, parent) | — | rolls up #3 + #4 | by 2027-06-29 | — | **25%** |
| — | FTP Zwift 200W | — | — | — | **abandoned** (2026-06-15, per user request) | n/a |

## Step 3 — Progress & trajectory detail

- **Running frequency (#1)** is the load-bearing bottleneck. May's comeback opened at a near-weekly cadence (5 sessions in the first 5 weeks); June widened the gaps (weekly → 9-day gaps); the most recent 7 days (2026-07-05 → 2026-07-11) logged **zero** running activity — only e-bike commuting (4 rides, 76 km, 3.9 h). This is a deceleration, not a plateau: rolling cadence has gone from the intended ramp to reverse.
- **Long run (#2)** has not moved past the 7.51 km set on 2026-06-20; the two subsequent runs were *shorter* (3.48 km, 6.00 km) — consistent with restarting after the frequency gaps rather than building on the prior long effort.
- **Weight (#3)**: pace since baseline is -0.197 kg/wk (105.22 → 103.67 over ~8 weeks) against a required -0.339 kg/wk to hit 95 kg by 2026-12-30. Projected weight at the deadline on current pace ≈ **98.8 kg**, ~3.8 kg short. Note this pace (0.19% bodyweight/wk) is well *inside* the evidence-based safe fat-loss range (0.5–1%/wk ≈ 0.52–1.04 kg/wk) — the shortfall is a rate problem, not a safety problem; there is headroom to accelerate safely if nutrition adherence improves.
- **Protein (#5)** moved the wrong direction week-over-week (115.4 g → 107.6 g, -6.8%), despite continued logging discipline (31 days tracked). This directly undercuts #3: adequate protein is the primary lever for preserving lean mass and satiety during the deficit implied by the weight objective.
- **Half marathon (#4)**: no live signal (no race in the window); entirely dependent on #1 and #2 resolving first.
- **Bloodwork (#6)**: no annual gap risk yet (last panel 7 months ago vs. 12-month target cadence), but the Vitamin D-specific retest flagged in `state/latest.json` (25 ng/mL, low, tested 2025-12-01) as "due ~July 2026" has not been scheduled.

## Step 4 — Coherence across objectives

- **Critical path**: #1 (running frequency) gates #2 (long run) and #4 (half marathon) and materially supports #7 (global comeback). It is currently the *worst-performing* objective (18% confidence) while being the prerequisite for two others — fixing it has the highest leverage of anything on this list.
- **Shared root cause**: #3 (weight) and #5 (protein) are linked by design (`notes` on #5 flags this from the prior cycle) — and the link is currently working against Benjamin: protein intake fell as weight-loss pace stayed flat, i.e., the nutrition lever isn't being pulled.
- **Not a physiological conflict**: ACWR is comfortably mid-band (~1.10 as of 2026-07-08, comeback ceiling 1.5) — there is no injury-risk reason for the frequency shortfall. The bottleneck reads as behavioral/scheduling (e-bike commuting may be substituting for run slots) rather than a tissue-tolerance or overtraining constraint.
- **Possible headwind**: HRV dipped to 29 ms on 2026-07-10 (well below the 7d avg of ~35–37) and body battery has trended down over the last 5 days (48→42→48→34→27) alongside a sleep-score dip (71 last night). This is a plausible — not confirmed — contributor to the frequency gap this past week; worth one or two more days of observation before treating it as a trend (this repo has no access to the cohabitant/baby sleep connector in this session to cross-check for infant-driven sleep fragmentation).
- **Target-date tension**: #1's 2026-09-29 deadline (11 weeks out) requires roughly tripling current cadence with zero slack; #5's identical deadline has the same problem. Both were set on 2026-04-26 before the June/July deceleration was visible — worth revisiting the dates rather than the targets themselves once frequency stabilizes.

## Step 5 — Highest-leverage action

**Restore running frequency to ≥2x/week this week, independent of distance.** This is the single objective gating the most downstream progress (#2, #4, #7) and is currently the furthest below plan (18% confidence, actively regressing) despite having the most physiological headroom to act on safely (ACWR mid-band, well under the comeback ceiling). Two consistent short runs (even 15–20 min) this week matter more right now than one longer run — consistency, not distance, is the binding constraint. Concretely for the daily/rolling training plan: prioritize scheduling and protecting run slots over incremental distance progression until the 4-week rolling cadence is back above 2/week.

---
*Full query trail available on request. Objectives table refreshed live via `upsert_objective` for #1–#5 on 2026-07-11. Next weekly review: 2026-07-18.*

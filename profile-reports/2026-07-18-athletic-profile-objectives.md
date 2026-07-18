# Weekly Athletic Profile & Objectives Review — 2026-07-18

## Data note (system health)

Still no confirmed daily-digest output on this branch line: `state/history/` and `digests/` remain empty, and `state/latest.json` is still frozen at `as_of_date: 2026-06-14` (34 days stale) — unchanged since the last review flagged this on 2026-07-11. The objectives table itself continues to receive live weekly refreshes (most recently through 2026-07-18), so this weekly review is not blocked, but the daily rolling-plan / calendar pipeline described in `CLAUDE.md` still has no evidence of running end-to-end. Recommend checking the daily-digest automation/scheduler directly.

---

# PART 1 — Athletic Profile Classification

## 1. Raw numbers (lifetime, 2014-05-01 → 2026-07-16, ~12.2 years)

- **2,434 activities**, **24,393 km**, **2,154 hours** (~90 days of continuous training time)
- Top modalities by distance: Ride 11,983 km (742 acts, 635 h) · Run 6,996 km (820 acts, 746 h) · EBikeRide 3,719 km (230 acts, 197 h, commuting) · VirtualRide 812 km (43 acts) · Workout 328 acts / 287 h (gym, no distance) · WeightTraining 121 acts / 77 h · Walk 251 km (76 acts) · Hike 189 km (24 acts) · AlpineSki 317 km (12 acts) · Swim 29 km (24 acts)
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
| G — Return-to-running comeback (active) | May 2026 → present | ~1.2 structured (16 runs / ~76 days) + e-bike commuting | ~0.7 h structured/wk (+ ~2 h/wk e-bike commuting) | 16 runs since 2026-05-03, distances 1.25–8.03 km, HR-capped Z1-Z2 rebuild under `protocols/return-to-running.md`; first cross-training swim of the comeback logged 2026-07-16 |

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

**Benchmarking**: 1:34:33 for a half marathon is competitive-amateur territory in France — roughly top 5–10% of finishers in typical open road races (club-runner pace, ~4:29/km sustained). 3:39:55 for a marathon is comfortably sub-4:00 and above the median amateur finisher. Both PRs stand from the 2018–2019 build; nothing since has come close. **The current objective — half marathon sub-1:45 (105 min) — is ~11 minutes slower than Benjamin's demonstrated 2019 ceiling**, meaning it is a return-to-form target, not a stretch target, contingent on rebuilding the aerobic base and losing the ~18 kg gained since 2021. No race since Oct 2025; no new data this cycle.

## 4. Physiological markers (quarterly)

| Metric | 2025 Q2 | 2025 Q3 | 2025 Q4 | 2026 Q1 | 2026 Q2 | 2026 Q3 (partial, thru 7/16) |
|---|---|---|---|---|---|---|
| VO2max running | 42.2 | 43.2 | 41.2 | 40.9 | 40.1 | 41.5 |
| VO2max cycling | 40.3 | 41.2 | 40.4 | 39.4 | 38.7 | 38.6 |
| RHR | 50.3 | 48.5 | 52.5 | 53.0 | 50.4 | 49.6 |
| Steps/day | 10,389 | 9,131 | 8,443 | 10,831 | 10,937 | 11,187 |

At age 42, VO2max running of ~40–41 ml/kg/min sits at the **Fair–Good boundary** on ACSM age-graded norms for men 40–49 (Fair 38.5–41.6, Good 41.7–45.3) — a step below the "Good" band and well below what his historical performances imply for his 2019 self. It bottomed in 2026 Q2 (40.1, coincident with peak body weight) and continues recovering into Q3 (41.5) alongside the running comeback and the two longer July sessions. RHR (48–53 bpm) sits at the **Excellent–Good boundary** and never fully deconditioned — a favorable sign, since cardiac/autonomic fitness is historically the slower marker to lose and the faster one to reconstitute. Daily steps (9,000–11,000, now trending to ~11,200 in Q3) reflect a genuinely active lifestyle (e-bike commuting) independent of structured training, a solid NEAT floor to rebuild on.

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

Body composition tracks training volume almost 1:1 — every low-volume phase (2017, 2020–2021 excepted since 2021 is the lean outlier from sustained cycling) corresponds to a weight/fat% increase, and every high-run-volume phase (2015, 2018–2019) corresponds to the leanest readings. The ~+20 kg swing from 2021 (84.6 kg) to the 2025/26 average (~104 kg) is the single largest driver of both the VO2max regression and the half-marathon pace regression. **Latest reading is still 2026-06-20 (103.67 kg, 26.3% fat) — 28 days stale, no new Withings sync this cycle.** The last confirmed downtrend (105.22 → 103.67 kg since late April) has not been re-confirmed; the weigh-in gap is itself a signal worth naming (see Part 2, objective #3).

## 6. The verdict

**Master's-age (42) recreational endurance athlete in an active, structured post-layoff/post-paternity rebuild, with a demonstrated competitive-amateur ceiling (sub-1:35 half marathon, sub-3:40 marathon, both 2018–2019) that current fitness sits well below.** Cardiorespiratory fitness (VO2max ~40–41.5 ml/kg/min) currently classifies as **Fair-to-Good** per ACSM age-graded norms — below his historical implied ceiling — while resting cardiac fitness (RHR 48–52 bpm, Excellent-Good) has been comparatively well-preserved, indicating the deficit is more body-composition- and volume-driven than a loss of trained cardiac capacity. Mitchell classification places his sports (running/cycling) in the low-risk High-Dynamic category, supporting continued progressive endurance loading. He is 11 weeks into a deliberately conservative return-to-running protocol (16 sessions, 1.25–8.03 km, HR-capped Z1-Z2) layered on an e-bike-commute aerobic base — physiologically on track (ACWR currently ~1.37, mid-band, well under the comeback ceiling of 1.50) with a **genuine but fragile improvement** this cycle: after a zero-run week (flagged 7/11), the trailing 7 days produced 2 runs, one of which (8.03 km, Saint-Malo) set a new demonstrated-tolerance high. Frequency remains the binding constraint (see Part 2), and this week's uptick is one data point, not yet a trend.

---

# PART 2 — Objectives Tracker

## Active objectives — live status (refreshed 2026-07-18)

| # | Objective | Baseline | Current (live) | Target | Progress | Confidence |
|---|---|---|---|---|---|---|
| 1 | Reprendre la course 3x/semaine (habit) | — | **2 runs in trailing 7d** (7/12, 7/14) — 4wk rolling cadence still 1.0/wk (6/27:1, 7/4:1, 7/11:0, 7/18:2); no run in 4 days since 7/14 | 3/wk by 2026-09-29 | 67% of target rate this week, 33% on 4wk trend | **24%** (↑ from 18%) |
| 2 | Courir jusqu'au Parc des Beaumonts (12 km) | 5.8 km | **8.03 km** (new max, 2026-07-14, up from 7.51 km 3-week plateau) | 12 km by 2026-10-30 | 35.9% | **38%** (↑ from 30%) |
| 3 | Descendre à 95 kg | 105.22 kg | **103.67 kg** (stale — no Withings sync in 28 days) | 95 kg by 2026-12-30 | 15.4% of Δ | **25%** (↓ from 30%) |
| 4 | Semi-marathon < 1h45 | — | no recent race | 105 min by 2027-03-30 | n/a | **25%** (unchanged) |
| 5 | 160 g protéines/jour (30d avg) | 115.4 g (7/4) | **81.8 g literal avg** (nutrition logging stopped for 9 straight days, 7/9–7/17; true avg on logged days = 115.2 g, essentially flat) | 160 g by 2026-09-29 | logging artifact, not a real regression | **18%** (↓ from 20%) |
| 6 | Bilan sanguin complet annuel | — | last full panel 2025-12-01 (7.5 mo ago); Vitamin D retest still not scheduled, now further overdue | by 2026-12-30 | on track for annual cadence, Vit-D component increasingly overdue | **55%** (↓ from 65%) |
| 7 | Retour au niveau compétiteur (global, parent) | — | rolls up #3 + #4 | by 2027-06-29 | — | **27%** (↑ from 25%) |
| — | FTP Zwift 200W | — | — | — | **abandoned** (2026-06-15, per user request) | n/a |

## Step 3 — Progress & trajectory detail

- **Running frequency (#1)** is still the load-bearing bottleneck, but shows the first positive signal in three cycles. After zero runs in the 7 days ending 2026-07-11, the following week logged 2 runs (2026-07-12, 4.53 km; 2026-07-14, 8.03 km — both from Saint-Malo, suggesting a travel/holiday window opened up training time). But the 4-week rolling cadence is unchanged at 1.0/wk, and there has been no run in the 4 days since 7/14 (today is Saturday 2026-07-18 — a plausible running day). One good week does not yet resolve the deceleration flagged last cycle.
- **Long run (#2)** broke its 3-week plateau: 8.03 km on 2026-07-14 vs. the prior max of 7.51 km (2026-06-20). Notably this came from only the second run of the week, not a build on consecutive sessions — consistent with demonstrated tolerance being higher than the recent cadence has been testing. Per the return-to-running protocol's anti-clamping rule (§4F), this overshoot should raise the working long-run target, not be treated as an outlier to discount.
- **Weight (#3)**: no new Withings data since 2026-06-20 — the gap has grown from 21 to 28 days. Pace calculations are unchanged from last cycle (-0.197 kg/wk actual vs. -0.339 kg/wk required), but the growing weigh-in gap is now a standalone engagement signal independent of the underlying trend.
- **Protein (#5)**: the literal 30-day average cratered to 81.8 g, but this is entirely a logging artifact — 9 consecutive zero-logged days (2026-07-09 through 2026-07-17). Restricting to the 22 days actually logged in the last 30, the average is 115.2 g, essentially unchanged from the 115.4 g baseline recorded 2026-07-04. The real signal is that nutrition logging itself stopped for over a week, which happens to overlap with the travel window that also disrupted running — worth naming as one disruption (travel/routine break) with two downstream effects (frequency dip, then logging gap), rather than two independent problems.
- **Half marathon (#4)**: no live signal; unchanged.
- **Bloodwork (#6)**: annual cadence still fine (7.5 months since last panel vs. 12-month target), but the Vitamin D-specific retest (27 ng/mL, low, tested 2025-12-01, flagged "due ~July 2026") remains unscheduled with no action taken across two consecutive weekly reviews.

## Step 4 — Coherence across objectives

- **Critical path unchanged**: #1 (running frequency) still gates #2 (long run) and #4 (half marathon), and materially supports #7 (global comeback). Its confidence improved (18%→24%) but it remains the lowest-confidence objective with the most downstream dependents.
- **A plausible shared cause emerged this cycle**: the running dip (0 runs 7/5–7/11) and the nutrition-logging gap (0 logged days 7/9–7/17) overlap almost exactly in time, and both runs that did happen were logged from Saint-Malo — consistent with a single travel/routine disruption affecting both training and logging discipline, rather than two unrelated regressions. If so, the fix for both is the same: re-establish routine post-travel, not two separate interventions.
- **Not a physiological conflict**: ACWR is comfortably mid-band (~1.37 as of 2026-07-16, comeback ceiling 1.50) — no injury-risk reason for the frequency shortfall or a reason to throttle the plan. HRV and sleep in the trailing week (HRV weekly avg 34–37, sleep 5.8–8.0h with one short night 7/11) look broadly stable, slightly better than the 7/11 review's readout (HRV 29 → 40 by 7/16). No cohabitant/baby-sleep cross-check available in this session.
- **Weight (#3) and protein (#5) shared-root-cause link** is now harder to evaluate: the protein number is a measurement artifact this cycle, not necessarily a real adherence collapse, so drawing a causal line to the flat weight trend is weaker evidence than last cycle implied.
- **Target-date tension** flagged last cycle stands: #1's and #5's 2026-09-29 deadlines (10 weeks out) still require a large acceleration from current trend. Worth revisiting dates once (if) the frequency trend actually turns, rather than reacting to this single good week.

## Step 5 — Highest-leverage action

**Confirm whether running frequency and nutrition logging are genuinely turning around, or whether this was a one-off travel week.** The single most informative near-term data point is what happens in the 7 days starting today (2026-07-18, a Saturday with no run since Tuesday 7/14): a third run this week would break the 1.0/wk rolling-average ceiling that has held for a month; resumed nutrition logging would resolve whether protein intake is actually on track (115g logged-day average) or genuinely regressing. Until then, treat this cycle's improvement as encouraging but unconfirmed — the highest-leverage action for the daily/rolling training plan is still to prioritize scheduling and protecting run slots (now with the added latitude that 8 km is demonstrated-tolerable) over pushing distance further before frequency stabilizes.

---
*Full query trail available on request. Objectives table refreshed live via `upsert_objective` for all 7 active objectives on 2026-07-18. Next weekly review: 2026-07-25.*

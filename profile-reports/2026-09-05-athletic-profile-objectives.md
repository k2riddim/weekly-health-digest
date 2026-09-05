# Athletic Profile & Objectives Tracker — 2026-09-05

Weekly deep-pass (separate from the daily digest routine). Data window: full Strava/Withings/Garmin history (2014-05 → 2026-09) for Part 1; live re-query of all active objectives for Part 2.

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers — lifetime totals

- **2,475 logged activities** (2014-05-01 → 2026-08-29, ~12.3 years), **2,222 excluding e-bike commutes**.
- **20,766 km** / **1,968 hours** of non-e-bike training; including e-bike commuting: **24,897 km** / **2,186 hours**.
- Activity-type distribution (all-time, n / km / hours):

| Type | n | km | hours |
|---|---|---|---|
| Run | 836 | 7,087.3 | 756.3 |
| Ride | 742 | 11,982.7 | 635.1 |
| Workout (gym/HIIT) | 328 | 76.3 | 286.9 |
| EBikeRide (commute) | 253 | 4,131.5 | 218.0 |
| WeightTraining | 121 | 0.5 | 77.3 |
| Walk | 76 | 251.0 | 63.1 |
| VirtualRide | 43 | 811.9 | 34.7 |
| Swim | 26 | 29.3 | 14.5 |
| Hike | 24 | 189.2 | 56.7 |
| AlpineSki | 12 | 317.0 | 33.0 |
| Other (Crossfit, Rowing, Surf, Snowshoe, Yoga, SUP) | 9 | 17.7 | 8.2 |

Cycling dominates lifetime distance (Ride + EBikeRide = 65% of km), but running dominates lifetime *session count share of "hard" training* and carries the competitive results (see §3).

### 2. Volume trajectory — distinct training phases

| Phase | Years | Sessions/wk | Hours/wk | Character |
|---|---|---|---|---|
| **Build-up** | 2014–2016 | 5.5–7.2 | 3.1–4.6 | Heavy bike-commute base (partial 2014) + rising run volume; marathon debut 2016 (3:58) |
| **Competitive peak** | 2015, 2019 | 4.0–4.4 | 3.4–3.8 | Highest running specificity; PRs in both years (half 1:34:33 in 2019, marathon 3:39:55 in 2019) |
| **Cycling-tilted plateau** | 2017–2018 | 4.0–4.1 | 3.1–3.7 | Running volume nearly halved (46, then 116 runs/yr) while cycling stayed high |
| **COVID trough** | 2020–2022 | 1.3–2.9 | 1.6–2.7 | Running collapses to 13, 18, then **1 run in all of 2022**; "Other" (home workouts) partially offsets |
| **Cycling-driven rebound (historical chronic-load peak)** | 2023 | 4.1 | 4.1 | Highest recorded 28-day chronic training load (peak 2,100, avg 1,608 — `state/historical-peak.json`), but running still marginal (33 runs, 237 km) — this is a **cycling peak, not a running peak** |
| **Post-peak decline** | 2024–2025 | 1.6–2.9 | 1.6–2.9 | Volume falls again; two "warm body" half marathons finished off minimal specific prep (2024: 1:56:59; 2025: 2:10:27) |
| **Current comeback** | 2026 (partial, ~35 wks) | 1.5 (all sports) | 0.9 | Running-specific rebuild since ~2026-04-26/05-03, structured under active block C4 since 2026-07-29; see Part 2 |

**Key structural insight**: the system's own `historical-peak.json` chronic-load record (2023, 2,100) is a *cycling* peak with almost no running in it. Chasing that raw load number would not reproduce the competitive-running fitness Benjamin actually wants back — the 2015/2019 running-specific phases are the correct historical anchor for the *running* comeback, even though they never set the all-time chronic-load record. This distinction should stay explicit in any future replanning.

### 3. Competitive performance — race results

All runs >20 km, with clearly identifiable races bolded:

| Date | Event | Distance | Time | Pace | Avg HR |
|---|---|---|---|---|---|
| 2015-03-08 | **Semi Marathon de Paris** | 21.39 km | 1:49:11 | 5:06/km | 176 |
| 2015-10-11 | **20km de Paris** | 20.25 km | 1:40:10 | 4:57/km | 179 |
| 2016-03-06 | **Semi de Paris** | 21.21 km | 1:40:20 | 4:44/km | 172 |
| 2016-04-03 | **Marathon de Paris** | 42.34 km | 3:58:16 | 5:38/km | 172 |
| 2016-10-09 | **20km de Paris** | 20.10 km | 1:47:12 | 5:20/km | 169 |
| 2017-10-22 | **Trail du Haut Planet** | 24.51 km | 2:58:00 | 7:16/km (hilly) | 174 |
| 2018-04-08 | **Semi de Bourg-lès-Valence** | 21.09 km | 1:54:22 | 5:25/km | 186 |
| 2018-10-21 | **Trail du Haut Planet** | 24.35 km | 2:33:02 | 6:17/km (hilly) | 175 |
| 2019-03-17 | **Semi de Rueil-Malmaison — PR** | 20.54 km | **1:34:28** | **4:36/km** | 177 |
| 2019-04-14 | **Marathon de Paris — PR** | 42.99 km | **3:37:05** | **5:03/km** | 173 |
| 2024-03-03 | **Semi de Paris** | 21.27 km | 1:56:59 | 5:30/km | 165 |
| 2025-10-19 | **Semi-marathon du Bois de Vincennes** | 21.24 km | 2:10:27 | 6:09/km | 169 |

(Remaining >20 km entries are named "SL ..." — unraced long-run training sessions, mostly marathon-block long runs 2015–2016 and 2019, excluded from the race table above.)

**Lifetime PRs**: Half marathon **1:34:33** (2019-03-16), Marathon **3:39:55** (2019-04-13). Both same training cycle — 2019 is the unambiguous competitive peak.

**Benchmarking** (approximate — French amateur / population reference bands, not a precise percentile lookup): a sub-1:35 half marathon for an adult male sits in roughly the top decile of half-marathon *finishers* in France (median amateur half-marathon finish is commonly cited around 1:50–2:00 for men); a sub-3:40 marathon sits roughly in the top quartile of marathon finishers (median male marathon finish in France is commonly cited around 4:15–4:30). Both PRs correspond to an estimated VDOT in the low-to-mid 50s — solidly "competitive amateur," short of national-class. The 2024/2025 half marathons (1:57, 2:10) were finished on minimal specific preparation and are not representative of demonstrated ceiling — they reflect fitness carried over from cycling/general conditioning, not a running-specific taper.

### 4. Physiological markers (Garmin, quarterly averages; data begins 2023-Q4)

| Period | VO2max run | VO2max cycle | RHR | Steps/day |
|---|---|---|---|---|
| 2025-Q2 | 42.2 | 40.3 | 50.3 | 10,389 |
| 2025-Q3 | 43.2 | 41.2 | 48.5 | 9,131 |
| 2025-Q4 | 41.2 | 40.4 | 52.5 | 8,443 |
| 2026-Q1 | 40.9 | 39.4 | 53.0 | 10,831 |
| 2026-Q2 | 40.1 | 38.7 | 50.4 | 10,937 |
| 2026-Q3 (partial) | 42.2 | 40.2 | 50.5 | 10,059 |

Current point values (early Sept 2026): VO2max running 42.5, VO2max cycling 42.9 (data-quality flag carried from prior refresh — cycling estimate jumped to match running exactly on 2026-08-11 and has not diverged since; still treat as an artifact, not a real gain, until it moves independently), RHR 90-day avg 50.3 (σ 2.2) but running **53–55 for the last 14 straight days**.

**ACSM context** (age 42, male; population reference bands are approximate and vary by source): VO2max ~42 mL/kg/min sits at the boundary of the "Good"/"Excellent" bands for a man in his 40s — well preserved despite the multi-year running layoff. RHR 50–55 sits in the "Athlete"/"Excellent" band under commonly-cited ACSM-style resting-HR tables. Both markers indicate genuine retained cardiovascular fitness that outperforms his current running-specific output (10.5 km longest continuous run) — the ceiling is aerobic capacity, not current run-specific tolerance or consistency.

### 5. Body composition trajectory

| Year | Avg weight (kg) | Avg fat % | Avg muscle mass (kg, from 2025) |
|---|---|---|---|
| 2015 (running peak) | 86.9 | 22.0 | — |
| 2019 (running peak) | 86.3 | 21.5 | — |
| 2020–2021 (COVID trough) | 84.6–85.9 | 21.3–22.0 | — |
| 2022–2024 (post-peak decline) | 91.4 → 97.0 | 25.4 → 31.5 | — |
| 2025 | 103.5 | 28.0 | 71.0 |
| 2026 (comeback year, to date) | 103.9 | 27.0 | 71.9 |
| **Latest reading** (2026-09-01) | **101.15** | — | — |

Body composition tracks training phase almost exactly: weight/fat% trough during the two running-specific peaks (2015, 2019, ~86 kg / ~21–22%), then a near-monotonic climb through the COVID trough and cycling-tilted years to a 2024–2025 high (~97–103 kg, ~28–31% fat). The 2026 comeback has started reversing this (105.2 kg baseline 4/26 → 101.15 kg now, ~4.1 kg in ~19 weeks), but the pace has **flattened over the last 3 weeks** (100.68 kg 8/11 → 101.15 kg 9/1, i.e. essentially flat/slightly up) coinciding with the current protein blackout and reduced training — see Part 2 §218d1c78.

Height 178 cm → current BMI ≈ 31.9 (WHO "Class I obesity" by BMI alone), but this **overstates adiposity**: retained lean mass (~71 kg) and fat% in the "average" band for age (26–28%, not "high") make BMI a poor single proxy here. Body fat % and the weight *trend*, not BMI, are the more informative levers.

### 6. The verdict

**Classification**: a 42-year-old male, Mitchell Class IC/IIIC endurance athlete (running + cycling — high dynamic, low-to-moderate static cardiovascular demand; no structural cardiac risk factors in this dataset), currently in an **active, protocol-gated return-to-running comeback** roughly 5 months post-initiation, rebuilding from a multi-year running layoff (near-zero running 2020–2023) superimposed on a genuine historical competitive-amateur peak (sub-1:35 half, sub-3:40 marathon, both 2019 — top-decile-adjacent by French amateur benchmarks). Cardiovascular fitness (VO2max ~42 mL/kg/min, ACSM "Good"-to-"Excellent" for age; RHR 50–55, "Athlete" band) has been substantially preserved through the layoff via sustained cycling volume, but current running-specific capacity (10.5 km demonstrated ceiling, inconsistent 3×/week frequency) sits well below both his 2019 competitive ceiling and what a half-marathon attempt would require. The single limiting factor right now is **not** aerobic engine — it is a sustained (14-day, ~2σ) autonomic recovery suppression (HRV, RHR) that the automated coaching protocol is correctly refusing to train through, compounded by a concurrent nutrition-adherence lapse (see Part 2). In sports-medicine shorthand: **a well-preserved engine, a under-built running-specific chassis, and a currently red recovery-readiness light.**

---

## PART 2 — Objectives Tracker

### Step 1–2 — Active objectives, live values

| Objective | Target | Live current value | Source |
|---|---|---|---|
| Reprendre la course 3×/semaine (a1bde447) | ≥3 runs/wk by 2026-09-29 | **0/3 this week** (Aug31–Sep6, through Sep4); **2/3 prior week** (Aug24–30) | `strava_activities`, sport_type Run/TrailRun, weekly count |
| Atteindre 160 g protéines/j (49829c29) | ≥160 g/day avg by 2026-09-29 | 30d mechanical avg **70.4 g** (includes zero days); **121.2 g** on the 18 logged days; **13 of the last 31 days at zero** (a 12-day unbroken zero streak, Aug23–Sep4, still open) | `oh_daily_nutrition_summary.total_protein_g`, avg_30d |
| Descendre à 95 kg (218d1c78) | ≤95 kg by 2026-12-30 | **101.15 kg** (2026-09-01, most recent reading) | `withings_measurements.weight_kg`, latest, filter >70 |
| Bilan sanguin complet annuel (42361937) | Reach by 2026-12-30 | Last full panel **2025-12-01** (279 days ago); Vitamin D retest (27 ng/mL, insufficient) ~9–10 weeks overdue, still not logged | `oh_observations`, latest |
| Courir jusqu'à Beaumonts, 12 km (9b982443) | ≥12 km by 2026-10-30 | **10.5 km** max since 2026-06-14 (unchanged for 6 full weeks) | `strava_activities.distance`, max, sport_type Run/TrailRun |
| Semi-marathon <1h45 (96910249) | ≤105 min by 2027-03-30 | No qualifying long run or scheduled race; gated by 9b982443 | — |
| Retour compétiteur amateur — parent (a0000000) | Qualitative, 2027-06-29 | Rolls up all of the above | — |

### Step 3 — Progress & trajectory

- **Running frequency**: two consecutive weeks below target (2/3, then 0/3-to-date). The current blank week is **not** silent non-adherence — it is a legitimate, protocol-correct deload extension: the daily coaching routine's "porte deload" gate (HRV weekly ≥36 AND RHR 7d ≤51 to reopen full volume) has not cleared since it was first checked on 2026-08-28, and three planned re-entry runs (Aug29, Sep2, Sep4) were each contingently skipped because morning readiness criteria were not met. The system is behaving correctly; the underlying physiology is the problem (see cross-domain note below).
- **Protein**: trajectory has worsened, not stabilized — the zero-protein streak grew from 3 days (flagged 2 refreshes ago) to 6 days (last refresh) to **12 days now, still open**. Logged-day capability (~121 g/day) is unchanged and still ~24% short of target even when logging happens.
- **Weight**: 128-day demonstrated pace since baseline is 0.222 kg/wk (105.22→101.15 kg), which has now fallen **below** the 0.359 kg/wk required over the 120 remaining days to hit 95 kg by 2026-12-30 — a genuine deceleration versus last refresh's "on pace" read, concentrated in the last 3 weeks (100.68 kg 8/11 → 101.15 kg 9/1).
- **Labs**: no change; zero-cost item, still simply not actioned.
- **12 km long run**: unchanged at 10.5 km for 6 straight weeks — the longest stall on this objective since it was opened (2026-06-14).
- **Half marathon**: fully dependent on the above; no independent movement possible until the long-run ceiling rises.

### Step 4 — Coherence across objectives

No objectives are in direct conflict — weight loss, protein, and running all pull in mutually reinforcing directions. But they share a **single physiological bottleneck**: the 14-day, ~2σ suppression in HRV (90d avg 35.0, σ2.2 → currently 30, z≈-2.3) and matching RHR elevation (90d avg 50.3, σ2.2 → currently 53-55, z≈+1.7 to +2.1) is simultaneously (a) the reason the running-frequency and long-run objectives cannot progress (deload gate stays shut), and (b) very plausibly *worsened* by the concurrent 12-day zero-protein stretch (inadequate protein intake impairs recovery and autonomic normalization) and by the weight-loss plateau's own possible under-fueling. No oh_symptoms_log entry explains the suppression — no illness has been logged — and sleep over the same window (6.5–8.2h/night) is not the driver either. This reads as a genuine, unexplained, and now clinically-relevant-in-duration recovery signal, not routine noise.

**Dependency chain**: 9b982443 (12 km) and 96910249 (half marathon) both gate on a1bde447 (frequency) recovering, which itself gates on the HRV/RHR normalizing, which is plausibly gated by protein (49829c29) normalizing. **The critical path runs through protein, not through training.**

### Step 5 — Confidence scores (0–100, probability of hitting target_date given current trajectory)

| Objective | Confidence | Δ vs last week | Rationale |
|---|---|---|---|
| a1bde447 — 3 runs/wk | **16%** | ↓ from 34% | Two straight sub-target weeks (2/3, then 0/3), deload gate still shut after 14 days, 24 days left to target date. Rate insufficiency is now severe. |
| 49829c29 — 160g protein | **5%** | ↓ from 9% | Worst-trending objective in the set: the blackout has doubled in length two refreshes running (3→6→12 days) with zero sign of reversal, arithmetic gap to target still ~25%+ on logged days alone. |
| 218d1c78 — 95kg | **28%** | ↓ from 42% | Demonstrated pace has fallen below the required pace for the first time this cycle; 3-week plateau coincides with reduced training and the protein blackout (lean-mass-loss risk, not fat-loss stall, is the sharper concern). |
| 42361937 — bilan sanguin | **24%** | ↓ from 29% | Zero-cost item still not actioned; Vitamin D retest now ~9–10 weeks overdue. Runway (116 days) is still numerically adequate but administrative inertia is the binding constraint, consistent with reduced life-admin bandwidth generally. |
| 9b982443 — 12km Beaumonts | **20%** | ↓ from 33% | Sixth straight week with zero distance attempt; target date is 8 weeks out and the gating frequency objective is itself declining. |
| 96910249 — half <1h45 | **10%** | ↓ from 17% | Fully dependent on 9b982443, which just weakened further; historical precedent (1:34:33 PR) remains strong evidence of physiological ceiling but is not informative about near-term trajectory. |
| a0000000 — parent comeback goal | **17%** | ↓ from 26% | Every sub-objective weakened simultaneously this cycle around one shared, plausible root cause (see below) — genuinely a worse week than the last refresh, but the long runway (9+ months) and the fact the coaching system is gating correctly rather than forcing training through red recovery markers keep this from being a crisis. |

**Contextual factors weighed**: new-parenthood headwind is explicit and current — Benjamin is on "Congés - adaptation à la crèche" (daycare adaptation leave) 2026-09-01 through 2026-09-12, which plausibly explains both the administrative slippage (labs, protein logging) and the flexible-but-inconsistent training schedule; the daily routine is already adapting session timing around it. Historical precedent (2019 PRs, and the demonstrated ability to log 120g+/day of protein when he does log) shows the *capability* is real — the current dip is adherence- and recovery-driven, not a ceiling problem.

### Narrative synthesis

These objectives remain mutually compatible in principle — nothing here trades off against anything else — but this week is the first time **all of them moved the wrong way simultaneously**, and the pattern points at one shared cause rather than seven independent problems: a sustained, unexplained autonomic recovery suppression (HRV/RHR, 14 days, ~2σ) that is being correctly respected by the training gate but is plausibly being *fed* by 12 days of essentially zero protein intake, itself coinciding with reduced life-admin bandwidth during a family transition (daycare adaptation leave). Timelines are still realistic relative to each other — the half-marathon and 12 km targets have enough runway (8 and 29 weeks respectively) to absorb a 1–2 week stall without becoming implausible — but a third consecutive week of this pattern would start to genuinely threaten the September 29 frequency deadline and put real pressure on the October 30 long-run date.

**Single highest-leverage action right now**: fix protein logging and intake first, before pushing training. It is the one lever in this list that (a) requires zero training capacity at a moment when training capacity is exactly what's gated, (b) has a plausible causal path to normalizing the HRV/RHR suppression that is blocking every running objective, and (c) directly protects the weight-loss objective's lean-mass risk. Concretely: break the current zero-streak today, and treat 3 consecutive protein-logged days ≥120g as the signal to re-check the deload gate rather than waiting on HRV/RHR alone to move first.

---
*Full report. Objective notes in the `objectives` table were updated in place with this cycle's confidence scores and live values.*

# Athletic Profile & Objectives Tracker — 2026-08-08

*Weekly deep-pass digest. Supersedes 2026-07-25 report as the reference snapshot. Feeds `CLAUDE.md` and `objectives` (biometrics DB) for the daily digest pipeline.*

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers — lifetime totals

| Metric | Value |
|---|---|
| Span | 2014-05-01 → 2026-08-06 (12.3 years) |
| Total activities | 2,452 |
| Total distance | 24,600 km |
| Total moving time | 2,168 hours |

**Activity type distribution (lifetime):**

| Type | Sessions | km |
|---|---|---|
| Ride | 742 | 11,983 |
| Run | 829 | 7,053 |
| EBikeRide | 238 | 3,869 |
| Workout | 328 | 76 |
| WeightTraining | 121 | ~1 |
| Walk | 76 | 251 |
| VirtualRide | 43 | 812 |
| AlpineSki | 12 | 317 |
| Hike | 24 | 189 |
| Swim | 25 | 29 |
| Other (Crossfit, Rowing, Surfing, Snowshoe, Yoga, SUP) | 13 | ~20 |

Cycling (Ride + EBikeRide + VirtualRide) dominates lifetime distance (16,664 km, 68%); running is the largest session count (829, 34% of all sessions) but only 29% of distance — consistent with running being the higher-intensity, shorter-duration modality throughout.

### 2. Volume trajectory — distinct phases

| Phase | Years | Run sessions/wk | Run km/wk | Ride+EBike km/wk | Dominant signal |
|---|---|---|---|---|---|
| **Build-up** | 2014–2015 | 1.8–3.4 | 13.4–32.5 | 4.9–23.0 | Ramping into first marathon block |
| **Marathon peak I** | 2016 | 3.0 | 29.0 | 23.3 | Marathon 3:58:12 (Apr), half-PR pursuit |
| **Transition / low-run, high-ride** | 2017 | 0.9 | 5.8 | 34.9 | Run volume collapses, cycling fills the gap |
| **Rebuild + Marathon peak II (true peak)** | 2018–2019 | 1.8–1.4 | 14.1–14.9 | 0.3–2.8 | **Marathon PR 3:39:55 (2019-04-13), Half PR 1:34:33 (2019-03-16)** — best-ever fitness |
| **COVID / low volume** | 2020–2021 | 0.2–0.3 | 2.2–2.7 | 17.5–20.8 | Run volume near-zero; cycling-only maintenance |
| **Cycling-dominant, running dormant** | 2022–2024 | 0.02–0.6 | 0.2–4.1 | 17.4–39.4 | Weight climbs 91→97 kg avg; running essentially absent |
| **E-bike commuting era + 1 race** | 2025 | 0.9 | 5.6 | 45.6 (incl. e-bike) | 118 e-bike commutes; one half-marathon on minimal specific prep (2:10:30, well off PR pace) |
| **Layoff** | 2025-11-02 → 2026-05-03 | 0 | 0 | — | 182-day running gap (4th-longest in 12y history) |
| **Comeback (current)** | 2026-05-03 → present | ~1.8* | ~9.7* | reduced | Structured C4 rebuild block, 25 runs, 130.7 km YTD — see §Comeback below |

\* 2026 YTD run rate through Aug 8 (≈31.3 weeks elapsed, but comeback itself only spans 14 of those weeks: 25 runs / 14.1 weeks ≈ **1.8 runs/wk avg since May 3**, rising toward the current 3/wk target — see Objectives §a1bde447).

**Historical peak chronic load** (`state/historical-peak.json`, computed 2026-04-16): 28-day chronic load average 1,608 (peak block 2,100), dated to a high-volume 2023 block — this is a rolling-window peak, not a full-year average (2023's whole-year run rate was actually low; the peak block reflects a concentrated high-intensity multi-sport stretch that year, not the athlete's best sustained fitness era in absolute terms). **Note:** the *performance* peak (marathon/half PRs) and the *load* peak (highest recorded chronic training load) occurred in different years (2019 vs. 2023) — expected, since chronic load is dominated by cycling volume, while running PRs came from a lower-volume, higher-specificity block.

Current chronic_load_28d ≈ 28.8 (2026-08-06) = **1.8% of historical peak load** — reflecting how deep the 182-day layoff plus multi-year decline dug, and how early the rebuild still is in absolute load terms even though running-specific fitness (VO2max, pace tolerance) is recovering faster than raw load would suggest.

### 3. Competitive performance — race results

| Date | Race | Distance | Time | Pace | Context |
|---|---|---|---|---|---|
| 2015-03-07 | Semi Marathon de Paris | 21.39 km | 1:49:27 | 5:11/km | |
| 2015-10-10 | 20km de Paris | 20.25 km | 1:40:06 | 4:57/km | |
| 2016-03-05 | Semi de Paris | 21.21 km | 1:40:18 | 4:44/km | |
| 2016-04-02 | **Marathon de Paris** | 42.34 km | 3:58:12 | 5:38/km | First marathon |
| 2016-10-08 | 20km de Paris | 20.10 km | 1:47:43 | 5:21/km | |
| 2018-04-07 | Semi de Bourg-lès-Valence | 21.09 km | 1:54:24 | 5:26/km | |
| 2019-03-16 | **Semi de Rueil-Malmaison — PR** | 20.54 km | **1:34:33** | **4:36/km** | Lifetime half-marathon PR |
| 2019-04-13 | **Marathon de Paris — PR** | 42.99 km | **3:39:55** | **5:07/km** | Lifetime marathon PR, sub-3:40 |
| 2024-03-02 | Semi de Paris 2024 | 21.27 km | 1:57:00 | 5:30/km | Post-decline, minimal specific prep |
| 2025-10-18 | Semi-marathon du Bois de Vincennes | 21.24 km | 2:10:30 | 6:08/km | Pre-layoff, deconditioned/heavier |

**Benchmarking (French amateur, adult male):** national median half-marathon finish time is ≈1:53–1:56; the top-decile threshold is ≈1:40:35 ([reference-trail.fr](https://reference-trail.fr/quel-est-le-temps-moyen-sur-semi-marathon-en-france/), [athleexplique.fr](https://athleexplique.fr/cest-quoi-un-bon-temps-au-semi-marathon-comparez-vous-par-rapport-a-votre-age-et-votre-sexe/)). Benjamin's 1:34:33 PR sits **comfortably inside the top-10% of French amateur male finishers** — a genuine sub-elite-amateur performance, not merely "recreational." His two most recent races (2024, 2025), run without a specific training block and at 15–18 kg above racing weight, land close to national median — illustrating the gap between demonstrated peak capability and current conditioning, not a ceiling on capability.

### 4. Physiological markers

| Marker | Latest (2026-08-07) | Trend (2025-Q3 → 2026-Q3\*) | Context |
|---|---|---|---|
| VO2max running | 42.8 ml/kg/min | 41.2 → 42.8, rising monotonically since comeback start (38.3 on 2026-05-03) | ACSM 40–49y male norms: "Good" band (40–43.9); trending toward "Excellent" (≥44) |
| VO2max cycling | 38.6 ml/kg/min | 40.4 → 38.6, essentially flat/slightly down | Reduced cycling-specific volume during running rebuild |
| Resting HR | 47–51 bpm (7d range) | 52.5 → 48.9 avg, improving | ACSM 40–49y norms: <54 bpm = "Athlete" tier — despite elevated body weight, cardiac autonomic fitness is elite-adjacent |
| Steps | ~10,500–10,900/day (quarterly avg) | Stable, high NEAT baseline | Well above the 7-10k general-health benchmark |

\*Garmin `vo2max_running`/`vo2max_cycling` series only populated from 2025-Q1 onward in this database.

### 5. Body composition trajectory

| Year | Avg weight (kg) | Avg fat % | Context |
|---|---|---|---|
| 2015 | 86.9 | 22.0 | Marathon-block leanness building |
| 2019 | 86.3 | 21.5 | **Peak fitness era — leanest sustained weight on record** |
| 2021 | 84.6 | 21.3 | **Lifetime-low weight** (COVID low-volume but lean; muscle likely reduced too) |
| 2022–2024 | 91.4 → 97.0 | 25.4 → 31.5 | Steady climb — running dormant, cycling insufficient to offset; **2024 fat% (31.5%) is the worst on record** |
| 2025 | 103.5 | 28.0 | New-parenthood year (Léonie born 2026-01-09 — pregnancy/newborn prep likely shifted household priorities from H2 2025) |
| 2026 (YTD avg) | 104.3 | 27.1 | Comeback launched from the heaviest annual-average weight in the dataset |
| **Live (2026-08-04)** | **101.16** | **25.8** | **-4.06 kg since comeback baseline (105.22 kg, 2026-04-26), fat% down 1.3pp** — the correction is real and underway |

Weight and fat% move inversely with running volume almost perfectly across the 12-year record (r ≈ strong negative by inspection) — 2019 (peak running) = leanest sustained point; 2024 (zero running) = heaviest/fattest point on record. The current rebuild is reproducing that pattern: fat% has already dropped 1.3pp in ~14 weeks of comeback running layered on top of the pre-existing weight-loss objective.

### 6. The verdict

**Classification: a 42-year-old male masters-age recreational endurance athlete, sub-elite-amateur by demonstrated historical performance (top-decile French half-marathon PR, sub-3:40 marathon), currently in an active post-layoff rebuild phase from the heaviest/most deconditioned baseline in his 12-year training history.**

- **ACSM cardiorespiratory fitness classification:** VO2max running 42.8 ml/kg/min places him in the "Good" band for age 40–49 (ACSM norms), trending toward "Excellent" (≥44) on current trajectory — a materially better classification than his BMI (≈31–32, "obese" by BMI alone) would suggest, consistent with the well-documented BMI-fitness discordance in athletes carrying above-average muscle mass (muscle_mass_kg ~71–73 vs. general-population norms for this height range).
- **Resting HR 47–51 bpm** is in the ACSM "Athlete" tier for his age/sex — strong evidence of retained cardiac-autonomic conditioning despite years of reduced training load; this is the single strongest piece of evidence that the underlying engine never fully de-trained, only the peripheral/tissue conditioning (muscular endurance, running-specific tissue tolerance) did.
- **Mitchell classification** (cardiac risk stratification by static/dynamic demand): running and cycling are both **high-dynamic, low-to-moderate-static** disciplines (Mitchell class IC/IIIA) — low absolute cardiovascular risk profile for continued endurance training, contingent on the lipid finding below being followed up.
- **One flag for the GP conversation, not a diagnosis:** Dec 2025 labs showed Total Cholesterol 2.27 g/L (≈227 mg/dL, flagged "high" by the lab) with LDL 1.57 g/L (≈157 mg/dL) — worth a natural mention at the next GP visit alongside the overdue Vitamin D retest (27 ng/mL, insufficient, retest due since ~July 2026, not yet done as of 2026-08-08 — no observations logged since 2025-12-03).
- **Verdict in one line:** *not* a deconditioned novice and *not* currently at his competitive peak — a proven sub-3:40 marathoner and sub-1:35 half-marathoner rebuilding tissue tolerance and aerobic base from a genuine trough, with the cardiovascular engine (VO2max, RHR) recovering noticeably faster than body composition, which is itself now on a real (if unhurried) downward trajectory for the first time since 2019.

---

## PART 2 — Objectives Tracker

### Step 1–3: Active objectives, live values, progress

| Objective | Baseline → Target | Live value (2026-08-08) | Progress | Trajectory |
|---|---|---|---|---|
| **a0000000** Retour niveau compétiteur (semi <1h45, poids <95kg) — global rollup, due 2027-06-29 | — | rollup | — | improving |
| **9b982443** 12 km Beaumonts, due 2026-10-30 | 5.8 → 12.0 km | 10.5 km (max, unchanged since 2026-07-24) | 75.8% of baseline→target delta | on-plan, static this fortnight by design (elevation-exposure block, not distance block) |
| **96910249** Semi <1h45, due 2027-03-30 | — → 105 min | no race scheduled | n/a | gated, no new evidence |
| **a1bde447** 3 runs/wk, due 2026-09-29 | — → 3 sessions/wk | 3/wk confirmed for a 3rd consecutive ISO week (W29, W30, W31 — live Strava cross-check: W31 = 3 runs, 7.01+5.02+5.06 km, matches C4 deload plan almost exactly) | at target | **strengthening — first 3-week streak of the rebuild** |
| **49829c29** Protein 160 g/day (30d avg), due 2026-09-29 | 115.4 → 160 g | **15.6 g** (30d avg incl. zero-days; recomputed live) | worsened vs 54.6g (2026-07-25) | **degrading** — logging blackout continued through late July, a brief 3-day relog (Aug 4-6, avg 103.5g on logged days, close to target) then dropped back to zero Aug 7 |
| **42361937** Bilan sanguin annuel, due 2026-12-30 | — | last full panel 2025-12-01 (8.2 months ago); no new `oh_observations` since 2025-12-03 | on track for annual cadence, Vit D retest overdue | flat/stalled on the sub-item |
| **218d1c78** Weight ≤95kg, due 2026-12-30 | 105.22 → 95.0 kg | **101.16 kg** (2026-08-04, live — 2.5 kg fresher than the stale 103.67 kg on file) | 39.7% of baseline→target delta | **improving markedly — pace now nearly matches required rate** |
| ~~c0eac7c5 FTP Zwift 200W~~ | — | abandoned 2026-06-15 | — | excluded from tracking |

**Live-value notes:**
- `9b982443`: no new PB since Run #20 (2026-07-24, 10.50 km); the five runs since (7/28–8/6) were deliberately shorter (4.8–7.0 km) per `protocols/active_block.md` W31 deload / W32 elevation-exposure design — Run #25 (2026-08-06, 4.81 km, 87 m D+ = 18 m/km) is the qualifying hill-density recon session the block's elevation reframe called for. Distance and D+ progress on separate rungs by design; this is plan-conforming, not a stall.
- `49829c29`: recomputed the literal 30-day `AVG(total_protein_g)` (treating unlogged days as 0, matching the objective's own `avg_30d` semantics) → 15.6 g. On the 3 days actually logged in the window (Aug 4–6), the average was 103.5 g — proof the behavior is achievable, not that intake itself collapsed to near-zero; but the pattern (weeks-long blackout, brief relog, blackout again) is now the dominant signal over two consecutive refresh cycles.
- `218d1c78`: latest Withings sync closed the 35-day gap flagged on 7/25 (last read then was 2026-06-20) — two new readings landed 2026-08-02 and 2026-08-04, both weight and fat%.

### Step 4: Coherence across objectives

- **No conflicts identified.** Weight-loss pace (0.284 kg/wk, ≈0.28%/wk of body mass) sits comfortably inside the evidence-based 0.5–1%/wk fat-loss ceiling and specifically inside `return-to-running.md`'s stricter tendon-adaptation guardrail (no loss >1 kg/wk) — the two objectives are not fighting each other.
- **Dependency chain intact:** `96910249` (semi <1h45) is correctly gated behind `a1bde447` (running frequency) and `9b982443` (long-run distance) — both of those are now the strongest-trending objectives in the set, which is the right order of operations for a comeback.
- **`c4_block` periodization is doing its job:** the active block explicitly separates the distance rung from the elevation rung specifically to avoid stacking two progressions on tissue that's 5 months post-182-day-layoff — visible in this week's live data (RECON hill run intentionally shorter than the flat-run distance rung).
- **The two objectives now diverging from plan are both pure logging/admin gaps, not physiological problems:** protein logging (`49829c29`) and the Vitamin D retest (`42361937`, sub-item) share a common failure mode — zero-cost, non-training-dependent actions that keep slipping. Neither is gated by anything else, so neither has an excuse rooted in training load or recovery state.

### Step 5: Confidence scores (0–100, probability of hitting target_date)

| Objective | Prior (date) | New | Δ | Rationale |
|---|---|---|---|---|
| `a0000000` global rollup | 24% (7/25) | **31%** | +7 | Running-frequency streak (3 consecutive weeks) and the weight-trajectory correction (pace now near-required) are the two components that most needed to turn; both did. Still gated by the ungated half-marathon leg and by an 11-month runway that's mostly untested. |
| `9b982443` 12km Beaumonts | 55% (7/29) | **57%** | +2 | Plan-conforming week, elevation-exposure requirement satisfied (18 m/km recon), 7 weeks of buffer remain before the 10/30 deadline. Distance static this fortnight by design, not by stall. |
| `96910249` Semi <1h45 | 25% (7/25) | **25%** | 0 | No new evidence either way; still fully gated. |
| `a1bde447` 3 runs/wk | 45% (7/29) | **55%** | +10 | Three consecutive on-target ISO weeks (W29–W31) is the strongest consistency signal of the entire rebuild — this is now a demonstrated habit, not an aspiration. Residual risk is still August scheduling/family disruption, not physiology. |
| `49829c29` Protein 160g | 10% (7/25) | **8%** | -2 | A second consecutive refresh cycle shows the same blackout-then-brief-relog pattern; the brief relog proves capability but the net trend (15.6g vs 54.6g prior) is worse, not better. |
| `42361937` Bilan sanguin | 45% (7/25) | **40%** | -5 | Annual-cadence target itself still has runway (12/30), but the low-effort Vitamin D retest sub-item is now ~1 month past its informal July due date with zero action — a leading indicator the annual panel may slip too without a nudge. |
| `218d1c78` Weight ≤95kg | 20% (7/25) | **45%** | +25 | The single biggest mover this cycle. Achieved rate (0.284 kg/wk) now almost exactly matches the required forward rate (0.292 kg/wk) — a genuine trajectory change, not just fresher data. Two new syncs (8/2, 8/4) also closed the reporting-gap risk that was previously the dominant negative signal. |

### Narrative synthesis

The physiological rebuild is ahead of the behavioral/admin rebuild. Every objective anchored in Strava/Garmin/Withings data (running frequency, long-run distance, body weight) improved or held plan this cycle — running consistency in particular just posted its best signal of the whole comeback (three straight weeks at target). Every objective anchored in manual self-report (protein logging, blood panel scheduling) either stalled or worsened, and both failures share the same shape: multi-week blackout, brief high-quality relog, blackout again. That's a logging-habit problem, not a physical-capacity problem, and it's now the clearest bottleneck in the whole tracker.

**Critical path to the global objective (`a0000000`, semi <1h45 by 2027-06-29):** `a1bde447` (frequency) → `9b982443` (long-run/elevation, attempt window W36, ~Sept 5–6) → race selection for `96910249`. The frequency leg just de-risked itself materially; the long-run leg is on schedule with 7 weeks of buffer. The weight leg, now also trending correctly, is a supporting (not gating) factor for the half-marathon time goal but is the direct driver of the standalone weight objective.

**Single highest-leverage action right now:** neither training load nor recovery — both are already well-managed by the C4 block and this week's readiness data. It's closing the two zero-cost logging gaps: **(1) resume daily protein logging** (demonstrated 103.5g/day average when actually logged, i.e., the behavior works when done) and **(2) book the Vitamin D retest**, now ~1 month overdue. Both require no training-load trade-off and would immediately convert two of the weakest-confidence objectives into either genuine progress or genuine (and actionable) bad news — right now they're neither, just silence.

---

*Report generated 2026-08-08. Sources: `biometrics` MCP (strava_activities, withings_measurements, garmin_health, training_load_daily, oh_daily_nutrition_summary, oh_observations, objectives), `state/historical-peak.json`. Next refresh: weekly cadence, see `objectives` table notes for live confidence tracking between refreshes.*

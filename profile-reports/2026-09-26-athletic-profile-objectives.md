# Weekly Athletic Profile & Objectives Tracker — 2026-09-26

**Scope:** full-history athletic classification (Part 1) + live objectives audit (Part 2). This is a
weekly pass, distinct from the daily 6-phase digest (`CLAUDE.md`) — no calendar/training-plan changes
are made here.

**Pipeline flag (read this first):** the daily digest routine's last commit to `main` is
**2026-09-05** (PR #139) — **21 days** with no new `state/latest.json`, no digest, no calendar
replanning. Over the same window the `objectives` table shows five consecutive weekly refreshes
(2026-08-22 → 2026-09-19) written directly to the database by some other process, but never
committed to this repo — `profile-reports/` did not exist here before this run. Two separate
findings, both load-bearing for Part 2: (1) the git-committed daily pipeline that owns calendar
scheduling has been silent for three weeks — nobody has scheduled a training session since Sep 5,
and `protocols/active_block.md` (C4, expired 2026-09-13) was never archived per its own instruction;
(2) the weekly objectives refresh exists as a process, but its output wasn't persisted to git until
now. **Recommend checking the Daily Health Digest Routine's schedule/connector health** — this is
almost certainly the root cause behind the running-frequency and long-run stalls documented below,
not a motivation problem.

---

## PART 1 — Athletic Profile Classification

### 1. Raw numbers (lifetime, 2014-05-02 → 2026-09-21)

| | |
|---|---|
| Total activities | 2,481 |
| Total distance | 24,990 km |
| Total duration | 2,193 h (~91.4 days) |
| Span | 12.4 years |

**Activity type distribution (all-time):**

| Type | N | km | hours |
|---|---|---|---|
| Run | 839 | 7,104 | 758.3 |
| Ride | 744 | 12,055 | 639.0 |
| Workout (gym/HIIT) | 328 | 76 | 286.9 |
| EBikeRide (commute, excluded from training load) | 253 | 4,132 | 218.0 |
| WeightTraining | 121 | 0.5 | 77.3 |
| Walk | 77 | 255 | 64.2 |
| VirtualRide (Zwift) | 43 | 812 | 34.7 |
| Swim | 26 | 29 | 14.5 |
| Hike | 24 | 189 | 56.7 |
| AlpineSki | 12 | 317 | 33.0 |
| Other (Crossfit, StairStepper, Rowing, Surfing, Snowshoe, Yoga, SUP) | 9 | ~21 | ~7.3 |

Running and road cycling are the two load-bearing modalities (57% of all sessions, 76% of all
distance); everything else is supplementary conditioning or life-stage-driven substitution (e-bike
commuting, gym blocks during running troughs).

### 2. Volume trajectory — distinct phases

Sessions/week and hours/week below are annualized (n ÷ 52, hours ÷ 52) across Run+Ride+WeightTraining+Workout
for full calendar years; 2014 and 2026 are partial.

| Phase | Years | Sessions/wk | Hours/wk | Character |
|---|---|---|---|---|
| **A — Marathon-build ramp** | 2015–2016 | 4.4 → 5.5 | 3.8 → 4.6 | Highest lifetime running volume: 179 runs/1,692 km (2015), 157 runs/1,506 km (2016). Two marathons run (2016: 3:58:12). |
| **B — Focused competitive peak** | 2018–2019 | 4.0 → 4.4 | 3.7 → 3.4 | Lower running frequency than Phase A but added structured strength (43 WeightTraining + 85 Workout sessions in 2019) — quality over raw volume. **Lifetime PRs set here**: marathon 3:39:55, half-marathon 1:34:33, both April/March 2019. |
| **C — COVID-era trough** | 2020–2022 | 2.7 → 1.0 | 2.7 → 2.6 | Running collapses (13, 18, 1 runs/yr); partial substitution with cycling and home workouts. 2021 is the lowest-frequency year on record (1.29 sessions/wk). |
| **D — Multi-sport, cycling-dominant rebuild** | 2023–2024 | 2.8 → 1.9 | 4.15 → 2.87 | Cycling volume peaks (2023: 2,123 km, matches `historical-peak.json`'s "high-volume multi-sport year," chronic load 2,100 — the all-time high). Running stays marginal (33, 32 runs/yr). Body composition **worsens** despite rising session count (see §5). |
| **E — Post-paternity, GLP-1-assisted running comeback** (current) | 2025–2026 | 1.46 → 1.22 | 1.60 → ~1.0 | Léonie born 2026-01-09. Running comeback nominally restarted ~May 2026 under a structured block (C4), but 2026's annualized session rate is **the lowest of any year with continuous data except 2021–2022**. Longest run capped at 10.5 km since 2026-07-25, unchanged for 9 weeks. Wegovy initiated 2026-08-12. |

The headline pattern: total training *frequency* has been on a near-monotonic 8-year decline since
the 2016 peak (5.5 → ~1.2 sessions/wk), interrupted only by the 2023 cycling rebound. The current
"comeback" phase is, by session count, not materially different from the lowest troughs on record —
it is a comeback in *intent and medical support* more than in *demonstrated volume* so far.

### 3. Competitive performance

**Lifetime PRs** (from `lifetime_prs` + race log, runs >20 km):

| Distance | PR | Date | Pace |
|---|---|---|---|
| 5K | 29:23 | 2014-07-10 | 5:44/km |
| 10K | 44:42 | 2016-02-06 | 4:30/km |
| Half marathon | **1:34:33** | 2019-03-16 (Rueil-Malmaison) | 4:29/km |
| Marathon | **3:39:55** | 2019-04-13 (Paris) | 5:05/km |

**Race progression (official/flat road races, chronological):**

| Date | Race | Distance | Time | Pace |
|---|---|---|---|---|
| 2015-03-07 | Semi de Paris | 21.39 km | 1:49:27 | 5:07/km |
| 2015-10-10 | 20 km de Paris | 20.25 km | 1:40:06 | 4:56/km |
| 2016-03-05 | Semi de Paris | 21.21 km | 1:40:18 | 4:44/km |
| 2016-04-02 | Marathon de Paris | 42.34 km | 3:58:12 | 5:38/km |
| 2016-10-08 | 20 km de Paris | 20.10 km | 1:47:43 | 5:22/km |
| 2018-04-07 | Semi de Bourg-lès-Valence | 21.09 km | ~1:54:24 (Strava) | 5:25/km |
| **2019-03-16** | **Semi de Rueil-Malmaison — PR** | 20.54 km | **1:34:33** | **4:29/km** |
| **2019-04-13** | **Marathon de Paris — PR** | 42.99 km | **3:39:55** | **5:05/km** |
| 2024-03-02 | Semi de Paris | 21.27 km | ~1:57:00 (Strava) | 5:30/km |
| 2025-10-18 | Semi du Bois de Vincennes | 21.24 km | ~2:10:30 (Strava) | 6:14/km |

**Benchmarking (approximate, French amateur / general population; Strava-derived times for the two
non-"official" entries are elapsed-moving-time estimates, not chip times):**
- The 2019 half-marathon PR (4:29/km) sits roughly in the **top 15–20% of half-marathon finishers**
  nationally — solid "confirmed club runner" tier (not elite: French elite amateur men are sub-1:15).
- The 2019 marathon PR (3:39:55) is roughly **top quartile of marathon finishers** — well above the
  typical amateur median (~4:15–4:30 for men).
- The most recent effort (2025, 6:14/km) is **35+ minutes slower** than the 2019 PR pace over the
  same distance and sits closer to the population median — a genuine, large, measured decline, not
  noise.

### 4. Physiological markers (Garmin, quarterly averages; optical/algorithmic estimates, not lab VO2max)

| Quarter | VO2max run | VO2max cycle | RHR | Steps/day |
|---|---|---|---|---|
| 2025 Q2 | 42.2 | 40.3 | 50.3 | 10,389 |
| 2025 Q3 | 43.2 | 41.2 | 48.5 | 9,131 |
| 2025 Q4 | 41.2 | 40.4 | 52.5 | 8,443 |
| 2026 Q1 | 40.9 | 39.4 | 53.0 | 10,831 |
| 2026 Q2 | 40.1 | 38.7 | 50.4 | 10,937 |
| 2026 Q3 (partial, to Sep 21) | 42.2 | 40.2 | 51.4 | 11,144 |

Garmin didn't compute VO2max/RHR before 2025 Q2 in this dataset, so a direct "then vs. now" reading
is only possible via estimation: the 2019 marathon PR pace (5:05/km) corresponds to roughly
**VDOT ≈ 39** on Daniels' tables, which maps to an estimated VO2max in the low-to-mid 40s — **in the
same range as the current measured 42.2 mL/kg/min**. This is a genuinely useful, non-obvious
finding: the aerobic engine itself has likely **not collapsed** to the degree race times suggest.
The ~35-minute half-marathon slowdown is better explained by body mass (+~17 kg vs. 2019, see §5)
and detraining of running-specific mechanics/frequency than by a lost cardiovascular ceiling.

**ACSM context:** for a 42-year-old male, normative VO2max percentile bands place 42.2 mL/kg/min
around the **~60th percentile for age/sex** ("Good," approaching "Excellent" in most published
tables) — respectable for a masters-age recreational athlete, current RHR (~51 bpm) similarly sits
in the "Good" band. Both figures carry the standing **GLP-1 qualifier**: RHR is expected to run
+1–5 bpm above Benjamin's pre-Wegovy baseline (49.3 bpm) as a class effect (`protocols/health-profile.md`),
so 51.4 bpm is consistent with medication, not a fitness signal on its own.

Steps/day (~11,100 in Q3 2026) are well above general-population averages and rising — daily
non-exercise activity is not the limiting factor here.

### 5. Body composition trajectory (Withings, yearly averages, weight_kg > 70 filter)

| Year | Weight (kg) | Fat % | Muscle (kg) | n readings |
|---|---|---|---|---|
| 2011 | 102.3 | 32.1 | — | 23 |
| 2015 | **86.9** (lifetime low) | **22.0** | — | 188 |
| 2016 | 92.0 | 25.3 | — | 35 |
| 2019 | 86.3 | 21.5 | — | 227 |
| 2021 | **84.6** (lifetime low) | **21.3** (lifetime low) | — | 76 |
| 2022 | 91.4 | 25.4 | — | 64 |
| 2023 | 94.8 | 27.9 | — | 35 |
| 2024 | 97.0 | 31.5 | — | 28 |
| 2025 | 103.5 | 28.0 | 71.0 | 23 |
| 2026 (YTD avg) | 103.6 | 26.9 | 71.7 | 22 |

**Correlation with training phases is counter-intuitive and worth stating plainly:** the best-ever
body composition (2021: 84.6 kg / 21.3%) occurred during the **lowest-volume training year on
record** (1.29 sessions/wk), while the worst body composition (2024–2025: 97–103.5 kg) occurred
during a **relatively high cycling-volume phase** (2023–2024, up to 4.15 h/wk). This points to
nutrition/energy-balance, not training volume, as the primary lever for weight — consistent with the
health profile's own note of a 101–107 kg plateau "despite calorie tracking and regular training."
The current GLP-1 therapy is the first intervention targeting that actual lever directly.

**Most recent trend (last 60 days, live query):**

| Date | Weight (kg) | Fat mass (kg) | Muscle mass (kg) |
|---|---|---|---|
| 2026-08-02 | 102.01 | 25.71 | 72.55 |
| 2026-08-11 | 100.68 | 26.05 | 70.94 |
| 2026-09-01 | 101.15 | — | — |
| 2026-09-14 | **99.68** (first sub-100 kg reading) | 26.52 | 69.54 |
| **2026-09-22** | **100.84** | 26.00 | 71.14 |

Net: −1.17 kg over 51 days (non-monotonic — a 1.16 kg rebound in the most recent 8 days). This
partially overlaps a resolving cold (per objectives notes, Sep 8–15), which can transiently mask or
inflate readings via fluid shifts; the dose remains at the 0.25 mg starter step (no escalation
confirmed), so a slower-than-eventual pace is expected. Muscle mass (69.5–72.6 kg) has not shown a
clear downward trend distinct from weight noise — no current evidence of a lean-mass-loss problem,
but only 6 readings with a body-composition split exist in 60 days, which is thin evidence.

### 6. The verdict

**Benjamin is a 42-year-old masters-age recreational endurance athlete with a genuine, data-verified
sub-elite amateur competitive ceiling (2019: marathon 3:39:55, half-marathon 1:34:33 — both
approximately top-quartile amateur performances), now 7+ years past that peak and in his third
distinct rebuild attempt following a multi-year volume decline (2020–2024) and a body-composition
regression to Class I obesity (BMI ≈ 33 at plateau).** His primary training modalities — distance
running and road cycling — are Mitchell/Bethesda **Class IIIA/IIIB** sports (high dynamic, low-to-
moderate static cardiovascular demand), i.e., a low structural-cardiac-risk profile appropriate to
his (unremarkable, per `health-profile.md`) cardiac history. His current ACSM cardiorespiratory
fitness classification (VO2max 42.2 mL/kg/min) is **"Good," ~60th percentile for age/sex** — the
aerobic engine is closer to his 2019-implied fitness than his current race times suggest; the
performance gap is driven primarily by **body mass (+16–17 kg vs. 2019) and running-specific
detraining/frequency**, not a lost cardiovascular ceiling. He is currently best classified as a
**"detrained masters endurance athlete in a medically-supported (GLP-1) body-recomposition phase,
attempting a supervised return-to-running,"** with demonstrated historical capability (Phases A/B)
but a training-frequency trajectory that, as of this week, is at multi-year lows rather than showing
comeback momentum.

---

## PART 2 — Objectives Tracker

7 active objectives + 1 abandoned (FTP 200W, dropped 2026-06-15 per user request, excluded below).
Live current values below were fetched directly against `source_table`/`source_column`/`source_filter`/
`source_agg` on 2026-09-26, superseding the stale `current_value` stored on each row (which is
refreshed only weekly).

### Live values & progress

| Objective | Target | Baseline | **Live value (2026-09-26)** | Target date | Runway |
|---|---|---|---|---|---|
| a0000000 — Retour compétiteur amateur (global) | semi <1h45 & <95 kg | — | composite (see below) | 2027-06-29 | 276 d |
| a1bde447 — Reprendre la course 3x/sem | ≥3 runs/wk | — | **~0.3–0.5/wk actual (1 run in last 2 weeks: Sep 16, 4.02 km; 0 runs since; last 21 days: 3 runs total)** | **2026-09-29** | **3 days** |
| 49829c29 — 160 g protéines/j (moy. 30j) | ≥160 g | 115.4 g | **0.0 g — 34 consecutive zero-log days (2026-08-23 → 2026-09-25), confirmed genuine gap: `oh_nutrition_intakes` has zero rows since 2026-08-22** | 2026-09-29 | 3 days |
| 42361937 — Bilan sanguin annuel | complete panel | — | **still no new `oh_observations` since 2025-12-01 (300 days)** | 2026-12-30 | 95 days |
| 218d1c78 — Descendre à 95 kg | ≤95 kg | 105.22 kg | **100.84 kg** (2026-09-22; −4.38 kg vs. baseline, −0.206 kg/wk lifetime pace) | 2026-12-30 | 95 days |
| 9b982443 — Sortie 12 km Beaumonts | ≥12 km | 5.8 km | **10.5 km — unchanged since 2026-07-25 (63 days / 9 weeks stalled)** | 2026-10-30 | 34 days |
| 96910249 — Semi <1h45 | ≤105 min | — | **no qualifying effort; gated by 9b982443 and a1bde447** | 2027-03-30 | ~6.3 months |

### Trajectory detail

- **a1bde447 (run 3×/wk):** Required rate ≥3/wk with 3 days of runway left — mathematically this
  objective is closed regardless of what happens next (even a run today, tomorrow, and Monday would
  be the first 3-in-a-week in the entire tracked history of this objective). **Falsifiable
  prediction: this objective will read as "missed" at its 2026-09-29 target date barring an
  immediate and unprecedented change in behavior.**
- **49829c29 (protein 160 g):** Same 3-day runway, same verdict — mathematically closed. The deeper
  issue is the 34-day *total* logging blackout (not merely a protein shortfall) — this is now the
  single worst-trending metric across the entire tracker for six consecutive weekly passes.
- **218d1c78 (weight → 95 kg):** Required pace from today = (100.84−95)/13.6 wk ≈ **−0.43 kg/wk**;
  demonstrated pace since baseline ≈ **−0.21 kg/wk**, or ≈ **−0.28 kg/wk** measured to the Sep-14 low
  point before the recent rebound. Both are below the required rate, and both sit **below the
  GLP-1-expected minimum** of 0.5%/wk (0.5 kg/wk at 100.8 kg) — physiologically plausible only
  because the dose has not yet escalated past the 0.25 mg starter step. The gap is real but not yet
  alarming; it should close mechanically once the 0.5 mg step is confirmed.
- **9b982443 (12 km long run):** No new maximum in 63 days against a 2026-10-30 deadline (34 days
  left). At the demonstrated rate of progress (zero km/week for 9 weeks), this will not close
  without an active plan — mechanically identical diagnosis to a1bde447.
- **96910249 (semi <1h45):** Fully gated by the two objectives above; 6+ months of nominal runway is
  irrelevant while the gating chain is stalled.
- **42361937 (bloodwork):** The one objective with zero training/schedule dependency and zero
  medical urgency signal, yet zero action in 300 days. Purely administrative inertia.

### Coherence & dependency check

1. **a1bde447 → 9b982443 → 96910249 is a single causal chain, not three independent failures.**
   All three stalled in the same window, for the same reason: no structured training block has
   existed since C4 expired 2026-09-13, and no daily replanning has run since 2026-09-05 (see
   pipeline flag above). Treating these as three separate willpower problems would be wrong — they
   share one root cause.
2. **Tension inside the nutrition/weight pair:** the health profile correctly frames appetite
   suppression as an expected GLP-1 effect, but **34 consecutive days of *zero* logged food of any
   kind** (not just low protein) is inconsistent with "eating less" — a person eats *something*.
   This is more consistent with **logging cessation** than **true near-zero intake**, which is
   itself the important distinction: if he is eating but not logging, the protein objective is a
   data problem; if intake really is near zero, it is a medical one (energy availability, on an
   appetite-suppressing drug, in an athlete trying to rebuild running volume). This should be asked
   directly rather than inferred — flagged as a genuine known-unknown, not resolved here.
3. **The global objective (a0000000) requires progress on both axes** (weight *and* running
   performance) — partial success on the medically-driven weight axis does not compensate for the
   stalled running axis in a compound "reach" objective.
4. No direct resource conflict was found between objectives (e.g., nothing requires mutually
   exclusive time/recovery budgets); the constraint is a **missing planning process**, not competing
   goals.

### Confidence scores (0–100, probability of hitting target_date)

| Objective | Confidence | Δ vs. last recorded (Sep-19) | Key factors |
|---|---|---|---|
| a1bde447 — 3 runs/wk | **1%** | ↓ from 8% | 3-day runway vs. required behavior change; zero historical precedent of hitting 3/wk even once in this objective's life; no active plan |
| 49829c29 — protein 160 g | **1%** | ↓ from 2% | 3-day runway; 34-day total logging blackout, still worsening |
| 42361937 — bloodwork | **13%** | ↓ from 16% | Trajectory flat (zero momentum for 300 days); rate is trivial (one appointment) so plausibility is high *if* initiated, but nothing suggests initiation is imminent; 95 days runway is still real cushion — held above the near-zero tier for that reason |
| 218d1c78 — weight ≤95 kg | **22%** | ↓ from 30% | Demonstrated pace (−0.21 to −0.28 kg/wk) below required (−0.43 kg/wk) and below GLP-1-expected minimum; tailwind = dose escalation still pending (would mechanically accelerate loss); headwind = this week's 1.16 kg rebound and illness confound; physiologically plausible only post-escalation |
| 9b982443 — 12 km long run | **4%** | ↓ from 10% | 9-week stall, zero momentum, deadline now closer (34 days) than the stall duration; fully dependent on a1bde447 resuming |
| 96910249 — semi <1h45 | **3%** | ↓ from 6% | Gated by the above two; historical precedent (2019 sub-1:35) proves capability exists under *actual* structured training, which does not currently exist |
| **a0000000 — global comeback** | **9%** | ↓ from 13% | Weighted composite: weight axis is the only one moving in the right direction (and only marginally); running axis is at its worst point since this objective opened |

**Confidence-factor methodology used throughout:** trajectory momentum (weighted heaviest —
everything except weight is flat-to-negative), rate sufficiency vs. required pace, dependency
satisfaction (running chain), contextual headwinds (new parenthood, 8 months in; a resolving
illness Sep 8–15; no active structured plan; GLP-1 side-effect windows Thu–Sat) vs. tailwinds
(medication is working directionally on weight; steps/day and general activity remain high),
historical precedent (2015–2016 and 2019 both prove ≥3 runs/wk and marathon-PR-level training are
within demonstrated capability, so this is not a ceiling problem), and physiological plausibility
(GLP-1 weight-loss-rate bands, 0.5–1%/wk).

### Narrative synthesis

The seven objectives are **mutually compatible in principle** — nothing about losing weight competes
with running more, and the global objective was designed as a coupled pair for exactly that reason.
What has actually happened is that **one axis (weight, via medication) is progressing slowly but
correctly, while the other axis (running frequency → long-run distance → race readiness) has been
essentially unattended for three weeks**, for a structural reason (no active training block, no
daily replanning) rather than a motivation or capability reason — the 2015–2016 and 2019 history
proves the capability exists. Timelines are **not realistic relative to each other** as currently
set: `a1bde447` and `49829c29` both expire 2026-09-29, three days from this report, and both are
already mathematically unreachable; they should be re-baselined (new target date, or re-scoped as
ongoing habits without a hard deadline) rather than left to register as failures for no diagnostic
value.

**Critical path:** 9b982443 (long run) → 96910249 (half time) is the binding constraint for the
*performance* half of the global objective, and it in turn is downstream of a1bde447 (frequency),
which is downstream of **whether a training plan exists at all**.

**Single highest-leverage action right now:** confirm why the daily digest routine stopped running
on 2026-09-05 and restore it (or manually stand up a replacement structured block per
`protocols/active_block.md`'s own end-of-block instruction, which was never executed). This one fix
is upstream of three of the seven objectives simultaneously (a1bde447, 9b982443, 96910249) and would
also restore the daily nutrition-logging nudge that likely underlies the 34-day protein blackout —
higher leverage than attacking any single objective in isolation.

---

*Full data-anchored queries available on request via `biometrics:query`. This report and the current
objective confidence scores are also mirrored into `CLAUDE.md` (Memory section) so the daily digest
routine carries this context automatically on its next run.*

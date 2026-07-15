# Return-to-Running Briefing — Benjamin, May 2026

**For the coach.** Context, risk factors, and weekly planning attention points. The training plan itself is yours to design — this document gives you the constraints and signals to factor in.

Gap broken: 2026-05-03, after 182 days off running (4th-longest gap in 12 years of training history).

---

## 1. Athlete snapshot

*Last refreshed 2026-07-15 (73 days into comeback, 15 running activities completed).*

| Field | Value |
|---|---|
| Age | 42, male |
| Body weight | **103.67 kg** (last Withings reading June 20 — 25 days stale, no weigh-in since; up ~1 kg from 102.6 kg on June 6; still down from 104.8 kg at comeback start; peak running era 84–85 kg, 2019-2020 → +19 kg) |
| Resting HR | 50 bpm (7d avg; 30d avg 49.6) — stable, unchanged from last refresh |
| HRV (Garmin) | 38 (last score Jul 13), weekly avg ~34–35, status flipping BALANCED/UNBALANCED — plateaued at this level for a month (down from 39–40 pre-comeback, but no further decline since mid-June) |
| VO2max running | 41.6 (up from 40.6 mid-June, 38.3 at comeback start — continuing to climb with run volume) |
| VO2max cycling | 38.6 (stable, unchanged for months) |
| Sleep (30-day avg) | 7.54 h — improved from 7.26 h at last refresh |
| Current ACWR (all activities) | **~1.04 — normalized, back within the general 0.8–1.3 band** (down from 1.35 in mid-June) |
| Comeback runs to date | Run #1: 2026-05-03, 2.47 km / 21 min (avg HR 135); Run #2: 2026-05-09, 2.01 km / 18 min (avg HR 144); Run #3: 2026-05-15, 3.53 km / 29 min (avg HR 139); Run #4: 2026-05-18, 5.01 km / 43 min (avg HR 140); Run #5: 2026-05-23, 5.02 km / 41 min (avg HR 136); Run #6: 2026-05-31, 3.78 km / 30 min (avg HR 140); unnumbered opportunistic run: 2026-06-02, 1.25 km / 9 min (avg HR 144, "run to catch the RER"); Run #7: 2026-06-03, 5.23 km / 41 min (avg HR 141); Run #8: 2026-06-07, 5.56 km / 44 min (avg HR 138); Run #9: 2026-06-10, 5.79 km / 45 min (avg HR 142); Run #10: 2026-06-14, 4.90 km / 38 min (avg HR 136); Run #12: 2026-06-21, 7.51 km / 57 min (avg HR 140) — **longest run to date, no reported issues**; Run #13: 2026-06-28, 3.48 km / 27 min (avg HR 138, Forêt de Chantilly); Run #14: 2026-07-05, 6.00 km / 46 min (avg HR 138, Bois de Vincennes, deliberate overshoot — absorbed cleanly); Run #15: 2026-07-13, 4.53 km / 35 min (avg HR 142, Saint-Malo — travel context, shorter run) |
| Last run before gap | 2025-11-02 (EF 45'), 6 weeks after Vincennes half-marathon (21.2 km, 6:11/km, 2025-10-19) |
| Gap duration | 182 days (2025-11-02 → 2026-05-03) |
| Lifetime running base | 12 years, 800+ logged runs, half-marathon-fit at this body weight 6 months ago |
| Family context | First child (Léonie) born 2026-01-09. Sleep currently adequate (7.54h 30d avg); occasional fragmented nights. |
| Vitamin D (Dec 2025) | **27 ng/mL — INSUFFICIENT** (optimal 40–60). Supplementation active; retest was due ~July 2026 and has not yet been logged. |
| Ferritin / Hb | 159 ng/mL / 15 g/dL — both normal (Dec 2025) |

---

## 2. Why this comeback is materially riskier than past ones

Cardio fitness is intact. The risk is purely tissue-tolerance and cumulative load:

1. **Body mass × impact.** Ground reaction force scales linearly with BW. At 105 kg vs 85 kg, every footstrike delivers ~25% more peak load to Achilles, patellar tendon, plantar fascia, tibia. Tendons remodel in 6–12 weeks; cardio adapts in 2–3.
2. **Already at functional overreaching from cycling** (ACWR 1.49). Adding impact on top of an elevated chronic load is the canonical injury setup.
3. **Vitamin D 27 ng/mL.** Burgi 2011 / Miller 2016: ~2× stress-fracture risk below 40 ng/mL.
4. **Age 42.** Tendon collagen turnover slows ~0.5%/year after 30 → healing is ~30% slower than at 25.

---

## 3. What past comebacks revealed

| Comeback | Gap | Weight | What happened |
|---|---|---|---|
| **Mar 2025** | 193 d | 101.5 kg | First run 6.3 km. W5: 3.2 km then 8.3 km back-to-back (suffer 81). Long silences then cluster-runs. Got sick + cervical pain at W10. **Closest analog. Erratic, opportunistic, no structure.** |
| **Jul 2024** | 65 d | 99.8 kg | 12 km in W1 → drops to 4 km W4 → multi-week silence. Trajectory consistent with overload pain forcing step-back. |
| **Mar 2020** | 88 d | 89.5 kg | 8 km W1, 19 km W3 with two 10 km long runs. Aggressive but successful — at 89.5 kg with no cycling load competing. **NOT replicable today.** |

**Pattern:** every successful past comeback was at ≤ 90 kg with nothing else loading the system. None had structure. The body weight × cycling-base combination today has no historical precedent in his data.

---

## 4. Coach's weekly planning checklist

Run through this every Sunday before publishing the next 7 days. If any item is RED, downgrade rather than push through.

### A. Load state (data lives in Garmin / Strava / training_load_daily)

- [ ] **ACWR ≤ 1.50** at start of week (all activities combined). The chronic-load denominator is still artificially depressed by the 182-day layoff, so the general 1.30 band is too tight during the comeback — up to 1.50 is expected and acceptable while tissue feedback (Section C) stays clean. 1.50–1.70 → reduce **cycling** to make room for running, not the running itself. > 1.70 → repeat previous week. (`T.training.comeback_acwr_upper_bound`.)
- [ ] **Chronic load 28d trending up**, not flat or down.
- [ ] **Weekly volume may ramp up to +15%** week-over-week during the comeback (`T.training.comeback_weekly_acute_ramp_cap`), overriding the general +10% cap — a low chronic base tolerates faster early progression than a maintenance block. No single week more than doubles the prior week ("no hero weeks" still holds).
- [ ] **Longer single runs are encouraged, not capped.** The daily-load-spike guardrail from the general routine does **not** gate the long run here — a progressively longer easy Z2 run *is* the point of this phase. Extend the long run by ≤ ~10 min per step (currently ~55–60 min, 7.5 km on June 21; progress toward 60–75 min as tissue feedback allows), keeping it Z1–Z2. A hard-effort spike is still a flag; a longer *easy* run is not.

### B. Recovery state

- [ ] **HRV 7-day avg within 10% of 4-week baseline.** If dropped > 10%, swap a run for cycling or rest.
- [ ] **RHR not elevated > 5 bpm above 4-week baseline for 3+ consecutive days.**
- [ ] **Sleep ≥ 7 h/night avg over last 7 days.** If < 6 h with Léonie waking ≥ 2× → reduce week's load.
- [ ] **Training readiness median ≥ 50** over last 7 days.
- [ ] **Body battery max ≥ 50** at least 4 of 7 days.

### C. Tissue feedback (athlete-reported, ask before planning)

- [ ] No localized pain that lasted > 24 h after the previous week's runs (Achilles, patellar, tibia, plantar, ITB, hip).
- [ ] No bony tenderness anywhere along tibia / fibula / navicular / metatarsals.
- [ ] No worsening morning stiffness in calves or Achilles.
- [ ] Subjective soreness ≤ 4/10 at start of week.

### D. Adjunct compliance

- [ ] Strength done as planned the previous week.
- [ ] Vitamin D supplementation taken daily.
- [ ] Body weight trend over last 4 weeks stable or modestly down. No rapid loss > 1 kg/week (compromises tendon adaptation).

### E. Context

- [ ] Cycling volume capped to keep ACWR in range — running is being added on top of an already-loaded baseline, not in isolation.
- [ ] Calendar: any major work / family disruption in the upcoming week? (anticipate sleep, not just fatigue).

### F. Prescribing run length — anchor to what he has already tolerated

The single biggest planning error is prescribing runs **shorter than what Benjamin has already run comfortably**, then treating the inevitable overshoot as a problem. Cardio fitness is intact — he was half-marathon-fit 6 months ago. The limiter is tissue tolerance, and tissue tolerance is revealed by *what recent runs he absorbed without symptoms*, not by an abstract conservative floor.

- **Set the easy-run floor to his demonstrated tolerance.** The floor = the longest run in roughly the last 3 weeks that was completed without gait change or pain **and** followed by clean next-morning recovery (no HRV crash, no RHR spike, no lingering soreness). Do **not** prescribe below that without a specific, current recovery or injury reason.
- **Reference point (as of this comeback):** the long run has reached 7.5 km (June 21) at Z2, plus a 6.0 km deliberate overshoot (July 5) — both absorbed with clean recovery and no reported tissue issues. The July 13 run (4.5 km, Saint-Malo) was a travel-context shorter session, not evidence of a lower ceiling. The easy-run floor is therefore ~6–7 km / ~45 min, and the long run should be **progressing toward 8–10 km**, not clamped to the shorter outlier.
- **Progress the long run from that anchor**, by ≤ ~1 km or ~10 min per step, keeping it easy Z1–Z2. Extend the long run, not the number of junk-short runs.
- **Overshoot of a well-tolerated target is data, not disobedience.** If Benjamin repeatedly runs longer than prescribed and absorbs it cleanly, the target was set too low → **raise it toward demonstrated capacity.** Never respond to well-tolerated overshoot by cutting the next target.
- **Banned as planning tools:** GPS turnaround alarms, forced-mid-run cutoffs, and "STRICT MAX" distance caps used to enforce an artificially low target. These are control gimmicks, not coaching. A hard cap is legitimate **only** in a genuine red-flag context — post-injury return-to-run progression, active illness, or red recovery markers (Section B) — and even then it is framed as a recovery decision with a reason, not a punishment for running well.

---

## 5. Red flags — abort criteria during the week

| Signal | Action |
|---|---|
| Achilles or patellar pain > 48 h after a run | Skip next 2 runs, swap for cycling. Still present at day 5 → kiné. |
| Localized bony tenderness (tibia, navicular, metatarsal) > 2 days | **Stop running entirely.** GP consult for stress reaction workup. |
| HRV drop > 10% from weekly average for 3 consecutive days | Swap next run for easy bike or rest. |
| RHR elevated > 5 bpm above baseline for 3+ days | Likely overload or sub-clinical illness — rest. |
| ACWR > 1.7 for 5+ days while running | Insert extra rest day; reduce next week. (1.50–1.70 is tolerated during the comeback — see §4A.) |
| Any unilateral pain pattern (one side only) | Always investigate. Asymmetry = compensation = next injury upstream/downstream. |
| Sharp pain altering gait mid-run | Stop the run. Don't try to walk it off past 5 minutes. |

---

## 6. Background factors the coach should know about (not prescriptions)

- **Vitamin D supplementation has started** outside the running plan. Retest planned around 8 weeks in.
- **Strength work**: Benjamin will run two sessions/week independently. Eccentric calf work is the main priority given the BW + Achilles risk profile (Beyer 2015, Heavy Slow Resistance evidence).
- **Cycling**: primary modality for the past 6 months; will need to be dialed back to make room for running impact volume without pushing ACWR.
- **Body composition**: a modest deficit (−3 to −5 kg over the comeback window) is desired. Each kg lost ≈ 3 kg less per-stride peak impact. Aggressive deficits are off the table — they compromise tendon adaptation.
- **Footwear**: 2-shoe rotation in use (Malisoux 2013 evidence). Max-cushion options preferred given current BW.
- **Surface**: Bois de Vincennes dirt loops accessible — soft surfaces preferred over asphalt for impact mitigation.
- **Heat**: apply `protocols/heat.md` to every outdoor session. The first lever is **timing** — move runs to the coolest hour (dawn) — then reduction, then indoor substitution or rest. During and after a heatwave the bands shift cooler; do not push outdoor running in the heat "to not lose fitness" — a comeback loses nothing by moving one session indoors or resting a day.
- **No race, no threshold, no intervals** until the comeback is consolidated. The athlete and coach align on when this gate opens — not a fixed date, depends on the data.

---

## 7. What success looks like at the end of the comeback window

Coach and athlete agree on these gates before re-introducing intensity:
- Asymptomatic across consecutive weeks.
- Consistent weekly volume sustained without ACWR > 1.5.
- Strength sessions sustained alongside running (not sacrificed when volume rises).
- Vitamin D ≥ 40 ng/mL on retest.
- Body weight trend on track.

If any of those is missed, the consolidation phase extends rather than progressing to intensity work.

---

*Generated 2026-05-03 from longitudinal Strava / Garmin / Withings / lab data. Last refreshed 2026-07-15 (monthly maintenance pass). Update each Sunday after the weekly health digest.*

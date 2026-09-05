# GLP-1 Receptor Agonists in an Endurance Athlete — Research Module

Load this module whenever a signal touches resting HR, HRV, weight, body composition,
appetite / nutrition logging, GI symptoms, hydration or fatigue **while
`protocols/health-profile.md` lists an active GLP-1 receptor agonist**. It exists because the
standard interpretation of those signals (overload, illness, detraining, under-logging) is wrong
by default in a patient on this drug class.

Evidence classes follow `protocols/thresholds.yaml > evidence_classes`.

## 1. Cardiac autonomic effects — the confounder that breaks readiness gates

- **Resting heart rate rises** as a class effect. Semaglutide 2.4 mg (STEP trials, and the product
  label) reports a mean RHR increase of roughly 1–4 bpm; tirzepatide (SURMOUNT) ~2–3 bpm,
  dose-dependent; liraglutide 3.0 mg ~2–3 bpm. Individual responses can exceed the mean.
  [RCT]
- **HRV falls** in several controlled studies of liraglutide and semaglutide (reduced SDNN / RMSSD,
  shift toward sympathetic dominance), consistent with direct GLP-1 receptor action on the
  sinoatrial node and sympathetic activation. [RCT / preliminary — smaller substudies]
- The offset appears within days of initiation, tends to grow with dose escalation, and persists
  for the duration of therapy. It does **not** indicate overreaching or infection.

**Operational consequences**

1. The personal 90-day baseline for RHR and HRV is contaminated once initiation falls inside the
   window. Split the baseline at the initiation date; after
   `T.glp1.rebaseline_after_days_on_stable_dose` days on a stable dose, the post-initiation
   window is the new reference. Until then, compare day-to-day *within* the post-initiation
   period, not against pre-medication values.
2. A readiness / deload gate written as an absolute pre-medication threshold (e.g. "RHR 7d ≤ 51")
   will never clear. Re-express gates relative to the post-initiation baseline, or replace the
   single-marker gate with a **two-signal rule**: RHR/HRV drift only counts as a red flag when a
   second independent marker agrees (sleep score / duration, skin temperature, respiration,
   logged symptoms, HR-at-pace drift in `strava_activities`, subjective feedback).
3. Garmin-derived statuses (`training_status`, `hrv_status`, `training_readiness`) inherit the
   same bias; they re-baseline slowly and will read "unbalanced / strained / detraining" for weeks.
   Treat them as descriptive, not prescriptive, during the first 4–6 weeks and after each dose step.

## 2. Body composition — weight loss is the goal, lean-mass loss is the risk

- Expected loss on therapeutic doses: ~0.5–1 % body weight per week over the first months,
  plateauing later; 12–20 % at 68–72 weeks in trials. [RCT]
- **Lean mass makes up a large share of the loss** without countermeasures: DXA substudies report
  roughly 25–40 % of lost mass as lean tissue (STEP 1 ≈ 39 %, SURMOUNT-1 ≈ 25 %). For an endurance
  athlete this is the dominant long-term performance risk (power-to-weight gains are partly
  cancelled, tendon/bone loading changes, RMR falls). [RCT substudy]
- Countermeasures with evidence: **resistance training ≥ 2×/week** and **protein ≥ 1.6 g/kg/day**
  (up to ~2.0–2.4 g/kg during rapid loss) preserve fat-free mass during energy deficit. Spread
  protein across ≥ 3–4 feedings; a leucine-rich feeding within ~2 h of training. [RCT / consensus —
  ISSN, obesity-society statements]
- Very rapid loss (> `T.glp1.weight_loss_rate_flag_pct_per_week`) raises gallstone risk and the
  lean-mass share. Flag it; do not celebrate it. [guideline — product labelling]
- Withings `muscle_mass_kg` / `fat_mass_kg` (bio-impedance) is noisy and hydration-sensitive.
  Use 7-day or 14-day averages, same time of day, before calling a lean-mass trend.

## 3. Energy availability — the under-fueling trap

- GLP-1 agonists reduce appetite, hunger and food reward; spontaneous intake typically drops
  20–35 %. In a sedentary patient that is the mechanism of action; in an athlete training
  3–5×/week it can push **energy availability** (intake − exercise energy expenditure, per kg
  fat-free mass) below ~30 kcal/kg FFM/day, the threshold associated with RED-S physiology
  (suppressed HRV, elevated RHR, worse sleep, low testosterone, poor bone turnover, stalled
  adaptation). [consensus — IOC RED-S 2018/2023]
- Practical reading: a zero or very low `oh_daily_nutrition_summary` day on GLP-1 is not
  automatically a *logging* gap; it may be a genuine intake gap. Distinguish them by
  cross-checking `oh_nutrition_intakes` row counts, weight direction, body-battery recovery
  and subjective feedback. Ask, do not assume.
- The pipeline's protein objective (160 g/day) remains valid — on GLP-1 it becomes *harder*
  to reach and *more* important. Recommend protein-dense, low-volume, low-fat foods (the drug
  slows gastric emptying and worsens fat tolerance) rather than simply "eat more".

## 4. GI effects and fuelling around sessions

- Nausea (~40–45 % on semaglutide 2.4 mg), diarrhoea, constipation, vomiting, reflux and early
  satiety are the most common adverse effects; they peak in the 24–72 h after an injection and
  during dose escalation, and usually fade after 4–8 weeks on a dose. [RCT]
- **Delayed gastric emptying** is strongest early in therapy and after dose increases (partial
  tachyphylaxis over weeks for semaglutide). A normal-sized meal 1–2 h before a run is now a
  reflux / nausea / side-stitch risk. Move the last solid meal to ≥ `T.glp1.pre_run_meal_gap_hours_min`
  h before, prefer liquid or low-fat, low-fibre carbohydrate close to the session, and take
  in-session carbohydrate in small, frequent doses.
- Benjamin already had recurrent functional GI episodes before initiation (high-fat / high-caffeine
  and FODMAP triggers, one exercise-linked episode — see `oh_symptoms_log`, Apr–May 2026). Treat
  GLP-1 as an *additional* GI risk factor layered on that baseline; keep the older triggers in
  the differential.
- A GI-affected day is a legitimate reason to shift or soften a session in the rolling plan.
  Log it as "moved — GI side effect" rather than "silently skipped".

## 5. Hydration, heat and kidneys

- Reduced thirst + vomiting/diarrhoea can cause volume depletion; product labels carry an
  acute-kidney-injury warning in that setting. [guideline]
- Endurance training in heat multiplies the risk. When the heat protocol (`protocols/heat.md`)
  is in Yellow or above **and** GLP-1 is active, prescribe explicit pre-hydration and
  electrolyte intake; in Orange shorten more aggressively than the generic cut.
- Target ~`T.glp1.hydration_target_ml_per_kg` mL/kg/day baseline plus sweat losses; the Withings
  `hydration_kg` trend and morning body weight day-to-day swings (> 1 %) are usable proxies.

## 6. Glycaemia

- In a non-diabetic patient without insulin or sulfonylureas, clinically significant
  hypoglycaemia is rare. [RCT] However, a long or intense session on top of a suppressed intake
  can produce hypoglycaemia-like symptoms (shakiness, light-headedness, unusual fatigue). Fuel
  sessions longer than `T.glp1.session_duration_min_requiring_fuel` min and treat those symptoms
  as a stop-and-fuel signal, not a "push through" one.

## 7. Other things to watch (mention to prescriber, never diagnose)

- Mood changes / low mood: labels ask for monitoring; a sustained drop in mental-clarity scores
  in `cognitive_sessions` or self-reported mood is worth mentioning at the monthly review.
- Gallbladder symptoms (right-upper-quadrant pain after meals) with rapid loss.
- Persistent severe abdominal pain (pancreatitis warning on all labels) — stop training, seek care.
- Sleep apnoea history: weight loss should *improve* it; the reverse trend would be notable.
- Vitamin D and iron status become more important with a lower intake — reinforce the overdue panel.

## 8. How the digest should phrase it

- Correct: "RHR 7d avg 54 bpm, +4 bpm vs the pre-GLP-1 baseline of 50 — within the expected
  class effect; no second recovery marker is off, so not treated as a red flag."
- Correct: "Logged intake 0 kcal for 12 days: on GLP-1 this may be real under-eating rather than
  a logging lapse — protein floor not verifiable, treated as a P0 fuelling risk."
- Wrong: "Unexplained 14-day HRV/RHR suppression, no illness logged."
- Wrong: "Weight trend reversing — possible under-fueling" when the loss rate is inside the
  expected band and lean-mass share is not flagged.

## References (for further reading; verify before citing numbers in a digest)

- Wilding et al., NEJM 2021 — STEP 1 (semaglutide 2.4 mg), incl. DXA body-composition substudy.
- Jastreboff et al., NEJM 2022 — SURMOUNT-1 (tirzepatide), incl. body-composition substudy.
- Pi-Sunyer et al., NEJM 2015 — SCALE (liraglutide 3.0 mg).
- Kumarathurai et al., Diabetes Care 2017 — liraglutide, heart rate and HRV.
- Mountjoy et al., Br J Sports Med 2018 / 2023 — IOC consensus on RED-S.
- Product labelling (EMA SmPC) for semaglutide 2.4 mg, tirzepatide, liraglutide 3.0 mg —
  heart-rate, dehydration/AKI, gallbladder and pancreatitis warnings.

TODO: add exercise-specific trial data as it appears (GLP-1 + structured training RCTs,
e.g. Lundgren et al. NEJM 2021 on liraglutide + exercise for weight-loss maintenance), and
Benjamin's own post-initiation baselines once ≥ 21 days on a stable dose are available.

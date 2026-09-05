# Standing Health Profile — Benjamin

**Read this file at Phase 0 of every run, before any data is interpreted.** It holds the
*standing* medical facts that the daily "rediscover everything from data" loop cannot infer
from wearables and must never forget: medications, conditions, surgical history, care team.
Everything that evolves (weight, HRV, load, VO2max) stays out of this file and is re-read from
the database each day.

Update this file by hand when something changes (new prescription, dose change, therapy
stopped, new diagnosis). Mirror any change into `state/latest.json > medications` and, where
relevant, into `protocols/thresholds.yaml > glp1`.

---

## 1. Medications — ACTIVE

### GLP-1 receptor agonist (weekly subcutaneous injection)

| Field | Value | Source / confidence |
|---|---|---|
| Class | GLP-1 receptor agonist ("analogue du GLP-1"), weight-management indication | Teleconsultation transcript 2026-08-04 (ARIA `meeting:20260804-141724-184fc4`) — high |
| Molecule / brand | **TO CONFIRM** (semaglutide vs tirzepatide vs liraglutide not stated in the transcript) | unknown |
| Current dose / escalation step | **TO CONFIRM** — standard protocols escalate every 4 weeks from 2026-08-12 (candidate step dates: 2026-09-09, 2026-10-07, 2026-11-04); the prescriber reassesses dose monthly. Apply `T.glp1.dose_escalation_watch_days` after any confirmed step | consult: "chaque mois on réévalue … même dosage ou on ajuste" |
| Injection day | **Wednesday** (weekly). Post-injection side-effect window = Thu–Sat (`T.glp1.post_injection_side_effect_window_days`); schedule the long run and any harder work Sun–Tue. Logging each injection in `oh_supplement_logs` (`GLP-1 injection`) is still useful to capture dose changes | Benjamin, 2026-09-05 — high |
| Prescriber | Dr Delphine Monnier (téléconsultation Doctolib) | transcript — high |
| Initiation | **First injection Wednesday 2026-08-12.** Decision taken at the 2026-08-04 consult. Wearable signature matches: Garmin RHR jumped 51→54 bpm on 2026-08-12 itself and has sat at 52–55 bpm since (vs 48–50 pre-initiation); HRV weekly avg drifted 36→30 over the following 3 weeks | Benjamin, 2026-09-05 — high |
| Follow-up cadence | Monthly with the prescriber (first follow-up planned ~2026-09-04) | transcript — high |
| Intended duration | Multi-year (prescriber mentioned ~3 years is typical, then taper) | transcript, degraded audio — medium |
| Indication context | BMI ≈ 33, weight plateau 101–107 kg for ~15 months despite calorie tracking and regular training; episodic hyperphagia linked to fatigue; 15+ years of weight cycling (down to ~85 kg with a dietitian in the past) | transcript — high |

**Why this matters for every assessment** (details and evidence in
`.claude/skills/research-modules/glp1-endurance.md`):

1. **Resting HR is pharmacologically raised** by ~1–5 bpm as a class effect, and HRV tends to fall.
   A post-initiation RHR/HRV shift is *expected*, not an "unexplained overload / sub-clinical illness"
   signal. Readiness gates that compare to the pre-medication baseline will stay shut forever.
   → Use a **post-initiation baseline** (see `T.glp1.rebaseline_after_days_on_stable_dose`) and require
   a *second* corroborating signal (sleep, skin temperature, symptoms, HR-at-pace drift, subjective
   feedback) before treating RHR/HRV alone as a red flag.
2. **Appetite and intake are suppressed by design.** Low logged calories, skipped meals, or a
   protein shortfall are partly an effect of the drug, not only a logging or willpower problem.
   The risk flips from "eating too much" to **under-fueling an endurance athlete**: low energy
   availability, lean-mass loss, poor recovery, worse HRV. Protein floor and energy-availability
   floor in `T.glp1` apply on every training day.
3. **Weight is expected to fall.** A downward weight trend is the therapeutic goal and must not
   trigger a "weight trend reversal" or under-fueling alarm on its own. What *is* worth flagging:
   loss faster than `T.glp1.weight_loss_rate_flag_pct_per_week`, or a lean-mass share of the loss
   above `T.glp1.lean_mass_share_of_loss_flag_pct` (Withings `muscle_mass_kg` / `fat_mass_kg`).
4. **GI side effects and delayed gastric emptying** (nausea, reflux, diarrhoea/constipation,
   early satiety) cluster in the days after each injection and around dose escalations.
   Pre-run fuelling has to be earlier and lighter (`T.glp1.pre_run_meal_gap_hours_min`); a GI-heavy
   day is a legitimate reason to move or soften a session, not a "silent skip".
5. **Hydration.** Reduced thirst plus GI losses raise the dehydration risk; this compounds the
   heat protocol (`protocols/heat.md`). Hydration target in `T.glp1.hydration_target_ml_per_kg`.
6. **Lean-mass preservation** is the main long-term athletic risk of GLP-1 weight loss. Keep at
   least one resistance/strength stimulus per week in the rolling plan and protein at target.
7. **Running mechanics benefit**: every kg lost reduces ground-reaction force on the Achilles,
   patellar tendon and tibia (see `return-to-running.md` §2). Weight loss is a tailwind for the
   comeback, provided energy availability stays adequate.
8. **Hypoglycaemia** risk is low without insulin or sulfonylureas, but long sessions on a
   suppressed intake can still produce hypoglycaemia-like symptoms — fuel sessions > `T.glp1.session_duration_min_requiring_fuel` min.

**Pipeline rule:** the words "unexplained", "sub-clinical illness", "overload" or "detraining"
may not be applied to RHR, HRV, weight, appetite, nutrition-logging or GI signals without first
stating, in the same sentence, how GLP-1 therapy does or does not account for them.

## 2. Supplements

- Vitamin D — supplementation active since the Dec 2025 result (27 ng/mL, insufficient). Retest overdue.
  (Tracked in `return-to-running.md` and `objectives`; not restated here.)

## 3. Conditions and history (from the 2026-08-04 consult unless noted)

| Item | Detail | Relevance to the digest |
|---|---|---|
| Obesity, BMI ≈ 33 | Long-standing weight cycling since ~2011; plateau 101–107 kg over 15 months before GLP-1 | Primary reason for GLP-1; weight objective 95 kg (`objectives` 218d1c78) |
| Episodic hyperphagia | Fatigue-driven overeating episodes (self-reported) | Sleep fragmentation → intake spikes; GLP-1 expected to blunt this |
| Obstructive sleep apnoea — resolved | Tonsillectomy (amygdalectomie) for OSA; "réglé complètement" since | If snoring/SpO2 dips reappear with weight change, worth mentioning to GP |
| Left-ear tympanoplasty | After recurrent otitis | None for training |
| Cystic-fibrosis carrier (heterozygous) | Found during PMA genetic work-up; partner not a carrier | No clinical impact expected; note only for GP context |
| Family history | Maternal grandfather: stomach cancer + diabetes (type unknown); maternal grandmother: cancer (generalised) | Diabetes family history → keep an eye on fasting glucose / HbA1c in the annual panel |
| Former smoker | Quit (date not stated) | None |
| Alcohol | Near-abstinent for ~6 months as of Aug 2026 (rare cider on holiday) | Alcohol not a confounder for HRV/sleep by default |
| Recurrent functional GI episodes (Apr–May 2026) | Loose stools after high-fat / high-caffeine or high-FODMAP meals; one exercise-linked episode (`oh_symptoms_log`) | Baseline GI reactivity exists **before** GLP-1 — do not attribute every GI episode to the drug, and vice-versa |
| Mechanical low-back pain (Jun 2026) | Mild, linked to carrying Léonie + e-bike posture | Watch with rising run volume |

## 4. Care team

| Role | Name | Channel |
|---|---|---|
| GLP-1 prescriber / weight management | Dr Delphine Monnier | Doctolib teleconsultation, monthly |
| GP (médecin traitant) | not recorded | — |
| Past dietitian (Ipso, 6 months) | not named | Protein-deficit finding, pre/post-training snack structure |

## 5. Life context (stable facts only)

- Age 42, male, 178 cm. First child Léonie born 2026-01-09 (cohabitant sleep data via `baby mcp`).
- IT project manager at AXA (Nanterre); e-bike commute ~2×/week; "sur site" calendar events = no training.

## 6. Known unknowns — ask Benjamin / update when known

- [ ] Molecule, brand and current dose of the GLP-1 agonist; dates of any dose escalation
- [x] Date of first injection — 2026-08-12 (confirmed 2026-09-05)
- [x] Weekly injection day — Wednesday (confirmed 2026-09-05)
- [ ] Whether the prescriber gave any exercise-specific guidance
- [ ] Médecin traitant identity for the GP-conversation-seeds section
- [ ] `oh_user_profile.medications` in the biometrics DB is still `[]` — Benjamin should add the GLP-1 entry there so DB-side tooling sees it too

---
*Created 2026-09-05 after Benjamin flagged that every health assessment was ignoring his GLP-1 therapy.*

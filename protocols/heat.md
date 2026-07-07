# Heat Protocol — Outdoor Training in Warm Conditions

**For the coach.** How to adjust (or cancel) outdoor sessions when it's hot. Air temperature alone is a poor guide — humidity, sun, and the athlete's own physiology decide the real strain. This protocol is deliberately conservative for Benjamin's current profile and overrides any generic "trim the duration a bit" instinct.

Numeric bands live in `protocols/thresholds.yaml` under `heat:` — never hardcode them here. This document is the reasoning; the YAML is the source of truth for the numbers.

---

## 1. Why the generic thresholds are wrong for Benjamin right now

Population heat guidance assumes a lean, heat-acclimatized athlete. Benjamin is the opposite on every axis that matters, so every band shifts **cooler** (more conservative):

1. **Body mass ~103 kg.** Metabolic heat production and heat storage scale with mass; a big athlete's core temperature rises faster for the same pace. More mass, less surface-area-to-mass ratio to dump heat.
2. **Comeback / deconditioned.** Lower running fitness ⇒ higher relative cardiovascular strain at any pace ⇒ less spare capacity for skin blood flow and sweating. VO2max still well below peak-year.
3. **Poorly heat-acclimatized.** Primary modality has been e-bike commuting; likely little sustained heat exposure. Acclimatization takes 7–14 days of exposure to build and decays within ~1–2 weeks without it.
4. **Age 42, and a young child at home.** Sleep is adequate but occasionally fragmented; heat plus sleep debt compounds strain.
5. **Tissue-tolerance is already the bottleneck.** Heat pushes HR and perceived effort up for the same mechanical load — easy to drift out of the intended easy zone without noticing.

**Use apparent temperature ("feels-like" / heat index), not the raw air temperature.** If a WBGT reading is available, prefer it (see §4 mapping). The forecast pulled in Phase 1 should be the feels-like value for the planned session hour, not the daily high in the abstract.

---

## 2. The bands (see `thresholds.yaml: heat`)

Applied to the **feels-like temperature at the session's actual start hour**, after the post-heatwave modifier in §3.

| Feels-like | Flag | Outdoor running | Cycling |
|---|---|---|---|
| ≤ `green_max` | **Green** | Normal training. | Normal. |
| `green_max`–`yellow_max` | **Yellow — caution** | Move to the coolest window (early AM before ~8h, or late evening). Z1–Z2 only, ease pace 10–20 s/km. Pre-hydrate; carry ≥500 mL + electrolytes for runs >40 min. Shade + soft surface. | Fine at endurance intensity; hydrate. |
| `yellow_max`–`orange_max` | **Orange — high** | Easy Z1–Z2 only, **cut duration ~30–40%**, dawn only — **or substitute indoor** (treadmill in AC) — **or swap to rest**. No moderate/hard. ≥750 mL + electrolytes. | Endurance only, dawn or move indoors (home trainer). |
| > `orange_max` | **Red — extreme** | **No outdoor running.** Indoor treadmill in AC at reduced volume, or rest / mobility / strength. | No outdoor endurance rides; home trainer or rest. |

**Timing is the first lever, not duration.** Before trimming a session, move it to the coolest hour of the day. A 45-min easy run at 06:30 is safer than a 30-min run at 11:00. Only after timing is optimized do duration cuts and substitution come into play. "Trim 20% and run at midday" is never the right answer.

---

## 3. Post-heatwave modifier (this is the part the coach keeps getting wrong)

A recent heatwave does **not** clear the moment temperatures drop. Acclimatization is incomplete, and cumulative strain — sleep debt, dehydration, elevated RHR, suppressed HRV — lingers for days.

**Trigger:** a heatwave in the last `heat.post_heatwave_window_days` days, defined as ≥3 consecutive days of feels-like max ≥ `heat.heatwave_defining_feels_like`, **or** any official Météo-France *canicule* (orange/red) alert in that window.

**While the modifier is active:**
- **Lower every band boundary by `heat.post_heatwave_shift_celsius`°C.** A 25°C day one week after a heatwave is treated like ~28°C — i.e., Orange, not Yellow. Easy dawn run or substitute; not a normal session.
- **Default toward substitution** in the Orange band rather than pushing an outdoor run.
- **Cross-check recovery markers.** If RHR is still elevated vs the 4-week baseline, or HRV still suppressed, treat conditions as **one band hotter** until they normalize. This ties the heat decision to Benjamin's actual physiological state, not just the thermometer.

---

## 4. WBGT mapping (if available)

If a WBGT (wet-bulb globe temperature) figure is available, prefer it — it captures humidity, radiant sun, and wind. Rough equivalence to the flags above, already shifted for this athlete:

- WBGT < 18°C → Green
- 18–23°C → Yellow
- 23–28°C → Orange
- > 28°C → Red (many road races cancel here for the general field)

---

## 5. Hydration & cooling (all bands above Green)

- Pre-hydrate: ~400–500 mL in the 1–2 h before.
- During: ~500–750 mL/h with electrolytes (sodium) for efforts >45 min in the heat; more if visibly sweating heavily.
- Pre-cooling (cold drink, cool shower) and post-session cooling help at Orange+.
- Light-colored, breathable kit; cap/visor in sun; plan a route with shade and water access.

---

## 6. Abort mid-session — stop immediately

Heat illness escalates fast. Stop and cool down if any of:
- Dizziness, headache, nausea, or feeling "off."
- Goosebumps / chills or **stopping sweating** despite the heat (danger sign).
- Disorientation, confusion, or loss of coordination.
- HR drifting far above the zone for the pace, or unable to bring it down when easing off.

These override any planned session. Walk to shade, cool the skin, hydrate; seek help if symptoms don't ease quickly.

---

## 7. What NOT to do

- ❌ Run at midday because "it's only 34°C, just cut 20%."
- ❌ Treat the daily forecast high as the session condition when the run is at a cooler hour — but equally, don't use a cool dawn number to justify a midday run.
- ❌ Ignore a recent heatwave once the peak has passed.
- ❌ Push an outdoor run in Orange/Red to "not lose fitness." Substituting indoors or resting one day costs nothing against the comeback; a heat-illness episode or a heat-driven overreach costs weeks.

---

*Evidence class: consensus / guideline (ACSM Position Stand on Exertional Heat Illness; WBGT flag systems used in road-race medical guidance). Thresholds personalized conservatively for a ~103 kg, deconditioned, poorly-acclimatized 42-year-old in a running comeback. Revisit as body weight drops and heat acclimatization builds.*

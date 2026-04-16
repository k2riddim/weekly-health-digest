# HR Training Zones

*Populated by bootstrap from recent Strava HR distribution (2026-04-16). Update manually if a new fitness test warrants revision.*

## Estimation basis

- **Estimated HRmax**: 198 bpm — derived from highest observed max_heart_rate in Strava over last 2 years (210 bpm, likely near-maximal effort), adjusted conservatively. All-time max of 235 bpm excluded as probable recording artifact.
- **Resting HR**: 53 bpm — 7-day average from Garmin (April 9–16, 2026).
- **Method**: Standard %HRmax bands. Karvonen reserve-based ranges provided for reference.

## Zone table

| Zone | Name            | %HRmax  | BPM Range   | Karvonen (%HRR) | Typical use                    |
|------|-----------------|---------|-------------|------------------|--------------------------------|
| Z1   | Active Recovery | 50–60%  | 99–119 bpm  | 50–60% → 126–140 | Warm-up, cooldown, easy walks  |
| Z2   | Aerobic Base    | 60–70%  | 119–139 bpm | 60–70% → 140–155 | Long rides, easy runs, base    |
| Z3   | Tempo           | 70–80%  | 139–158 bpm | 70–80% → 155–169 | Tempo runs, sustained efforts  |
| Z4   | Threshold       | 80–90%  | 158–178 bpm | 80–90% → 169–183 | Intervals, threshold work      |
| Z5   | VO2max          | 90–100% | 178–198 bpm | 90–100% → 183–198| Short intervals, sprints       |

## Validation against recent data

- E-bike commutes: avg HR 108 bpm → **Z1** (expected — motor-assisted, low effort)
- Virtual ride (Zwift Sweet Spot): avg HR 132, max 149 → **Z2** avg, **Z3** peak (consistent with sweet spot training)
- Gravel ride (last 90d): avg HR 145, max 168 → **Z3** avg, **Z4** peak (typical for outdoor efforts)
- 2023 peak-year running: avg HR 146 → **Z3** (tempo-dominant running profile)
- 2023 peak-year cycling: avg HR 133 → **Z2** (aerobic base riding)

## Notes

- These zones are approximate until validated by a field test (e.g., 30-min time trial for lactate threshold, or graded exercise test).
- The relatively low HRV scores (35–42 ms) and VO2max estimate (40.9) suggest current fitness is significantly below peak. Zones remain valid as they're anchored to HRmax, which is physiology-stable.
- During rebuild phase, >80% of training time should be in Z1–Z2.

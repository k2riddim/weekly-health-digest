# HR Training Zones

*Last refreshed 2026-08-15 from live Garmin/Strava data. Update manually if a new fitness test warrants revision.*

## Estimation basis

- **Estimated HRmax**: 198 bpm — derived from highest observed max_heart_rate in Strava over last 2 years (210 bpm, likely near-maximal effort), adjusted conservatively. All-time max of 235 bpm excluded as probable recording artifact. (HRmax is physiology-stable — not revisited monthly unless a field test says otherwise; most recent 2-year window now tops out at 184 bpm in the live query, consistent with no near-maximal efforts logged recently, not a change in true HRmax.)
- **Resting HR**: 52 bpm — 7-day average from Garmin (Aug 8–14, 2026). Up from 50 bpm (June); last 3 days (Aug 12–14) elevated to 52–55 bpm, coinciding with travel (Saint-Malo) — watch for continued drift before resuming full training volume.
- **Method**: Standard %HRmax bands. Karvonen reserve-based ranges provided for reference.

## Zone table

| Zone | Name            | %HRmax  | BPM Range   | Karvonen (%HRR) | Typical use                    |
|------|-----------------|---------|-------------|------------------|--------------------------------|
| Z1   | Active Recovery | 50–60%  | 99–119 bpm  | 50–60% → 124–138 | Warm-up, cooldown, easy walks  |
| Z2   | Aerobic Base    | 60–70%  | 119–139 bpm | 60–70% → 138–153 | Long rides, easy runs, base    |
| Z3   | Tempo           | 70–80%  | 139–158 bpm | 70–80% → 153–168 | Tempo runs, sustained efforts  |
| Z4   | Threshold       | 80–90%  | 158–178 bpm | 80–90% → 168–183 | Intervals, threshold work      |
| Z5   | VO2max          | 90–100% | 178–198 bpm | 90–100% → 183–198| Short intervals, sprints       |

## Validation against recent data (2026 activities)

- E-bike commutes (n=30): avg HR 104 bpm → **Z1** (expected — motor-assisted, low effort)
- Virtual rides (n=8): avg HR 129, max 167 → **Z2** avg, **Z3–Z4** peak
- Gravel rides (n=4): avg HR 141, max 168 → **Z3** avg, **Z3–Z4** peak
- Running comeback (n=27, May–Aug 2026): avg HR 133–146 bpm → **Z2–Z3** (appropriate pacing); longest run to date 10.5 km (Jul 25, Saint-Malo hills) at avg HR 145
- 2023 peak-year running: avg HR 146 → **Z3** (tempo-dominant running profile)
- 2023 peak-year cycling: avg HR 133 → **Z2** (aerobic base riding)

## Notes

- These zones are approximate until validated by a field test (e.g., 30-min time trial for lactate threshold, or graded exercise test).
- HRV weekly avg holding at 35 ms as of Aug 2026 (flat vs June, still below the 39–40 mid-May peak). VO2max running now 42.9 (up from 40.6 in June). VO2max cycling shows an anomalous jump to 42.9 (from a stable 38.6, now identical to the running figure) starting Aug 11 — likely a Garmin sync artifact rather than a genuine gain; do not treat as a real training-zone input until it diverges from the running value. Zones stay valid as they're anchored to HRmax, which is physiology-stable.
- Running comeback underway since May 3, 2026 (27 runs completed; distances now ranging 4–10.5 km, active block in `protocols/active_block.md` progressing toward a 12 km objective). During this phase, >80% of training time should be in Z1–Z2.

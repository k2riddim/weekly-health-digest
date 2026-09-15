# HR Training Zones

*Last refreshed 2026-09-15 (monthly maintenance pass) from live Garmin/Strava data. Update manually if a new fitness test warrants revision.*

## Estimation basis

- **Estimated HRmax**: 198 bpm — derived from highest observed max_heart_rate in Strava over last 2 years (210 bpm, likely near-maximal effort), adjusted conservatively. All-time max of 235 bpm excluded as probable recording artifact. (HRmax is physiology-stable — not revisited monthly unless a field test says otherwise; still no near-maximal efforts logged recently, not a change in true HRmax.)
- **Resting HR**: 54 bpm — 7-day average from Garmin (Sep 7–13, 2026), up from 52 bpm (Aug 8–14). Sep 8–9 saw a sharper spike to 57–58 bpm, coinciding with the Wegovy label's *expected* 0.5 mg step date (2026-09-09) — **unconfirmed**, see `protocols/health-profile.md`. RHR has since settled back to 51–53 bpm (Sep 10–13). Read against the post-initiation baseline (`T.glp1`), not the pre-medication one — see `.claude/skills/research-modules/glp1-endurance.md`.
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
- Running comeback (n=34, May–Sep 2026): avg HR 133–146 bpm → **Z2–Z3** (appropriate pacing); longest run to date still 10.5 km (Jul 25, Saint-Malo hills) at avg HR 145 — no run has exceeded that since
- 2023 peak-year running: avg HR 146 → **Z3** (tempo-dominant running profile)
- 2023 peak-year cycling: avg HR 133 → **Z2** (aerobic base riding)

## Notes

- These zones are approximate until validated by a field test (e.g., 30-min time trial for lactate threshold, or graded exercise test).
- HRV weekly avg down to 30–31 ms as of mid-Sep 2026 (Garmin status **LOW** since ~Sep 5, vs 35 ms/BALANCED in Aug and the 39–40 mid-May peak). Falls inside the expected GLP-1 class effect on the post-initiation baseline — see `T.glp1` and `.claude/skills/research-modules/glp1-endurance.md` before treating it as a red flag on its own. VO2max running now 42.3 (down slightly from a 42.9 Aug peak, tracking reduced run volume — see below). VO2max cycling is still 42.9, unchanged since Aug 11; it has now **diverged** from the running figure (42.3), which weakens the original "identical to running = likely shared artifact" read — still unconfirmed as a genuine cycling-fitness signal, now better read as a stuck/stale reading. Zones stay valid as they're anchored to HRmax, which is physiology-stable.
- Running comeback underway since May 3, 2026 (34 runs completed; distances ranging 3.5–10.5 km). The C4 active block (`protocols/active_block.md`, rev 2026-07-29) reached its 13/09 end-of-block deadline without the 12 km objective attempt and has been archived to `protocols/archive/2026-c4-block-21-40.md`; no active block currently covers the coming week — see that file for the next-block starting point. During this phase, >80% of training time should be in Z1–Z2.

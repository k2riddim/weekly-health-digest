---
name: investigation
description: Spawns a standalone deep-dive investigation when a Phase 3 signal warrants extended analysis. Creates structured files under investigations/.
---

# Investigation Skill

Activated when a Phase 3 deep-dive signal is strong enough to warrant a standalone study. This skill handles all file scaffolding and index maintenance.

## Trigger criteria

Spawn an investigation when the signal is:
1. **Strong enough** — deviation exceeds 2σ from personal baseline, or a novel pattern not seen in prior weeks
2. **Requires extended analysis** — more than a single paragraph of interpretation, possibly chart-based
3. **Novel** — not a repeat of a previously investigated topic (check `investigations/README.md` index)

## Procedure

### 1. Create investigation directory

```
investigations/YYYY-WW-<slug>/
├── hypothesis.md
├── analysis.py    (optional — only if computational analysis needed)
└── findings.md    (written after analysis completes)
```

Where `<slug>` is a short kebab-case descriptor (e.g., `hrv-downtrend`, `sleep-fragmentation-spike`, `ferritin-drop`).

### 2. Write `hypothesis.md`

Must contain all of the following:

- **Expected signal**: What pattern was observed and what it might mean
- **Falsification criterion**: What result would disprove the hypothesis
- **Tables queried**: List every biometrics/baby MCP table that will be consulted
- **Sample size**: How many days/observations are available for this analysis
- **Prior investigations**: Reference any related prior investigations from the index

Example structure:
```markdown
# Hypothesis: [title]

## Expected signal
[Description of the observed anomaly and proposed explanation]

## Falsification criterion
[Specific result that would disprove this hypothesis]

## Data sources
- Tables: [list]
- Date range: [range]
- Sample size: [N observations]

## Related prior investigations
- [links or "none"]
```

### 3. Write `analysis.py` (optional)

If the investigation requires computation beyond SQL queries:
- Write a Python script that processes data exported from MCP queries
- Script should read from stdin or a JSON file and write results to stdout
- Keep dependencies to stdlib only (json, statistics, csv, datetime)
- Run the script and capture output

### 4. Run the analysis

- Execute all planned SQL queries via `biometrics:query` and/or `baby mcp:query`
- If `analysis.py` exists, run it with the query results
- Cross-reference at least 2 tables per claim

### 5. Write `findings.md`

Summarize results:
- **Conclusion**: supported / refuted / inconclusive
- **Key data points**: the numbers that drive the conclusion
- **Confidence level**: high / medium / low, with reasoning
- **Recommendation**: actionable next step, if any
- **Limitations**: what data gaps exist

### 6. Update `investigations/README.md` index

Append a new entry:
```markdown
## YYYY-WW-<slug>
- **Topic**: [one-line description]
- **Status**: [complete / in-progress]
- **Conclusion**: [one-line summary]
- **Files**: `investigations/YYYY-WW-<slug>/`
```

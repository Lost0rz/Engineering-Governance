# Incident Record — <Short Title>

## 1. Context & Observed Identity
- **Scope / Symptom (`USER_REPORTED_SYMPTOM`):**
- **Runtime Identity:** `REPO_REV=<sha|unknown>` · `BUILD=<id|unknown>` · `ENV/CONFIG=<id|unknown>` · `WINDOW=<ts|unknown>`
- **Evidence Reviewed:** <paths, logs, test outputs, or `codebase-context` route>

## 2. Blocked Decision & Hypotheses
- **Evidence Sufficiency:** `SUFFICIENT (NO NEW PROBE)` | `INSUFFICIENT`
- **Missing Fact & Blocked Decision:** <concrete missing fact -> blocked decision>
- **Hypotheses (`OPEN | SUPPORTED | WEAKENED | FALSIFIED`):**
  1. `<hypothesis>` — Support: `<obs>` · Falsify: `<obs>` · Result: `<observed>`

## 3. Minimal Probe & Fresh Observations
- **Probe (if added):** `<smallest discriminating probe>` · **Class:** `TEMPORARY | DURABLE | NO_PROBE` · **Remove when:** `<condition>`
- **`DIRECT_OBSERVATION`:** <exact capture post-probe>
- **`INTERPRETATION`:** <reasoned inference kept distinct from observations>

## 4. Root Cause & Minimum Fix Boundary
- **`ROOT_CAUSE_CLAIM`:** <evidence-backed causal boundary | `UNKNOWN` | `BOUNDED`>
- **Minimum Fix Boundary:** <smallest safe code/config change, or `none / unresolved`>
- **Authorization:** <within current `G1`/`G2` task scope, or paused for `G3`/scope user confirmation>

## 5. Verification, Probe Cleanup & Open Unknowns
- **Post-fix Verification (`V1`–`V3`):** <selected tier + commands + observed pass/fail>
- **Probe Disposition:** <removed/reverted | retained with justification>
- **Unresolved Unknowns:** <remaining gaps, if any>

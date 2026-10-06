# Reference Audit — OpenSSF Scorecard

**Verified:** 2026-10-06  
**Source identity:** OpenSSF `ossf/scorecard` upstream `main` README, check
registry, and check docs as accessed on the date above. These upstream pages
are mutable; the access date is recorded as the reference revision.

**Primary sources:**

- [Scorecard README](https://github.com/ossf/scorecard/blob/main/README.md)
- [Check documentation](https://github.com/ossf/scorecard/blob/main/docs/checks.md)
- [Source check registry](https://github.com/ossf/scorecard/blob/main/docs/checks/internal/checks.yaml)
- [Beginner guide to checks](https://github.com/ossf/scorecard/blob/main/docs/beginner-checks.md)

## Shared 14-question audit

### 1. What problem does it solve?

Scorecard automatically evaluates open-source software security practices and
provides per-check results to help maintainers and consumers identify supply
chain risk.

### 2. What is the canonical source of truth?

The checked repository and hosting-provider data are inputs to an evaluator.
The upstream `checks.yaml` is the source of truth for check descriptions and
remediation text; a result/report is a dated evaluation, not the repository's
canonical configuration or a universal compliance authority.

### 3. How do global policy and project-local configuration relate?

Scorecard supplies a reusable set of checks, but its README states it is not a
one-size-fits-all requirement: which checks matter depends on audience,
applicability, and feasibility. A project can run a subset. It does not define
a general global-to-local profile inheritance model.

### 4. How are rules and checks represented?

Checks have stable names, scoring criteria, risk labels, descriptions, and
remediation guidance. The source registry is structured YAML and generates
human-readable docs. Results include per-check score, reason/details, and a
link to check documentation; a weighted aggregate is optional output.

### 5. How are machine-decidable and judgment-based checks distinguished?

Checks are automated heuristics over detectable repository/provider evidence.
The project explicitly warns about false positives, false negatives, and
undetected equivalent practices. The numeric result must not be presented as
human judgment or complete proof.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Check selection and some check-specific configuration allow tailoring. A `?`
result can mean the evaluator lacked a qualifying observation in an example;
it must not be silently converted to pass or confused with an approved waiver.
Scorecard does not supply a universal scoped, expiring waiver contract.

### 7. How are version, compatibility, and compliance tracked?

The executable can be installed at a release/tag, and checks evolve over time.
The README warns that check heuristics and aggregate scores can change. A
reproducible evaluation therefore needs tool version, check-registry revision,
target revision, and observation time.

### 8. What evidence does a finding require?

The per-check reason and details point to detected evidence and the applicable
check documentation/remediation. Evidence should be retained per check instead
of relying on a weighted aggregate, which can hide distinct behaviors.

### 9. How is remediation represented?

Each check documents risk and remediation steps. Scorecard reports those steps;
it does not itself rewrite the repository to remediate a finding.

### 10. How are automatic enforcement and advisory separated?

The CLI/action evaluates and reports. Teams may use CI status or repository
rules to gate changes, but that gate is an external policy choice. Scorecard's
result is not itself a repair action.

### 11. How does it avoid stale configuration or meaningless repeated checks?

The GitHub Action can run on repository changes; the public scan data is
weekly and explicitly dated/cached. These schedules expose freshness as a
separate property. Scorecard does not provide semantic dependency-based
rechecking for unrelated project checks.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

The security-specific heuristic library, large provider integrations,
aggregate weighted score, public dataset, and supply-chain scanning workflow
are not a general engineering governance model.

### 13. What capability gap does it expose?

It demonstrates individual check identity, severity/risk, applicability
caveats, actionable remediation, and reason/detail-bearing results. It also
shows why a single aggregate score obscures the underlying decisions.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** the per-check registry and evidence-bearing finding contract, while
preserving explicit `UNVERIFIED` and `NOT_APPLICABLE` meanings. Do not adopt a
single composite governance score as acceptance.

## Mechanism dispositions

- **ADOPT:** stable individual check identity, risk/severity, applicability,
  evidence/result details, and remediation pointer.
- **ADAPT:** heuristic result confidence and freshness into explicit
  `MACHINE`/`AI_JUDGMENT`/`HUMAN`/`HYBRID` review modes and evidence status.
- **DEFER:** broad security check library and public cross-project scanning.
- **REJECT:** an aggregate score as a substitute for finding-level evidence or
  project-specific acceptance.

# Reference Audit — Open Policy Agent and Conftest

**Verified:** 2026-10-06  
**Source identity:** Open Policy Agent official documentation and the
`open-policy-agent/conftest` upstream README, accessed on the date above;
documentation/repository links are mutable and no release pin is claimed.

**Primary sources:**

- [OPA documentation](https://www.openpolicyagent.org/docs)
- [OPA policy language](https://www.openpolicyagent.org/docs/policy-language)
- [OPA deployment](https://www.openpolicyagent.org/docs/deploy)
- [OPA integration](https://www.openpolicyagent.org/docs/integration)
- [Conftest README](https://github.com/open-policy-agent/conftest)

## Shared 14-question audit

### 1. What problem does it solve?

OPA separates policy decision-making from the application or system that
enforces a decision. Conftest applies policy tests to structured configuration
and infrastructure data, returning pass/fail results and messages.

### 2. What is the canonical source of truth?

Policy source files and their input data are the evaluator inputs. OPA's
decision result is a derived answer for a particular input and policy bundle;
it does not become the authority for the underlying application fact.
Conftest similarly evaluates files without replacing them as source.

### 3. How do global policy and project-local configuration relate?

OPA can distribute policy bundles and evaluate caller-supplied input; the
integration determines how policy is loaded and which input is in scope.
Conftest commonly keeps Rego tests with the repository/configuration. Neither
defines a universal profile inheritance or exception chain for this candidate.

### 4. How are rules and checks represented?

OPA policies are written in Rego, which expresses decisions over structured
data. Conftest discovers policy tests and evaluates them against supported
structured files; test names and failure messages can identify the rule and
the reason a case failed.

### 5. How are machine-decidable and judgment-based checks distinguished?

Rego evaluation is machine-decidable for a given input. The policy authors'
choice of desired architecture, risk tolerance, or applicability can still
encode a human decision. An automated result must not disguise those policy
assumptions as objective facts.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Policies can encode input-specific branches and repository-level policy
choices, but OPA/Conftest do not impose a standard, expiring exception record
with grantor, rationale, scope, evidence, and revocation. Undefined or absent
input is not automatically an approved exception.

### 7. How are version, compatibility, and compliance tracked?

OPA, Rego, policy bundles, and input schemas have separate version identities.
Deployments can distribute versioned bundles, but the tools do not define a
general governance-standard/profile compatibility ledger. Reproducibility
requires recording policy revision, evaluator version, input revision, and
evaluation time.

### 8. What evidence does a finding require?

The useful evidence is the exact input/source revision, policy bundle or Git
revision, evaluator version, result, and failure message. A pass/fail response
without those identities is difficult to reproduce and does not prove that
the intended source was evaluated.

### 9. How is remediation represented?

Conftest reports test failures and messages so a maintainer can change the
source configuration or policy. OPA returns decisions to an integration
point. Neither requires an automatic source rewrite as part of evaluation.

### 10. How are automatic enforcement and advisory separated?

OPA explicitly separates a policy decision point from a policy enforcement
point. The caller decides whether and how a decision blocks or changes an
operation. Conftest can run in CI, but an external CI status rule is the gate.
This separation is a key candidate contract.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Integrations select policy bundles, inputs, and evaluation triggers. Bundle
revision and input freshness can be controlled by the adopter, but OPA does
not automatically determine semantic dependencies between arbitrary
governance evidence. Conftest reruns when its configured workflow runs.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

A central policy decision service, Rego runtime, bundle distribution,
provider integrations, and a general policy engine are unnecessary for a
documentary Git-native candidate.

### 13. What capability gap does it expose?

It makes the decision/enforcement boundary concrete and demonstrates that
policy inputs, policy source, evaluator, and action belong to distinct
identities. The candidate needs a lighter decision record and must leave
enforcement to an explicitly authorized caller.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** the policy decision/evaluation separation and evidence-bearing test
results. Keep v0.1 evaluations advisory or explicitly human-approved gates;
do not introduce a policy service or an automatic remediation point.

## Mechanism dispositions

- **ADOPT:** distinguish policy evaluation from the caller's enforcement
  decision; preserve input, policy, evaluator, and result identity.
- **ADAPT:** named machine checks and messages into a small check registry and
  finding record.
- **DEFER:** Rego execution, bundle APIs, and centralized policy distribution.
- **REJECT:** treating a policy result as source authority or silently
  performing remediation.

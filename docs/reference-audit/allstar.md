# Reference Audit — OpenSSF Allstar

**Verified:** 2026-10-06  
**Source identity:** OpenSSF `ossf/allstar` upstream `main` README and linked
configuration documentation as accessed on the date above; no immutable source
revision was captured, so the access date is the audit anchor.

**Primary sources:**

- [Allstar README](https://github.com/ossf/allstar/blob/main/README.md)
- [Manual installation](https://github.com/ossf/allstar/blob/main/manual-install.md)

**Current operational fact:** the README states the OpenSSF-hosted Allstar
GitHub App has been retired. Allstar remains maintained, but adopters must run
their own GitHub Action or service daemon. This was verified from the upstream
README on the audit date.

## Shared 14-question audit

### 1. What problem does it solve?

Allstar monitors GitHub organizations/repositories for selected security
configuration policies, reports violations, and for some policies can restore
a setting to the configured value.

### 2. What is the canonical source of truth?

Policy configuration is stored in the organization `.allstar` control
repository and, when allowed, repository-local `.allstar` files. The actual
GitHub repository settings being evaluated remain the live state Allstar
observes; configuration expresses desired policy, not proof that the setting
currently holds.

### 3. How do global policy and project-local configuration relate?

Allstar has organization-level opt-in/opt-out configuration, repository
overrides gated by an org setting, and policy-level configuration. The docs
specify source precedence and an optional `baseConfig` merge using JSON Merge
Patch. This is an explicit inheritance mechanism, but it is specialized to
GitHub security settings.

### 4. How are rules and checks represented?

Enablement and individual policy behavior are declared in YAML. A policy file
selects a policy and its action; org-level and repository-level paths have
documented lookup order.

### 5. How are machine-decidable and judgment-based checks distinguished?

The monitored repository settings and files are evaluated by software, so the
check result is machine-oriented. The upstream docs do not provide an
AI/human-judgment review mode; detected state can still be incomplete or scoped
to GitHub capabilities and permissions.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Repository opt-in/opt-out and policy enablement provide explicit scope controls.
They are not a generic exception record: the README does not require an owner,
reason, evidence, expiry, review date, or revocation history for each override.
It does not define a general `NOT_APPLICABLE` result.

### 7. How are version, compatibility, and compliance tracked?

Allstar releases and its own deployment version are separately managed from
the Git-versioned configuration. Configuration carries no general governance
standard/profile version or cross-version migration record.

### 8. What evidence does a finding require?

The evidence is the checked repository setting/configuration and the resulting
policy evaluation, commonly surfaced as an issue or check. A useful audit must
also record the repo, observation time, policy/config revision, and permission
scope because an unreadable setting is not proof of compliance.

### 9. How is remediation represented?

The configured action may be advisory (for example, create an issue) or may
change a supported GitHub setting back to its expected value. Action policy is
separate from the checked condition.

### 10. How are automatic enforcement and advisory separated?

Actions are selected in policy YAML. `log` is the default, `issue` reports a
finding, and policy-specific `fix` can change supported GitHub settings. The
README's action list marks `block` as proposed but not implemented, even though
the GitHub App permission discussion mentions support for it. This mismatch is
recorded rather than treating `block` as current behavior. The deployment
operator owns the GitHub App, permissions, schedule/service, and consequences;
this is stronger enforcement than the v0.1 candidate authorizes.

### 11. How does it avoid stale configuration or meaningless repeated checks?

The GitHub Action checks on a configured schedule; the daemon monitors
continuously. Repo overrides and explicit opt-in/out scope control coverage.
This detects configuration drift against remote settings but adds a running
integration and does not express dependency-based rechecking for semantic
changes.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

A self-hosted GitHub App identity, secret/key management, issue/check write
permissions, scheduled action or service daemon, and live mutation are out of
scope. The hosted OpenSSF app is retired, so it is not an available
zero-operations shortcut.

### 13. What capability gap does it expose?

It demonstrates explicit inherited defaults, repository overrides, scope
selection, and separation between policy condition and action. Governance v0.1
needs to add expiry/reason/evidence for exceptions and must cover authorities
and facts beyond GitHub configuration.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** explicit profile inheritance and project overrides, with one
reviewable precedence rule and a versioned local record. Keep evaluation and
optional enforcement separate. Do not carry Allstar's GitHub-specific live
mutation into v0.1.

## Mechanism dispositions

- **ADOPT:** configuration precedence must be explicit and project scope must
  be inspectable.
- **ADAPT:** org/base profile and repository override into a small, Git-versioned
  ProjectProfile with reasoned exceptions.
- **DEFER:** recurring policy evaluation and provider-specific issue/check
  integrations.
- **REJECT:** automatic setting repair, an always-on service, and treating a
  retired hosted app as an available governance dependency.

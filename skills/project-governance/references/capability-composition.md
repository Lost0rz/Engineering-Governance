# Capability composition

The nine Skills cooperate without competing controllers.

`project-governance` owns task/control authority, lifecycle/reconciliation, workspace boundaries, verification choice and closeout. A narrower Skill owns only its bounded capability.

## Typical composition

```text
request
-> project-governance
-> project-profile?         compact project context/index artifact only
-> solution-design?         material engineering architecture/state-ownership ambiguity
-> design?                  bounded UI/UX/frontend visual design or redesign
-> domain-navigation?       unclear semantic/source/test/runtime route
-> execution-orchestrator? useful decomposition/delegation/recovery
-> agent-handoff?           responsibility crosses contexts
-> implementation / verification
-> incident-doctor?         blocking evidence gap
-> evidence-audit?          formal independent/read-only verdict boundary
-> project-governance       alignment / closeout
```

Question marks are real gates. Installed capability is not a reason for ceremony.

`solution-design` and `design` may both participate in one governed task without competing: Solution Design resolves engineering requirements/architecture/state ownership; Design resolves bounded product-interface/frontend visual direction and execution. Project Governance remains the task/lifecycle owner.

## Handoff dimensions

Handoff `CAPABILITY` and `MODE` are separate:

- `CAPABILITY` identifies the bounded Skill/capability the receiver should use, or `NONE`;
- `MODE` identifies receiver action/side-effect class.

A mode name never replaces Skill routing or grants mutation authority.

## Artifact roles

- Normative/current/design/implementation authorities own project rules, current authorization/state, durable decisions, project-specific design facts, or implementation semantics for their class.
- Derived projections include Project Profile and Domain/navigation maps; authority wins when they are stale.
- Observed evidence/transport includes handoffs, briefs, ledgers, audits, CI/test/runtime/review observations; these cannot expand scope or replace authority.

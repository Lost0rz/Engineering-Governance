# Capability composition

The eight Skills cooperate without competing controllers.

`project-governance` owns task/control authority, lifecycle/reconciliation, writer/workspace boundaries, verification choice and closeout. A narrower Skill owns only its bounded capability.

## Typical composition

```text
request
-> project-governance
-> project-profile?         compact project context/index artifact only
-> solution-design?         material design ambiguity
-> domain-navigation?       unclear semantic/source/test/runtime route
-> execution-orchestrator? useful decomposition/delegation/recovery
-> agent-handoff?           responsibility crosses contexts
-> implementation / verification
-> incident-doctor?         blocking evidence gap
-> evidence-audit?          formal independent/read-only verdict boundary
-> project-governance       alignment / closeout
```

Question marks are real gates. Installed capability is not a reason for ceremony. Advisory read-only inspection does not require a new formal audit boundary merely because evidence is being viewed.

## Handoff dimensions

Handoff `CAPABILITY` and `MODE` are separate:

- `CAPABILITY` identifies the bounded Skill/capability the receiver should use, or `NONE`;
- `MODE` identifies receiver action/side-effect class.

A mode name never replaces Skill routing or grants mutation authority.

## Artifact roles

- **Normative/current/design/implementation authorities:** sources that own project rules, current authorization/state, durable decisions, or implementation semantics for their class.
- **Derived projections:** Project Profile and Domain/navigation maps; authority wins when they are stale.
- **Observed evidence / transport:** handoffs, briefs, ledgers, audits, CI/test/runtime/review observations; these cannot expand scope or replace authority.

Same-purpose work keeps one task across agents/contexts. One objective may span repositories, but each repository keeps its own control/write authority. Parallel writers require proven-disjoint semantic write authority and integration evidence.

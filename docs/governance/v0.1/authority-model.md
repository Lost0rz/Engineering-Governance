# Authority Model and Authority Map

## Definitions

- **Canonical authority:** the source authorized to define or record a
  particular class of fact.
- **Consumer projection:** a derived view assembled for display, search, or
  convenience. It points to an authority and does not supersede it.
- **Governance control:** a rule or task boundary that constrains an agent or
  operator but does not automatically become product behavior.
- **Evidence:** a dated observation/result that supports a claim about an
  authority or consumer; evidence is not itself the underlying fact.

There may be distinct owners for product intent, domain facts, implementation,
runtime state, and governance controls. A single repository may host several
authorities, but the map must state each fact class and its owner. A distinction
is required whenever separate sources can change independently, consumers
derive a view, or an authority boundary affects a consequential decision.

## Authority map entry

Each entry SHOULD include:

- `authority_id` and `fact_class`;
- `owner` and accountable contact/role;
- `canonical_location` (repository/path, API, data store, or human decision
  record);
- `scope` and explicitly excluded scope;
- `consumers` and relationship (`READS`, `DERIVES`, `MIRRORS`,
  `PROPOSES_CHANGE_TO`);
- `contract_or_schema` and exact version/revision where available;
- `freshness_source` and expected update/verification condition;
- semantic impact when this authority changes;
- `state`: `AS_IS` or `TO_BE`;
- last verified revision/time and evidence pointer.

If exact identity is unavailable, say `UNKNOWN`; do not invent a canonical
source. A read projection may be authoritative for its own returned shape
while still being derived from another canonical fact source; record both
scopes explicitly.

## Typed authority routing

Authority classes are distinct; they do not form a total precedence list.
Each claim or action is routed to the owner for its class:

| Claim/action class | Authority and boundary |
|---|---|
| Product, domain, and architecture semantics | The project's declared canonical product/domain source and accepted contract/ADR define meaning. They do not grant permission to perform work outside the active task. |
| Repository and remote-host state | Verified Git/GitHub state owns repository, branch, commit, PR, and CI claims. Those facts do not decide product semantics. |
| Shared current-state snapshot | `CURRENT_STATUS.md` publishes a concise verified project snapshot for coordination. It is authoritative for the snapshot it declares, but cannot rewrite the underlying semantic, Git, runtime, or data facts it summarizes. |
| Execution authorization and scope | User authorization and the active `CURRENT_TASK.md` define what work is allowed now, subject to durable `AGENTS.md` workflow rules. A task cannot rewrite canonical business/domain truth. |
| Runtime and data facts | Use the project-declared runtime or data authority for that fact, with verified identity, scope, and observation time. |
| Derived evidence and projections | Evaluations, findings, summaries, generated views, and AI analysis support claims but are not source authorities. |

Business/domain truth does not authorize work outside `CURRENT_TASK.md`;
`CURRENT_TASK.md` cannot rewrite business/domain truth; Git/GitHub facts do not
decide product semantics; and findings, evidence, or projections do not
become source authorities. When two sources compete for the same claim or
action class, use that class's declared owner and resolution rule. If the
owner is unclear or evidence cannot resolve a same-class conflict, stop the
affected decision. Split mixed claims into their distinct classes rather
than letting one class override another.

## Change propagation

When an authority changes, identify dependent profile fields, checks, and
evidence. Mark the freshness assessment for impacted evaluations stale until
required dependency rechecks are complete; preserve each historical result.
Do not copy the changed fact into the finding as a new source of truth;
retain a link to the authoritative revision.

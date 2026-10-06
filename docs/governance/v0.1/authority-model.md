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

## Default authority order

The applicable project controls declare actual authority. As a navigation
order when inspecting an adopted repository:

1. The canonical owner for the fact class in question.
2. Accepted domain/product/architecture contract defining its semantics.
3. Verified Git/GitHub state for repository, branch, commit, PR and CI facts.
4. Root `AGENTS.md` for stable workflow boundaries.
5. `CURRENT_STATUS.md` for concise current-state claims.
6. `CURRENT_TASK.md` for active task scope and acceptance.
7. Evaluations, findings, summaries, generated views, and AI suggestions as
   derived evidence only.

This list does not override a repository's explicit authority contract. If
the declared owner differs, follow the declaration only if it is itself
authorized and verified. Otherwise record a conflict and stop the affected
decision.

## Change propagation

When an authority changes, identify dependent profile fields, checks, and
evidence. Mark impacted evaluations stale until the required dependency
rechecks are complete. Do not copy the changed fact into the finding as a new
source of truth; retain a link to the authoritative revision.

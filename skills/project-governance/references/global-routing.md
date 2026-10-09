# Global Skill routing

Use this contract when Engineering Governance is adopted into a user's cross-project agent rules. It answers one question only: **which Engineering Governance Skill should handle the request now?** It does not duplicate the detailed workflow owned by any Skill.

## Routing precedence

1. Follow higher-priority system, developer, user, and explicitly selected Skill instructions.
2. Follow the selected repository's applicable `AGENTS.md` and declared project controls.
3. For software/project/repository engineering work that acts on or reasons about a project/repository, use `project-governance` as the normal Engineering Governance entry point unless a higher-priority instruction already selected a narrower Engineering Governance route.
4. Route conditionally from that governed work when one of the narrower capability triggers below is met.

Project Governance is intentionally lightweight for simple, low-risk repository work: entering through it does not require creating extra plans, branches, worktrees, broad scans, or broad validation when the project/task does not need them. Do not force Engineering Governance onto casual conversation, general knowledge work, writing-only requests, or other non-project/non-engineering activity merely because the Plugin is installed.

## Route table

| Situation | Route | Return path |
| --- | --- | --- |
| Starting, planning, executing, reconciling, verifying, handing off, or closing project/repository engineering work, including simple low-risk changes | `project-governance` | Remain in Project Governance unless a narrower route is needed; scale procedure to actual risk. |
| The responsible Domain/capability, semantic authority, source location, symbol, runtime entry, dependency, or relevant test cannot be established safely | `domain-navigation` | Return the verified route/unresolved gap to the caller, normally Project Governance. |
| A real failure, unexplained behavior, or unsafe ambiguity blocks safe progress **and** current evidence is insufficient for the next safe decision | `incident-doctor` | Return evidence/fix boundary to Project Governance when task reconciliation or behavior-change authorization is needed. |
| Incident investigation also cannot locate the relevant Domain/authority/code/test evidence | `incident-doctor -> domain-navigation -> incident-doctor` | Domain Navigation locates/verifies evidence; Incident Doctor retains diagnosis ownership. |
| Existing evidence already supports the next safe decision for a bug/failure | Stay in the authorized Project Governance flow | Do not enter Incident Doctor merely because a defect exists. |
| Non-project/non-engineering request | No Engineering Governance route required | Not applicable. |

## Composition rules

- `project-governance -> domain-navigation -> project-governance` is the normal discovery composition when the work is authorized but the semantic/source route is unclear.
- `project-governance -> incident-doctor` is allowed only when Doctor's evidence gate is satisfied.
- `incident-doctor -> domain-navigation -> incident-doctor` is allowed only for locating or verifying candidate evidence. Domain Navigation does not own diagnosis, hypothesis status, or root-cause claims.
- If Incident Doctor identifies a behavior change that the active task does not authorize, return to Project Governance before mutation.
- A routing handoff does not create a second task authority and does not override project-local controls.

## Anti-duplication boundary

The global routing block should contain only enough text to make the route decision. Do not copy into global `AGENTS.md`:

- the three-file control-plane procedure;
- workspace lifecycle details;
- `V0`–`V3` verification details;
- Domain Navigation evidence/mapping procedure;
- Incident Doctor evidence/probe procedure;
- current repository, branch, task, runtime, or incident facts.

Those details stay in their owning Skills or project-local authorities. This keeps global routing small enough to remain stable while Skills evolve independently.

## Ambiguity rule

If two routes appear applicable, prefer the narrower capability only for the part it owns, then return to the normal Project Governance flow. Do not create a new Router Skill to resolve route ambiguity; this document is the routing policy.

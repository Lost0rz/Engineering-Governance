# Artifact ownership and refresh

Keep each kind of truth with its real owner.

| Artifact | Role |
| --- | --- |
| Source, schema, runtime config | Implemented behavior |
| Product/architecture decision docs | Accepted durable design |
| Installed Skills | Shared engineering methods and quality standards |
| Project `AGENTS.md` | Project-specific durable constraints |
| Issue | Optional task plan, findings and collaboration |
| PR, CI, commits | Actual remote delivery and verification state |
| Profile, handoff or report | Derived context or observed evidence |

Update an owner only when its underlying fact changes. Refresh dependent pointers when they would otherwise mislead; do not copy the same task/CI history into a separate ledger. Ordinary continuation needs no extra alignment commit.

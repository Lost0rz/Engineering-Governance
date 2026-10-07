# Engineering Governance

A lightweight, Git-native governance system for AI-assisted software development across multiple repositories.

The accepted `EngineeringGovernanceStandard` v0.1.0 defines typed authority routing, seven lifecycle layers, six cross-cutting axes, evidence-backed checks, freshness/exception semantics, and independent review boundaries.

Bootstrap, Doctor, and Audit are the next planned tooling layer; they are not implemented yet.

## Design goals

- Keep governance evidence in version control and close to the code it governs.
- Separate global reusable standards from project-specific facts and authorities.
- Prefer evidence-backed checks over narrative claims.
- Detect and explain drift before attempting enforcement or auto-remediation.
- Keep adoption lightweight enough for small projects and AI-agent workflows.
- Preserve independent verification between local execution and remote/web audit.

## Accepted lifecycle layers

1. Intent and outcomes
2. Domain and authority
3. Architecture and quality
4. Implementation and integration
5. Verification and release
6. Runtime and operability
7. Incident and feedback

MCP services, background enforcement daemons, and automatic remediation remain out of scope unless explicitly authorized by a later task.

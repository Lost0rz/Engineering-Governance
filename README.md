# Engineering Governance

A lightweight, Git-native governance system for AI-assisted software development across multiple repositories.

The project defines a reusable engineering governance standard, project authority routing, audit gates, and portable skills for initialization, health checks, and six-layer audits.

## Design goals

- Keep governance evidence in version control and close to the code it governs.
- Separate global reusable standards from project-specific facts and authorities.
- Prefer evidence-backed checks over narrative claims.
- Detect and explain drift before attempting enforcement or auto-remediation.
- Keep adoption lightweight enough for small projects and AI-agent workflows.
- Preserve independent verification between local execution and remote/web audit.

## Initial scope

1. Product / business intent
2. Domain design
3. Architecture, implementation, and integration
4. Verification and release
5. Runtime / operability
6. Incident learning and feedback

MCP services, background enforcement daemons, and automatic remediation are deliberately out of scope for the first usable release.

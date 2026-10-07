# Probe lifecycle

Classify every probe as `TEMPORARY` or `DURABLE` and record its owner, scope, and disposition.

- **TEMPORARY:** the default for incident-specific evidence collection. After the evidence is captured and verified, retire/remove the probe and record that disposition. Retain it temporarily only with an explicit reason and scope; do not let an unresolved incident silently make it permanent.
- **DURABLE:** ongoing diagnostic capability. Promotion requires all of: repeated evidence of continuing value, an explicit owner, an explicit scope, and separate authorization. A single incident does not justify automatic promotion.

Preserve the evidence needed for the incident record before removing a temporary probe. Record whether removal occurred or, if promotion is proposed, the evidence and authorization still required. Diagnostic value alone does not authorize a permanent observability change.

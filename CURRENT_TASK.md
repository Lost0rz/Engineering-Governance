# CURRENT TASK — Final Root and Cross-Skill Corrective

Task ID: `EG-FINAL-ROOT-CROSS-SKILL-CORRECTIVE-026`

State: `AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

Mode: `ROOT_CONSISTENCY_CORRECTIVE`

## Objective

Resolve the remaining root/reference consistency findings after all three Skills passed individual re-audit, then perform the final repository-wide audit before adoption.

## Authority and baseline

- Accepted Incident Doctor corrective/main head: `03d85ca998913e62cb47bbc160a2ea5c040c108e`.
- Frozen pre-audit comparison baseline: `4bc63eadbf1e1166ef8d9106c7f387a8ebb42c18`.
- Planned branch: `codex/final-root-cross-skill-corrective`.

## Authorized durable files

- `AGENTS.md`
- `references/UPSTREAMS.md`
- `references/LICENSE_NOTES.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change for handoff/closeout.

## Required corrective

1. Update the Aider/Repo Map upstream note to the accepted three-layer distinction: semantic authorities may own meaning; a navigation projection is optional/derived; Repo Map is optional/dynamic/read-only candidate selection and is not a runtime dependency.
2. Replace Phase-A-only license wording with a time-neutral policy: upstream concepts are attributed in `UPSTREAMS.md`; this note is not an exhaustive legal/provenance determination; copying code or substantial text requires checking the applicable license and required attribution/notices before inclusion.
3. Align root Incident Doctor guidance with the accepted handoff: Doctor may establish evidence and the minimum fix boundary, but if the active task does not authorize the behavior change/side effects, return to Project Governance before changing behavior.

## Explicit no-change areas

- Do not rewrite `docs/superpowers/**`; it is maintainer history and may accurately preserve earlier design decisions that were later superseded.
- Do not change any `skills/**` file under this Task ID.
- Do not change `README.md` unless final audit finds a direct contradiction that cannot be resolved in the three authorized durable files.

## Final audit requirements

After correction, independently verify:

- exactly three top-level Skills;
- all three Skill frontmatter blocks and all relative Skill/reference/template links resolve;
- cross-Skill routing has one coherent direction: Project Governance default -> Domain Navigation when location/authority is unclear -> Incident Doctor only for a real blocker with insufficient evidence -> Project Governance if diagnosis identifies an unauthorized fix;
- no Skill creates a competing semantic authority or mandates a literal `DOMAIN_MAP.md`;
- normal business/product delivery remains default;
- no executable/runtime/dependency/index/database/daemon/installer/new Skill exists;
- no open PRs;
- all retained task/control branches are fully contained in `main` or are explicitly reported as non-contained;
- root references match the live three-Skill contracts;
- any remaining issue is classified `BLOCKING`, `IMPORTANT`, `MINOR`, or `NO_CHANGE`.

## Verification level

`V0 — repository/Skill contract consistency`.

## Adoption gate

Adoption is allowed only after the final audit reports zero `BLOCKING` and zero `IMPORTANT` findings. Do not begin adoption under this Task ID.

## Current stop point

`AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

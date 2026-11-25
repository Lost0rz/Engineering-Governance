# Provenance — Microsoft final Design review module

Upstream project: `microsoft/skills`

Upstream URL: `https://github.com/microsoft/skills`

Upstream source: `.github/skills/frontend-design-review/`

Observed upstream main commit for this adaptation: `d2f769fd9d7ee81b4d768301bcd2eae14ddcfd0a`

Observed upstream `SKILL.md` blob: `6fd8fe378026252e3810eae36844704f3c684fe3`

Observed upstream review-output-format blob: `065f3cef3e43ea5ac2b1727a9ffcbcaa4639216b`

Observed upstream quick-checklist blob: `7c29054b2f307d76b71ac54a2da81edcf3014d09`

Upstream license: MIT

Upstream repository license blob observed: `79656060de00aa4659ad2c276d5be8830664d544`

Local adapted file: `final-review.md`

## Adaptation status

The upstream Skill contains two modes: Design Review and Creative Frontend Design. Engineering Governance intentionally adapts only the **Design Review** responsibilities for this internal downstream module: user-task review, design-system compliance where real authority exists, the Frictionless / Quality Craft / Trustworthy pillars, severity-prioritized findings, and final corrective/re-review behavior.

The local adaptation deliberately excludes the upstream Creative Frontend Design mode from this stage because Anthropic `frontend-design` already owns upstream aesthetic/design reasoning in Engineering Governance. This prevents two competing design-direction authorities inside one Design pass.

The local module also makes upstream Figma/Storybook/design-token assumptions evidence-conditional: those sources are checked when the target project actually has them and are never fabricated when unavailable.

Keep `LICENSE.txt` adjacent to this provenance record while this adapted module is distributed in the Plugin.

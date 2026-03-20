# Project 02 — OT Patch Management Risk Acceptance

## Overview

OT environments cannot follow IT patch cycles. Control systems run 24/7. Vendor support contracts sometimes prohibit unauthorized patches. Some systems are so old the vendor no longer exists. The result: known vulnerabilities stay open by necessity.

The GRC job is not to pretend this is acceptable without documentation. The GRC job is to make the decision visible, defensible, and time-bounded — and to ensure that the right people understand what residual risk they are signing off on.

This project covers the formal risk acceptance process for a known vulnerability on the Schneider Electric EcoStruxure SCADA HMI at Lone Star Transmission Services, where patching is operationally impossible for at least 6 months and the vendor patch is 18 months away.

## Scenario Summary

- **Organization:** Lone Star Transmission Services, LLC
- **Affected asset:** WJSS-001 — EcoStruxure GridAdvance HMI (Schneider Electric, 2014 vintage; fictional product)
- **Vulnerability:** CVE-2024-LST-0047 (fictional) — network-adjacent, low complexity, high confidentiality impact
- **Vendor status:** Acknowledged; patch ETA 18 months
- **Patching constraint:** 72-hour maintenance window required; next window 6 months out; patching before vendor patch voids support agreement
- **Required approvals:** OT Security Lead, Operations Manager, CISO

## Files

| File | Purpose |
|------|---------|
| [scenario.md](./scenario.md) | Asset description, CVE details, threat scenario, stakeholder context |
| [templates/risk-acceptance-form.md](./templates/risk-acceptance-form.md) | Full risk acceptance form with 7 sections |
| [templates/executive-summary-template.md](./templates/executive-summary-template.md) | One-page plain-language version for non-technical leadership |
| [examples/annotated-reasoning-example.md](./examples/annotated-reasoning-example.md) | Complete risk acceptance form for this scenario with reasoning annotations |
| [deliverables/](./deliverables/) | Signed risk acceptance outputs (populated by the practitioner) |

## What the Auditor Will Challenge

1. **Your compensating controls — do they actually reduce the likelihood of exploitation, or do they just look good on paper?** Walk me through how network segmentation changes the attack surface for CVE-2024-LST-0047 given the HMI's current network connectivity.

2. **Who owns the action to revisit this when the vendor patch arrives?** Is there a calendar entry? An assigned owner? A process that ensures this doesn't sit in a drawer for 18 months?

3. **If this asset were exploited, what is the blast radius?** The HMI has access to SCADA monitoring and control functions — what is the worst-case operational scenario?

4. **Did you consider network segmentation as a compensating control? Why or why not?** If you implemented micro-segmentation on the SCADA LAN, does that meaningfully constrain the attacker's post-compromise options?

5. **How does this risk acceptance relate to your CIP-007 patch management program?** CIP-007 R2 requires documented processes for managing software vulnerabilities. This risk acceptance is part of that record — is it correctly referenced?

## Standards Referenced

- NERC CIP-007-6, Requirement R2 (Patch Management)
- MITRE ATT&CK for ICS v2 — referenced in threat scenario
- NIST SP 800-82 (Guide to OT Security) — risk acceptance methodology

# Executive Risk Acceptance Summary
## Lone Star Transmission Services, LLC

**Document Reference:** RA-WJSS-2024-001
**Asset:** EcoStruxure GridAdvance HMI — Waco Junction Substation Control Room
**Prepared for:** CISO, VP Operations
**Date:** October 14, 2024

---

## What Is the Risk?

We have identified a security vulnerability in the operator workstation at Waco Junction Substation — the screen and keyboard our operators use to monitor and control our 345 kV transmission equipment. This system shows operators the real-time status of every breaker and relay at the substation and lets them issue switching commands when needed.

The vulnerability — confirmed by our vendor, Schneider Electric — would allow an attacker who can reach our substation's internal network to take control of that workstation. Once they have control, they could alter what our operators see on screen or, in the worst case, attempt to issue switching commands through the system.

The technical severity score is **8.1 out of 10**, which the cybersecurity industry classifies as **High**.

---

## Why We Cannot Fix It Right Now

There are three reasons we cannot patch this system immediately:

1. **The fix does not exist yet.** Schneider Electric has acknowledged the vulnerability and is developing a patch. Their current estimate for patch availability is approximately **18 months from now** (April 2026). We cannot apply a patch that has not been released.

2. **The patch requires a planned outage.** Applying any software update to this system requires a **72-hour maintenance window** during which the workstation is taken offline. Our next approved maintenance window at Waco Junction is in **Q3 2025 — approximately 6 months away**. Taking the workstation offline outside of a planned window means our operators cannot see or control the substation for 3 days with no contingency — an unacceptable operational risk on a 345 kV substation serving approximately 180,000 customers.

3. **Applying an unauthorized patch voids our vendor support agreement.** Until Schneider releases their official patch, applying anything else ends our hardware and software support contract. If the system then failed, we would bear the full cost of emergency replacement with no vendor assistance — and no budget allocated for it until the current capital plan cycle ends in 4 years.

---

## What We Are Doing About It in the Meantime

While we wait for the vendor patch, the following protective measures are in place:

- **Network isolation.** The workstation is on a restricted network segment inside the substation. An attacker must first gain access to our substation's internal network before they can exploit this vulnerability — it is not accessible from the internet.
- **Multi-factor authentication on all remote access.** Vendors and engineers accessing the substation network remotely must use two-factor authentication. This substantially reduces the risk that an attacker could use a stolen password to reach the substation network.
- **Real-time anomaly detection.** Our Dragos industrial security platform monitors substation network traffic and would generate an alert if it detected network activity consistent with this type of attack.
- **Session recording for vendor access.** All remote access sessions by contractors and vendors are logged and recorded.
- **Physical security.** The substation control room requires badge plus PIN to enter. An attacker cannot reach the substation network from outside the facility without bypassing physical access controls.

These measures reduce the likelihood that this vulnerability is exploited. They do not eliminate the risk.

---

## What Risk Remains

Even with these protective measures in place, a skilled attacker — particularly one capable of first compromising our vendor remote access or another path into our corporate network and then pivoting toward the substation — could potentially exploit this vulnerability.

The realistic worst-case scenario is: an attacker who successfully exploited this vulnerability could alter what our operators see on the substation monitoring display, potentially leading them to make incorrect switching decisions based on false information. In an extreme scenario, the attacker could also attempt to issue unauthorized switching commands through the workstation. Our protective relays at the 345 kV level operate independently and would continue to protect the transmission lines regardless — but an attacker-induced switching error could still create a grid contingency.

We rate the residual risk as **Medium-High** after compensating controls are in place.

---

## The Decision

We are recommending that leadership formally **accept** this risk for the period from **October 17, 2024** through **October 14, 2025**. This means:

- We acknowledge the vulnerability exists and cannot be patched immediately
- We commit to maintaining the protective measures described above
- We commit to applying the vendor patch within the next available maintenance window after it is released (not to exceed 90 days from release)
- We will escalate immediately if we receive any indication this vulnerability is being actively exploited against utilities like ours

This decision is revisited at the quarterly OT security review and at any of the specific trigger events defined in the full risk acceptance form. This acceptance **must be re-approved** before October 14, 2025 — it does not automatically renew.

---

## What We Are Asking You to Approve

By signing this document, you are authorizing the organization to accept the security risk described above for the period stated. You are **not** authorizing us to defer this indefinitely — the patch deployment clock begins the moment Schneider releases the patch, and this acceptance expires in 12 months regardless.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | Jennifer Wu | *[signed]* | October 17, 2024 |
| VP Operations / Operations Manager | Scott Akers | *[signed]* | October 16, 2024 |
| OT Security Lead | Marcus Delgado | *[signed]* | October 14, 2024 |

---

*For full technical detail, see Risk Acceptance Form RA-WJSS-2024-001 — retained in the OT Security program documentation and referenced in the CIP-007 patch management evidence package.*

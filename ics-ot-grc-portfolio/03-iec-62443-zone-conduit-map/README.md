# Project 03 — IEC 62443 Zone and Conduit Map

## Overview

IEC 62443 is the international standard for industrial automation and control system cybersecurity. Unlike NERC CIP, it is not mandatory in the US by statute — but it is increasingly required in vendor contracts, capital project specifications, and insurance underwriting. The core judgment is architectural: where do you draw Security Zone boundaries, and what Security Level (SL 1–4) is justified for each zone and conduit?

This project produces a zone and conduit map for Lone Star Transmission Services' Waco Junction Substation, driven by a capital project contract requirement. The hard question is the vendor remote access conduit — it terminates deep in the architecture, and the Security Level assignment requires choosing between a pragmatic SL-2 and a more conservative SL-3.

## Scenario Summary

- **Organization:** Lone Star Transmission Services, LLC
- **Scope:** Waco Junction Substation — four functional layers: Corporate IT, OT DMZ, Control LAN, Field Devices
- **Driver:** New capital project contract requires IEC 62443 alignment documentation
- **Complication:** The OT DMZ was designed in 2016 and was not built to IEC 62443 specification
- **Key judgment:** Vendor remote access conduit SL assignment and zone boundary placement

## Files

| File | Purpose |
|------|---------|
| [scenario.md](./scenario.md) | Substation architecture, asset list by layer, remote access description |
| [templates/zone-conduit-register.md](./templates/zone-conduit-register.md) | Zone and conduit register tables with one pre-filled example each |
| [templates/security-level-justification.md](./templates/security-level-justification.md) | SL assignment reasoning template |
| [examples/annotated-reasoning-example.md](./examples/annotated-reasoning-example.md) | Vendor remote access conduit SL-2 vs SL-3 argument; ambiguous zone assignment example |
| [deliverables/](./deliverables/) | Completed zone/conduit map outputs |

## What the Auditor Will Challenge

1. **Why does the vendor remote access conduit not terminate in the DMZ before reaching the Control LAN?** The standard expectation is that third-party access is demilitarized before touching control network assets. What justifies routing it deeper?

2. **Your OT DMZ assets — are they at the same Security Level as the zones they bridge?** A DMZ that bridges SL-2 and SL-3 zones must itself be at SL-3 or higher, or the DMZ becomes the weak link. Is this documented?

3. **How do you enforce conduit security requirements operationally, not just on paper?** A conduit at SL-3 has specific system requirements under IEC 62443-3-3. What controls actually implement those requirements on this network?

4. **What changes to this map if you add a historian replication path to corporate IT?** The AVEVA PI historian at WJSS-008 is already replicating to the enterprise data lake — does that create a conduit that belongs on this map?

5. **Have you validated these SL assignments against IEC 62443-3-3 system requirements?** SL selection requires mapping to the 51 foundational requirements in 62443-3-3. Has that mapping been done, or is this an SL assignment without the underlying requirements analysis?

## Standards Referenced

- IEC 62443-1-1 (Concepts and models)
- IEC 62443-2-1 (Security management system requirements)
- IEC 62443-3-2 (Security risk assessment for system design)
- IEC 62443-3-3 (System security requirements and security levels)

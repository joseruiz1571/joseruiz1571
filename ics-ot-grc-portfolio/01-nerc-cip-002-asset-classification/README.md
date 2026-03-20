# Project 01 — NERC CIP-002 BES Cyber Asset Classification

## Overview

NERC CIP-002-5.1a requires Responsible Entities to identify and categorize BES Cyber Systems by impact level. This is the foundation of the entire CIP compliance program. Every subsequent standard — CIP-003 through CIP-011 — applies differently depending on whether an asset is High, Medium, or Low impact. Get the classification wrong and you are either under-protecting critical infrastructure or spending compliance resources on assets that do not warrant them.

This project walks through the classification exercise for Lone Star Transmission Services, LLC, a fictional Texas transmission operator with 12 assets across two substations, a lean compliance team, and an audit on the horizon.

## Scenario Summary

- **Organization:** Lone Star Transmission Services, LLC
- **Substations:** Waco Junction (345 kV) and Brazos Switching Station (138 kV)
- **Assets in scope:** 12
- **Compliance team:** 2 FTEs
- **Regulatory deadline:** NERC CIP audit scheduled within 90 days
- **Ambiguity:** Two assets whose classification is genuinely non-obvious; both arguments documented before a decision is reached

## Files

| File | Purpose |
|------|---------|
| [scenario.md](./scenario.md) | Organization description, asset inventory, classification context |
| [templates/asset-classification-worksheet.md](./templates/asset-classification-worksheet.md) | Classification table with 4 pre-filled rows and 8 for completion |
| [examples/annotated-reasoning-example.md](./examples/annotated-reasoning-example.md) | Step-by-step Attachment 1 analysis for three representative assets |
| [deliverables/](./deliverables/) | Completed classification worksheet with all 12 assets assessed and signed |

## What the Auditor Will Challenge

1. **Why was Asset WJSS-004 (substation automation controller) rated Medium instead of High?** Walk me through your Attachment 1 analysis and explain at what criterion you stopped.

2. **You excluded Asset BJSS-004 (network time protocol server) — walk me through the Attachment 1 analysis.** What is the argument for inclusion, and why did you reject it?

3. **If Waco Junction Substation lost all inter-substation communication, what would the reliability impact be on the transmission system?** Can you demonstrate that your High-impact classifications reflect that analysis?

4. **Who reviewed and approved these classifications, and when?** Is there a documented approval workflow, and does it include Operations sign-off — not just the compliance team?

5. **How will you maintain this inventory as assets change?** What is your process for re-evaluating classifications when firmware is updated, connectivity changes, or new assets are added mid-cycle?

## Standards Referenced

- NERC CIP-002-5.1a, Attachment 1 (BES Cyber System Categorization)
- NERC CIP-002-5.1a, Attachment 2 (exemptions and special cases)
- NERC Glossary of Terms — definitions for BES Cyber Asset, BES Cyber System, Electronic Security Perimeter

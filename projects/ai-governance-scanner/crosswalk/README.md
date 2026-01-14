# AI Governance Framework Crosswalk

## Overview

This directory contains the **"Rosetta Stone"** for AI governance - comprehensive mappings that show how to satisfy multiple regulatory frameworks (ISO 42001, NIST AI RMF, EU AI Act, SOC 2) with unified controls.

**Problem Solved**: Organizations waste time and money implementing frameworks separately. This crosswalk enables integrated governance - implement once, satisfy many.

**Value Proposition**:
- 67% faster time to compliance
- 60% cost reduction vs. traditional approach
- 70% reduction in audit preparation time

---

## Documents in This Directory

### 1. [Master Crosswalk](master_crosswalk.md) (Comprehensive Reference)
**Use When**: You need to understand how specific framework requirements map to each other

**Contains**:
- 7 control domains covering the AI lifecycle
- Row-by-row mapping of ISO 42001, NIST AI RMF, EU AI Act, SOC 2
- TIAG control numbering system
- Sample evidence for each control
- Unified implementation guidance (how to satisfy all frameworks at once)

**Example Use Cases**:
- "Show me all controls that address NIST AI RMF MEASURE 2.1"
- "What evidence do I need for EU AI Act Article 15 compliance?"
- "How does AWS SageMaker Model Monitor satisfy multiple frameworks?"

**Format**: Markdown tables with 7 columns (ISO / NIST / EU / SOC 2 / TIAG / Evidence / Implementation)

---

### 2. [Executive Summary](executive_summary.md) (Strategic Overview)
**Use When**: You need to explain integrated governance to executives or secure buy-in

**Contains**:
- The business case for integrated governance
- ROI calculation (827% Year 1 ROI example)
- Visual "Rosetta Stone" architecture diagram
- Phased implementation roadmap (4 quarters)
- Key strategic advantages

**Example Use Cases**:
- Board presentation: "Why we should pursue ISO 42001 + NIST + EU AI Act simultaneously"
- Budget justification: "ROI of unified governance vs. siloed approach"
- Stakeholder alignment: "How this reduces audit burden by 70%"

**Format**: Executive memo (6 pages), board-ready

---

### 3. [Unified Controls](unified_controls.md) (Implementation Checklist)
**Use When**: You're actually building AI governance controls

**Contains**:
- 22 unified controls (TIAG-R, TIAG-D, TIAG-M, TIAG-S, TIAG-T, TIAG-H, TIAG-I)
- Detailed implementation guidance with AWS examples
- Code snippets for SageMaker, Bedrock, CloudTrail, IAM
- Evidence requirements per control
- 16-week phased implementation roadmap
- Final compliance checklist

**Example Use Cases**:
- "How do I implement Bedrock Guardrails to satisfy all frameworks?"
- "What IAM policies satisfy ISO 42001 Annex A.7.1, NIST GOVERN 2.1, EU Article 16?"
- "What logs do I need to retain for EU AI Act Article 12 compliance?"

**Format**: Technical implementation guide (30+ pages), engineer-ready

---

## How to Use This Crosswalk

### Scenario 1: Starting AI Governance from Scratch
**Path**: Executive Summary → Unified Controls → Master Crosswalk

1. **Read Executive Summary** to understand strategic approach
2. **Follow Unified Controls roadmap** (Phases 1-4 over 16 weeks)
3. **Reference Master Crosswalk** when you need framework-specific details

**Output**: Comprehensive AI governance program compliant with all four frameworks

---

### Scenario 2: Preparing for ISO 42001 Certification
**Path**: Master Crosswalk (filtered for ISO) → Unified Controls → Evidence Collection

1. **Filter Master Crosswalk** for all ISO 42001 requirements
2. **Implement controls** from Unified Controls that map to ISO clauses
3. **Collect evidence** using the "Sample Evidence" column

**Output**: ISO 42001 audit readiness package

---

### Scenario 3: Responding to EU AI Act High-Risk Classification
**Path**: Master Crosswalk (filtered for EU) → Unified Controls → Incident Response

1. **Identify EU AI Act requirements** for your AI system type (Annex III)
2. **Implement mandatory controls**: Risk assessment (Article 9), documentation (Article 11), monitoring (Article 15), oversight (Article 14)
3. **Establish incident reporting** (Article 62) - serious incidents within 15 days

**Output**: EU AI Act compliance for high-risk AI deployment

---

### Scenario 4: Customer Security Questionnaire (SOC 2 AI)
**Path**: Master Crosswalk (filtered for SOC 2) → Evidence Collection

1. **Map questionnaire items** to SOC 2 Trust Services Criteria (CC#.#)
2. **Locate controls** in Master Crosswalk that satisfy each criterion
3. **Provide evidence** from "Sample Evidence" column

**Output**: Completed security questionnaire with audit trail

---

### Scenario 5: U.S. Federal Contract (NIST AI RMF Required)
**Path**: Master Crosswalk (filtered for NIST) → Unified Controls

1. **Map contract requirements** to NIST AI RMF functions (GOVERN, MAP, MEASURE, MANAGE)
2. **Implement controls** that address required functions
3. **Document in NIST format** (separate outputs from same control implementation)

**Output**: NIST AI RMF compliance documentation

---

## Integration with AI Governance Scanner

The **AI Governance Scanner** (in parent directory) automates detection of gaps in these controls.

### How They Work Together

1. **Scanner Detects Gaps**:
   ```bash
   python scanner.py --scan all --format json --output gaps.json
   ```
   Output: Technical findings (e.g., "No Bedrock Guardrail attached")

2. **Crosswalk Explains Impact**:
   ```
   Finding: AWS-BEDROCK-001 (No guardrail)
   → Master Crosswalk shows this violates:
     - ISO 42001 Annex A.8.1 (Prompt injection controls)
     - NIST MANAGE 1.1 (Safety controls)
     - EU AI Act Article 15 (Manipulation prevention)
     - SOC 2 CC6.8 (Input validation)
   ```

3. **Unified Controls Provides Fix**:
   ```
   → Unified Controls TIAG-S-005 shows how to implement
     Bedrock Guardrails to satisfy all four frameworks
   ```

**Result**: Detection → Impact Analysis → Remediation Guidance (closed loop)

---

## TIAG Control Numbering System

**Format**: TIAG-[Domain]-[Sequence Number]

| Domain Code | Domain Name | Example Controls |
|-------------|-------------|------------------|
| **R** | Risk Management | TIAG-R-001 (Risk Assessment), TIAG-R-003 (Risk Treatment) |
| **D** | Documentation & Data | TIAG-D-001 (AI Inventory), TIAG-D-003 (Model Cards) |
| **M** | Monitoring & Measurement | TIAG-M-001 (Performance Monitoring), TIAG-M-003 (Audits) |
| **S** | Security & Safety | TIAG-S-001 (Access Controls), TIAG-S-005 (Guardrails) |
| **T** | Transparency | TIAG-T-001 (User Transparency), TIAG-T-003 (Explainability) |
| **H** | Human Oversight | TIAG-H-001 (Oversight Controls), TIAG-H-003 (Accountability) |
| **I** | Incident Response | TIAG-I-001 (Incident Response Plan), TIAG-I-003 (Logging) |

**Purpose**: Consistent control references across client engagements, reusable templates, maturity tracking

---

## Common Questions

### Q: Do I need to implement all four frameworks?
**A**: No. Implement controls based on your compliance obligations:
- **Mandatory**: EU AI Act (if serving EU customers with high-risk AI), SOC 2 (if SaaS provider)
- **Voluntary**: ISO 42001 (for certification / competitive advantage), NIST AI RMF (best practice)

The crosswalk allows you to implement once and "future-proof" for when additional frameworks become mandatory.

---

### Q: What's the difference between the Master Crosswalk and Unified Controls?
**A**:
- **Master Crosswalk** = Reference table showing framework mappings (what to satisfy)
- **Unified Controls** = Implementation guide with code examples (how to satisfy)

Think of Master Crosswalk as the "map" and Unified Controls as the "GPS turn-by-turn directions."

---

### Q: Can I use this for non-AWS environments (Azure, GCP)?
**A**: Yes, with modifications:
- **Control objectives** are cloud-agnostic (e.g., "encrypt models at rest" applies everywhere)
- **Implementation details** need translation (AWS Bedrock → Azure OpenAI, SageMaker → Vertex AI)
- **Unified Controls** provides AWS examples; you'd adapt for your cloud provider

The framework mappings in Master Crosswalk are universally applicable.

---

### Q: How often should I update this crosswalk?
**A**:
- **Quarterly**: Review for framework updates (EU AI Act implementation deadlines, NIST revisions)
- **Annually**: Comprehensive review for new frameworks (e.g., state-level AI regulations)
- **As-needed**: When deploying new AI system types or entering new markets

---

### Q: What's the minimum control set for high-risk AI compliance?
**A**: For EU AI Act high-risk AI systems, prioritize:
- TIAG-R-001 (Risk Assessment) - Article 9
- TIAG-D-003 (Model Cards) - Article 11
- TIAG-D-005 (Training Data Documentation) - Article 10
- TIAG-M-001 (Performance Monitoring) - Article 15
- TIAG-S-001 (Access Controls) - Article 16
- TIAG-H-001 (Human Oversight) - Article 14
- TIAG-I-001 (Incident Response) - Article 62

**Total: 7 controls** (subset of the 22 unified controls)

---

## Related Resources

### Standards & Frameworks
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) - AI Management Systems (official standard)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) - AI Risk Management Framework (free download)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) - Official legal text
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI (threat taxonomy)

### Tools & Templates
- [AI Governance Scanner](../README.md) - Automated compliance scanning (this project)
- [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) - Implementation guidance
- [ISO 42001 Toolkit](https://committee.iso.org/sites/jtc1sc42/home/projects/published/iso-iec-420012023.html) - Official toolkit

### Professional Development
- [ISO/IEC 42001 Lead Auditor Training](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001) - Certification course
- [ISACA: Auditing Generative AI](https://www.isaca.org/training-and-events) - Audit methodology
- [SANS AIS247](https://www.sans.org/cyber-security-courses/ai-security-essentials-for-business-leaders/) - AI Security Essentials

---

## Feedback & Contributions

This crosswalk is maintained as part of a professional AI governance portfolio.

**Feedback Welcome**:
- Framework mapping corrections
- Additional implementation examples
- New framework additions (e.g., NIST AI 600-1, state regulations)

**Contact**:
- Jose Ruiz-Vazquez, ISO/IEC 42001:2023 Lead Auditor
- LinkedIn: [linkedin.com/in/joseruiz1571](https://linkedin.com/in/joseruiz1571)
- Email: joseruiz1571@gmail.com

---

**Document Version**: 1.0
**Last Updated**: 2025-01-15
**License**: Professional Portfolio (Educational Use)
**Purpose**: Enable efficient, integrated AI governance implementation

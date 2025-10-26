# 🧩 Vendor Risk Summary Report  
**Vendor:** Horizon Labs  
**Client:** Oscorp Industries  
**Analyst:** Jose J. Ruiz-Vazquez  
**Assessment Type:** Third-Party Risk Assessment (TPRM)  
**Frameworks Applied:** NIST Cybersecurity Framework 2.0, CIS Controls v8  

## 🧾 Executive Summary

Horizon Labs, a SaaS provider handling sensitive scientific data for Oscorp Industries, completed a vendor security questionnaire.  
The review revealed several high- and medium-severity gaps in cybersecurity governance and technical controls.  
While the vendor shows awareness of security practices, the absence of formal frameworks and proactive testing increases the overall risk posture.

| Risk Area | Vendor Response (Excerpt) | Severity | NIST CSF Reference | CIS Control |
|------------|---------------------------|-----------|--------------------|--------------|
| **Sensitive data handled without clear classification or controls** | “The application handles confidential data. The data is stored in AWS S3 buckets …” | 🔴 **High** | **ID.AM-1** — Identify assets and data | **3.1** – Data protection management |
| **No formal cybersecurity framework or policy baseline** | “Horizon Labs is a startup; we still don’t follow any specific framework.” | 🟠 **Medium** | **GV.SC-01** – Establish governance structure | **17.3** – Establish and maintain a security policy |
| **No vulnerability management program** | “We don’t have a vulnerability scanner but we investigate incidents manually.” | 🔴 **High** | **PR.IP-12** – Vulnerability management | **7.3** – Remediate detected vulnerabilities |
| **No penetration testing program** | “We haven’t done a penetration test yet, but we plan to in the future.” | 🔴 **High** | **PR.IP-10** – Security testing | **18.1** – Establish a penetration testing program |
| **No documented incident response process** | “The IT team manages all incidents.” | 🟠 **Medium** | **RS.RP-1** – Response planning | **17.1** – Establish an incident response process |

## 📊 Risk Visualization

![Horizon Labs TPRM Heatmap](Horizon_Labs_TPRM_Heatmap.png)

**Figure: Horizon Labs Third-Party Risk Heatmap**  
This heatmap visualizes the distribution of identified vendor risks by their corresponding **NIST CSF** and **CIS Controls** references.  
Each plotted point represents a key finding from Horizon Labs’ questionnaire, color-coded by severity.  
The clustering in the *Protect* and *Respond* domains highlights maturity gaps in vulnerability management, testing, and incident response.  
By aligning findings to frameworks, this visualization transforms qualitative responses into structured, actionable insight for risk reporting.

## 🧠 Analyst Commentary

- **Framework Integration:** Using NIST CSF as the primary taxonomy ensured clear mapping between governance, protection, and response functions.  
- **Control Maturity Gaps:** Horizon Labs’ lack of a structured vulnerability management and testing program indicates a reactive rather than preventive approach.  
- **Governance Observations:** The absence of a formal cybersecurity framework is common among small vendors but introduces consistency and accountability risks.  

## 📈 Recommended Next Steps

1. **Formalize Framework Adoption:** Encourage Horizon Labs to align with NIST CSF or ISO/IEC 27001 to establish baseline governance.  
2. **Implement a Vulnerability Management Tool:** Integrate regular scanning, patch tracking, and risk scoring.  
3. **Conduct Annual Penetration Testing:** Validate external and internal controls using independent assessors.  
4. **Develop an Incident Response Plan:** Include defined roles, escalation procedures, and testing cadence.  
5. **Integrate Vendor Oversight:** Add Horizon Labs to Oscorp’s vendor risk register and track progress quarterly.

## 🎓 Learning Reflection

- Translating qualitative responses into structured, framework-aligned findings demonstrated how **GRC frameworks operationalize vendor risk**.  
- Applying both NIST CSF and CIS Controls bridged **strategic governance** and **technical control specificity**, an essential skill for GRC and TPRM professionals.  
- Visualizing results reinforced how **data storytelling** supports executive decision-making in risk management.

## 🧩 References

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)  
- [CIS Controls v8](https://www.cisecurity.org/controls/cis-controls-list)  
- [NIST SP 800-30 Rev.1 – Guide for Conducting Risk Assessments](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf)  
- [Shared Assessments TPRM Toolkit](https://sharedassessments.org/toolkits/)  
- [ENISA Supply Chain Threat Landscape](https://www.enisa.europa.eu/publications/supply-chain-threat-landscape)

**Artifact Type:** Vendor Risk Summary Report  
**Estimated Effort:** 3–4 hours  
**Learning Focus:** Framework mapping, vendor risk assessment, executive reporting

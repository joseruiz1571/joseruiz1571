# AI Chatbot Risk Assessment – Financial Services
**Analyst:** Jose Ruiz-Vazquez  
**Date:** November 2025  
**Frameworks:** NIST AI RMF 1.0, ISO/IEC 42001:2023, MITRE ATLAS  
**Methodology:** Threat-Informed AI Governance (TIAG) 

---

## 1. Executive Summary

This assessment evaluates risks associated with deploying a customer-facing AI chatbot for a financial services organization. The system provides account inquiries, balance checks, transaction history retrieval, and basic fraud alerts. 

Applying the **NIST AI Risk Management Framework (AI RMF)** and aligning with **ISO/IEC 42001** principles, we identified several high-priority risks including hallucinated financial advice, data leakage, prompt injection vulnerabilities, and governance gaps. 

The report provides a risk register, mitigation recommendations, and governance controls to support safe and compliant deployment aligned with financial services regulations (FFIEC, GLBA, UDAAP).

---

## 2. System Context

**Use Case:** The AI chatbot enables customers to retrieve account information, check balances, review transactions, receive basic fraud notifications, and ask questions about banking services.

**Data Processed:** Customer PII, masked account numbers, transaction metadata, authentication session data, and interaction logs.

**Regulatory Environment:** FFIEC guidance on AI, GLBA (Gramm-Leach-Bliley Act), UDAAP (Unfair, Deceptive, or Abusive Acts or Practices), NIST Privacy Framework, ISO/IEC 42001 AI governance expectations.

**AI Architecture:** LLM-powered chatbot with Retrieval-Augmented Generation (RAG) pipeline, policy enforcement layer, and human escalation pathways for high-risk queries.

**Assessment Note:** This assessment draws on practical experience evaluating LLM outputs for accuracy and safety, combined with formal training in AI governance frameworks (ISO 42001 Lead Auditor, NIST AI RMF, ISACA Auditing Generative AI).

---

## 3. NIST AI RMF Functions Applied

### GOVERN
**Risk:** Unclear accountability structure and governance gaps in AI lifecycle management  
**Controls:**  
- Establish AI governance committee with defined roles (AI Owner, Risk Owner, Compliance Reviewer)
- Document AI system inventory and use-case approval process
- Define lifecycle management procedures (development, deployment, monitoring, retirement)

### MAP
**Risk:** Potential for model to access or leak sensitive customer data beyond query scope  
**Controls:**  
- Implement data minimization and scoped retrieval (limit access to only necessary data)
- Enforce context boundaries to prevent data leakage across customer sessions
- Deploy comprehensive query logging and access controls

### MEASURE
**Risk:** No testing for hallucinations or inaccurate financial guidance  
**Controls:**  
- Regular accuracy testing against ground-truth financial data
- Adversarial testing to identify edge cases and failure modes
- Human-in-the-loop review for high-risk output categories (financial advice, account actions)

### MANAGE
**Risk:** Biased outputs that may disadvantage certain customer demographics  
**Controls:**  
- Fairness testing across customer demographics (language, age, geography)
- Model drift monitoring to detect degradation or bias emergence
- Regular retraining with diverse, representative datasets

---

## 4. Risk Register

| Risk ID | Risk Description | NIST AI RMF Function | Likelihood | Impact | Priority | Mitigation Summary |
|---------|------------------|---------------------|------------|--------|----------|-------------------|
| **AI-001** | Model hallucinates financial advice leading to customer harm | MEASURE | Medium | High | **HIGH** | Human review for financial guidance, disclaimers, accuracy testing |
| **AI-002** | Customer data leakage: Model accesses or exposes data inappropriately | MAP | Low | Critical | **HIGH** | Data minimization, access controls, query logging, privacy techniques |
| **AI-003** | Prompt injection attack bypasses security controls | MANAGE | Medium | High | **HIGH** | Input validation, rate limiting, security testing, sanitization |
| **AI-004** | Biased responses disadvantage certain customer demographics | MANAGE | Medium | Medium | **MEDIUM** | Fairness testing, diverse training data, drift monitoring |
| **AI-005** | Governance gaps: Unclear roles, accountability, lifecycle management | GOVERN | Medium | High | **HIGH** | AI governance committee, documented roles, lifecycle procedures |

---

## 5. Control Recommendations (Aligned with ISO 42001)

### Governance Controls
- Establish comprehensive AI system inventory with classification (risk tier, data sensitivity)
- Define and document AI use-case approval process with risk-based thresholds
- Assign clear accountability: AI Owner, Risk Owner, Compliance Reviewer, Business Sponsor
- Implement AI lifecycle documentation (design decisions, testing results, incidents)

### Technical Controls
- **Input validation and sanitization:** Prevent prompt injection and malicious queries
- **Output filtering:** Block sensitive data leakage (full account numbers, SSNs, credentials)
- **Model monitoring and drift detection:** Automated alerts for accuracy degradation
- **Secure audit logging:** Capture all AI interactions with tamper-evident storage
- **Rate limiting and anomaly detection:** Identify and block abuse patterns

### Operational Controls
- **Human review workflow:** Mandatory review for high-risk decision categories
- **Quarterly AI risk reviews:** Reassess risks as system evolves and threats emerge
- **Stress testing and red teaming:** Simulate adversarial attacks (prompt injection, data extraction)
- **Error documentation and lessons learned:** Capture hallucinations, failures, and mitigations

### Compliance Controls
- **Privacy Impact Assessment (PIA):** Document customer data flows and privacy risks
- **FFIEC alignment:** Map controls to FFIEC guidance on AI/ML in financial services
- **GLBA compliance:** Ensure safeguarding of customer financial information
- **UDAAP compliance:** Prevent unfair, deceptive, or abusive AI-driven practices
- **Explainability documentation:** Prepare for regulatory examination on AI decision logic

---

## 6. Key Risk Indicators (KRIs)

The following metrics should be monitored continuously and reported quarterly to the AI governance committee:

- **AI response accuracy rate** (target: >95% against ground truth)
- **Hallucination incidents per 1,000 interactions** (target: <5)
- **Blocked prompt injection attempts** (monitored for attack trends)
- **Customer complaints related to AI chatbot** (tracked and root-cause analyzed)
- **Model drift detection thresholds** (alert when accuracy drops >3%)
- **% of AI responses requiring human intervention** (indicates confidence and risk level)
- **Average response time and availability** (ensure service reliability)

---

## 7. Conclusion & Next Steps

This assessment identified **five key risks** requiring mitigation prior to production deployment. Implementing the outlined governance, technical, operational, and compliance controls will support responsible and compliant AI usage aligned with the **NIST AI RMF** and **ISO/IEC 42001** principles.

**Recommended Next Steps:**
1. Establish KRI dashboards for real-time monitoring
2. Deploy technical controls (input validation, output filtering, logging)
3. Formalize AI governance committee and assign accountability roles
4. Conduct Privacy Impact Assessment (PIA) and FFIEC compliance mapping
5. Perform quarterly AI risk reviews to adapt to evolving threats and regulations
6. Document all decisions, testing results, and incidents for audit readiness

By addressing these risks proactively, the organization can deploy the AI chatbot with confidence while protecting customers, maintaining regulatory compliance, and upholding trust in AI-enabled services.

---

## Learning Reflection

This project reinforced several key principles:
- **AI risk management requires both technical and governance controls** – technology alone cannot mitigate human, process, and policy risks
- **NIST AI RMF provides a comprehensive structure** for identifying and managing AI-specific threats
- **ISO/IEC 42001 principles operationalize AI governance** by defining roles, lifecycle management, and accountability
- **Financial services AI deployments demand heightened scrutiny** due to regulatory expectations and customer trust implications
- **Human oversight remains essential** in high-stakes AI applications, especially where inaccurate outputs could cause financial or reputational harm

**Artifact Type:** AI Risk Assessment Report  
**Estimated Effort:** 4 hours  
**Learning Focus:** NIST AI RMF, ISO 42001, AI risk assessment, financial services compliance  

---

## References

- [NIST AI Risk Management Framework (AI RMF) 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001:2023 – Artificial Intelligence Management System](https://www.iso.org/standard/81230.html)
- [FFIEC – Artificial Intelligence / Machine Learning Risk Management](https://www.ffiec.gov/)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [ISACA – Auditing Generative AI](https://www.isaca.org/)
- [Gramm-Leach-Bliley Act (GLBA) – Financial Privacy](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act)

---

**Portfolio Project by Jose Ruiz-Vazquez**  
*GRC & Third-Party Risk Professional | ISO 27001 & 42001 Lead Auditor*  
[LinkedIn](https://linkedin.com/in/joseruiz1571) | [GitHub](https://github.com/joseruiz1571)

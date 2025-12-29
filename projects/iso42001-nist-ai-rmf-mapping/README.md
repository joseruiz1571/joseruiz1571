# ISO 42001 to NIST AI RMF Knowledge Base

A structured knowledge base mapping ISO/IEC 42001:2023 AI Management System controls to NIST AI Risk Management Framework (AI RMF 1.0) categories.

## Purpose

This project provides a systematic mapping between:
- **ISO 42001:2023**: International standard for AI management systems
- **NIST AI RMF 1.0**: Framework for managing risks associated with artificial intelligence

The mapping enables organizations to:
1. Understand how ISO 42001 controls support NIST AI RMF implementation
2. Leverage existing NIST AI RMF assessments when pursuing ISO 42001 certification
3. Create comprehensive AI governance programs using both frameworks
4. Demonstrate regulatory compliance through integrated control implementation

## Project Structure

### Files

- **iso42001-control-schema.json**: JSON Schema defining the structure for ISO 42001 control data
- **iso42001-controls-section5-leadership.json**: Example implementation with Section 5 (Leadership) controls

### Future Sections (Planned)

- Section 6: Planning
- Section 7: Support
- Section 8: Operation
- Section 9: Performance Evaluation
- Section 10: Improvement

## Schema Structure

Each ISO 42001 control includes:

### Core Fields
- **controlId**: Unique identifier (e.g., "5.1", "6.2.1")
- **title**: Official control title from ISO 42001
- **section**: ISO 42001 section name
- **purpose**: Control objective and purpose
- **implementationGuidance**: Detailed implementation instructions

### AI Lifecycle Mapping
- **aiLifecycleStages**: Array of applicable stages
  - Planning and Design
  - Data Collection and Processing
  - Model Development
  - Verification and Validation
  - Deployment
  - Operation and Monitoring
  - Continuous Improvement
  - Decommissioning

### Risk Categories
- **riskCategories**: Array of AI risk domains
  - Bias and Fairness
  - Privacy and Data Protection
  - Security and Robustness
  - Transparency and Explainability
  - Accountability and Governance
  - Safety and Reliability
  - Legal and Regulatory Compliance
  - Ethical Considerations
  - Environmental Impact
  - Human Oversight and Control

### NIST AI RMF Mappings
- **nistAiRmfMappings**: Array of mappings to NIST functions
  - **function**: GOVERN, MAP, MEASURE, or MANAGE
  - **category**: NIST category ID (e.g., "GV-1.1", "MS-2.3")
  - **categoryTitle**: Full category title
  - **mappingRationale**: Explanation of the mapping
  - **alignmentStrength**: Direct, Partial, or Supporting

### Additional Context
- **relatedControls**: References to related ISO 42001 controls
- **implementationNotes**: Practical implementation considerations
- **evidenceExamples**: Examples of audit evidence

## Section 5: Leadership Controls

The initial implementation includes 5 controls from Section 5 (Leadership):

1. **5.1 - Leadership and Commitment**: Top management accountability for AIMS effectiveness
2. **5.2 - AI Policy**: Establishing and maintaining organizational AI policy
3. **5.3 - Organizational Roles, Responsibilities, and Authorities**: Defining AI governance structure
4. **5.1.a - Leadership Accountability for AIMS Effectiveness**: Executive oversight and decision-making
5. **5.2.a - AI Policy Framework for Objectives**: Framework for setting AI objectives

### NIST AI RMF Coverage

Section 5 controls primarily map to the **GOVERN** function:
- GV-1.1: Legal and Regulatory Requirements
- GV-1.2: Roles and Responsibilities
- GV-1.3: Organizational AI Risk Tolerance
- GV-1.4: Organizational Teams
- GV-1.5: Values and Principles
- GV-1.6: Policies, Processes, and Procedures
- GV-1.7: Processes for Continuous Improvement

With supporting mappings to:
- MAP function: Context establishment
- MANAGE function: Risk and benefits management, tracking mechanisms

## Usage

### Validating Control Data

Use a JSON Schema validator to verify control data against the schema:

```bash
# Example using ajv-cli
npm install -g ajv-cli
ajv validate -s iso42001-control-schema.json -d iso42001-controls-section5-leadership.json
```

### Querying the Knowledge Base

Use tools like `jq` to query the control data:

```bash
# Find all controls mapping to GOVERN function
jq '.controls[] | select(.nistAiRmfMappings[].function == "GOVERN") | {controlId, title}' iso42001-controls-section5-leadership.json

# List all controls addressing "Accountability and Governance" risk
jq '.controls[] | select(.riskCategories[] == "Accountability and Governance") | .controlId' iso42001-controls-section5-leadership.json

# Get controls for specific lifecycle stage
jq '.controls[] | select(.aiLifecycleStages[] == "Planning and Design") | {controlId, title}' iso42001-controls-section5-leadership.json
```

## Integration with Other Frameworks

This knowledge base can be extended to include mappings to:
- EU AI Act requirements
- GDPR privacy controls
- ISO 27001 information security controls
- MITRE ATLAS threat tactics
- NIST Cybersecurity Framework (CSF)

## Contributing

When adding new controls:
1. Follow the schema structure exactly
2. Provide comprehensive implementation guidance
3. Map to all relevant NIST AI RMF categories with rationale
4. Include practical evidence examples
5. Cross-reference related controls

## References

- **ISO/IEC 42001:2023**: Information technology — Artificial intelligence — Management system
- **NIST AI RMF 1.0**: AI Risk Management Framework (January 2023)
- **NIST AI 600-1**: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (July 2024)

## Version History

- **v1.0** (2025-12-29): Initial release with Section 5 Leadership controls

---

**Author**: Jose Ruiz-Vazquez
**LinkedIn**: [linkedin.com/in/joseruiz1571](https://linkedin.com/in/joseruiz1571)
**Certification**: ISO/IEC 42001:2023 Lead Auditor

# Library AI Governance & Explainability Dashboard

**A Portfolio Project for AI GRC (Governance, Risk, and Compliance)**

## Project Overview

This interactive dashboard demonstrates how AI explainability tools can be used to audit machine learning systems for bias, ensure regulatory compliance, and provide transparency in automated decision-making.

**Scenario**: A library uses an AI system to decide which patrons should receive access to high-value archival materials. This dashboard audits that system to ensure it makes fair, transparent, and compliant decisions.

## Why This Project Matters for AI GRC

In AI Governance, Risk, and Compliance, you need to:
- **Identify bias** in AI systems before they cause harm
- **Explain decisions** to comply with regulations (GDPR, AI Act, etc.)
- **Audit systems** to ensure they follow organizational policies
- **Document findings** for compliance and legal purposes

This project demonstrates all of these capabilities.

## Key Features

### 1. Data Overview
- Synthetic dataset of 200 library patrons
- Intentional bias built into the data (geographic discrimination)
- Statistical analysis of approval rates by demographic factors

### 2. Feature Importance Analysis
- Visualization of which factors the AI uses most
- Automatic flagging of problematic features (like zip code)
- Risk scoring based on bias indicators

### 3. Individual Explanations
- "Right to Explanation" for each patron
- Shows exactly why the AI approved or denied access
- Identifies when zip code may have influenced the decision

### 4. What-If Analysis
- Interactive tool to test how changing patron attributes affects decisions
- Automated bias testing across all zip codes
- Demonstrates disparate impact

### 5. GRC Audit Report
- Compliance assessment against real regulations (GDPR, Fair Housing Act analogues)
- Risk scoring and findings documentation
- Downloadable audit trail for records
- Actionable recommendations for remediation

## Technical Stack

- **Python 3.8+**
- **Streamlit**: Web dashboard framework
- **Pandas**: Data manipulation
- **Scikit-learn**: Machine learning
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computing

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
cd ai-grc-explainability-dashboard
pip install -r requirements.txt
```

### Step 2: Run the Dashboard

```bash
streamlit run library_explainability_dashboard.py
```

The dashboard will automatically open in your web browser at `http://localhost:8501`

## How to Use This Dashboard

### For Learning AI GRC Concepts

1. **Start with the Overview tab** to understand the dataset
   - Notice the variation in approval rates by zip code
   - This is your first clue that bias exists

2. **Check Feature Importance** to see what the AI actually uses
   - Red bars = zip code features (should be minimal or zero)
   - Look at the total zip code influence percentage

3. **Explore Individual Explanations** to understand decisions
   - Select different patrons
   - Compare patrons from different zip codes with similar histories

4. **Use What-If Analysis** to test for bias
   - Keep all attributes the same, change only zip code
   - Run the automated bias test
   - See if decisions change based solely on location

5. **Review the GRC Audit Report** to understand compliance
   - See how technical findings map to legal requirements
   - Learn the structure of a real AI audit report

### For Your Portfolio

When presenting this project:

1. **Explain the problem**: "AI systems can perpetuate bias. This dashboard detects it."

2. **Demonstrate the tool**: Walk through the tabs, showing:
   - How you identified the bias (Feature Importance)
   - How you tested for it (What-If Analysis)
   - How you documented it (Audit Report)

3. **Connect to real-world GRC**:
   - "This maps to GDPR Article 22 (right to explanation)"
   - "This demonstrates disparate impact under civil rights law"
   - "This creates an audit trail for SOC 2 compliance"

4. **Show technical skills**:
   - Python programming
   - Data analysis with Pandas
   - Machine learning with Scikit-learn
   - Web development with Streamlit
   - Regulatory knowledge

## Key AI GRC Concepts Demonstrated

### 1. Explainability
The ability to understand why an AI made a specific decision. Required by GDPR and increasingly by other regulations.

### 2. Bias Detection
Identifying when an AI system discriminates based on protected or irrelevant characteristics (like zip code as a proxy for race/income).

### 3. Fairness Metrics
Measuring whether an AI system treats different groups equitably (approval rate variance across zip codes).

### 4. Audit Trail
Documentation of AI decisions and the factors that influenced them, required for compliance and legal defense.

### 5. Disparate Impact
When a seemingly neutral policy (using zip code) has a disproportionate effect on certain groups.

## Learning Path: From This Project to AI GRC Career

1. **Understand the code** (you don't need to write it from scratch)
   - Read through the Python file
   - Understand how the bias was intentionally created
   - See how Streamlit creates web interfaces

2. **Modify the project**
   - Change the bias (try age or total books borrowed)
   - Add new features to track
   - Modify the GRC recommendations

3. **Apply to real scenarios**
   - Replace library patrons with loan applicants
   - Replace archive access with job candidate screening
   - Replace zip code with any other sensitive attribute

4. **Build your narrative**
   - "As a librarian, I understand metadata and information systems"
   - "I used Claude Code to build an AI audit tool"
   - "I can bridge the gap between policy and technology"

## Next Steps for Expanding This Project

### Technical Enhancements
- Add SHAP or LIME for more sophisticated explanations
- Implement fairness constraints in model training
- Add user authentication and role-based access
- Connect to a real database instead of synthetic data
- Add more ML models to compare (Random Forest, Neural Networks)

### GRC Enhancements
- Map to specific regulations (full GDPR, AI Act, NIST AI RMF)
- Add risk scoring based on ISO 31000
- Implement automated compliance checking
- Create exportable reports in multiple formats (PDF, Word)
- Add incident tracking for bias findings

### Portfolio Enhancements
- Deploy to the cloud (Streamlit Cloud is free)
- Add a video walkthrough
- Write a blog post explaining the project
- Present at a library/tech conference

## Resources for Learning More

### AI GRC Frameworks
- **NIST AI Risk Management Framework**: https://www.nist.gov/itl/ai-risk-management-framework
- **EU AI Act**: Understanding high-risk AI systems
- **ISO/IEC 42001**: AI Management System standard

### Explainability Tools
- **SHAP (SHapley Additive exPlanations)**: Game-theory based explanations
- **LIME (Local Interpretable Model-agnostic Explanations)**: Local approximations
- **ExplainerDashboard**: Python library for ML explainability

### Fairness in ML
- **Fairlearn**: Microsoft's fairness toolkit
- **AI Fairness 360**: IBM's comprehensive toolkit
- **What-If Tool**: Google's interactive visualization

## About the Creator

This project was built as a portfolio piece for transitioning from librarianship to AI GRC. It combines:
- Library science background (metadata, information systems)
- Database knowledge (from grad school courses)
- Light coding experience (WordPress, Drupal, HTML/CSS/PHP)
- Linux and cybersecurity studies
- Interest in Python automation and AI governance

## License

This is a portfolio/educational project. Feel free to use, modify, and learn from it.

## Acknowledgments

Built with Claude Code - an AI coding assistant that helps translate ideas into working software.

---

**Questions or feedback?** This dashboard is designed to be a learning tool. Experiment with it, break it, and rebuild it. That's how you learn AI GRC.

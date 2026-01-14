"""
Library AI Governance Dashboard
================================
An explainability dashboard for auditing AI decisions in library access control.

This dashboard demonstrates AI GRC principles by providing transparency into
how an AI model makes decisions about granting patrons access to high-value
archive materials.

Author: AI GRC Portfolio Project
Purpose: Demonstrate explainability for AI governance and compliance
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Library AI GRC Dashboard",
    page_icon="📚",
    layout="wide"
)

# Seed for reproducibility
np.random.seed(42)

@st.cache_data
def generate_synthetic_data(n_samples=200):
    """
    Generate synthetic library patron data with intentional bias.

    This simulates a real-world scenario where zip code might be used as a
    proxy for socioeconomic status, creating potential discrimination issues
    that GRC auditors need to identify.
    """
    data = {
        'Patron_ID': [f'P{str(i).zfill(4)}' for i in range(1, n_samples + 1)],
        'Years_as_Member': np.random.randint(1, 25, n_samples),
        'Books_Returned_Late': np.random.randint(0, 15, n_samples),
        'Total_Books_Borrowed': np.random.randint(5, 200, n_samples),
        'Age': np.random.randint(18, 75, n_samples),
        'Zip_Code': np.random.choice(['10001', '10002', '10003', '10004', '10005'], n_samples)
    }

    df = pd.DataFrame(data)

    # Calculate derived features
    df['Late_Return_Rate'] = (df['Books_Returned_Late'] / df['Total_Books_Borrowed'] * 100).round(2)

    # Create target variable with INTENTIONAL BIAS
    # This simulates a biased approval process where zip code unfairly influences decisions
    df['Approved_for_Archive_Access'] = 0

    for idx, row in df.iterrows():
        score = 0

        # Legitimate factors
        if row['Years_as_Member'] > 5:
            score += 30
        if row['Late_Return_Rate'] < 10:
            score += 40
        if row['Total_Books_Borrowed'] > 50:
            score += 20

        # BIAS ALERT: Zip code shouldn't matter, but we're making it matter
        # This represents redlining or geographic discrimination
        if row['Zip_Code'] in ['10001', '10002']:  # "Wealthy" neighborhoods
            score += 25  # Unfair advantage
        elif row['Zip_Code'] in ['10004', '10005']:  # "Less wealthy" neighborhoods
            score -= 15  # Unfair penalty

        # Add some randomness
        score += np.random.randint(-10, 10)

        # Approve if score > 50
        df.at[idx, 'Approved_for_Archive_Access'] = 1 if score > 50 else 0

    return df

@st.cache_resource
def train_model(df):
    """Train a decision tree model on the patron data."""
    features = ['Years_as_Member', 'Books_Returned_Late', 'Total_Books_Borrowed',
                'Age', 'Late_Return_Rate']

    # One-hot encode zip codes
    df_encoded = pd.get_dummies(df, columns=['Zip_Code'], prefix='Zip')

    # Get all feature columns (including encoded zip codes)
    feature_cols = features + [col for col in df_encoded.columns if col.startswith('Zip_')]

    X = df_encoded[feature_cols]
    y = df_encoded['Approved_for_Archive_Access']

    # Train model
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X, y)

    return model, feature_cols

def predict_with_explanation(model, patron_data, feature_cols):
    """Make a prediction and provide explanation."""
    prediction = model.predict(patron_data)[0]
    probability = model.predict_proba(patron_data)[0]

    return {
        'decision': 'APPROVED' if prediction == 1 else 'DENIED',
        'confidence': max(probability) * 100,
        'probability_approved': probability[1] * 100,
        'probability_denied': probability[0] * 100
    }

# ================================
# MAIN DASHBOARD
# ================================

st.title("📚 Library AI Governance & Explainability Dashboard")
st.markdown("### Auditing AI Decisions for Archive Access")

st.markdown("""
**Purpose**: This dashboard provides transparency into how an AI system decides which
library patrons should receive access to high-value archival materials. It demonstrates
key AI GRC principles including explainability, bias detection, and audit trail generation.
""")

# Generate data and train model
df = generate_synthetic_data(200)
model, feature_cols = train_model(df)

# Create tabs for different views
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "🔍 Feature Importance",
    "👤 Individual Explanations",
    "🎯 What-If Analysis",
    "📋 GRC Audit Report"
])

# ================================
# TAB 1: OVERVIEW
# ================================
with tab1:
    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Patrons", len(df))
    with col2:
        approved_count = df['Approved_for_Archive_Access'].sum()
        st.metric("Approved", approved_count)
    with col3:
        denied_count = len(df) - approved_count
        st.metric("Denied", denied_count)
    with col4:
        approval_rate = (approved_count / len(df) * 100)
        st.metric("Approval Rate", f"{approval_rate:.1f}%")

    st.subheader("Sample Patron Data")
    st.dataframe(df.head(10), use_container_width=True)

    # Approval by Zip Code - KEY GRC CONCERN
    st.subheader("⚠️ Approval Rates by Zip Code (Potential Bias Alert)")

    zip_analysis = df.groupby('Zip_Code').agg({
        'Approved_for_Archive_Access': ['sum', 'count', 'mean']
    }).round(3)
    zip_analysis.columns = ['Approved', 'Total', 'Approval_Rate']
    zip_analysis['Approval_Rate'] = (zip_analysis['Approval_Rate'] * 100).round(1)

    st.dataframe(zip_analysis, use_container_width=True)

    fig_zip = px.bar(
        zip_analysis.reset_index(),
        x='Zip_Code',
        y='Approval_Rate',
        title='Approval Rate by Zip Code',
        labels={'Approval_Rate': 'Approval Rate (%)', 'Zip_Code': 'Zip Code'},
        color='Approval_Rate',
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig_zip, use_container_width=True)

    st.warning("""
    **GRC Red Flag**: Significant variation in approval rates across zip codes may indicate:
    - Geographic discrimination (digital redlining)
    - Use of zip code as a proxy for socioeconomic status
    - Potential violation of equal access policies
    - Risk of disparate impact under civil rights law
    """)

# ================================
# TAB 2: FEATURE IMPORTANCE
# ================================
with tab2:
    st.header("Feature Importance Analysis")

    st.markdown("""
    This shows which factors the AI considers most important when making decisions.
    In a fair system, **zip code should have minimal or zero influence**.
    """)

    # Get feature importances
    df_encoded = pd.get_dummies(df, columns=['Zip_Code'], prefix='Zip')
    importances = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)

    # Highlight zip code features
    importances['Is_Zip_Code'] = importances['Feature'].str.startswith('Zip_')
    importances['Importance_Pct'] = (importances['Importance'] * 100).round(2)

    # Create visualization
    fig_importance = px.bar(
        importances,
        x='Importance_Pct',
        y='Feature',
        orientation='h',
        title='Feature Importance in Access Decisions',
        labels={'Importance_Pct': 'Importance (%)', 'Feature': 'Feature'},
        color='Is_Zip_Code',
        color_discrete_map={True: '#ff4b4b', False: '#0068c9'}
    )

    st.plotly_chart(fig_importance, use_container_width=True)

    # Calculate total zip code influence
    zip_importance = importances[importances['Is_Zip_Code']]['Importance'].sum() * 100

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Zip Code Influence", f"{zip_importance:.2f}%")
    with col2:
        if zip_importance > 15:
            st.error("⚠️ HIGH RISK: Zip code has excessive influence")
        elif zip_importance > 5:
            st.warning("⚠️ MODERATE RISK: Zip code influence should be investigated")
        else:
            st.success("✓ LOW RISK: Zip code has minimal influence")

    st.subheader("GRC Interpretation")
    st.markdown(f"""
    **Finding**: Zip code features collectively account for **{zip_importance:.2f}%** of the model's decision-making.

    **Governance Implication**:
    - If library policy states that "access should be based solely on patron history," this model is non-compliant.
    - Geographic data may serve as a proxy for protected characteristics (race, income).

    **Recommended Action**:
    - Review training data for geographic bias
    - Consider removing zip code from model inputs
    - Implement fairness constraints in model training
    - Document this finding in the AI risk register
    """)

# ================================
# TAB 3: INDIVIDUAL EXPLANATIONS
# ================================
with tab3:
    st.header("Individual Patron Decision Explanation")

    st.markdown("""
    Select a patron to see exactly why the AI approved or denied their access request.
    This provides the "Right to Explanation" required by regulations like GDPR.
    """)

    # Patron selector
    patron_id = st.selectbox("Select Patron ID", df['Patron_ID'].tolist())

    patron_row = df[df['Patron_ID'] == patron_id].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Patron Details")
        st.write(f"**Patron ID**: {patron_row['Patron_ID']}")
        st.write(f"**Years as Member**: {patron_row['Years_as_Member']}")
        st.write(f"**Books Returned Late**: {patron_row['Books_Returned_Late']}")
        st.write(f"**Total Books Borrowed**: {patron_row['Total_Books_Borrowed']}")
        st.write(f"**Late Return Rate**: {patron_row['Late_Return_Rate']:.2f}%")
        st.write(f"**Age**: {patron_row['Age']}")
        st.write(f"**Zip Code**: {patron_row['Zip_Code']}")

    with col2:
        st.subheader("AI Decision")

        # Prepare data for prediction
        patron_df = df[df['Patron_ID'] == patron_id].copy()
        patron_encoded = pd.get_dummies(patron_df, columns=['Zip_Code'], prefix='Zip')

        # Ensure all expected columns exist
        for col in feature_cols:
            if col not in patron_encoded.columns:
                patron_encoded[col] = 0

        patron_features = patron_encoded[feature_cols]

        result = predict_with_explanation(model, patron_features, feature_cols)

        if result['decision'] == 'APPROVED':
            st.success(f"✓ **{result['decision']}**")
        else:
            st.error(f"✗ **{result['decision']}**")

        st.write(f"**Confidence**: {result['confidence']:.1f}%")
        st.write(f"**Probability of Approval**: {result['probability_approved']:.1f}%")
        st.write(f"**Probability of Denial**: {result['probability_denied']:.1f}%")

    # Feature contribution (simplified)
    st.subheader("Key Factors in This Decision")

    factors = []

    if patron_row['Years_as_Member'] > 5:
        factors.append(("✓ Long-term member (positive)", "green"))
    else:
        factors.append(("✗ Relatively new member (negative)", "red"))

    if patron_row['Late_Return_Rate'] < 10:
        factors.append(("✓ Low late return rate (positive)", "green"))
    else:
        factors.append(("✗ High late return rate (negative)", "red"))

    if patron_row['Total_Books_Borrowed'] > 50:
        factors.append(("✓ Active borrower (positive)", "green"))
    else:
        factors.append(("✗ Infrequent borrower (negative)", "red"))

    # Zip code bias check
    if patron_row['Zip_Code'] in ['10001', '10002']:
        factors.append(("⚠️ Zip code may provide unfair advantage (bias concern)", "orange"))
    elif patron_row['Zip_Code'] in ['10004', '10005']:
        factors.append(("⚠️ Zip code may create unfair penalty (bias concern)", "orange"))

    for factor, color in factors:
        if color == "green":
            st.success(factor)
        elif color == "red":
            st.error(factor)
        else:
            st.warning(factor)

# ================================
# TAB 4: WHAT-IF ANALYSIS
# ================================
with tab4:
    st.header("What-If Analysis Tool")

    st.markdown("""
    Modify patron characteristics to see how the AI's decision changes.
    This helps identify which factors have the most impact and whether changes are fair.
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Modify Patron Attributes")

        whatif_years = st.slider("Years as Member", 1, 25, 5)
        whatif_late = st.slider("Books Returned Late", 0, 15, 3)
        whatif_total = st.slider("Total Books Borrowed", 5, 200, 50)
        whatif_age = st.slider("Age", 18, 75, 35)
        whatif_late_rate = (whatif_late / whatif_total * 100) if whatif_total > 0 else 0
        whatif_zip = st.selectbox("Zip Code", ['10001', '10002', '10003', '10004', '10005'])

    with col2:
        st.subheader("Predicted Decision")

        # Create what-if dataframe
        whatif_data = pd.DataFrame({
            'Years_as_Member': [whatif_years],
            'Books_Returned_Late': [whatif_late],
            'Total_Books_Borrowed': [whatif_total],
            'Age': [whatif_age],
            'Late_Return_Rate': [whatif_late_rate],
            'Zip_Code': [whatif_zip]
        })

        whatif_encoded = pd.get_dummies(whatif_data, columns=['Zip_Code'], prefix='Zip')

        # Ensure all expected columns exist
        for col in feature_cols:
            if col not in whatif_encoded.columns:
                whatif_encoded[col] = 0

        whatif_features = whatif_encoded[feature_cols]

        whatif_result = predict_with_explanation(model, whatif_features, feature_cols)

        if whatif_result['decision'] == 'APPROVED':
            st.success(f"✓ **{whatif_result['decision']}**")
        else:
            st.error(f"✗ **{whatif_result['decision']}**")

        st.metric("Confidence", f"{whatif_result['confidence']:.1f}%")

        # Probability gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=whatif_result['probability_approved'],
            title={'text': "Approval Probability"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgray"},
                    {'range': [30, 70], 'color': "gray"},
                    {'range': [70, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)

    st.subheader("Bias Testing")
    st.markdown("""
    **Test for Geographic Bias**: Try changing only the zip code while keeping all other
    factors constant. If the decision changes, the model is using location as a discriminatory factor.
    """)

    if st.button("Run Automated Zip Code Bias Test"):
        st.write("Testing all zip codes with current attributes...")

        test_results = []
        for zip_code in ['10001', '10002', '10003', '10004', '10005']:
            test_data = pd.DataFrame({
                'Years_as_Member': [whatif_years],
                'Books_Returned_Late': [whatif_late],
                'Total_Books_Borrowed': [whatif_total],
                'Age': [whatif_age],
                'Late_Return_Rate': [whatif_late_rate],
                'Zip_Code': [zip_code]
            })

            test_encoded = pd.get_dummies(test_data, columns=['Zip_Code'], prefix='Zip')
            for col in feature_cols:
                if col not in test_encoded.columns:
                    test_encoded[col] = 0

            test_features = test_encoded[feature_cols]
            test_result = predict_with_explanation(model, test_features, feature_cols)

            test_results.append({
                'Zip_Code': zip_code,
                'Decision': test_result['decision'],
                'Approval_Probability': f"{test_result['probability_approved']:.1f}%"
            })

        results_df = pd.DataFrame(test_results)
        st.dataframe(results_df, use_container_width=True)

        # Check if decisions vary
        decisions = results_df['Decision'].unique()
        if len(decisions) > 1:
            st.error("""
            ⚠️ **BIAS DETECTED**: The AI makes different decisions based solely on zip code,
            even when all other patron characteristics are identical. This is a clear case
            of geographic discrimination and violates fair access principles.
            """)
        else:
            st.success("""
            ✓ **NO ZIP CODE BIAS DETECTED**: The AI makes consistent decisions regardless
            of zip code for this particular patron profile.
            """)

# ================================
# TAB 5: GRC AUDIT REPORT
# ================================
with tab5:
    st.header("GRC Audit Report")

    st.markdown(f"""
    **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    **System**: Library Archive Access AI
    **Audit Type**: Explainability & Bias Assessment
    **Auditor**: AI Governance Dashboard
    """)

    st.subheader("Executive Summary")

    # Calculate key metrics
    zip_importance = importances[importances['Is_Zip_Code']]['Importance'].sum() * 100
    approval_by_zip = df.groupby('Zip_Code')['Approved_for_Archive_Access'].mean() * 100
    zip_variance = approval_by_zip.std()

    # Risk scoring
    risk_score = 0
    risk_factors = []

    if zip_importance > 15:
        risk_score += 40
        risk_factors.append("High zip code feature importance (>15%)")
    elif zip_importance > 5:
        risk_score += 20
        risk_factors.append("Moderate zip code feature importance (5-15%)")

    if zip_variance > 15:
        risk_score += 40
        risk_factors.append(f"High variance in approval rates by zip code ({zip_variance:.1f}%)")
    elif zip_variance > 10:
        risk_score += 20
        risk_factors.append(f"Moderate variance in approval rates by zip code ({zip_variance:.1f}%)")

    # Overall risk level
    if risk_score >= 60:
        risk_level = "🔴 HIGH RISK"
        risk_color = "red"
    elif risk_score >= 30:
        risk_level = "🟡 MEDIUM RISK"
        risk_color = "orange"
    else:
        risk_level = "🟢 LOW RISK"
        risk_color = "green"

    st.markdown(f"**Overall Risk Level**: {risk_level}")
    st.markdown(f"**Risk Score**: {risk_score}/100")

    if risk_color == "red":
        st.error("This AI system exhibits significant bias and compliance concerns.")
    elif risk_color == "orange":
        st.warning("This AI system shows moderate bias indicators requiring attention.")
    else:
        st.success("This AI system shows low bias indicators.")

    st.subheader("Findings")

    st.markdown(f"""
    #### 1. Feature Importance Analysis
    - **Zip Code Influence**: {zip_importance:.2f}%
    - **Assessment**: {"❌ Non-compliant" if zip_importance > 15 else "⚠️ Requires monitoring" if zip_importance > 5 else "✓ Acceptable"}

    #### 2. Approval Rate Disparities
    - **Variance Across Zip Codes**: {zip_variance:.2f}%
    - **Assessment**: {"❌ Significant disparity detected" if zip_variance > 15 else "⚠️ Moderate disparity" if zip_variance > 10 else "✓ Acceptable variance"}

    #### 3. Identified Risk Factors
    """)

    if risk_factors:
        for factor in risk_factors:
            st.markdown(f"- {factor}")
    else:
        st.markdown("- No significant risk factors identified")

    st.subheader("Compliance Assessment")

    compliance_items = [
        {
            "Requirement": "Explainability",
            "Standard": "GDPR Art. 22 (Right to Explanation)",
            "Status": "✓ COMPLIANT",
            "Notes": "Dashboard provides individual decision explanations"
        },
        {
            "Requirement": "Non-discrimination",
            "Standard": "Fair Housing Act / Equal Credit Opportunity Act (analogous)",
            "Status": "❌ NON-COMPLIANT" if zip_importance > 15 else "⚠️ AT RISK",
            "Notes": "Geographic bias detected in decision-making process"
        },
        {
            "Requirement": "Transparency",
            "Standard": "AI Act (proposed) - High-Risk AI Systems",
            "Status": "✓ COMPLIANT",
            "Notes": "Feature importance and decision logic are documented"
        },
        {
            "Requirement": "Audit Trail",
            "Standard": "SOC 2 / Internal Controls",
            "Status": "✓ COMPLIANT",
            "Notes": "All decisions can be logged and reviewed"
        }
    ]

    compliance_df = pd.DataFrame(compliance_items)
    st.dataframe(compliance_df, use_container_width=True)

    st.subheader("Recommendations")

    st.markdown("""
    1. **Immediate Actions**:
       - Suspend use of zip code as a model feature
       - Review all denied applications from zip codes 10004 and 10005 for potential bias
       - Implement geographic fairness constraints in model retraining

    2. **Medium-term Actions**:
       - Retrain model using only patron history features (years, borrowing patterns)
       - Establish fairness metrics and monitoring dashboards
       - Document model decisions in compliance system

    3. **Long-term Actions**:
       - Implement continuous bias monitoring
       - Establish an AI ethics review board
       - Create patron appeal process for AI decisions
       - Regular third-party fairness audits

    4. **Policy Updates**:
       - Update AI acceptable use policy to prohibit geographic discrimination
       - Create formal model governance framework
       - Establish clear accountability for AI decisions
    """)

    st.subheader("Export Audit Report")

    # Create downloadable report
    report_text = f"""
LIBRARY AI GOVERNANCE AUDIT REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

EXECUTIVE SUMMARY
Risk Level: {risk_level}
Risk Score: {risk_score}/100

KEY FINDINGS
1. Zip Code Influence: {zip_importance:.2f}%
2. Approval Rate Variance: {zip_variance:.2f}%

RISK FACTORS
{chr(10).join(['- ' + factor for factor in risk_factors]) if risk_factors else '- No significant risk factors identified'}

COMPLIANCE ASSESSMENT
{compliance_df.to_string()}

RECOMMENDATIONS
See full dashboard for detailed recommendations.

---
This is an automated assessment. Human review required for final compliance determination.
    """

    st.download_button(
        label="📥 Download Audit Report (TXT)",
        data=report_text,
        file_name=f"library_ai_audit_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

    # Export data
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Dataset (CSV)",
        data=csv_data,
        file_name=f"library_patrons_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ================================
# FOOTER
# ================================
st.markdown("---")
st.markdown("""
**About This Dashboard**: This is a demonstration project for AI Governance, Risk, and Compliance (GRC)
in library systems. It shows how explainability tools can identify bias, ensure transparency, and
support regulatory compliance in AI decision-making systems.

**Technical Stack**: Python, Streamlit, Scikit-learn, Plotly
**Portfolio Project**: Librarian → AI GRC Career Transition
""")

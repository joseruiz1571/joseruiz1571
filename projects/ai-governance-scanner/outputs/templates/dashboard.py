"""
HTML Dashboard Generator

Generates an interactive HTML dashboard for governance scan results.
The dashboard provides executive-level visibility into AI compliance posture.
"""

from core.schema import ScanReport, Severity


def generate_dashboard(report: ScanReport) -> str:
    """
    Generate HTML dashboard from scan report

    Args:
        report: ScanReport containing findings

    Returns:
        Complete HTML document as string
    """
    severity_counts = report.get_severity_counts()

    # Calculate risk score (weighted by severity)
    weights = {'Critical': 10, 'High': 5, 'Medium': 2, 'Low': 1, 'Informational': 0}
    risk_score = sum(severity_counts.get(sev, 0) * weight for sev, weight in weights.items())
    max_score = len(report.findings) * 10 if report.findings else 1
    risk_percentage = min(100, int((risk_score / max_score) * 100)) if report.findings else 0

    # Group findings by severity
    findings_by_severity = {s.value: [] for s in Severity}
    for finding in report.findings:
        findings_by_severity[finding.severity.value].append(finding)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Governance Scan Report - {report.scan_timestamp}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #2d3748;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        .header {{
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .header h1 {{
            color: #2d3748;
            font-size: 2em;
            margin-bottom: 10px;
        }}

        .header .meta {{
            color: #718096;
            font-size: 0.9em;
        }}

        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        .card {{
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .card h3 {{
            color: #4a5568;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 10px;
        }}

        .card .value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #2d3748;
        }}

        .card.critical .value {{ color: #e53e3e; }}
        .card.high .value {{ color: #dd6b20; }}
        .card.medium .value {{ color: #d69e2e; }}
        .card.low .value {{ color: #38a169; }}

        .risk-meter {{
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .risk-meter h2 {{
            margin-bottom: 20px;
            color: #2d3748;
        }}

        .meter-bar {{
            width: 100%;
            height: 40px;
            background: #e2e8f0;
            border-radius: 20px;
            overflow: hidden;
            position: relative;
        }}

        .meter-fill {{
            height: 100%;
            background: linear-gradient(90deg, #38a169 0%, #d69e2e 50%, #e53e3e 100%);
            transition: width 1s ease;
        }}

        .meter-label {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-weight: bold;
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }}

        .findings {{
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .findings h2 {{
            margin-bottom: 20px;
            color: #2d3748;
        }}

        .finding {{
            border-left: 4px solid #cbd5e0;
            padding: 20px;
            margin-bottom: 20px;
            background: #f7fafc;
            border-radius: 4px;
        }}

        .finding.critical {{ border-left-color: #e53e3e; }}
        .finding.high {{ border-left-color: #dd6b20; }}
        .finding.medium {{ border-left-color: #d69e2e; }}
        .finding.low {{ border-left-color: #38a169; }}

        .finding-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}

        .finding-id {{
            font-weight: bold;
            font-size: 1.1em;
            color: #2d3748;
        }}

        .severity-badge {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            color: white;
        }}

        .severity-badge.critical {{ background: #e53e3e; }}
        .severity-badge.high {{ background: #dd6b20; }}
        .severity-badge.medium {{ background: #d69e2e; }}
        .severity-badge.low {{ background: #38a169; }}
        .severity-badge.informational {{ background: #4299e1; }}

        .finding-resource {{
            color: #718096;
            font-size: 0.85em;
            margin-bottom: 15px;
            font-family: 'Courier New', monospace;
        }}

        .finding-description {{
            margin-bottom: 15px;
            line-height: 1.6;
        }}

        .finding-description strong {{
            display: block;
            color: #4a5568;
            margin-bottom: 5px;
        }}

        .executive-summary {{
            background: #edf2f7;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 15px;
            border-left: 3px solid #4299e1;
        }}

        .executive-summary strong {{
            color: #2c5282;
            display: block;
            margin-bottom: 8px;
        }}

        .compliance-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }}

        .tag {{
            background: #e6fffa;
            color: #234e52;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            border: 1px solid #81e6d9;
        }}

        .tag.nist {{ background: #fef5e7; color: #7d6608; border-color: #f9e79f; }}
        .tag.iso {{ background: #e8f4fd; color: #1e4e79; border-color: #a9d4f5; }}
        .tag.mitre {{ background: #fce4ec; color: #880e4f; border-color: #f48fb1; }}

        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
            opacity: 0.9;
        }}

        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .card, .findings, .header, .risk-meter {{
                box-shadow: none;
                border: 1px solid #e2e8f0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ AI Governance Scan Report</h1>
            <div class="meta">
                <strong>Scan Time:</strong> {report.scan_timestamp} |
                <strong>AWS Account:</strong> {report.aws_account_id} |
                <strong>Region:</strong> {report.aws_region}
            </div>
        </div>

        <div class="dashboard">
            <div class="card">
                <h3>Total Findings</h3>
                <div class="value">{len(report.findings)}</div>
            </div>
            <div class="card critical">
                <h3>Critical</h3>
                <div class="value">{severity_counts.get('Critical', 0)}</div>
            </div>
            <div class="card high">
                <h3>High</h3>
                <div class="value">{severity_counts.get('High', 0)}</div>
            </div>
            <div class="card medium">
                <h3>Medium</h3>
                <div class="value">{severity_counts.get('Medium', 0)}</div>
            </div>
            <div class="card low">
                <h3>Low</h3>
                <div class="value">{severity_counts.get('Low', 0)}</div>
            </div>
        </div>

        <div class="risk-meter">
            <h2>Compliance Risk Score</h2>
            <div class="meter-bar">
                <div class="meter-fill" style="width: {risk_percentage}%">
                    <div class="meter-label">{risk_percentage}% Risk Exposure</div>
                </div>
            </div>
        </div>

        <div class="findings">
            <h2>Findings Detail</h2>
            {_generate_findings_html(report.findings)}
        </div>

        <div class="footer">
            <p>Generated by AI Governance Scanner | Threat-Informed AI Governance (TIAG)</p>
            <p>Mapping technical vulnerabilities to NIST AI RMF, ISO 42001, and MITRE ATLAS</p>
        </div>
    </div>
</body>
</html>"""


def _generate_findings_html(findings) -> str:
    """Generate HTML for findings list"""
    if not findings:
        return "<p style='color: #38a169; font-size: 1.2em;'>✅ No findings detected. AI systems meet governance requirements.</p>"

    html_parts = []

    for finding in findings:
        severity_class = finding.severity.value.lower()

        # Build compliance tags
        tags = []
        for control in finding.mappings.nist_ai_rmf:
            tags.append(f'<span class="tag nist">NIST: {control}</span>')
        for control in finding.mappings.iso_42001:
            tags.append(f'<span class="tag iso">ISO: {control}</span>')
        for control in finding.mappings.mitre_atlas:
            tags.append(f'<span class="tag mitre">MITRE: {control}</span>')

        tags_html = '\n'.join(tags)

        executive_summary_html = ""
        if finding.executive_summary:
            executive_summary_html = f"""
            <div class="executive-summary">
                <strong>📊 Executive Summary</strong>
                {finding.executive_summary}
            </div>
            """

        finding_html = f"""
        <div class="finding {severity_class}">
            <div class="finding-header">
                <div class="finding-id">{finding.finding_id}</div>
                <span class="severity-badge {severity_class}">{finding.severity.value}</span>
            </div>
            <div class="finding-resource">{finding.resource_arn}</div>

            {executive_summary_html}

            <div class="finding-description">
                <strong>Technical Finding:</strong>
                {finding.technical_finding}
            </div>

            <div class="finding-description">
                <strong>Recommended Mitigation:</strong>
                {finding.mitigation_applied}
            </div>

            <div class="compliance-tags">
                {tags_html}
            </div>
        </div>
        """

        html_parts.append(finding_html)

    return '\n'.join(html_parts)

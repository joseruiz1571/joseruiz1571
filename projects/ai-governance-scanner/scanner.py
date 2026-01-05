#!/usr/bin/env python3
"""
AI Governance Scanner - Command Line Interface

Scans AWS AI services for compliance with NIST AI RMF, ISO 42001,
and maps vulnerabilities to MITRE ATLAS attack vectors.

Usage:
    python scanner.py --scan all --output report.json
    python scanner.py --scan bedrock-guardrails --format dashboard
    python scanner.py --list-scans
"""

import argparse
import sys
import json
from datetime import datetime
from pathlib import Path
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

from core import ScanReport, ExecutiveNarrator
from scans import AVAILABLE_SCANNERS


class AIGovernanceScanner:
    """Main scanner orchestrator"""

    def __init__(self, region: str = None, profile: str = None, use_ai_narrator: bool = True):
        """
        Initialize scanner

        Args:
            region: AWS region (default: from environment/config)
            profile: AWS profile name (default: default)
            use_ai_narrator: Whether to use AI for executive summaries
        """
        self.session = self._create_session(region, profile)
        self.use_ai_narrator = use_ai_narrator
        self.narrator = None

        if use_ai_narrator:
            try:
                self.narrator = ExecutiveNarrator(self.session)
            except Exception as e:
                print(f"Warning: Could not initialize AI narrator ({e}). Using templates instead.")
                self.use_ai_narrator = False

    def _create_session(self, region: str, profile: str) -> boto3.Session:
        """Create boto3 session with error handling"""
        try:
            session_kwargs = {}
            if region:
                session_kwargs['region_name'] = region
            if profile:
                session_kwargs['profile_name'] = profile

            session = boto3.Session(**session_kwargs)

            # Validate credentials
            sts = session.client('sts')
            sts.get_caller_identity()

            return session

        except NoCredentialsError:
            print("ERROR: No AWS credentials found.")
            print("Configure credentials using 'aws configure' or set AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY")
            sys.exit(1)
        except ClientError as e:
            print(f"ERROR: Failed to authenticate with AWS: {e}")
            sys.exit(1)

    def run_scan(self, scan_names: list) -> ScanReport:
        """
        Execute specified scans

        Args:
            scan_names: List of scan names to run, or ['all'] for all scans

        Returns:
            ScanReport containing all findings
        """
        # Determine which scans to run
        if 'all' in scan_names:
            scans_to_run = list(AVAILABLE_SCANNERS.keys())
        else:
            scans_to_run = scan_names

        # Validate scan names
        invalid_scans = set(scans_to_run) - set(AVAILABLE_SCANNERS.keys())
        if invalid_scans:
            print(f"ERROR: Unknown scan(s): {', '.join(invalid_scans)}")
            print(f"Available scans: {', '.join(AVAILABLE_SCANNERS.keys())}")
            sys.exit(1)

        # Create report
        sts = self.session.client('sts')
        account_id = sts.get_caller_identity()['Account']

        report = ScanReport(
            scan_timestamp=datetime.utcnow().isoformat() + 'Z',
            aws_account_id=account_id,
            aws_region=self.session.region_name or 'us-east-1'
        )

        # Execute each scan
        for scan_name in scans_to_run:
            print(f"\n[*] Running scan: {scan_name}")

            scanner_class = AVAILABLE_SCANNERS[scan_name]
            scanner = scanner_class(self.session)

            print(f"    {scanner.get_scan_description()}")

            try:
                findings = scanner.execute()
                print(f"    Found {len(findings)} issue(s)")

                # Enrich findings with AI-generated executive summaries
                if self.use_ai_narrator and self.narrator and findings:
                    print(f"    Generating executive summaries...")
                    for finding in findings:
                        self.narrator.enrich_finding(finding, use_ai=True)

                report.findings.extend(findings)

            except Exception as e:
                print(f"    ERROR: Scan failed - {str(e)}")
                import traceback
                traceback.print_exc()

        return report

    def output_report(self, report: ScanReport, output_format: str, output_file: str = None):
        """
        Output scan report in specified format

        Args:
            report: ScanReport to output
            output_format: 'json', 'summary', or 'dashboard'
            output_file: Optional file path to write to (default: stdout)
        """
        if output_format == 'json':
            self._output_json(report, output_file)
        elif output_format == 'summary':
            self._output_summary(report, output_file)
        elif output_format == 'dashboard':
            self._output_dashboard(report, output_file)
        else:
            print(f"ERROR: Unknown output format: {output_format}")
            sys.exit(1)

    def _output_json(self, report: ScanReport, output_file: str):
        """Output JSON format"""
        json_output = report.to_json(indent=2)

        if output_file:
            Path(output_file).write_text(json_output)
            print(f"\n[+] Report written to: {output_file}")
        else:
            print("\n" + "="*80)
            print("SCAN REPORT (JSON)")
            print("="*80)
            print(json_output)

    def _output_summary(self, report: ScanReport, output_file: str):
        """Output human-readable summary format"""
        lines = []
        lines.append("="*80)
        lines.append("AI GOVERNANCE SCAN REPORT")
        lines.append("="*80)
        lines.append(f"Scan Time:    {report.scan_timestamp}")
        lines.append(f"AWS Account:  {report.aws_account_id}")
        lines.append(f"AWS Region:   {report.aws_region}")
        lines.append("")
        lines.append("SUMMARY")
        lines.append("-"*80)
        lines.append(f"Total Findings: {len(report.findings)}")
        lines.append("")

        severity_counts = report.get_severity_counts()
        for severity, count in severity_counts.items():
            if count > 0:
                lines.append(f"  {severity:12s}: {count}")

        if report.findings:
            lines.append("")
            lines.append("FINDINGS DETAIL")
            lines.append("-"*80)

            for i, finding in enumerate(report.findings, 1):
                lines.append(f"\n[{i}] {finding.finding_id} - {finding.severity.value}")
                lines.append(f"    Resource: {finding.resource_arn}")
                lines.append(f"    Issue:    {finding.technical_finding}")
                lines.append(f"    Fix:      {finding.mitigation_applied}")

                if finding.executive_summary:
                    lines.append(f"\n    Executive Summary:")
                    lines.append(f"    {finding.executive_summary}")

                lines.append(f"\n    Compliance Mappings:")
                if finding.mappings.nist_ai_rmf:
                    lines.append(f"      NIST AI RMF: {', '.join(finding.mappings.nist_ai_rmf)}")
                if finding.mappings.iso_42001:
                    lines.append(f"      ISO 42001:   {', '.join(finding.mappings.iso_42001)}")
                if finding.mappings.mitre_atlas:
                    lines.append(f"      MITRE ATLAS: {', '.join(finding.mappings.mitre_atlas)}")
                lines.append("")

        lines.append("="*80)

        output_text = "\n".join(lines)

        if output_file:
            Path(output_file).write_text(output_text)
            print(f"\n[+] Report written to: {output_file}")
        else:
            print("\n" + output_text)

    def _output_dashboard(self, report: ScanReport, output_file: str):
        """Output HTML dashboard format"""
        from outputs.templates.dashboard import generate_dashboard

        html = generate_dashboard(report)

        if not output_file:
            output_file = f"ai-governance-scan-{datetime.now().strftime('%Y%m%d-%H%M%S')}.html"

        Path(output_file).write_text(html)
        print(f"\n[+] Dashboard written to: {output_file}")
        print(f"    Open in browser: file://{Path(output_file).absolute()}")


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="AI Governance Scanner - Audit AWS AI services for compliance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all scans and output JSON
  python scanner.py --scan all --format json --output report.json

  # Run specific scan with summary output
  python scanner.py --scan bedrock-guardrails --format summary

  # Generate HTML dashboard
  python scanner.py --scan all --format dashboard --output dashboard.html

  # List available scans
  python scanner.py --list-scans
        """
    )

    parser.add_argument('--scan', nargs='+', metavar='SCAN_NAME',
                       help='Scan(s) to run (use "all" for all scans)')
    parser.add_argument('--list-scans', action='store_true',
                       help='List available scans and exit')
    parser.add_argument('--format', choices=['json', 'summary', 'dashboard'],
                       default='summary',
                       help='Output format (default: summary)')
    parser.add_argument('--output', '-o', metavar='FILE',
                       help='Output file (default: stdout for json/summary, auto-generated for dashboard)')
    parser.add_argument('--region', help='AWS region (default: from AWS config)')
    parser.add_argument('--profile', help='AWS profile name (default: default)')
    parser.add_argument('--no-ai-narrator', action='store_true',
                       help='Disable AI-generated executive summaries (use templates instead)')

    args = parser.parse_args()

    # Handle --list-scans
    if args.list_scans:
        print("\nAvailable Scans:")
        print("-" * 80)
        for scan_name, scanner_class in AVAILABLE_SCANNERS.items():
            # Instantiate temporarily to get description
            temp_session = boto3.Session()
            scanner = scanner_class(temp_session)
            print(f"\n{scan_name}")
            print(f"  {scanner.get_scan_description()}")
        print()
        sys.exit(0)

    # Require --scan if not listing
    if not args.scan:
        parser.error("--scan is required (or use --list-scans)")

    # Initialize scanner
    print(f"[*] Initializing AI Governance Scanner...")
    print(f"    Region: {args.region or 'default'}")
    print(f"    Profile: {args.profile or 'default'}")
    print(f"    AI Narrator: {'disabled' if args.no_ai_narrator else 'enabled'}")

    scanner = AIGovernanceScanner(
        region=args.region,
        profile=args.profile,
        use_ai_narrator=not args.no_ai_narrator
    )

    # Run scans
    report = scanner.run_scan(args.scan)

    # Output results
    scanner.output_report(report, args.format, args.output)

    # Exit with appropriate code
    critical_high = sum(1 for f in report.findings if f.severity.value in ['Critical', 'High'])
    if critical_high > 0:
        print(f"\n[!] WARNING: {critical_high} Critical/High severity findings require attention")
        sys.exit(1)
    else:
        print(f"\n[+] Scan complete")
        sys.exit(0)


if __name__ == '__main__':
    main()

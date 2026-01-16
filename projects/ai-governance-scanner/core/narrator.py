"""
AI Governance Scanner - Executive Narrator

Uses GenAI (AWS Bedrock) to translate technical findings into
executive-level risk explanations that connect vulnerabilities
to business impact and regulatory compliance.
"""

import json
import boto3
from typing import Optional
from .schema import Finding


class ExecutiveNarrator:
    """
    Generates executive summaries for technical findings using GenAI.

    The narrator follows a specific format:
    - Sentence 1: Business impact of the vulnerability
    - Sentence 2: Specific attack it enables (reference MITRE)
    - Sentence 3: How fixing this fulfills compliance requirements
    """

    SYSTEM_PROMPT = """You are an AI Governance and Risk Expert. Take the provided JSON scanning result and write a 3-sentence executive summary.

Sentence 1: The business impact of the vulnerability.
Sentence 2: The specific attack it enables (reference MITRE).
Sentence 3: How fixing this fulfills specific requirements of NIST AI RMF and ISO 42001.

Use professional, non-alarmist language. Focus on liability, regulatory compliance, and operational risk."""

    def __init__(self, session: boto3.Session, model_id: str = "anthropic.claude-3-haiku-20240307-v1:0"):
        """
        Initialize narrator with AWS Bedrock client

        Args:
            session: Configured boto3 Session
            model_id: Bedrock model ID (default: Claude 3 Haiku - fast and cost-effective)
        """
        self.session = session
        self.model_id = model_id
        self.bedrock = None

    def _get_bedrock_client(self):
        """Lazy initialization of Bedrock client"""
        if self.bedrock is None:
            self.bedrock = self.session.client('bedrock-runtime')
        return self.bedrock

    def generate_summary(self, finding: Finding, use_ai: bool = True) -> str:
        """
        Generate executive summary for a finding

        Args:
            finding: The technical finding to explain
            use_ai: If True, use Bedrock AI. If False, use template (for testing/fallback)

        Returns:
            Executive summary string
        """
        if not use_ai:
            return self._generate_template_summary(finding)

        try:
            return self._generate_ai_summary(finding)
        except Exception as e:
            # Fallback to template if AI fails
            print(f"Warning: AI summary generation failed ({str(e)}), using template")
            return self._generate_template_summary(finding)

    def _generate_ai_summary(self, finding: Finding) -> str:
        """Generate summary using AWS Bedrock"""
        client = self._get_bedrock_client()

        # Prepare the finding as JSON for the AI
        finding_json = finding.to_json()

        # Construct the user prompt
        user_prompt = f"""Generate an executive summary for this security finding:

{finding_json}

Remember: 3 sentences covering business impact, attack vector (MITRE), and compliance fulfillment (NIST/ISO)."""

        # Call Bedrock with Claude's native API format
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 300,
            "temperature": 0.3,  # Lower temperature for consistent, professional output
            "system": self.SYSTEM_PROMPT,
            "messages": [
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }

        response = client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(request_body)
        )

        # Parse response
        response_body = json.loads(response['body'].read())
        summary = response_body['content'][0]['text'].strip()

        return summary

    def _generate_template_summary(self, finding: Finding) -> str:
        """Generate a template-based summary (fallback when AI is unavailable)"""
        # Extract first MITRE technique if available
        mitre_ref = finding.mappings.mitre_atlas[0] if finding.mappings.mitre_atlas else "Unknown attack vector"

        # Extract first NIST control if available
        nist_ref = finding.mappings.nist_ai_rmf[0] if finding.mappings.nist_ai_rmf else "AI RMF controls"

        # Extract first ISO control if available
        iso_ref = finding.mappings.iso_42001[0] if finding.mappings.iso_42001 else "ISO 42001 requirements"

        template = f"""{finding.technical_finding} creates regulatory and operational risk exposure. \
This vulnerability enables {mitre_ref} attacks, allowing adversaries to compromise AI system integrity. \
Remediation addresses {nist_ref} and fulfills {iso_ref}, demonstrating due diligence in AI governance."""

        return template

    def enrich_finding(self, finding: Finding, use_ai: bool = True) -> Finding:
        """
        Add executive summary to a finding (modifies in place)

        Args:
            finding: Finding to enrich
            use_ai: Whether to use AI generation

        Returns:
            The same finding object with executive_summary populated
        """
        finding.executive_summary = self.generate_summary(finding, use_ai=use_ai)
        return finding

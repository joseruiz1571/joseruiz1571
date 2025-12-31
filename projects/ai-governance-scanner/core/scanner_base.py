"""
AI Governance Scanner - Base Scanner Class

Abstract base class for all security scans. Each scan implements
the detection logic and compliance mappings for a specific control.
"""

from abc import ABC, abstractmethod
from typing import List
import boto3
from .schema import Finding


class BaseScanner(ABC):
    """
    Base class for all AWS AI governance scans.

    Each scanner focuses on a single control (e.g., Bedrock Guardrails)
    and knows how to:
    1. Query the AWS API
    2. Detect the vulnerability
    3. Map it to compliance frameworks
    4. Generate remediation guidance
    """

    def __init__(self, session: boto3.Session):
        """
        Initialize scanner with AWS session

        Args:
            session: Configured boto3 Session with appropriate credentials
        """
        self.session = session
        self.region = session.region_name or 'us-east-1'

    @abstractmethod
    def get_scan_name(self) -> str:
        """Return human-readable name of this scan"""
        pass

    @abstractmethod
    def get_scan_description(self) -> str:
        """Return detailed description of what this scan checks"""
        pass

    @abstractmethod
    def execute(self) -> List[Finding]:
        """
        Execute the scan and return findings.

        Returns:
            List of Finding objects for any issues discovered
        """
        pass

    def get_account_id(self) -> str:
        """Get the AWS account ID from the current session"""
        try:
            sts = self.session.client('sts')
            return sts.get_caller_identity()['Account']
        except Exception as e:
            return f"unknown-{str(e)[:20]}"

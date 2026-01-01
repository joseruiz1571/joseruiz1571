#!/usr/bin/env python3
"""
Home Network Security Scanner - MVP

Discovers devices on your local network and assesses security risks including:
- Active device discovery
- Manufacturer identification
- Open ports and services
- IoT device detection
- Risk scoring and recommendations

Author: Jose Ruiz-Vazquez
"""

import socket
import subprocess
import json
import ipaddress
import re
import sys
from datetime import datetime
from typing import Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed


class NetworkSecurityScanner:
    """Scan local network for security vulnerabilities."""

    # Common risky ports and their services
    RISKY_PORTS = {
        21: {"service": "FTP", "risk": "HIGH", "reason": "Unencrypted file transfer"},
        22: {"service": "SSH", "risk": "MEDIUM", "reason": "Remote access - ensure strong auth"},
        23: {"service": "Telnet", "risk": "CRITICAL", "reason": "Unencrypted remote access"},
        25: {"service": "SMTP", "risk": "MEDIUM", "reason": "Mail relay risk"},
        80: {"service": "HTTP", "risk": "MEDIUM", "reason": "Unencrypted web interface"},
        139: {"service": "NetBIOS", "risk": "HIGH", "reason": "Windows file sharing exposure"},
        445: {"service": "SMB", "risk": "HIGH", "reason": "File sharing - ransomware vector"},
        1433: {"service": "MSSQL", "risk": "HIGH", "reason": "Database exposure"},
        3306: {"service": "MySQL", "risk": "HIGH", "reason": "Database exposure"},
        3389: {"service": "RDP", "risk": "HIGH", "reason": "Remote desktop exposure"},
        5432: {"service": "PostgreSQL", "risk": "HIGH", "reason": "Database exposure"},
        5900: {"service": "VNC", "risk": "HIGH", "reason": "Remote desktop exposure"},
        8080: {"service": "HTTP-Alt", "risk": "MEDIUM", "reason": "Alternative web port"},
        8888: {"service": "HTTP-Alt", "risk": "MEDIUM", "reason": "Alternative web port"},
    }

    # IoT device indicators (MAC vendor prefixes and common patterns)
    IOT_VENDORS = [
        "ring", "nest", "amazon", "ecobee", "philips hue", "tp-link",
        "sonos", "roku", "samsung smartthings", "wemo", "lifx",
        "arlo", "wyze", "tuya", "shenzhen", "hangzhou", "espressif"
    ]

    def __init__(self):
        self.mac_vendors = self._load_mac_vendors()

    def _load_mac_vendors(self) -> Dict[str, str]:
        """Load common MAC vendor prefixes for device identification."""
        # Simplified vendor database - in production, use full OUI database
        return {
            "00:0C:29": "VMware",
            "00:50:56": "VMware",
            "08:00:27": "VirtualBox",
            "52:54:00": "QEMU/KVM",
            "B8:27:EB": "Raspberry Pi",
            "DC:A6:32": "Raspberry Pi",
            "E4:5F:01": "Raspberry Pi",
            "00:1B:44": "Cisco",
            "00:1E:13": "Netgear",
            "00:24:B2": "Netgear",
            "E8:FC:AF": "Amazon (Echo/Ring)",
            "74:C2:46": "Amazon (Echo/Ring)",
            "18:B4:30": "Nest",
            "64:16:66": "Nest",
            "00:17:88": "Philips Hue",
            "EC:FA:BC": "Philips Hue",
            "50:C7:BF": "TP-Link",
            "00:27:22": "TP-Link",
        }

    def get_local_network(self) -> str:
        """Detect the local network CIDR."""
        try:
            # Get default gateway
            if sys.platform == "darwin" or sys.platform.startswith("linux"):
                result = subprocess.run(
                    ["ip", "route", "show", "default"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    # Parse: default via 192.168.1.1 dev eth0
                    match = re.search(r'default via ([\d.]+)', result.stdout)
                    if match:
                        gateway = match.group(1)
                        # Get local IP and calculate network
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((gateway, 80))
                        local_ip = s.getsockname()[0]
                        s.close()

                        # Assume /24 network for MVP
                        network = ipaddress.ip_network(f"{local_ip}/24", strict=False)
                        return str(network)

            # Fallback: assume common home network
            return "192.168.1.0/24"

        except Exception as e:
            print(f"Warning: Could not detect network, using default: {e}")
            return "192.168.1.0/24"

    def discover_devices(self, network: str) -> List[Dict]:
        """Discover active devices on the network using ARP."""
        print(f"Scanning network: {network}")
        devices = []

        try:
            # Use arp-scan if available (requires sudo)
            result = subprocess.run(
                ["sudo", "arp-scan", "--localnet", "--quiet"],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                devices = self._parse_arp_scan(result.stdout)
                print(f"Found {len(devices)} devices using arp-scan")
                return devices

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Fallback: use nmap if available
        try:
            result = subprocess.run(
                ["nmap", "-sn", network, "-oG", "-"],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                devices = self._parse_nmap_ping_scan(result.stdout)
                print(f"Found {len(devices)} devices using nmap")
                return devices

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Final fallback: use arp command
        try:
            result = subprocess.run(
                ["arp", "-a"],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                devices = self._parse_arp_command(result.stdout)
                print(f"Found {len(devices)} devices using arp")
                return devices

        except Exception as e:
            print(f"Error discovering devices: {e}")

        return devices

    def _parse_arp_scan(self, output: str) -> List[Dict]:
        """Parse arp-scan output."""
        devices = []
        for line in output.strip().split('\n'):
            # Format: IP_ADDRESS	MAC_ADDRESS	VENDOR
            parts = re.split(r'\s+', line.strip())
            if len(parts) >= 2 and self._is_valid_ip(parts[0]):
                devices.append({
                    'ip': parts[0],
                    'mac': parts[1].upper(),
                    'vendor': ' '.join(parts[2:]) if len(parts) > 2 else 'Unknown'
                })
        return devices

    def _parse_nmap_ping_scan(self, output: str) -> List[Dict]:
        """Parse nmap ping scan output."""
        devices = []
        for line in output.split('\n'):
            if 'Host:' in line:
                match = re.search(r'Host: ([\d.]+).*MAC Address: ([0-9A-F:]+)', line)
                if match:
                    devices.append({
                        'ip': match.group(1),
                        'mac': match.group(2).upper(),
                        'vendor': 'Unknown'
                    })
        return devices

    def _parse_arp_command(self, output: str) -> List[Dict]:
        """Parse arp -a command output."""
        devices = []
        # Format varies by OS
        # Linux: ? (192.168.1.1) at aa:bb:cc:dd:ee:ff [ether] on eth0
        # macOS: router.local (192.168.1.1) at aa:bb:cc:dd:ee:ff on en0 ifscope [ethernet]

        for line in output.split('\n'):
            ip_match = re.search(r'\(([\d.]+)\)', line)
            mac_match = re.search(r'at ([0-9a-fA-F:]{17})', line)

            if ip_match and mac_match:
                ip = ip_match.group(1)
                mac = mac_match.group(1).upper()

                if self._is_valid_ip(ip) and mac != 'FF:FF:FF:FF:FF:FF':
                    devices.append({
                        'ip': ip,
                        'mac': mac,
                        'vendor': self._lookup_vendor(mac)
                    })

        return devices

    def _is_valid_ip(self, ip: str) -> bool:
        """Check if string is a valid IP address."""
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def _lookup_vendor(self, mac: str) -> str:
        """Lookup vendor from MAC address."""
        mac_prefix = mac[:8]  # First 3 octets
        return self.mac_vendors.get(mac_prefix, "Unknown")

    def scan_ports(self, ip: str, timeout: float = 0.5) -> List[int]:
        """Scan common risky ports on a device."""
        open_ports = []

        for port in self.RISKY_PORTS.keys():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                result = sock.connect_ex((ip, port))
                sock.close()

                if result == 0:
                    open_ports.append(port)

            except Exception:
                pass

        return open_ports

    def assess_device_risk(self, device: Dict, open_ports: List[int]) -> Dict:
        """Assess security risk for a device."""
        risk_score = 0
        risk_level = "LOW"
        findings = []
        recommendations = []

        # Check for IoT device
        is_iot = False
        vendor_lower = device.get('vendor', '').lower()
        for iot_vendor in self.IOT_VENDORS:
            if iot_vendor in vendor_lower:
                is_iot = True
                risk_score += 10
                findings.append(f"IoT device detected: {device.get('vendor', 'Unknown')}")
                break

        # Assess open ports
        critical_ports = []
        high_risk_ports = []
        medium_risk_ports = []

        for port in open_ports:
            port_info = self.RISKY_PORTS.get(port, {})
            risk = port_info.get('risk', 'MEDIUM')
            service = port_info.get('service', f'Port {port}')
            reason = port_info.get('reason', 'Exposed service')

            if risk == 'CRITICAL':
                critical_ports.append(port)
                risk_score += 30
                findings.append(f"CRITICAL: {service} (port {port}) - {reason}")
                recommendations.append(f"Disable {service} immediately or restrict to localhost only")
            elif risk == 'HIGH':
                high_risk_ports.append(port)
                risk_score += 15
                findings.append(f"HIGH: {service} (port {port}) - {reason}")
                recommendations.append(f"Restrict {service} access or use VPN/firewall")
            else:
                medium_risk_ports.append(port)
                risk_score += 5
                findings.append(f"MEDIUM: {service} (port {port}) - {reason}")

        # Determine overall risk level
        if risk_score >= 30 or len(critical_ports) > 0:
            risk_level = "CRITICAL"
        elif risk_score >= 20 or len(high_risk_ports) > 2:
            risk_level = "HIGH"
        elif risk_score >= 10 or len(high_risk_ports) > 0:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        # IoT-specific recommendations
        if is_iot:
            recommendations.extend([
                "Isolate IoT devices on separate VLAN/guest network",
                "Disable remote access/cloud features if not needed",
                "Check for firmware updates regularly"
            ])

        # General recommendations
        if len(open_ports) == 0:
            recommendations.append("No risky ports detected - good security posture")

        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'is_iot': is_iot,
            'findings': findings,
            'recommendations': recommendations,
            'open_ports_summary': {
                'critical': critical_ports,
                'high': high_risk_ports,
                'medium': medium_risk_ports
            }
        }

    def scan_device(self, device: Dict) -> Dict:
        """Complete security scan of a single device."""
        ip = device['ip']
        print(f"  Scanning {ip} ({device.get('vendor', 'Unknown')})...")

        # Scan ports
        open_ports = self.scan_ports(ip)

        # Assess risk
        risk_assessment = self.assess_device_risk(device, open_ports)

        # Compile results
        return {
            'ip': ip,
            'mac': device.get('mac', 'Unknown'),
            'vendor': device.get('vendor', 'Unknown'),
            'hostname': self._get_hostname(ip),
            'open_ports': open_ports,
            **risk_assessment
        }

    def _get_hostname(self, ip: str) -> str:
        """Try to resolve hostname for IP."""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except Exception:
            return "Unknown"

    def scan_network(self, network: str = None) -> Dict:
        """Perform complete network security scan."""
        if network is None:
            network = self.get_local_network()

        print("\n" + "="*70)
        print("Home Network Security Scanner - MVP")
        print("="*70)
        print(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Discover devices
        devices = self.discover_devices(network)

        if not devices:
            print("No devices found. Try running with sudo for better results.")
            return {'error': 'No devices discovered'}

        print(f"\nScanning {len(devices)} devices for security risks...")
        print("-"*70)

        # Scan each device
        scan_results = []
        for device in devices:
            result = self.scan_device(device)
            scan_results.append(result)

        # Generate summary statistics
        summary = self._generate_summary(scan_results)

        return {
            'metadata': {
                'scan_time': datetime.now().isoformat(),
                'network': network,
                'total_devices': len(scan_results)
            },
            'summary': summary,
            'devices': scan_results
        }

    def _generate_summary(self, results: List[Dict]) -> Dict:
        """Generate summary statistics."""
        summary = {
            'total_devices': len(results),
            'risk_distribution': {
                'CRITICAL': 0,
                'HIGH': 0,
                'MEDIUM': 0,
                'LOW': 0
            },
            'iot_devices': 0,
            'total_open_ports': 0,
            'most_common_risks': []
        }

        all_findings = []

        for device in results:
            # Count risk levels
            risk_level = device.get('risk_level', 'LOW')
            summary['risk_distribution'][risk_level] += 1

            # Count IoT devices
            if device.get('is_iot', False):
                summary['iot_devices'] += 1

            # Count open ports
            summary['total_open_ports'] += len(device.get('open_ports', []))

            # Collect findings
            all_findings.extend(device.get('findings', []))

        # Find most common risks
        finding_counts = {}
        for finding in all_findings:
            risk_type = finding.split(':')[0] if ':' in finding else finding
            finding_counts[risk_type] = finding_counts.get(risk_type, 0) + 1

        summary['most_common_risks'] = sorted(
            finding_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        return summary

    def print_report(self, scan_results: Dict):
        """Print human-readable security report."""
        if 'error' in scan_results:
            print(f"\nError: {scan_results['error']}")
            return

        print("\n" + "="*70)
        print("SCAN SUMMARY")
        print("="*70)

        summary = scan_results['summary']
        print(f"Total Devices Found: {summary['total_devices']}")
        print(f"IoT Devices: {summary['iot_devices']}")
        print(f"Total Open Risky Ports: {summary['total_open_ports']}")
        print()

        print("Risk Distribution:")
        for level in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            count = summary['risk_distribution'][level]
            if count > 0:
                print(f"  {level:10} {count:3} devices")

        print("\n" + "="*70)
        print("DEVICE DETAILS")
        print("="*70)

        # Sort devices by risk score (highest first)
        devices = sorted(
            scan_results['devices'],
            key=lambda x: x.get('risk_score', 0),
            reverse=True
        )

        for device in devices:
            self._print_device_details(device)

        print("\n" + "="*70)
        print("TOP RECOMMENDATIONS")
        print("="*70)

        # Collect all unique recommendations
        all_recommendations = set()
        for device in devices:
            if device.get('risk_level') in ['CRITICAL', 'HIGH']:
                all_recommendations.update(device.get('recommendations', []))

        for i, rec in enumerate(list(all_recommendations)[:10], 1):
            print(f"{i}. {rec}")

        print("\n" + "="*70)
        print("Scan completed: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("="*70)

    def _print_device_details(self, device: Dict):
        """Print details for a single device."""
        risk_colors = {
            'CRITICAL': '🔴',
            'HIGH': '🟠',
            'MEDIUM': '🟡',
            'LOW': '🟢'
        }

        risk_icon = risk_colors.get(device.get('risk_level', 'LOW'), '⚪')

        print(f"\n{risk_icon} {device['ip']} - {device.get('vendor', 'Unknown')}")
        print(f"   MAC: {device.get('mac', 'Unknown')}")
        print(f"   Hostname: {device.get('hostname', 'Unknown')}")
        print(f"   Risk Level: {device.get('risk_level', 'LOW')} (Score: {device.get('risk_score', 0)})")

        if device.get('is_iot'):
            print(f"   Device Type: IoT Device")

        if device.get('open_ports'):
            print(f"   Open Risky Ports: {', '.join(map(str, device['open_ports']))}")

        if device.get('findings'):
            print("   Findings:")
            for finding in device['findings'][:5]:  # Show top 5
                print(f"     - {finding}")

        if device.get('recommendations'):
            print("   Recommendations:")
            for rec in device['recommendations'][:3]:  # Show top 3
                print(f"     • {rec}")

    def export_json(self, scan_results: Dict, filename: str):
        """Export results to JSON file."""
        with open(filename, 'w') as f:
            json.dump(scan_results, f, indent=2)
        print(f"\nResults exported to: {filename}")

    def export_csv(self, scan_results: Dict, filename: str):
        """Export results to CSV file."""
        import csv

        if 'error' in scan_results:
            print("Cannot export - scan error occurred")
            return

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'IP Address',
                'MAC Address',
                'Vendor',
                'Hostname',
                'Risk Level',
                'Risk Score',
                'Is IoT',
                'Open Ports',
                'Findings',
                'Recommendations'
            ])

            for device in scan_results['devices']:
                writer.writerow([
                    device.get('ip', ''),
                    device.get('mac', ''),
                    device.get('vendor', ''),
                    device.get('hostname', ''),
                    device.get('risk_level', ''),
                    device.get('risk_score', 0),
                    device.get('is_iot', False),
                    ', '.join(map(str, device.get('open_ports', []))),
                    '; '.join(device.get('findings', [])),
                    '; '.join(device.get('recommendations', []))
                ])

        print(f"Results exported to: {filename}")


def main():
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Home Network Security Scanner - Discover and assess security risks'
    )
    parser.add_argument(
        '--network',
        help='Network CIDR to scan (e.g., 192.168.1.0/24)',
        default=None
    )
    parser.add_argument(
        '--json',
        help='Export results to JSON file',
        metavar='FILE'
    )
    parser.add_argument(
        '--csv',
        help='Export results to CSV file',
        metavar='FILE'
    )

    args = parser.parse_args()

    # Create scanner
    scanner = NetworkSecurityScanner()

    # Perform scan
    results = scanner.scan_network(args.network)

    # Print report
    scanner.print_report(results)

    # Export if requested
    if args.json:
        scanner.export_json(results, args.json)

    if args.csv:
        scanner.export_csv(results, args.csv)


if __name__ == "__main__":
    main()

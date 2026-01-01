# Home Network Security Scanner (MVP)

A Python tool to discover devices on your home network and assess security risks. Identifies vulnerable services, IoT devices, and provides actionable recommendations to improve your home network security posture.

## Features

### Device Discovery
- Automatic network detection and scanning
- ARP-based device discovery
- MAC address vendor identification
- Hostname resolution

### Security Assessment
- **Port Scanning**: Detects 13 common risky ports/services
- **IoT Detection**: Identifies IoT devices that may need isolation
- **Risk Scoring**: Assigns risk levels (CRITICAL, HIGH, MEDIUM, LOW)
- **Vulnerability Analysis**: Flags dangerous services like Telnet, SMB, RDP

### Reporting
- Human-readable terminal output with risk indicators
- JSON export for integration with other tools
- CSV export for spreadsheet analysis
- Prioritized recommendations based on findings

## Quick Start

### Prerequisites

**Python:** 3.6 or higher (uses standard library only)

**Optional Tools** (for better results):
```bash
# Ubuntu/Debian
sudo apt-get install nmap arp-scan

# macOS
brew install nmap arp-scan
```

The script will work without these tools using the built-in `arp` command, but results may be limited.

### Installation

```bash
# Clone or download to your project directory
cd projects/home-network-security-scanner

# Make script executable
chmod +x network_security_scanner.py
```

### Basic Usage

```bash
# Auto-detect and scan your local network
python3 network_security_scanner.py

# Scan specific network
python3 network_security_scanner.py --network 192.168.1.0/24

# Export results
python3 network_security_scanner.py --json results.json --csv results.csv
```

**For best results, run with sudo:**
```bash
sudo python3 network_security_scanner.py
```

## What It Scans For

### Critical Risks (30 points each)
- **Port 23 (Telnet)**: Unencrypted remote access - immediate security risk

### High Risks (15 points each)
- **Port 21 (FTP)**: Unencrypted file transfer
- **Port 139/445 (NetBIOS/SMB)**: Windows file sharing - ransomware vector
- **Port 3389 (RDP)**: Remote desktop exposure
- **Port 5900 (VNC)**: Remote desktop exposure
- **Ports 1433/3306/5432**: Database services exposure

### Medium Risks (5-10 points each)
- **Port 22 (SSH)**: Remote access (secure but should verify strong auth)
- **Port 80/8080/8888 (HTTP)**: Unencrypted web interfaces
- **Port 25 (SMTP)**: Mail relay risk
- **IoT Devices**: Smart home devices that may need isolation

## Example Output

```
======================================================================
Home Network Security Scanner - MVP
======================================================================
Scan started: 2025-12-27 10:30:45

Scanning network: 192.168.1.0/24
Found 8 devices using arp-scan

Scanning 8 devices for security risks...
----------------------------------------------------------------------
  Scanning 192.168.1.1 (Netgear)...
  Scanning 192.168.1.100 (Amazon)...
  Scanning 192.168.1.101 (Raspberry Pi)...

======================================================================
SCAN SUMMARY
======================================================================
Total Devices Found: 8
IoT Devices: 2
Total Open Risky Ports: 5

Risk Distribution:
  CRITICAL    1 devices
  HIGH        2 devices
  MEDIUM      3 devices
  LOW         2 devices

======================================================================
DEVICE DETAILS
======================================================================

🔴 192.168.1.101 - Raspberry Pi
   MAC: DC:A6:32:XX:XX:XX
   Hostname: raspberrypi.local
   Risk Level: CRITICAL (Score: 45)
   Open Risky Ports: 22, 23, 80
   Findings:
     - CRITICAL: Telnet (port 23) - Unencrypted remote access
     - MEDIUM: SSH (port 22) - Remote access - ensure strong auth
     - MEDIUM: HTTP (port 80) - Unencrypted web interface
   Recommendations:
     • Disable Telnet immediately or restrict to localhost only
     • Restrict SSH access or use VPN/firewall

🟠 192.168.1.100 - Amazon (Echo/Ring)
   MAC: E8:FC:AF:XX:XX:XX
   Hostname: echo-living-room.local
   Risk Level: HIGH (Score: 25)
   Device Type: IoT Device
   Open Risky Ports: 80, 8080
   Findings:
     - IoT device detected: Amazon (Echo/Ring)
     - MEDIUM: HTTP (port 80) - Unencrypted web interface
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟢 192.168.1.1 - Netgear
   MAC: 00:24:B2:XX:XX:XX
   Hostname: router.local
   Risk Level: LOW (Score: 0)
   Recommendations:
     • No risky ports detected - good security posture
```

## Understanding Risk Scores

**Risk Levels:**
- **CRITICAL (30+)**: Immediate action required - serious vulnerabilities
- **HIGH (20-29)**: High priority - significant security risks
- **MEDIUM (10-19)**: Should address - moderate concerns
- **LOW (<10)**: Good security posture - minor or no issues

**Common Findings:**

| Service | Risk | Why It Matters |
|---------|------|----------------|
| Telnet | CRITICAL | Sends passwords in plaintext - disable immediately |
| SMB/NetBIOS | HIGH | Common ransomware attack vector |
| RDP | HIGH | Brute force target for attackers |
| Database Ports | HIGH | Should never be exposed on home network |
| SSH | MEDIUM | Secure if using key auth and strong passwords |
| HTTP | MEDIUM | Management interfaces should use HTTPS |
| IoT Devices | MEDIUM+ | Often have security vulnerabilities, need isolation |

## Recommended Actions

### Critical Findings
1. **Disable Telnet immediately** - Replace with SSH
2. **Close database ports** - Should only listen on localhost
3. **Disable SMB** if not needed - Or restrict to specific IPs

### High Priority
1. **Isolate IoT devices** - Use guest network or separate VLAN
2. **Secure RDP/VNC** - Use VPN instead of direct exposure
3. **Review SSH access** - Disable password auth, use keys only

### General Best Practices
1. **Enable WPA3** (or WPA2) on your router
2. **Change default router credentials**
3. **Keep firmware updated** on all devices
4. **Disable UPnP** on router if not needed
5. **Enable router firewall**
6. **Use strong, unique passwords** for all devices

## Output Formats

### Terminal Output
- Color-coded risk indicators (🔴🟠🟡🟢)
- Prioritized device list (highest risk first)
- Summary statistics
- Actionable recommendations

### JSON Export (`--json results.json`)
```json
{
  "metadata": {
    "scan_time": "2025-12-27T10:30:45",
    "network": "192.168.1.0/24",
    "total_devices": 8
  },
  "summary": {
    "total_devices": 8,
    "iot_devices": 2,
    "risk_distribution": {...}
  },
  "devices": [...]
}
```

### CSV Export (`--csv results.csv`)
Spreadsheet-compatible format with columns:
- IP Address, MAC Address, Vendor
- Hostname, Risk Level, Risk Score
- Is IoT, Open Ports, Findings, Recommendations

## Limitations (MVP)

This is a Minimum Viable Product designed for home network security assessment:

**Current Limitations:**
- Scans only common risky ports (not comprehensive port scan)
- Basic MAC vendor database (subset of full OUI database)
- Requires devices to be in ARP cache or discoverable via ARP/ping
- No deep packet inspection or traffic analysis
- IoT detection based on vendor matching only

**Not Included in MVP:**
- Default credential testing (requires target device knowledge)
- Firmware version detection (requires device-specific APIs)
- Automated remediation
- Continuous monitoring
- Network segmentation verification beyond device listing

## Advanced Usage

### Scan Specific Network
```bash
# Scan different network
python3 network_security_scanner.py --network 10.0.0.0/24

# Scan smaller range
python3 network_security_scanner.py --network 192.168.1.0/28
```

### Integration with Other Tools

**Combine with vulnerability scanning:**
```bash
# Export to JSON and process with other tools
python3 network_security_scanner.py --json scan.json
cat scan.json | jq '.devices[] | select(.risk_level == "CRITICAL")'
```

**Scheduled scanning:**
```bash
# Add to crontab for weekly scans
0 2 * * 0 /usr/bin/python3 /path/to/network_security_scanner.py --json /var/log/network-scan-$(date +\%Y\%m\%d).json
```

## Troubleshooting

### "No devices found"
- Try running with `sudo` for better results
- Install `nmap` or `arp-scan` for improved discovery
- Verify you're on the correct network
- Some devices may have firewall rules blocking discovery

### Permission Errors
- Use `sudo` to access raw sockets for ARP scanning
- Some tools (arp-scan) require root privileges

### Slow Scanning
- Port scanning timeout is 0.5s per port per device
- Large networks may take several minutes
- Reduce network range or use `--network` with smaller CIDR

## Security & Privacy

**What This Script Does:**
- Scans only YOUR local network
- Does NOT send data externally
- Does NOT exploit vulnerabilities
- Only checks if ports are open (no authentication attempts)

**Running Safely:**
- Only scan networks you own or have permission to scan
- This tool is for defensive security assessment only
- Does not attempt to login or access devices

## Future Enhancements

Potential additions for future versions:
- Full MAC OUI database integration
- Web-based dashboard
- Continuous monitoring mode
- Automated remediation suggestions with scripts
- Integration with router APIs for firewall rule management
- VLAN configuration recommendations
- Historical tracking and change detection
- Email/SMS alerts for new devices or risk changes

## Project Context

This tool was developed as part of a cybersecurity portfolio demonstrating:

- **Network Security Assessment** - Practical home network hardening
- **Risk-Based Approach** - Quantitative risk scoring and prioritization
- **Python Development** - Clean, maintainable security tooling
- **Security Operations** - Vulnerability identification and remediation guidance

## Use Cases

### Home Users
- Identify vulnerable IoT devices before they're compromised
- Verify router security settings are effective
- Detect unauthorized devices on network

### IT Professionals
- Quick network security posture assessment
- Demonstration tool for security awareness training
- Template for custom network security automation

### Small Business
- Basic network security audit
- Identify shadow IT and unauthorized devices
- Compliance verification (PCI-DSS network segmentation)

## Related Projects

This project complements other security initiatives:
- **NIST CSF Program Design** - Network security controls implementation
- **ISO 27001 ISMS** - Asset inventory and risk assessment
- **TPRM Assessment** - Network-based third-party security validation

## Contributing

This is an MVP demonstration project. For production use, consider:
- Adding comprehensive OUI database
- Implementing deep packet inspection
- Adding CVE database integration for known device vulnerabilities
- Building web UI for non-technical users

## References

- **NIST Cybersecurity Framework** - Network security best practices
- **CIS Controls** - Network monitoring and access control
- **OWASP IoT Top 10** - IoT-specific security risks
- **SANS Internet Storm Center** - Home network security guidance

## Author

**Jose Ruiz-Vazquez**
AI Governance & Risk Professional
CompTIA Security+ | ISO 27001 Lead Auditor

## License

This tool is provided for educational and personal security assessment purposes. Only scan networks you own or have explicit permission to assess.

---

*Part of the Cybersecurity Portfolio - Demonstrating practical network security assessment and risk management.*

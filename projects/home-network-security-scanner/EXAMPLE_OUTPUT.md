# Example Scanner Output

This document shows example output from the Home Network Security Scanner on a typical home network.

## Terminal Output Example

```
======================================================================
Home Network Security Scanner - MVP
======================================================================
Scan started: 2025-12-27 14:30:22

Scanning network: 192.168.1.0/24
Found 12 devices using arp-scan

Scanning 12 devices for security risks...
----------------------------------------------------------------------
  Scanning 192.168.1.1 (Netgear)...
  Scanning 192.168.1.10 (Apple)...
  Scanning 192.168.1.15 (Samsung)...
  Scanning 192.168.1.20 (Amazon)...
  Scanning 192.168.1.25 (Raspberry Pi)...
  Scanning 192.168.1.30 (Philips Hue)...
  Scanning 192.168.1.50 (TP-Link)...
  Scanning 192.168.1.100 (Dell)...
  Scanning 192.168.1.101 (HP)...
  Scanning 192.168.1.102 (Nest)...
  Scanning 192.168.1.200 (Ring)...
  Scanning 192.168.1.254 (Unknown)...

======================================================================
SCAN SUMMARY
======================================================================
Total Devices Found: 12
IoT Devices: 5
Total Open Risky Ports: 8

Risk Distribution:
  CRITICAL    1 devices
  HIGH        3 devices
  MEDIUM      4 devices
  LOW         4 devices

======================================================================
DEVICE DETAILS
======================================================================

🔴 192.168.1.25 - Raspberry Pi
   MAC: DC:A6:32:12:34:56
   Hostname: raspberrypi.local
   Risk Level: CRITICAL (Score: 55)
   Open Risky Ports: 22, 23, 80, 445
   Findings:
     - CRITICAL: Telnet (port 23) - Unencrypted remote access
     - HIGH: SMB (port 445) - File sharing - ransomware vector
     - MEDIUM: SSH (port 22) - Remote access - ensure strong auth
     - MEDIUM: HTTP (port 80) - Unencrypted web interface
   Recommendations:
     • Disable Telnet immediately or restrict to localhost only
     • Restrict SMB access or use VPN/firewall
     • Restrict SSH access or use VPN/firewall

🟠 192.168.1.254 - Unknown
   MAC: 52:54:00:AA:BB:CC
   Hostname: Unknown
   Risk Level: HIGH (Score: 30)
   Open Risky Ports: 3389, 445
   Findings:
     - HIGH: RDP (port 3389) - Remote desktop exposure
     - HIGH: SMB (port 445) - File sharing - ransomware vector
   Recommendations:
     • Restrict RDP access or use VPN/firewall
     • Restrict SMB access or use VPN/firewall

🟠 192.168.1.100 - Dell
   MAC: 18:03:73:XX:YY:ZZ
   Hostname: desktop-pc.local
   Risk Level: HIGH (Score: 25)
   Open Risky Ports: 22, 139, 445
   Findings:
     - HIGH: SMB (port 445) - File sharing - ransomware vector
     - HIGH: NetBIOS (port 139) - Windows file sharing exposure
     - MEDIUM: SSH (port 22) - Remote access - ensure strong auth
   Recommendations:
     • Restrict SMB access or use VPN/firewall
     • Restrict NetBIOS access or use VPN/firewall
     • Restrict SSH access or use VPN/firewall

🟠 192.168.1.20 - Amazon (Echo/Ring)
   MAC: E8:FC:AF:11:22:33
   Hostname: echo-kitchen.local
   Risk Level: HIGH (Score: 20)
   Device Type: IoT Device
   Open Risky Ports: 80
   Findings:
     - IoT device detected: Amazon (Echo/Ring)
     - MEDIUM: HTTP (port 80) - Unencrypted web interface
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟡 192.168.1.30 - Philips Hue
   MAC: EC:FA:BC:44:55:66
   Hostname: philips-hue.local
   Risk Level: MEDIUM (Score: 15)
   Device Type: IoT Device
   Open Risky Ports: 80
   Findings:
     - IoT device detected: Philips Hue
     - MEDIUM: HTTP (port 80) - Unencrypted web interface
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟡 192.168.1.102 - Nest
   MAC: 64:16:66:77:88:99
   Hostname: nest-thermostat.local
   Risk Level: MEDIUM (Score: 10)
   Device Type: IoT Device
   Findings:
     - IoT device detected: Nest
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟡 192.168.1.200 - Amazon (Echo/Ring)
   MAC: 74:C2:46:AA:BB:CC
   Hostname: ring-doorbell.local
   Risk Level: MEDIUM (Score: 10)
   Device Type: IoT Device
   Findings:
     - IoT device detected: Amazon (Echo/Ring)
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟡 192.168.1.50 - TP-Link
   MAC: 50:C7:BF:12:34:56
   Hostname: smart-plug-01.local
   Risk Level: MEDIUM (Score: 10)
   Device Type: IoT Device
   Findings:
     - IoT device detected: TP-Link
   Recommendations:
     • Isolate IoT devices on separate VLAN/guest network
     • Disable remote access/cloud features if not needed
     • Check for firmware updates regularly

🟢 192.168.1.1 - Netgear
   MAC: 00:24:B2:XX:YY:ZZ
   Hostname: router.local
   Risk Level: LOW (Score: 0)
   Recommendations:
     • No risky ports detected - good security posture

🟢 192.168.1.10 - Apple
   MAC: A4:83:E7:11:22:33
   Hostname: macbook-pro.local
   Risk Level: LOW (Score: 0)
   Recommendations:
     • No risky ports detected - good security posture

🟢 192.168.1.15 - Samsung
   MAC: 28:6D:97:44:55:66
   Hostname: samsung-tv.local
   Risk Level: LOW (Score: 0)
   Recommendations:
     • No risky ports detected - good security posture

🟢 192.168.1.101 - HP
   MAC: D4:85:64:77:88:99
   Hostname: printer.local
   Risk Level: LOW (Score: 0)
   Recommendations:
     • No risky ports detected - good security posture

======================================================================
TOP RECOMMENDATIONS
======================================================================
1. Disable Telnet immediately or restrict to localhost only
2. Restrict SMB access or use VPN/firewall
3. Restrict RDP access or use VPN/firewall
4. Isolate IoT devices on separate VLAN/guest network
5. Restrict NetBIOS access or use VPN/firewall
6. Disable remote access/cloud features if not needed
7. Restrict SSH access or use VPN/firewall
8. Check for firmware updates regularly

======================================================================
Scan completed: 2025-12-27 14:32:15
======================================================================

Results exported to: network_scan_results.json
Results exported to: network_scan_results.csv
```

## Key Findings from Example

### Critical Issues (Immediate Action Required)
1. **Raspberry Pi (192.168.1.25)** - Telnet enabled (port 23)
   - **Risk:** Anyone on the network can intercept credentials
   - **Action:** Disable Telnet, use SSH with key authentication only

### High Priority Issues
1. **Unknown Device (192.168.1.254)** - RDP exposed (port 3389)
   - **Risk:** Brute force attack target
   - **Action:** Disable RDP or require VPN access

2. **Multiple Devices** - SMB/NetBIOS enabled (ports 139, 445)
   - **Risk:** Common ransomware infection vector
   - **Action:** Disable file sharing or restrict to specific IPs

### Medium Priority Issues
1. **5 IoT Devices** detected on main network
   - **Risk:** IoT devices often have unpatched vulnerabilities
   - **Action:** Move to isolated guest network or VLAN

2. **Unencrypted HTTP** interfaces on several devices
   - **Risk:** Management interfaces accessible without encryption
   - **Action:** Enable HTTPS or restrict to localhost

## JSON Export Example

```json
{
  "metadata": {
    "scan_time": "2025-12-27T14:30:22",
    "network": "192.168.1.0/24",
    "total_devices": 12
  },
  "summary": {
    "total_devices": 12,
    "risk_distribution": {
      "CRITICAL": 1,
      "HIGH": 3,
      "MEDIUM": 4,
      "LOW": 4
    },
    "iot_devices": 5,
    "total_open_ports": 8,
    "most_common_risks": [
      ["HIGH", 4],
      ["MEDIUM", 5],
      ["IoT device detected", 5]
    ]
  },
  "devices": [
    {
      "ip": "192.168.1.25",
      "mac": "DC:A6:32:12:34:56",
      "vendor": "Raspberry Pi",
      "hostname": "raspberrypi.local",
      "open_ports": [22, 23, 80, 445],
      "risk_score": 55,
      "risk_level": "CRITICAL",
      "is_iot": false,
      "findings": [
        "CRITICAL: Telnet (port 23) - Unencrypted remote access",
        "HIGH: SMB (port 445) - File sharing - ransomware vector",
        "MEDIUM: SSH (port 22) - Remote access - ensure strong auth",
        "MEDIUM: HTTP (port 80) - Unencrypted web interface"
      ],
      "recommendations": [
        "Disable Telnet immediately or restrict to localhost only",
        "Restrict SMB access or use VPN/firewall",
        "Restrict SSH access or use VPN/firewall"
      ],
      "open_ports_summary": {
        "critical": [23],
        "high": [445],
        "medium": [22, 80]
      }
    }
  ]
}
```

## CSV Export Example

| IP Address | MAC Address | Vendor | Hostname | Risk Level | Risk Score | Is IoT | Open Ports | Findings | Recommendations |
|------------|-------------|---------|----------|------------|------------|--------|------------|----------|-----------------|
| 192.168.1.25 | DC:A6:32:12:34:56 | Raspberry Pi | raspberrypi.local | CRITICAL | 55 | False | 22, 23, 80, 445 | CRITICAL: Telnet (port 23) - Unencrypted remote access; HIGH: SMB (port 445) - File sharing - ransomware vector | Disable Telnet immediately or restrict to localhost only; Restrict SMB access or use VPN/firewall |
| 192.168.1.254 | 52:54:00:AA:BB:CC | Unknown | Unknown | HIGH | 30 | False | 3389, 445 | HIGH: RDP (port 3389) - Remote desktop exposure; HIGH: SMB (port 445) - File sharing - ransomware vector | Restrict RDP access or use VPN/firewall; Restrict SMB access or use VPN/firewall |
| 192.168.1.20 | E8:FC:AF:11:22:33 | Amazon (Echo/Ring) | echo-kitchen.local | HIGH | 20 | True | 80 | IoT device detected: Amazon (Echo/Ring); MEDIUM: HTTP (port 80) - Unencrypted web interface | Isolate IoT devices on separate VLAN/guest network; Disable remote access/cloud features if not needed |

## Recommended Remediation Steps

Based on this example scan:

### Immediate Actions (Within 24 Hours)
1. **Disable Telnet** on Raspberry Pi - Replace with SSH
2. **Identify Unknown Device** at 192.168.1.254 - Investigate or remove from network
3. **Restrict RDP Access** - Require VPN or disable completely

### Short-Term Actions (Within 1 Week)
1. **Create Guest Network** for IoT devices
   - Move all 5 IoT devices to isolated network
   - Prevent IoT devices from accessing main network

2. **Disable SMB/NetBIOS** on devices that don't need file sharing
   - Or configure firewall rules to restrict to specific IPs

3. **Enable HTTPS** on all web management interfaces
   - Or restrict HTTP access to localhost only

### Long-Term Actions (Ongoing)
1. **Regular Scanning** - Run weekly to detect new devices
2. **Firmware Updates** - Keep all devices patched
3. **Network Segmentation** - Implement VLANs for device isolation
4. **Strong Authentication** - Use key-based auth for SSH, disable passwords
5. **Router Hardening** - Review router security settings

## Network Architecture Recommendation

Based on these findings, recommended network segmentation:

```
┌─────────────────────────────────────────┐
│         Internet                         │
└──────────────┬──────────────────────────┘
               │
        ┌──────▼──────┐
        │   Router    │
        └──┬────┬─────┘
           │    │
    ┌──────▼┐ ┌▼──────────┐
    │ Main  │ │ IoT/Guest │
    │ VLAN  │ │   VLAN    │
    └───┬───┘ └─────┬─────┘
        │           │
    Trusted     IoT Devices
    Devices     (Isolated)
```

**Main VLAN (192.168.1.0/24):**
- Router
- Personal computers/laptops
- Phones/tablets
- Printer

**IoT/Guest VLAN (192.168.2.0/24):**
- Smart speakers (Echo, Nest Hub)
- Smart lights (Philips Hue)
- Smart plugs (TP-Link)
- Security cameras (Ring)
- Smart thermostat (Nest)

**Firewall Rules:**
- IoT VLAN can access Internet only
- IoT VLAN blocked from Main VLAN
- Main VLAN can initiate connections to IoT (for control)
- All VLANs block incoming from Internet (except established connections)

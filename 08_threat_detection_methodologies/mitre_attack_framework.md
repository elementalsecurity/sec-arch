# MITRE ATT&CK Framework

The **MITRE ATT&CK Framework** (Adversarial Tactics, Techniques, and Common Knowledge) is a globally recognized, structured knowledge base of adversary behaviors based on real-world observations. It is designed to help organizations understand how attackers operate, strengthen their detection and defense strategies, and support threat intelligence, security operations, and risk assessments.

---

## Purpose and Scope

The ATT&CK Framework catalogs the **tactics**, **techniques**, and **procedures** (TTPs) adversaries use across the full lifecycle of an intrusion. It emphasizes:

- Real-world adversary behavior over theoretical attacks
- Post-compromise activities (what happens after initial access)
- Continuous updates based on public reporting and security research

ATT&CK is not limited to a single threat model; it supports use cases across enterprise environments, mobile devices, and industrial control systems (ICS).

---

## Structure of ATT&CK

| Component | Description |
|-----------|-------------|
| **Tactics** | The adversary's tactical goal or objective (e.g., Initial Access, Persistence, Lateral Movement) |
| **Techniques** | How adversaries achieve a tactic (e.g., Spearphishing, Credential Dumping, Command and Control) |
| **Sub-techniques** | More detailed refinements of techniques, specifying variations in attacker behavior |
| **Mitigations** | Defensive measures to prevent or detect specific techniques |
| **Detections** | Guidance for identifying techniques through telemetry and analysis |

ATT&CK matrices map these elements visually, providing an organized view of the adversary landscape.

---

## Common Use Cases

- **Threat Intelligence Enrichment**: Aligns incidents to known techniques and groups
- **Detection Engineering**: Prioritizes development of detections for high-risk techniques
- **Security Assessment and Gap Analysis**: Identifies where defensive coverage is strong or lacking
- **Red Team and Purple Team Exercises**: Simulates realistic attack scenarios mapped to techniques
- **Adversary Emulation Plans**: Creates tailored, threat-specific testing plans

---

## Advantages

- **Real-World Focus**: Techniques are derived from active threat campaigns
- **Consistent Language**: Standardizes terminology across intelligence reports and defenses
- **Actionable Insights**: Links tactics and techniques to mitigation and detection strategies
- **Broad Adoption**: Used by governments, commercial organizations, and security vendors worldwide

---

## Limitations

- **Volume of Techniques**: The large number of techniques can overwhelm unprioritized defenders
- **Detection Complexity**: Some techniques are difficult to detect or attribute accurately
- **Focus Area**: Primarily post-compromise; initial access vectors sometimes require supplementary frameworks

---

## Relationship to Other Models

| Framework | Relationship |
|-----------|-------------|
| **Cyber Kill Chain** | ATT&CK refines and expands the actions that occur during each Kill Chain phase |
| **D3FEND** | Provides defensive techniques and countermeasures mapped against ATT&CK tactics |
| **Diamond Model** | Enriches ATT&CK by correlating infrastructure, capabilities, and adversary personas |
| **NIST CSF** | ATT&CK tactics and techniques align to "Detect" and "Respond" functions |

---

## Summary

The **MITRE ATT&CK Framework** is a cornerstone of modern cyber defense. Its emphasis on observable attacker behavior, structured documentation of TTPs, and its broad applicability across operational, intelligence, and governance functions make it essential for security architecture, threat detection, and proactive risk management.

> "You cannot defend what you do not understand. ATT&CK brings adversary behavior into focus for every defender."
> Adapted from the MITRE Corporation

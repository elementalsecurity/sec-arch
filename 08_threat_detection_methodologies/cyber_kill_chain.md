# Cyber Kill Chain Framework

**The Cyber Kill Chain** is a threat model developed by **Lockheed Martin** in 2011 to describe the stages of a cyber attack and identify opportunities to detect, disrupt, or respond at each phase. Inspired by military doctrine, it is structured to help security professionals understand attacker behavior and deploy **defensive strategies** aligned to adversary actions.

---

## Attribution
- **Original Creator**: Lockheed Martin Corporation
- **First Publication**: Intelligence-Driven Computer Network Defense (2011)
- **Authors**: Eric M. Hutchins, Michael J. Cloppert, Rohan M. Amin

---

## The 7 Phases of the Cyber Kill Chain

| Phase | Description | Defensive Opportunities |
|-------|-------------|--------------------------|
| **1. Reconnaissance** | Adversary identifies targets, collects intel (e.g., IPs, emails, org charts) | Detect scanning, social engineering attempts, threat intel monitoring |
| **2. Weaponization** | Combines exploit with payload (e.g., malware, macro) into a deliverable | Threat intel on known toolchains, sandbox analysis, supply chain scrutiny |
| **3. Delivery** | Transmits weaponized payload to target (e.g., phishing, drive-by, USB drop) | Email and web filtering, USB control, endpoint protection |
| **4. Exploitation** | Executes code on the victim's system (e.g., exploiting a vulnerability) | Patch management, vulnerability scanning, behavioral detection |
| **5. Installation** | Installs malware or backdoor for persistence | EDR/AV monitoring, host integrity checks, privilege hardening |
| **6. Command and Control (C2)** | Attacker establishes remote control channel | DNS monitoring, beacon detection, outbound traffic filtering |
| **7. Actions on Objectives** | Adversary achieves goals (e.g., data theft, sabotage, lateral movement) | DLP, UEBA, lateral movement detection, response playbooks |

---

## Strengths of the Kill Chain Model

- Provides **linear attack progression** for blue team strategy
- Emphasizes **prevention and early detection**
- Maps **security controls** to each phase of attacker behavior
- Enables structured incident response and threat hunting

---

## Limitations

- Assumes **linear attack flow** (may not fit modern multi-stage APTs)
- Not ideal for modeling **insider threats** or **post-compromise persistence**
- Lacks granularity compared to frameworks like **MITRE ATT&CK**

---

## Use Cases

- Threat modeling and red team scenario development
- Security control gap analysis
- Purple team and attack simulation planning
- SOC playbook alignment (e.g., response actions by phase)

---

## Integration with Other Models

| Framework | Complementary Role |
|----------|--------------------|
| **MITRE ATT&CK** | Maps TTPs to specific Kill Chain stages |
| **D3FEND** | Defensive countermeasures aligned to attack phases |
| **Diamond Model** | Enriches each phase with adversary capabilities and infrastructure |
| **NIST CSF** | Kill Chain informs Detect/Respond functions |

---

## Summary

The **Cyber Kill Chain** remains a valuable foundation for security operations, detection engineering, and adversary modeling. While modern threats demand more dynamic and layered frameworks, the Kill Chain's **clear structure and operational relevance** make it an enduring tool in any defender's toolkit.

> "Intelligence-driven defense is a necessity and not a luxury." — Hutchins, Cloppert, Amin (Lockheed Martin, 2011)



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

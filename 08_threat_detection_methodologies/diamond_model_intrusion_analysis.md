# Diamond Model of Intrusion Analysis

The **Diamond Model of Intrusion Analysis** is a threat intelligence and intrusion analysis framework introduced in 2013 by **Sergio Caltagirone**, **Andrew Pendergast**, and **Christopher Betz**. It is designed to describe and understand cyber threats through relationships between adversaries, capabilities, infrastructure, and victims.

---

## Attribution
- **Authors**: Sergio Caltagirone, Andrew Pendergast, Christopher Betz
- **First Published**: 2013 via Center for Cyber Intelligence Analysis and Threat Research
- **Paper**: *The Diamond Model of Intrusion Analysis* (2013)

---

## Purpose

- Provide a structured model for **correlating cyber threat events**
- Describe intrusions as **relationships between key elements**
- Enable tracking of adversary campaigns and kill chains
- Support fusion of data for **threat attribution and incident response**

---

## Core Components of the Diamond

At the center of the model is a **cyber event** with an adversary leveraging a capability over infrastructure to affect a victim.

| Vertex | Description |
|--------|-------------|
| **Adversary** | The threat actor conducting the operation (human or organization) |
| **Capability** | Tools or malware used to perform the intrusion (exploit, malware, etc.) |
| **Infrastructure** | Systems used to deliver or control the attack (C2 servers, domains, email accounts) |
| **Victim** | The targeted system, organization, or individual |

### Additional Meta-Features:
- **Timestamp**: When the activity occurred
- **Phase**: Where in the Kill Chain or attack lifecycle the event resides
- **Result**: Outcome of the event (e.g., access granted, data exfiltrated)

---

## Diamond Model Principles

1. **Atomicity**: Each event is atomic and cannot be further subdivided.
2. **Completeness**: Each event has at least two vertices; ideally all four.
3. **Uniqueness**: Each vertex has distinct attributes.
4. **Mutability**: Relationships evolve over time (e.g., adversaries change infrastructure).

---

## Use Cases

- **Threat Intelligence Fusion**: Combine multiple data points across campaigns
- **Intrusion Analysis**: Analyze TTPs and link intrusions to common actors
- **Attribution**: Identify patterns across different campaigns
- **Visualization**: Graph-based correlation of events and actor behavior
- **Kill Chain Integration**: Apply Diamond Model to map intrusion progression

---

## Comparison to Other Models

| Attribute | Diamond Model | MITRE ATT&CK | Cyber Kill Chain |
|----------|----------------|---------------|-------------------|
| Focus | Relational threat analysis | Adversary techniques | Attack stages |
| Structure | Quadrant-based event model | Matrix (Tactics → Techniques) | Linear phases |
| Primary Use | Threat intel and campaign tracking | Detection and response | Response and disruption |
| Granularity | High | Very High | Moderate |

---

## Example

An observed phishing attack might be modeled as:
- **Adversary**: FIN7
- **Capability**: Custom macro-enabled Excel dropper
- **Infrastructure**: Compromised SMTP server
- **Victim**: Finance department of a U.S. retail company

From here, analysts can pivot:
- From victim to other targeted orgs (shared victimology)
- From infrastructure to other domains/IPs used
- From capability to malware families and TTPs

---

## Strategic Benefits for Security Architects and Threat Analysts

- Improve **campaign detection** and adversary profiling
- Drive **threat-informed architecture decisions** (e.g., infrastructure isolation, segmentation)
- Enhance incident response **playbook enrichment and data pivoting**
- Enable deeper **fusion across MITRE ATT&CK, Kill Chain, and intelligence feeds**

---

## Summary

The **Diamond Model** is a powerful analytical tool that helps defenders and intelligence teams frame and correlate complex intrusion events. It complements technical detection frameworks by offering a **strategic, relational view** of threat actor behavior, allowing teams to uncover patterns, infer relationships, and better prepare for future attacks.

> "At the heart of every intrusion event lies a relationship between adversary, infrastructure, capability, and victim. The Diamond Model reveals these links." — Caltagirone, Pendergast, Betz
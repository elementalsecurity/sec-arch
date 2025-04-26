# Threat Hunting Maturity Model (THMM)

The **Threat Hunting Maturity Model (THMM)** is a benchmarking framework created by **David J. Bianco** (of the Pyramid of Pain fame) to evaluate and guide the evolution of an organization’s threat hunting capabilities. It provides a roadmap for moving from reactive to **proactive, intelligence-driven hunting**.

---

## Attribution
- **Creator**: David J. Bianco
- **Affiliation**: Principal Engineer, Mandiant (at time of development)
- **First Presented**: 2015 at SANS Threat Hunting Summit

---

## Purpose

- Provide a **maturity model** for developing a threat hunting program
- Enable **self-assessment and roadmap planning**
- Emphasize the role of **detection gaps, hypothesis testing, and iterative improvement**
- Promote **proactive security** by empowering analysts to discover unknown threats

---

## THMM Levels Overview

| Maturity Level | Description |
|----------------|-------------|
| **Level 0: Initial** | No formal hunting. Entirely reactive. Relies on signature-based alerts. |
| **Level 1: Minimal** | Some manual investigations based on alerts. Little to no hypothesis-driven analysis. |
| **Level 2: Procedural** | Hunting conducted based on predefined procedures and known TTPs. Repeatable, but not adaptable. |
| **Level 3: Innovative** | Hypothesis-driven hunts using threat intelligence and behavioral analytics. Capable of identifying novel threats. |
| **Level 4: Leading** | Fully integrated hunting program with continuous feedback into detection engineering. Uses custom tooling, automation, and cross-team collaboration. |

---

## Key Capabilities by Maturity

| Capability Area | Level 0–1 | Level 2 | Level 3 | Level 4 |
|----------------|-----------|---------|---------|---------|
| Data Coverage | Minimal | Some centralization (e.g., SIEM) | Broad and high-fidelity | Complete telemetry and enrichment |
| Hunting Method | Reactive, alert-based | IOC- and TTP-driven | Hypothesis-driven | Intelligence-led, adaptive |
| Tooling | Manual queries | SIEM queries, scripting | Custom analytics, UEBA | Automation, ML, data science support |
| Integration | Siloed detection | Occasional collaboration | Shared learnings with IR and TI | Full feedback loop into SOC, IR, and dev teams |

---

## Enablers for Advancement

- **Data visibility**: Logs, endpoint telemetry, network flows, DNS, process execution
- **Threat intelligence**: Aligned to MITRE ATT&CK, actor profiles, campaigns
- **Experienced analysts**: Skilled in hypothesis generation and pivoting
- **Infrastructure**: Scalable query tools, custom hunting platforms (e.g., Jupyter, Splunk, Elastic, Azure Sentinel)
- **Metrics**: Track hypotheses, false positives, detection conversion rates

---

## Use Cases for Security Architects

- Guide **SOC capability development** and tool selection
- Identify **detection coverage gaps** through ATT&CK alignment
- Justify investment in **telemetry, enrichment, and behavioral analytics**
- Integrate **hunt feedback into SIEM and EDR tuning workflows**

---

## Related Models

| Model | Relationship |
|-------|-------------|
| **MITRE ATT&CK** | Used to map hunting hypotheses and detection gaps |
| **Cyber Kill Chain** | Informs hunt timing and adversary lifecycle |
| **Diamond Model** | Guides pivoting across actor, infrastructure, and capability |
| **Pyramid of Pain** | Created by same author; emphasizes value of detecting TTPs vs. IOCs |

---

## Summary

The **Threat Hunting Maturity Model (THMM)** provides a structured path from reactive detection to proactive, intelligence-informed hunting. By emphasizing **human-driven, hypothesis-based exploration**, it enables organizations to uncover stealthy threats, inform detection engineering, and evolve into agile, resilient security operations teams.

> "Hunting is the practice of proactively and iteratively searching through networks to detect and isolate advanced threats that evade existing security solutions." — David J. Bianco

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

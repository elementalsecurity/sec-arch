# Case Study: Detection Pipeline Architecture for Hybrid Infrastructure

## Context and Business Problem
A multinational logistics company with both legacy data centers and cloud-native services lacked consistent visibility into security events across its environments. The internal SOC team relied on fragmented log sources, outdated SIEM rules, and manual triage. Leadership demanded better threat detection coverage, faster response times, and alignment to MITRE ATT&CK.

The goal was to architect a modern, scalable detection and response pipeline that ingested telemetry from cloud, endpoint, identity, and network layers while supporting threat hunting and automated remediation.

---

## Architecture Requirements
- Centralized ingestion and normalization of security logs and telemetry
- Real-time alerting mapped to MITRE ATT&CK techniques
- Low-latency, high-volume data processing to support hybrid workloads
- Custom rule development, enrichment, and triage workflows
- Integration with SOAR and ticketing for automated response
- Role-based access controls and auditability for compliance (SOX, PCI DSS)

---

## Constraints and Risks
- Telemetry volume exceeded 500 GB/day across cloud and on-prem
- Inconsistent logging configurations on Linux, Windows, and Kubernetes nodes
- EDR deployed on 60% of endpoints with variable telemetry depth
- Legacy systems using Syslog only with no native API support
- Strict data residency requirements in the EU for specific business units

---

## Security Strategy

### Telemetry Ingestion
- Deployed **Elastic Beats** and **Fluent Bit** agents to forward logs from Windows, Linux, and containerized environments
- Ingested Azure, AWS, and on-prem logs through **Logstash** and **Azure Event Hub** connectors
- Enabled audit and diagnostic logging across Entra ID, Defender for Endpoint, AWS CloudTrail, and Palo Alto NGFWs

### Data Normalization and Enrichment
- Parsed logs using Elastic Common Schema (ECS) and Sigma-compatible mappings
- Enriched logs with threat intel from MISP and Recorded Future via REST APIs
- Annotated identity-based events with department tags from Entra ID

### Detection Engineering
- Built custom KQL and Elasticsearch rules mapped to ATT&CK (e.g., T1059.001 – PowerShell Execution)
- Used Jupyter Notebooks for hypothesis-driven threat hunting
- Created detection-as-code pipelines using GitHub Actions and Sigma rulesets
- Mapped detection rules to coverage tiers (critical, high-fidelity, investigative, noise-prone)

### Response and Automation
- Integrated Elastic and Microsoft Sentinel with **Cortex XSOAR**
- Built SOAR playbooks for:
  - Phishing triage and user notification
  - Suspicious login correlation across Entra ID, endpoint, and email telemetry
  - Isolation of compromised hosts using Defender APIs
- Automatic case creation in Jira for triaged alerts with contextual enrichment

### Compliance and Auditability
- Role-based access control enforced within Kibana and Sentinel for SOC, Audit, and Engineering
- Immutable log storage configured with 12-month retention and export to Azure Archive
- Alert logic, rule changes, and suppression lists version-controlled in GitHub

---

## Control Framework Mapping

| Category | Controls Implemented |
|----------|----------------------|
| Logging | ECS, audit logging, Azure diagnostics, EDR telemetry |
| Detection | Custom ATT&CK-mapped rules, enrichment, threat intel feeds |
| Response | SOAR playbooks, automated host isolation, user alerting |
| Governance | RBAC, change control, audit trails, immutable log retention |
| Compliance | PCI DSS 10.x, SOX logging, NIST IR controls |

---

## Outcome and Lessons Learned

- Reduced average triage time from 27 minutes to 6 minutes per alert
- Improved alert fidelity with enriched detections, reducing false positives by 35%
- Mapped 73 MITRE ATT&CK techniques across detection tiers with live dashboards
- Shifted the SOC from a reactive posture to proactive hunting on a weekly cadence
- Enabled faster containment of credential-based attacks through SSO correlation logic

### Lessons Learned
- Detection rules are not one-size-fits-all with tiered use case classification helped align effort to value
- Enrichment is key with contextual metadata (identity, location, process lineage) reduced analyst fatigue
- Tooling matters less than structure and the pipeline must be resilient, documented, and iterated

---

## Summary
This case study demonstrates the design of a detection pipeline that transforms fragmented telemetry into actionable insights. By aligning detection engineering to business risk and operational scale, the security team moved from log aggregation to threat-informed defense. Architects play a critical role in ensuring data structure, detection logic, and response automation are coordinated and adaptable.


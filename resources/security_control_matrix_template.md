# Security Control Matrix Template (Baseline Structure)

This document provides a reusable structure for mapping **threats to controls**, **framework requirements to implementations**, and **gaps to remediation plans**. It is designed to support Security Architects, GRC teams, and Engineers during system assessments, control rationalization, or framework alignment activities.

Use this matrix to:
- Build a control library across architectures
- Conduct gap analysis for compliance or risk assessments
- Track implementation status and ownership across domains

---

## Template Columns

| Control ID | Control Description | Mapped Threat(s) | Control Category | Framework(s) | Implementation Status | Owner | Notes |
|------------|----------------------|------------------|------------------|----------------|------------------------|--------|-------|
| CTRL-001 | Enforce MFA for all administrative accounts | Credential Theft, Privilege Escalation | Identity | NIST AC-7, CIS 6.2, ISO 9.4.2 | Implemented | IAM Team | Configured via Entra ID + conditional access |
| CTRL-002 | Encrypt sensitive data at rest using platform-native KMS | Data Theft, Compliance Violation | Data Security | PCI 3.4, NIST SC-12, ISO 10.1.1 | In Progress | Cloud Security | Awaiting CMK policy rollout on AWS |
| CTRL-003 | Implement EDR across all endpoints | Malware, Lateral Movement | Endpoint Security | CIS 8.2, MITRE T1059 | Planned | Endpoint Ops | Deployment delayed for legacy OS version support |

---

## Suggested Control Categories
- Identity & Access Management
- Data Security & Privacy
- Application Security
- Network Security
- Endpoint Security
- Cloud & Infrastructure
- Logging & Monitoring
- Threat Detection & Response
- Governance & Compliance

---

## Suggested Framework References
You may wish to align each control with multiple frameworks:
- **NIST SP 800-53 Rev 5**
- **ISO/IEC 27001:2022 Annex A**
- **PCI DSS 4.0.1**
- **SOC 2 Trust Services Criteria**
- **CIS Critical Security Controls v8**
- **MITRE ATT&CK Techniques (T#)**

---

## How to Use This Template
1. Create a copy per system or environment (e.g., public cloud, POS network, SaaS platform)
2. Populate the control descriptions and map threats using STRIDE, PASTA, or ATT&CK
3. Reference overlapping framework citations for audit alignment
4. Track implementation phases and assign owners for accountability
5. Periodically review this matrix as part of risk assessments or architectural reviews

> "Your control matrix should not be static. It should evolve with your architecture, your adversaries, and your business."


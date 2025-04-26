# Security Domains

This section introduces the **core security domains** that every Security Architect must understand and design for. Each domain represents a functional area where specific risks emerge, and where tailored controls, policies, and design patterns must be applied.

These domains are not silos — they intersect constantly in modern architectures. A strong Security Architect knows how to design across domains, ensuring that identity supports data protection, that network controls reinforce cloud segmentation, and that governance is built into every layer.

---

## What You'll Learn in This Section
- The purpose and scope of each security domain
- Common threats, risks, and architectural concerns
- Best practices and controls aligned to each area
- How these domains relate to compliance and business outcomes

This section provides the building blocks for cross-domain architectural thinking.

---

## Contents

| File | Description |
|------|-------------|
| `identity_and_access_management.md` | Covers authentication, authorization, federation, and privileged access【411†identity_and_access_management.md】 |
| `infrastructure_security.md` | Focuses on securing foundational systems, hypervisors, and compute layers【412†infrastructure_security.md】 |
| `network_security.md` | Details zoning, segmentation, firewalls, IDS/IPS, and zero trust network design【413†network_security.md】 |
| `application_security.md` | Explains how to secure software design, SDLC, APIs, and web interfaces【414†application_security.md】 |
| `cloud_security.md` | Covers cloud-native risks, control responsibilities, and architecture patterns across AWS, Azure, GCP【415†cloud_security.md】 |
| `compliance_governance.md` | Outlines the role of security policy, control frameworks, and auditability in architectural governance【416†compliance_governance.md】 |
| `data_security_privacy.md` | Focuses on encryption, classification, DLP, and regulatory compliance (e.g., GDPR)【417†data_security_privacy.md】 |
| `endpoint_security.md` | Details protections for end-user devices, EDR, configuration hardening, and endpoint compliance【418†endpoint_security.md】 |

---

## How to Use This Section
- Use this section to explore individual domains where you may need deeper understanding
- Cross-reference these with the Tools, Case Studies, and Frameworks sections for context
- Apply these concepts to architecture review boards, control design, or maturity assessments

> "Security Architecture is not just about what you protect... It’s about where, how, and why you protect it. Domains give you the map."
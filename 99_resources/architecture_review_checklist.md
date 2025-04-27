# Architecture Review Checklist

Use this checklist to guide structured security architecture reviews during project planning, solution onboarding, or major infrastructure changes. It is designed to surface high-impact risks, control gaps, and design flaws early in the system lifecycle.

---

## Identity and Access Management
- [ ] Are authentication mechanisms (e.g., SSO, MFA) clearly defined?
- [ ] Is least privilege enforced through RBAC, ABAC, or policies?
- [ ] Are privileged accounts isolated and governed (PAM)?
- [ ] Are dormant or orphaned accounts addressed?
- [ ] Is federation used securely across tenants or partners?

## Network Security
- [ ] Is the system segmented from other environments using zoning or VPCs?
- [ ] Are firewall rules and security groups defined per application?
- [ ] Is egress restricted to only necessary destinations?
- [ ] Are network flows encrypted (TLS 1.2+, IPsec, mTLS)?
- [ ] Are VPNs or Zero Trust solutions enforced for remote access?

## Application and Data Security
- [ ] Are input validation, encoding, and output sanitization in place?
- [ ] Is encryption at rest and in transit implemented for sensitive data?
- [ ] Are secrets managed using a vault or dynamic credentials?
- [ ] Are APIs protected via authentication and rate limiting?
- [ ] Is the application scanned with SAST, DAST, or SCA tools?

## Cloud and Infrastructure
- [ ] Is infrastructure provisioned using Infrastructure as Code (IaC)?
- [ ] Are cloud roles, policies, and trust boundaries reviewed?
- [ ] Are logging, monitoring, and alerting integrated with SIEM?
- [ ] Are ephemeral workloads used where possible to reduce persistence risk?
- [ ] Are hardcoded credentials and shared admin accounts avoided?

## Monitoring, Detection, and Response
- [ ] Are security logs collected and normalized (e.g., via SIEM)?
- [ ] Are detection rules aligned with MITRE ATT&CK or relevant TTPs?
- [ ] Is alert triage integrated with ticketing or SOAR platforms?
- [ ] Are thresholds defined for unusual behavior or policy violations?
- [ ] Are runbooks defined for common incident types?

## Compliance and Governance
- [ ] Does the design align with applicable frameworks (e.g., NIST, PCI, ISO)?
- [ ] Are data residency and privacy regulations addressed?
- [ ] Is a risk register or exceptions log being maintained?
- [ ] Are reviews documented and version-controlled?
- [ ] Is there a control ownership map for ongoing assurance?

## Business Continuity and Resilience
- [ ] Are RTO/RPO targets defined and tested?
- [ ] Is there automated backup and recovery for critical assets?
- [ ] Can the system degrade gracefully under partial failure?
- [ ] Are failover or regional recovery mechanisms in place?

## Finalization and Sign-Off
- [ ] Were all stakeholder teams involved (Security, Infra, Product, GRC)?
- [ ] Are key architecture diagrams archived and accessible?
- [ ] Has the project passed security gate criteria for go-live?

---

> This checklist should evolve with your organization's architecture maturity. Customize it to reflect the standards and threats relevant to your environment.



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

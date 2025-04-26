# Control Placement in ARCH-Based Security Design

## Purpose

This document provides guidance on how to strategically place security controls within system architectures, directly aligned to the principles of the ARCH Model — Asymmetric Resilient Cybersecurity Hardening.

Effective control placement is critical to achieving layered defenses, maximizing adversary friction, and maintaining operational resilience. Poorly placed controls lead to blind spots, excessive complexity, or easily bypassed defenses.

Security architects must design control layers intentionally, guided by adversary paths, critical asset locations, and system trust boundaries.


## Principles of Control Placement in ARCH

### 1. Defense-in-Depth with Asymmetry
- Layer controls so that each layer raises attacker cost, detection likelihood, or containment effectiveness.
- Avoid flat, single-point defenses that adversaries can bypass with minimal effort.

### 2. Trust Boundary Enforcement
- Place authentication, authorization, encryption, and monitoring controls at every trust boundary crossing.
- Assume no implicit trust between internal systems unless explicitly validated.

### 3. Attack Path Disruption
- Position controls where they disrupt likely adversary movement, privilege escalation, or data exfiltration paths.
- Use deception, access friction, and lateral movement barriers proactively.

### 4. Resilience Over Rigidity
- Design controls that support graceful degradation rather than creating single points of failure.
- Prefer stateless, distributed enforcement points where possible.

### 5. Simplicity and Maintainability
- Place controls where they can be consistently deployed, monitored, and updated without excessive operational burden.
- Reduce exceptions and special cases that complicate enforcement.


## Control Placement Layers

Security architects should think about control placement across multiple system layers, each contributing to overall resilience.

### 1. Identity Layer
- Strong authentication (e.g., MFA) at every user and system access point.
- Role-based access control (RBAC) or attribute-based access control (ABAC) for authorization.
- Session management, credential rotation, and least privilege enforcement.

### 2. Data Layer
- Data classification and segmentation.
- Encryption at rest and in transit.
- Data loss prevention (DLP) controls.
- Access governance and data masking.

### 3. Application Layer
- Secure development practices embedded into SDLC.
- Input validation, output encoding, and secure session handling.
- Application firewalls and runtime protection (e.g., RASP).

### 4. Infrastructure Layer
- Hardened system images and configuration baselines.
- Network segmentation, bastion hosts, and secure administrative access channels.
- Immutable infrastructure and ephemeral resource deployment.

### 5. Network Layer
- Segmentation of zones based on trust and criticality.
- Network intrusion detection and prevention systems (IDS/IPS).
- Deception technologies (honeypots, canary accounts).
- Encrypted communications using secure protocols.


## Example: Applying Control Placement to Secure a Cloud Environment

| Layer | Example Control Placement |
|:------|:---------------------------|
| Identity | Enforce SSO with MFA for all console and API access. |
| Data | Encrypt S3 buckets with KMS-managed keys and audit access logs. |
| Application | Deploy WAF policies to protect APIs from injection attacks. |
| Infrastructure | Use hardened AMIs with CIS benchmarks and automated compliance checks. |
| Network | Create private subnets with strict security group rules and centralized flow logging. |


## Common Control Placement Pitfalls

- Placing controls only at the perimeter and ignoring internal movement.
- Overlapping controls excessively without clear justification.
- Introducing brittle dependencies that undermine resilience.
- Sacrificing simplicity, leading to unmanageable configurations.


## Conclusion

Control placement is not an afterthought in security architecture. It is a strategic design activity that directly supports the ARCH Model's goals of raising attacker cost, improving system resilience, and simplifying secure operations.

By thinking in layers, enforcing trust boundaries, disrupting attack paths, and maintaining operational simplicity, security architects create environments that are adversary-aware, resilient, and sustainable.


---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

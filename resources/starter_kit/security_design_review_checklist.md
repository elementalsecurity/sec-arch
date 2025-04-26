# Security Design Review Checklist

Use this checklist during architecture and design reviews to surface security risks early and ensure key controls are considered.

---

# Project and System Context

- [ ] System description and scope are clearly defined.
- [ ] Key assets, data types, and critical business functions are identified.
- [ ] Data sensitivity classification is documented.
- [ ] Regulatory, compliance, and contractual obligations are considered.

---

# Authentication and Authorization

- [ ] Authentication mechanisms are appropriate for users, services, and APIs.
- [ ] Multi-Factor Authentication (MFA) is enforced where required.
- [ ] Authorization models (RBAC, ABAC, etc.) are defined and consistently applied.
- [ ] Least privilege principles are enforced.
- [ ] Session management is secure and includes expiration and revocation.

---

# Data Protection

- [ ] Data at rest is encrypted where appropriate.
- [ ] Data in transit is encrypted using modern protocols (TLS 1.2+).
- [ ] Sensitive data fields are masked, tokenized, or redacted when needed.
- [ ] Secure key management practices are defined and applied.
- [ ] Data retention, archival, and destruction policies are defined.

---

# Secure Communication and Integration

- [ ] All external communications use secure channels.
- [ ] APIs enforce authentication, authorization, rate limiting, and input validation.
- [ ] Third-party service integrations are risk assessed and contractually governed.

---

# Application and System Security

- [ ] Input validation and output encoding are applied to prevent injection attacks.
- [ ] Error handling avoids leaking sensitive information.
- [ ] Logging and monitoring are in place for critical security events.
- [ ] Secrets are not hardcoded; secrets management systems are used.
- [ ] Third-party components are tracked and updated regularly.

---

# Threat Modeling and Risk Analysis

- [ ] Threat modeling is conducted for critical components.
- [ ] High-risk threats are identified, prioritized, and mitigated.
- [ ] Design includes compensating controls for known limitations.

---

# Resilience and Recovery

- [ ] Availability requirements are defined and supported (e.g., redundancy, failover).
- [ ] Backup and recovery procedures are tested and validated.
- [ ] Incident response considerations are built into the design.

---

# Governance and Compliance Alignment

- [ ] Security architecture aligns with enterprise policies and standards.
- [ ] Design artifacts (diagrams, threat models, ADRs) are archived and version-controlled.
- [ ] Privacy requirements (GDPR, CCPA, etc.) are addressed if applicable.

---

*Security design reviews are not about finding every flaw. They are about building systems that are resilient, risk-informed, and continuously improvable.*
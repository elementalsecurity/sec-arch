# SOC 2 Framework: Type I, Type II, and Type III Explained

**SOC 2 (System and Organization Controls 2)** is a framework developed by the **American Institute of Certified Public Accountants (AICPA)** to evaluate and report on the design and operating effectiveness of an organization’s internal controls related to data security, availability, processing integrity, confidentiality, and privacy.

It is primarily relevant to **technology and SaaS companies** that manage or store customer data in the cloud.

---

## Purpose of SOC 2

- Demonstrate to customers and stakeholders that a service organization has appropriate internal controls
- Assure third-party data protection, risk management, and compliance practices
- Facilitate B2B trust, due diligence, and vendor onboarding in regulated industries

---

## Trust Services Criteria (TSC)
SOC 2 audits are based on one or more of the following five TSCs defined by AICPA:

| Trust Service Criteria | Description |
|------------------------|-------------|
| **Security** (Required) | Protection against unauthorized access |
| **Availability** | System availability for operation and use as committed |
| **Processing Integrity** | System processing is complete, valid, accurate, and timely |
| **Confidentiality** | Protection of sensitive information (e.g., business secrets, contracts) |
| **Privacy** | Collection, use, retention, and disposal of personal information in line with privacy policies and laws |

Most organizations include **Security + 1–2 additional criteria** based on business needs.

---

## Types of SOC 2 Reports

### SOC 2 Type I
- Evaluates the **design** of controls at a point in time
- Answers: "Are the controls suitably designed as of a specific date?"
- Best for: Early-stage or first-time audits

### SOC 2 Type II
- Evaluates the **operating effectiveness** of controls over a period of time (typically 3–12 months)
- Answers: "Are the controls functioning as intended over time?"
- Best for: Mature companies and recurring customer assurance

### SOC 2 Type III *(less common)*
- Public-facing summary report intended for broader audiences (e.g., marketing use)
- Provides general assurance **without confidential details** of the full Type I/II reports

---

## SOC 2 Report Contents

1. **Management Assertion**
2. **Independent Auditor's Opinion** (unqualified, qualified, or adverse)
3. **System Description** (business model, infrastructure, people, policies, procedures)
4. **Tests of Controls**
   - Control Objectives
   - Test procedures
   - Results of testing
5. **Optional Appendices** (e.g., subservice organizations, complementary user entity controls)

---

## SOC 2 vs. Other SOC Reports

| Report Type | Focus | Audience |
|-------------|-------|----------|
| **SOC 1** | Financial controls (e.g., payroll, ERP systems) | Auditors, regulators |
| **SOC 2** | Trust Services Criteria (Security, Availability, etc.) | Customers, partners |
| **SOC 3** | Public summary of SOC 2 Type II | Marketing, general public |

---

## Key Roles in a SOC 2 Program

- **Control Owners**: Implement and maintain daily operations
- **Compliance/GRC Team**: Manage evidence collection, policy maintenance, and audits
- **Security Architects**: Design control systems and monitor risk surfaces
- **External Auditor (CPA firm)**: Conduct independent review and issue formal report

---

## Common SOC 2 Controls

### Organizational
- Acceptable Use and Security Policies
- Incident Response Plan
- Risk Assessment and Vendor Due Diligence

### Logical & Physical Access
- Role-based access control (RBAC)
- Termination and access review procedures
- MFA enforcement

### Change Management
- SDLC with peer code review and CI/CD pipeline control
- Automated deployment approvals and rollback procedures

### Monitoring
- SIEM/EDR deployment and alerting
- Daily log reviews, weekly risk committee meetings

### Backup & Availability
- Daily offsite backups
- DR/BCP testing at least annually

---

## Timeline for SOC 2 Type I & Type II

| Phase | Duration | Description |
|-------|----------|-------------|
| Readiness Assessment | 1–2 months | Identify gaps and prepare for audit |
| SOC 2 Type I | ~2 weeks | Evaluate control design |
| Observation Period (Type II) | 3–12 months | Evidence must accumulate |
| SOC 2 Type II Audit | 4–6 weeks | Independent assessment |
| Remediation (if needed) | Varies | Fix control failures and retest |

---

## Tools That Support SOC 2 Readiness

- **GRC Platforms**: Vanta, Drata, Secureframe, Tugboat Logic
- **Ticketing and CI/CD**: Jira, GitHub, GitLab, Azure DevOps
- **Security Stack**: Okta, AWS IAM, Datadog, Splunk, SentinelOne, CrowdStrike

---

## Strategic Value of SOC 2 for Security Architects

Security Architects play a key role by:
- Designing control-aligned technical architectures
- Mapping infrastructure and SaaS workflows to TSC criteria
- Building reusable automation and logging pipelines for evidence collection
- Selecting tools that support audit trails, alerting, and granular access control
- Ensuring business continuity, DR, and incident management plans align with availability and security objectives

---

## Summary

SOC 2 is a cornerstone of modern B2B trust. While Type I validates design and Type II proves real-world execution, the responsibility for continuous control maturity rests with internal teams, especially the Security Architects (they're the weirdos you can't live without). A well-planned SOC 2 program not only satisfies auditors but accelerates deals, de-risks your architecture, and earns customer trust.



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

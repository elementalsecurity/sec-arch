# Architecture Review Report Template

This template provides a standardized structure for documenting the results of a Security Architecture Review.

The report captures the system design context, key findings, risk assessments, recommendations, and risk ownership decisions. It serves as a record of security engagement in technical initiatives and supports future audits, compliance needs, and continuous improvement.

---

## Project Information

- **Project Name:**
- **System or Application Name:**
- **Business Owner:**
- **Technical Lead / Architect:**
- **Review Date:**
- **Security Architect(s) Conducting Review:**

---

## Review Scope and Objectives

- **Scope Summary:**
  (Brief description of what was reviewed: new system, major change, integration, decommissioning)

- **Primary Objectives:**
  (Example: validate design against security requirements, identify critical risks, assess regulatory compliance alignment)

---

## Architecture Artifacts Reviewed

- [ ] High-Level Architecture Diagram
- [ ] Data Flow Diagram (DFD)
- [ ] Network Topology
- [ ] Identity and Access Flows
- [ ] Threat Model (if available)
- [ ] Others (Specify)

---

## Key Findings and Recommendations

| Area | Finding | Risk Level (Critical, High, Medium, Low) | Recommendation |
|:-----|:--------|:-----------------------------------------|:---------------|
| Identity and Access | Example: No MFA on admin accounts | High | Enforce MFA for all privileged access |
| Data Protection | Example: Sensitive data stored unencrypted | Critical | Encrypt data at rest using approved KMS |
| Network Security | Example: Flat network, no segmentation | High | Implement VLAN segmentation and firewalls |
| Application Security | Example: Missing input validation on APIs | Medium | Add server-side input validation checks |
| Cloud Security | Example: Unrestricted S3 bucket access | Critical | Apply least privilege access policies |
| Threat Detection | Example: No centralized log collection | Medium | Forward critical logs to SIEM with integrity controls |

*(Add more rows as needed.)*

---

## Residual Risks and Risk Acceptance

- **Residual Risks Identified:**
  (Summarize any risks that will remain open after recommended actions are taken.)

- **Risk Owners:**
  (Identify individuals or teams accepting responsibility for residual risks.)

- **Documented Risk Acceptance:**
  - [ ] Risk Acceptance Form Signed (attach if applicable)
  - [ ] Risk Owner Approval Recorded

---

## Next Steps and Action Items

| Action Item | Owner | Due Date | Status |
|:------------|:------|:---------|:-------|
| Example: Implement MFA for administrative users | IT Security | 2024-09-15 | In Progress |
| Example: Encrypt sensitive S3 buckets | Cloud Team | 2024-09-30 | Not Started |

*(Add more rows as needed.)*

---

## Review Closure Summary

- **Overall Security Posture Rating:**
  (Secure, Minor Issues, Moderate Risk, Significant Risk)

- **Notes:**
  (Summary of strengths observed, concerns, lessons learned, or recommendations for future improvements.)

- **Security Architecture Review Completed By:**
  (Name and title of lead reviewer)

- **Date of Report Submission:**

---

*Architecture Review Reports are critical artifacts for demonstrating that security was proactively evaluated and integrated into system designs. They provide transparency, accountability, and a foundation for continuous improvement.*

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

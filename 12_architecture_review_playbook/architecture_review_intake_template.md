# Architecture Review Intake Template

This intake form is used to collect essential information before scheduling and conducting a Security Architecture Review.

Completing this form helps ensure that the review is scoped appropriately, that stakeholders are identified early, and that the security team can prepare a targeted, efficient review.

Project owners or designated technical leads should complete this form and submit it as part of the Architecture Review Request process.

---

## Project Overview

- **Project Name:**
- **Business Owner:**
- **Technical Lead / Architect:**
- **Project Manager (if applicable):**
- **Contact Email(s):**

---

## System Purpose and Description

- **Brief description of the system, application, or service:**
- **Primary business function(s) supported:**
- **Is this a new system, a significant change, an integration, or a decommissioning?**

---

## Data Classification and Compliance Impact

- **Will the system process, store, or transmit any of the following?** (Select all that apply)
  - [ ] Personally Identifiable Information (PII)
  - [ ] Payment Card Information (PCI DSS scope)
  - [ ] Protected Health Information (PHI / HIPAA scope)
  - [ ] Regulated data (GDPR, CCPA, SOX, etc.)
  - [ ] Company confidential or proprietary data
  - [ ] Public data only

- **Are there any specific compliance or regulatory requirements applicable to this project?**

- **What is the highest sensitivity level of data handled?** (Confidential, Internal, Public)

---

## Deployment and Hosting Information

- **Deployment Model:** (Select all that apply)
  - [ ] On-Premises
  - [ ] Private Cloud
  - [ ] Public Cloud (AWS, Azure, GCP)
  - [ ] Hybrid
  - [ ] SaaS

- **Major external service providers involved:**

- **Are any third-party integrations planned?** (Briefly describe)

---

## Architecture Artifacts (Required for Review)

Please attach or link the following artifacts if available:
- [ ] High-Level Architecture Diagram
- [ ] Data Flow Diagram (DFD)
- [ ] Network Topology (if applicable)
- [ ] Identity and Access Flows (SSO, MFA, RBAC mappings)
- [ ] Threat Model (optional but recommended)
- [ ] List of known dependencies or shared services

---

## Key Risk Drivers and Business Considerations

- **What business risks would a security failure introduce?**
  (For example: financial loss, regulatory penalty, brand damage, customer impact)

- **What is the expected go-live date or major project milestones?**

- **Are there any known concerns or focus areas for the security review?**

---

## Stakeholders for the Review Session

- **Primary Participants:**
  (List names and roles)

- **Executive Sponsor (if needed):**

- **Expected duration and preferred dates for the review:**

---

*Providing complete and accurate intake information improves the quality and relevance of the security architecture review, and helps ensure risks are identified and addressed before they become issues.*

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

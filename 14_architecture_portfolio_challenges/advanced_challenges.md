# Advanced Challenges

This document presents advanced-level portfolio challenges for Security Architects who are ready to practice handling complex, multi-domain design problems.

Each exercise simulates real-world ambiguity, competing priorities, and the need for structured, risk-based decision making.

Document your work clearly, with attention to:
- Assumptions made
- Risks identified
- Tradeoff decisions
- Architecture diagrams
- Recommendations for governance and operationalization

---

## Challenge 1: Multi-Cloud Secure Data Lake Design

**Scenario:**
A global enterprise wants to create a centralized data lake pulling customer, transaction, and operational data from AWS, Azure, and on-premises sources.

**Task:**
- Design a secure data ingestion, storage, and access model.
- Define how encryption, identity management, and segmentation will be handled across clouds.
- Identify at least five major risks and propose mitigations.
- Describe how you would document and monitor compliance with GDPR and CCPA requirements.

---

## Challenge 2: Secure SaaS Platform for B2B Clients

**Scenario:**
Your company is launching a multi-tenant SaaS platform for business clients that will process sensitive financial data.

**Task:**
- Propose a high-level secure multi-tenant architecture.
- Define tenant isolation strategies.
- Design a secure onboarding and offboarding process.
- Document how you would align your design to SOC 2 Type 2 requirements.

---

## Challenge 3: Secure M&A Identity Federation

**Scenario:**
Following an acquisition, two companies need to establish identity federation between Azure Active Directory environments within 60 days, without fully merging user directories immediately.

**Task:**
- Propose a secure, minimal-trust federation model.
- Define authentication and authorization strategies across domains.
- Document temporary vs long-term controls for access.
- Identify major risks and compliance concerns.

---

## Challenge 4: Global E-Commerce Platform Threat Model

**Scenario:**
You are tasked with building a threat model for a global e-commerce platform that supports customers in 30 countries, with regional data centers.

**Task:**
- Identify at least six major threat categories.
- Map threats across customer, application, network, and backend layers.
- Propose security controls at different layers to mitigate key threats.
- Highlight compliance, localization, and data sovereignty risks.

---

## Challenge 5: Incident-Resilient Cloud Architecture

**Scenario:**
A mission-critical healthcare application must be hosted in the public cloud with high resilience against cyberattacks, operational failures, and cloud service disruptions.

**Task:**
- Design a cloud architecture focused on resilience.
- Include incident detection, containment, and recovery mechanisms.
- Address ransomware scenarios, insider threat scenarios, and cloud provider failure scenarios.
- Propose monitoring and logging strategies aligned to HIPAA and NIST SP 800-53 requirements.

---

*Advanced challenges prepare you to think deeply, reason across technical and business domains, and lead complex security designs. They are stepping stones toward becoming a trusted advisor and strategic Security Architect.*

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

# Learning Roadmap for Aspiring Security Architects

This roadmap is designed to guide aspiring Security Architects through a progressive learning journey, from foundational concepts to architectural mastery. Security Architecture requires more than technical acumen; it demands the ability to **integrate security principles into design**, **balance risk with usability**, and **guide enterprise-level decisions**.

This document outlines staged learning goals, core competencies, and curated topics to build the mindset, skillset, and toolset of a capable Security Architect.

---

## Stage 1: Foundation (0–2 years)
**Goal:** Build broad literacy across IT, networking, and security fundamentals.

### Key Topics
- TCP/IP, DNS, HTTP/S, routing, VLANs
- Windows and Linux administration
- Cloud platform basics (AWS, Azure, GCP)
- Identity and authentication (MFA, RBAC)
- CIA triad, threat types, basic cryptography
- Common tools: Wireshark, Nmap, Burp Suite (Community), Splunk, Nessus

### Suggested Learning
- **CompTIA Security+**
- TryHackMe or Hack The Box beginner tracks
- Microsoft Learn: Azure Security Fundamentals
- YouTube channels (e.g., NetworkChuck, John Hammond)

### Hands-On Practice
- Build a home lab with pfSense, Kali Linux, and Windows VM
- Use cloud free tiers to experiment with IAM, VPC, and compute instances

---

## Stage 2: Practitioner (2–5 years)
**Goal:** Deepen technical knowledge and begin aligning to architectural thinking.

### Key Topics
- Threat modeling and the STRIDE methodology
- Secure SDLC and DevSecOps fundamentals
- Network segmentation, firewalls, VPNs, IDS/IPS
- Cloud IAM, policy-as-code, shared responsibility
- Endpoint security, patch management, vulnerability scanning
- Introduction to Zero Trust and layered defense models

### Suggested Learning
- **CISSP** (broad body of knowledge)
- **Microsoft SC-100 or AWS Certified Security Specialty**
- **SANS SEC530 / GDSA** (for defensible architecture design)

### Hands-On Practice
- Create threat models using OWASP Threat Dragon or Microsoft TM Tool
- Build IaC with Terraform or Bicep for secure cloud configurations
- Scan infrastructure with tools like Checkov, tfsec, or Trivy

---

## Stage 3: Design-Focused Specialist (5–8 years)
**Goal:** Develop capability in designing secure systems and guiding control implementation.

### Key Topics
- Architecture frameworks (SABSA, TOGAF, NIST 800-160)
- Identity architecture: Federation, SSO, Entra, Okta, SailPoint
- Security data pipelines: SIEM, SOAR, log ingestion, UEBA
- Application architecture: secure microservices, API gateways
- Governance models: PCI DSS, NIST CSF, ISO 27001, GDPR

### Suggested Learning
- **CISSP-ISSAP** (architectural design focus)
- **SABSA Foundation or Practitioner**
- **CCSP** (cloud security design)
- **NIST Cybersecurity Framework Practitioner**

### Practice Projects
- Create a reference architecture diagram for a secure SaaS platform
- Build a security standards catalog for a DevOps environment
- Map detection coverage to MITRE ATT&CK techniques

---

## Stage 4: Strategic Architect (8+ years)
**Goal:** Lead architectural design, align to business goals, and drive security strategy.

### Key Topics
- Security governance integration with enterprise architecture
- Security services catalog development and operating models
- Executive communication, risk articulation, roadmap creation
- Controls rationalization and capability maturity models (e.g., NIST CSF Tiers)
- Cross-functional security planning across cloud, network, and identity

### Suggested Learning
- **GDSA** (GIAC Defensible Security Architecture)
- **SABSA Advanced / SCF (Strategic Control Frameworks)**
- **CRISC / CISM** for governance and leadership alignment

### Executive-Level Activities
- Design enterprise-wide security reference architectures
- Lead architecture review boards (ARBs)
- Align security strategy to business initiatives and compliance goals

---

## Optional Deep-Dive Domains (Throughout)
Choose 1–2 areas of deep specialization:
- Cloud-native security (Kubernetes, CSPM, CNAPP)
- Identity governance and zero trust (SSO, MFA, PAM)
- AppSec (SAST, DAST, threat modeling, DevSecOps)
- OT/ICS security (if in manufacturing/energy sectors)
- Data protection and privacy architecture (DLP, masking, encryption at rest/in transit)

---

## Portfolio Milestones
Throughout this journey, build tangible artifacts:
- Threat models and control matrices
- Architecture diagrams (cloud, hybrid, application)
- GitHub repos with secure IaC, detection rules, policy-as-code
- Documentation: risk assessments, standards, security gates

---

## Summary
Security Architecture is a discipline of depth and breadth. This roadmap is not linear—but if followed with intention, it helps you:
- Establish foundational literacy
- Specialize in your core domains
- Think like a designer, not just a defender
- Present security as a strategic enabler

> "An architect sees the forest, the trees, and the roots... Then aligns them all to a purpose."

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

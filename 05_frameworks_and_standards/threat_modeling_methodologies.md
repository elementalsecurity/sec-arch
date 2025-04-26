# Threat Modeling Methodologies Comparison: STRIDE vs. PASTA vs. LINDDUN

Threat modeling is a critical activity in secure architecture and secure development lifecycles (SDLC). It helps identify, evaluate, and prioritize potential threats to systems, applications, and data before exploitation occurs. The three most prominent methodologies like **STRIDE**, **PASTA**, and **LINDDUN** offer structured approaches based on different threat perspectives.

---

## Overview of Each Methodology

| Methodology | Origin | Focus |
|-------------|--------|-------|
| **STRIDE** | Microsoft | Security threats to systems and components |
| **PASTA** | OWASP / Security Compass | Risk-driven attack simulation across system layers |
| **LINDDUN** | KU Leuven (Belgium) | Privacy threat modeling in software and systems |

---

## STRIDE: A Threat-Centric Model

**STRIDE** is an acronym representing six categories of threats:

| Threat | Description |
|--------|-------------|
| **S**poofing | Impersonating identities |
| **T**ampering | Modifying data or code |
| **R**epudiation | Denying actions without accountability |
| **I**nformation Disclosure | Unauthorized data access |
| **D**enial of Service | Disrupting service availability |
| **E**levation of Privilege | Gaining unauthorized permissions |

### Best Use Cases:
- Component-level threat analysis
- Quick assessments during architecture design
- Integration into DevSecOps and SDLC pipelines

### Strengths:
- Simple and intuitive
- Broadly adopted in industry and tooling (e.g., Microsoft Threat Modeling Tool)

---

## PASTA: A Risk-Centric Model

**PASTA** (Process for Attack Simulation and Threat Analysis) is a 7-stage, risk-oriented methodology designed to simulate real-world attacks and prioritize mitigations based on business impact.

### Stages:
1. **Define Objectives** (business impact analysis)
2. **Define Technical Scope** (architectural inventory)
3. **Decompose Application** (data flow, trust boundaries)
4. **Analyze Threats** (using STRIDE or ATT&CK)
5. **Vulnerability Analysis**
6. **Attack Simulation**
7. **Risk and Impact Analysis**

### Best Use Cases:
- High-risk applications (e.g., fintech, healthcare, critical infrastructure)
- Regulatory-driven assessments

### Strengths:
- Risk prioritization tied to business objectives
- Integrates attack simulation with architecture analysis

---

## LINDDUN: A Privacy-Focused Model

**LINDDUN** targets threats to **privacy**, rather than general security. It maps privacy risks using **Data Flow Diagrams (DFDs)** and categorizes threats across 7 dimensions:

| Threat Category | Description |
|------------------|-------------|
| **L**inkability | Linking data to identities or sessions |
| **I**dentifiability | Identifying individuals from datasets |
| **N**on-repudiation | Lack of plausible deniability |
| **D**etectability | Ability to detect activity |
| **D**isclosure of Information | Privacy-specific data exposure |
| **U**nawareness | Lack of user control or transparency |
| **N**on-compliance | Violating legal or policy obligations |

### Best Use Cases:
- GDPR/CCPA compliance and data protection impact assessments (DPIAs)
- Privacy-by-design product reviews

### Strengths:
- Tailored to privacy engineers and legal/compliance teams
- Maps to global privacy regulations

---

## Summary Comparison

| Category | STRIDE | PASTA | LINDDUN |
|---------|--------|-------|----------|
| Focus | Security threats | Risk simulation | Privacy threats |
| Perspective | Attacker-centric | Business risk-centric | User and privacy-centric |
| Depth | Medium | Deep (multi-phase) | Medium-High (structured) |
| Best for | Engineers, DevSecOps | Risk, threat intel, architecture | Privacy engineers, compliance |
| Tools | Microsoft TMT | OWASP Threat Dragon, ThreatSpec | LINDDUN Toolkit, Privacy Threat Modeler |

---

## Strategic Integration

Security Architects may:
- Use **STRIDE** during design reviews and architecture boards
- Apply **PASTA** for high-assurance systems or executive reporting
- Integrate **LINDDUN** into data flow reviews and DPIA processes
- Combine all three within an **enterprise threat modeling program** for complete coverage

---

## Final Thought

Choosing the right threat modeling approach depends on system sensitivity, stakeholder needs, and regulatory context. Mastering multiple methodologies allows Security Architects to build **resilient, privacy-aware, and risk-aligned architectures** that can withstand modern adversarial pressures.

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

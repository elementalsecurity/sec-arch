# CCPA/CPRA vs. GDPR: Comparison Matrix and Architectural Implications

The **California Consumer Privacy Act (CCPA)** and its amendment, the **California Privacy Rights Act (CPRA)**, are key U.S. privacy laws inspired by the EU’s **General Data Protection Regulation (GDPR)**. While similar in many ways, they differ in scope, terminology, and enforcement.

This document compares the two frameworks from a Security Architect’s perspective, outlining obligations, architectural considerations, and strategic alignment.

---

## Overview

| Feature | GDPR (EU) | CCPA/CPRA (California, USA) |
|---------|-----------|------------------------------|
| Enacted | May 25, 2018 | CCPA: Jan 1, 2020 / CPRA: Jan 1, 2023 (enforceable July 2023) |
| Regulator | Data Protection Authorities (e.g., CNIL, ICO) | California Privacy Protection Agency (CPPA), Attorney General |
| Target Audience | Data controllers and processors worldwide | For-profit businesses interacting with California residents |
| Global Reach | Yes (extraterritorial) | Yes (if CA resident data is processed) |

---

## Applicability

| Criterion | GDPR | CCPA/CPRA |
|----------|------|------------|
| Revenue Threshold | Not applicable | $25M+ gross annual revenue OR |
| Data Volume | Not applicable | Buying/selling/sharing personal data of ≥100,000 consumers or households |
| Sector Exemptions | Minimal | Partial exemptions for nonprofits, HR, B2B contexts |

---

## Personal Data Scope

| Feature | GDPR | CCPA/CPRA |
|--------|------|------------|
| Definition of Personal Data | Broad: Any information related to an identifiable person | Broad: Includes household data; CPRA adds sensitive personal information (SPI) |
| Pseudonymized Data | Considered personal if re-identification is possible | Pseudonymized data may be exempt under CPRA |
| Sensitive Data Category | Yes (special category under Article 9) | Yes (CPRA introduces SPI) |

---

## Consumer Rights

| Right | GDPR | CCPA | CPRA Enhancement |
|-------|------|------|------------------|
| Access | ✅ | ✅ | — |
| Deletion | ✅ | ✅ | — |
| Correction | ✅ | ❌ | ✅ |
| Portability | ✅ | ✅ | — |
| Restriction of Processing | ✅ | ❌ | ❌ |
| Object to Processing | ✅ | Limited ("opt-out") | ✅ (opt-out of cross-context behavioral ads) |
| Non-Discrimination | ✅ | ✅ | Enhanced |
| Limit Use of Sensitive Data | ✅ | ❌ | ✅ |

---

## Legal Basis for Processing

| Feature | GDPR | CCPA/CPRA |
|--------|------|------------|
| Consent | Explicitly required in most cases | Only for selling/sharing SPI |
| Contractual Necessity | ✅ | Implied |
| Legitimate Interest | ✅ | ❌ |
| Opt-In Required for Minors | ✅ (under 16) | ✅ (under 16 must opt in to sale) |

---

## Enforcement and Penalties

| Factor | GDPR | CCPA/CPRA |
|--------|------|------------|
| Penalty | Up to €20M or 4% of global annual turnover | $2,500 per violation / $7,500 for intentional or SPI-related violations |
| Private Right of Action | Yes (limited to data breaches) | Yes (for breach-related violations) |
| DPA Investigations | Yes | Yes, via CPPA and Attorney General |

---

## Architectural Implications for Security Architects

| Capability | GDPR | CCPA/CPRA |
|-----------|------|------------|
| Data Mapping | Required (RoPA) | Essential for fulfilling rights and risk mitigation |
| Consent Management | Consent or lawful basis must be tracked | Opt-out banners and Do Not Sell links |
| Identity Verification | Data subject verification before fulfilling rights | Required, with documented methods |
| Purpose Limitation | Enforced via consent and minimization | Implicit through opt-out mechanics |
| Retention Controls | Defined per processing purpose | Must define and communicate |
| User Preference Portals | Data access, rectification, and objection workflows | Opt-out, data deletion, and SPI limitation workflows |

---

## Strategic Recommendations

- Implement a **centralized data inventory and classification** system
- Use **automated identity and access workflows** for privacy requests
- Design systems to **track consent, opt-outs, and SPI restrictions**
- Incorporate **privacy-enhancing technologies (PETs)**: encryption, differential privacy, tokenization
- Maintain **auditable trails for all access, deletion, and sharing events**

---

## Summary

While GDPR and CCPA/CPRA share foundational values—transparency, accountability, and user control—they diverge in implementation. Security Architects must design architectures that **scale across regulatory landscapes**, support privacy-by-design principles, and enable data governance at the infrastructure level.
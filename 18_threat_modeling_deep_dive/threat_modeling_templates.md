# Threat Modeling Templates

Templates help standardize and accelerate threat modeling across projects by providing reusable structures for documenting systems, threats, mitigations, and decisions.

This document provides practical starter templates that can be adapted to fit different team workflows, system complexities, and security maturity levels.

---

## 1. System Overview Template

**Purpose:** Summarize the basic system design and security context before identifying threats.

| Field | Description |
|:------|:------------|
| Project Name | Name of system, application, or service. |
| System Description | High-level overview of system purpose and major components. |
| Data Classification | Sensitivity of data handled (e.g., public, internal, confidential, regulated). |
| Key Assets | Data, services, and functions critical to business or compliance. |
| Trust Boundaries | Major boundaries between different levels of trust (e.g., public internet, internal network, admin zone). |
| External Integrations | Third-party services, APIs, or partners involved. |

---

## 2. Data Flow Diagram (DFD) Template

**Purpose:** Visualize components, data flows, and trust boundaries for threat analysis.

**DFD Elements:**
- **Processes:** Circles representing logical units that transform or process data.
- **Data Stores:** Open-ended rectangles representing storage repositories.
- **External Entities:** Squares representing users, systems, or services outside the design's control.
- **Data Flows:** Arrows showing movement of data between components.
- **Trust Boundaries:** Dashed lines highlighting shifts in trust assumptions.

*(Recommended: Keep diagrams simple and focused on critical paths.)*

---

## 3. Threat Identification Table Template

**Purpose:** Structure threat discovery and categorization.

| Threat ID | Threat Description | Affected Components | Threat Category (e.g., STRIDE) | Preconditions | Likelihood | Impact | Notes |
|:----------|:--------------------|:---------------------|:-------------------------------|:--------------|:-----------|:------|:------|
| T-001 | API Injection via Unvalidated Input | Public API Gateway | Tampering | Input validation missing | Medium | High | Add input sanitization at gateway |

*(Customize categories and fields as needed.)*

---

## 4. Threat Mitigation Plan Template

**Purpose:** Link identified threats to actionable mitigations and track resolution status.

| Threat ID | Mitigation Strategy | Owner | Status | Notes |
|:----------|:---------------------|:------|:------|:------|
| T-001 | Implement schema validation for all API requests | API Security Lead | In Progress | Scheduled for Sprint 18 |

---

## 5. Threat Checklist Starter (Reference)

**Purpose:** Provide quick prompts to guide threat brainstorming.

- Authentication: Could authentication mechanisms be bypassed?
- Authorization: Could users gain access to data or actions they should not?
- Data Handling: Could sensitive data be leaked, corrupted, or tampered with?
- Input Validation: Are all inputs sanitized to prevent injection or unexpected behavior?
- Communications: Are data flows encrypted and integrity-checked?
- Availability: How could service disruption be caused by abuse or attack?
- Third Parties: How could external services introduce risk?
- Auditability: Are critical security events logged and monitored?

---

## Template Usage Tips

- Use templates flexibly: tailor to project complexity and team maturity.
- Keep documentation lightweight for small or low-risk systems.
- Expand detail for high-risk, regulated, or mission-critical environments.
- Integrate templates into architecture reviews, sprint checklists, or design documents.
- Evolve templates over time based on feedback and incident learnings.

---

*Templates provide scaffolding. Critical thinking, collaboration, and adaptive judgment are what truly bring threat models to life.*


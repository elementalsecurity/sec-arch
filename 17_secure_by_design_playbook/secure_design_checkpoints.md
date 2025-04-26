# Secure Design Checkpoints

Security is most effective when embedded early and consistently throughout the design process, not bolted on afterward. Secure Design Checkpoints are structured moments where architects and engineers deliberately pause to assess security implications, apply principles, and refine risk mitigation strategies.

This document defines key checkpoints to integrate Secure-by-Design thinking across project and solution lifecycles.

---

## Secure Design Checkpoints

### 1. Project Intake and Requirements Gathering

**Checkpoint Actions:**
- Identify security-critical data, assets, and processes.
- Capture explicit security requirements (e.g., compliance obligations, business risk tolerances).
- Engage security architects early as stakeholders.

**Questions to Ask:**
- What is the sensitivity of the data involved?
- What regulatory, contractual, or customer obligations apply?
- What are the assumed threat models for this project?

---

### 2. High-Level Architecture Design

**Checkpoint Actions:**
- Apply Secure Design Principles (least privilege, minimal trust, defense in depth).
- Define trust boundaries, authentication points, and authorization layers.
- Choose architecture patterns that promote security and resilience.

**Questions to Ask:**
- Where are trust boundaries established?
- How is identity and access managed across the system?
- How are sensitive assets isolated and protected?

---

### 3. Detailed Solution Design

**Checkpoint Actions:**
- Map data flows and classify data at each step.
- Specify security controls at each layer (application, network, storage, infrastructure).
- Validate integration points for secure communication, authentication, and encryption.

**Questions to Ask:**
- How is sensitive data protected at rest, in transit, and during processing?
- What dependencies introduce third-party risk?
- How are credentials, secrets, and tokens managed?

---

### 4. Threat Modeling and Risk Analysis

**Checkpoint Actions:**
- Conduct a lightweight or formal threat modeling exercise.
- Identify key threat vectors, misuse cases, and abuse scenarios.
- Prioritize risk mitigations based on impact and likelihood.

**Questions to Ask:**
- What could go wrong?
- How could an attacker misuse or subvert the system?
- How can design changes mitigate the highest risks?

---

### 5. Pre-Implementation Review

**Checkpoint Actions:**
- Validate that critical security requirements are reflected in implementation plans.
- Review control effectiveness assumptions against the design.
- Finalize security acceptance criteria for build and deployment.

**Questions to Ask:**
- Are any critical security controls missing from implementation planning?
- Are operational security responsibilities clearly defined?
- Are monitoring and audit mechanisms in place from Day One?

---

### 6. Post-Implementation Validation

**Checkpoint Actions:**
- Conduct security testing (e.g., code review, penetration testing, red teaming).
- Confirm deployment configurations enforce intended security posture.
- Validate logging, monitoring, and incident response readiness.

**Questions to Ask:**
- Does the deployed system match the secure design?
- Have critical vulnerabilities been addressed before go-live?
- Can incidents be detected, investigated, and contained effectively?

---

*Secure Design Checkpoints institutionalize a culture of deliberate, proactive security thinking. They ensure that every design choice is evaluated not only for functionality and performance, but for defensibility and resilience.*


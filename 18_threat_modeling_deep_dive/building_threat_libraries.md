# Building and Using Threat Libraries

A threat library is a curated collection of known threat scenarios, attack patterns, and security weaknesses that can be referenced during threat modeling activities.

Building and maintaining a threat library improves the efficiency, consistency, and coverage of threat modeling by helping teams avoid reinventing the wheel for each project.

This document provides guidance on constructing, maintaining, and applying reusable threat libraries.

---

## Why Build Threat Libraries?

- **Consistency:** Helps teams use standardized terminology and threat analysis approaches.
- **Speed:** Accelerates threat identification by providing ready-to-use examples.
- **Coverage:** Reduces the risk of overlooking common attack vectors.
- **Knowledge Sharing:** Captures institutional security knowledge and experience.

---

## Core Components of a Threat Library

| Component | Purpose |
|:----------|:--------|
| Threat ID | Unique identifier for tracking threats. |
| Threat Name | Short, descriptive title of the threat. |
| Description | Detailed explanation of the threat and its potential impact. |
| Affected Assets or Components | Systems, services, or data types targeted by the threat. |
| Preconditions | Environmental conditions or assumptions necessary for the threat to succeed. |
| Attack Techniques | Methods attackers might use to exploit the threat. |
| Mitigation Strategies | Security controls or design choices that reduce or eliminate the risk. |
| References | Links to external resources, CVEs, or known attack frameworks (e.g., MITRE ATT&CK). |

---

## Building a Threat Library: Step-by-Step

1. **Define Scope and Focus**
   - Choose an initial focus (e.g., web applications, APIs, cloud infrastructure).

2. **Gather Baseline Threats**
   - Pull from recognized resources such as OWASP Top Ten, MITRE ATT&CK, CIS Critical Security Controls.

3. **Customize to Your Context**
   - Tailor threat entries to reflect your organization's technologies, architectures, and business models.

4. **Structure and Tag Threats**
   - Categorize threats by component (e.g., authentication, storage, communications).
   - Tag threats with keywords for easy searching (e.g., "data leakage", "session hijacking").

5. **Iterate and Expand Over Time**
   - Add new threats as they emerge from real incidents, assessments, or threat intelligence.
   - Periodically review and retire outdated or irrelevant threats.

---

## Best Practices for Using Threat Libraries

- **Reference, Not Replace:** Use the library to spark thinking during threat modeling sessions, but always adapt to project specifics.
- **Prioritize Relevance:** Focus on threats that map directly to the architecture and risk profile being modeled.
- **Avoid Blind Copy-Paste:** Treat each threat scenario as a prompt for tailored risk analysis, not a checklist.
- **Update Regularly:** Integrate lessons learned from real-world incidents into the library.
- **Share Across Teams:** Make the library available to architects, developers, operations teams, and risk managers.

---

## Example Threat Entry (Template)

| Field | Example |
|:------|:--------|
| Threat ID | T-001 |
| Threat Name | API Injection via Unvalidated Input |
| Description | Attackers inject malicious payloads into APIs by exploiting insufficient input validation. |
| Affected Assets | API endpoints, backend databases, user data |
| Preconditions | API does not enforce strict input validation or content-type enforcement. |
| Attack Techniques | Injection of SQL, NoSQL, or command payloads through API requests. |
| Mitigation Strategies | Strong input validation, parameterized queries, schema validation, web application firewalls (WAFs). |
| References | OWASP API Security Top 10, MITRE ATT&CK T1190 |

---

*Threat libraries turn experience into structure, and structure into speed. They help teams think faster, deeper, and more consistently about real-world risks.*
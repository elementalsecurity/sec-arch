# Threat Modeling Methods

Threat modeling can take many forms, depending on system complexity, organizational needs, and available resources. Understanding different structured methods allows architects to select the right approach for their context and goals.

This document provides an overview of common threat modeling methodologies and when to use each.

---

## STRIDE

**Origin:** Developed by Microsoft

**Focus:** Identifying threats based on types of security failures.

**STRIDE Categories:**
- **Spoofing:** Impersonating something or someone else.
- **Tampering:** Modifying data or systems maliciously.
- **Repudiation:** Claiming that actions were not performed.
- **Information Disclosure:** Exposing information to unauthorized parties.
- **Denial of Service:** Making services unavailable to intended users.
- **Elevation of Privilege:** Gaining unauthorized access to privileged capabilities.

**Strengths:**
- Easy to learn and apply.
- Well-suited for identifying common threat types in application and network designs.

**Limitations:**
- Focuses more on identifying types of problems than prioritizing risks.

---

## PASTA (Process for Attack Simulation and Threat Analysis)

**Origin:** Developed by VerSprite

**Focus:** Threat analysis driven by business impact and attacker simulation.

**PASTA Stages:**
1. Definition of business objectives.
2. Definition of technical scope.
3. Application decomposition and architecture analysis.
4. Threat analysis.
5. Vulnerability and weakness analysis.
6. Attack modeling and simulation.
7. Risk and impact analysis.

**Strengths:**
- Focuses heavily on business impact and attacker realism.
- Helps prioritize risks based on potential consequences.

**Limitations:**
- More resource-intensive; best for complex, high-value systems.

---

## VAST (Visual, Agile, and Simple Threat Modeling)

**Origin:** Developed by ThreatModeler

**Focus:** Scaling threat modeling across agile teams and large organizations.

**VAST Concepts:**
- Different models for application threats and operational threats.
- Emphasizes visual diagrams that evolve over time.
- Automation and integration with CI/CD pipelines.

**Strengths:**
- Designed for scalability and integration into agile workflows.
- Supports automation and centralized threat modeling governance.

**Limitations:**
- Requires tooling support to achieve full benefits.

---

## Attack Trees

**Origin:** Introduced by Bruce Schneier

**Focus:** Hierarchical analysis of attack objectives and pathways.

**Attack Tree Structure:**
- The root node represents an attack goal.
- Leaf nodes represent methods to achieve that goal.
- Branching structures explore different attack paths and combinations.

**Strengths:**
- Visualizes attacker decision-making processes.
- Helps identify multiple paths to compromise and prioritize defenses.

**Limitations:**
- Can become complex for large systems.
- Focuses primarily on attack strategies rather than defender mitigation planning.

---

## Choosing the Right Method

| Situation | Recommended Method |
|:----------|:-------------------|
| Simple or early-stage projects | STRIDE or Lightweight DFD-based Threat Modeling |
| High-value systems needing deep analysis | PASTA |
| Large-scale agile or DevOps environments | VAST (with tool support) |
| Targeted attack analysis or red team preparation | Attack Trees |

Often, hybrid approaches combining elements of multiple methods work best.

---

*Threat modeling is not about rigidly applying one framework. It is about systematically thinking like an attacker and using structured tools to make risk visible, understandable, and actionable.*



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

# Threat Modeling in ARCH-Based Design

## Purpose

This document explains how to integrate threat modeling directly into the ARCH Model — Asymmetric Resilient Cybersecurity Hardening — to ensure that security architecture is informed by adversary behavior, critical asset protection, and disruption strategies from the earliest design stages.

Threat modeling in this context is not a one-time exercise. It becomes a continuous, lightweight process that adapts designs based on evolving adversary tactics and system changes.


## Why Threat Modeling is Essential in ARCH

- **Informs Asymmetry:** Threat models expose the paths attackers are most likely to take, allowing architects to deploy asymmetric defenses where they impose maximum attacker cost.
- **Strengthens Resilience:** By identifying likely failure modes and breach paths, threat modeling guides the design of systems that recover quickly and degrade gracefully.
- **Drives Intentional Hardening:** Focuses control placement and simplification efforts on the areas with the greatest attack surface or business impact.


## Lightweight Threat Modeling Approach for ARCH

### Step 1: Define the System Context
- Identify key assets, data flows, users, and external systems.
- Establish the system's boundaries and critical business functions.

### Step 2: Identify Trust Boundaries
- Map where data, identities, or processes cross levels of trust.
- Highlight where validation, authentication, and control should occur.

### Step 3: Identify Threat Actors and Motivations
- Consider both internal and external adversaries.
- Model likely attacker goals (data theft, disruption, privilege escalation, lateral movement).

### Step 4: Map Adversary Paths
- Diagram plausible attacker entry points and lateral movement paths.
- Focus on minimal paths to high-value assets, not exhaustive permutations.

### Step 5: Prioritize Threats Based on Asymmetry and Impact
- Rank threats by how easily attackers can exploit them versus how costly they are to defend.
- Emphasize disruption strategies that create friction, early detection, or high attacker overhead.

### Step 6: Define Resilience and Disruption Controls
- Identify controls that disrupt attacker paths, isolate failure domains, or accelerate detection.
- Map controls explicitly to ARCH pillars: Asymmetry, Resilience, Cybersecurity-Driven Architecture, Simplicity.


## Embedding Threat Modeling in the Design Lifecycle

- **At Planning:** Conduct high-level threat modeling during system scoping to inform architectural decisions.
- **At Design:** Update threat models as system components, integrations, or deployment models change.
- **At Review:** Validate that security controls mapped to threat models are still relevant and effective.
- **At Evolution:** Continuously reassess threat models when adversary capabilities, business operations, or technology stacks evolve.


## Practical Tips for Lightweight Threat Modeling

- Focus on attacker goals, not exhaustive threat lists.
- Use simple diagrams that show trust boundaries, attacker paths, and high-value targets.
- Prioritize speed and relevance over formalism.
- Document assumptions, gaps, and design tradeoffs explicitly.


## Example: Embedding Threat Modeling into an ARCH Deployment

- **Context:** Designing a secure DevOps pipeline.
- **Threat Model Outcome:** Identified the pipeline credentials store as the highest-value target.
- **ARCH Design Impact:**
  - Introduce deception credentials to detect unauthorized access attempts (Asymmetry).
  - Use hardware-backed vaults with zero standing access (Resilience).
  - Embed secrets scanning gates in every pipeline stage (Cybersecurity-Driven Architecture).
  - Remove legacy credential stores entirely (Hardening Through Simplicity).


## Conclusion

Threat modeling is not a separate compliance activity in ARCH-based design. It is a lightweight, continuous source of intelligence that feeds strategic architectural decisions.

By embedding threat modeling into ARCH, security architects create designs that are not only compliant but truly adversary-aware, resilient, and sustainable.

---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

# ARCH Tactical Implementation Guide

This guide provides a practical, step-by-step breakdown for applying the **ARCH Model** — Asymmetric Resilient Cybersecurity Hardening — to real-world security program design and operationalization.

While the ARCH Overview describes the philosophy and principles, this guide is meant to **operationalize those principles across teams, systems, and timeframes**. It is for Security Architects, CISOs, DevOps engineers, and security leaders who want to apply ARCH strategically, tactically, and measurably.

---

## Strategic Deployment Sequence

ARCH is best implemented in **four progressive phases**, each mapped to one of the pillars.

### Phase 1: Architect Asymmetry
- **Goal**: Impose disproportionate cost on attackers
- **Tactics**:
  - Identify high-value assets and simulate adversary paths (ATT&CK + threat modeling)
  - Deploy canaries, deception proxies, and honeypots in lateral movement zones
  - Rotate keys and credentials at unpredictable intervals
  - Remove predictable admin workflows and standard ports (e.g., disable RDP/SSH by default)

### Phase 2: Engineer Resilience
- **Goal**: Build for failure, not just prevention
- **Tactics**:
  - Define blast radii for every critical service and enforce segmentation boundaries
  - Adopt immutable infrastructure and ephemeral workloads (e.g., Lambda, k8s pods)
  - Use queue-based messaging over tightly coupled RPCs
  - Automate detection-to-response playbooks with SOAR tools

### Phase 3: Elevate Cybersecurity Architecture
- **Goal**: Shift security left and up
- **Tactics**:
  - Embed security architects into cloud and platform teams
  - Create reference architectures for IAM, logging, Zero Trust, and incident response
  - Add threat modeling to the architecture review board process
  - Define service-level objectives (SLOs) for detection latency and control coverage

### Phase 4: Harden Through Simplicity
- **Goal**: Reduce complexity and attack surface
- **Tactics**:
  - Eliminate dormant identities, orphaned endpoints, and non-expiring access
  - Replace complex RBAC trees with role templates and inheritance models
  - Remove unused SaaS integrations and deprecated protocols
  - Prefer managed platforms with known secure defaults

---

## Control Examples Mapped to ARCH

| Control | ARCH Pillar | Tactical Detail |
|--------|--------------|-----------------|
| Canary tokens in critical file shares | Asymmetry | Alert on attacker interaction with decoy data |
| Immutable EC2 + image pipelines | Resilience | Block post-exploit persistence by eliminating mutable state |
| CI/CD security gates | Architecture | Prevent drift and enforce secrets scanning before deploy |
| Access package automation | Simplicity | Auto-expire third-party access to reduce identity sprawl |

---

## Team Integration

To implement ARCH:

### Security Architects:
- Define posture by design (not by policy)
- Maintain reference patterns and alignment guides
- Map business goals to asymmetric threat priorities

### Engineering/DevOps:
- Integrate scanning and control gates into pipelines
- Build with zero standing access and infrastructure isolation
- Rotate keys, secrets, and certs automatically

### Governance/Risk:
- Use ARCH to justify prioritization of compensating controls
- Define acceptable residual risk per application class
- Use threat-informed risk scoring, not just control inventories

---

## Metrics and Outcomes

| Metric | Measurement Target | Maturity Signal |
|--------|---------------------|-----------------|
| Mean time to detect/contain (MTTD/MTTC) | <10 minutes | Responsive and prepared ops |
| % of ephemeral workloads | >80% | Reduction in persistence surface |
| % of access with expiration | 100% | Zero standing privilege enforced |
| Number of attacker paths blocked at tier-1 | Increase quarter-over-quarter | Threat modeling-to-control loop is active |

---

## Common Pitfalls to Avoid
- Treating ARCH as a compliance overlay rather than a design principle
- Applying asymmetry only at the network layer (it must go into identity, data, workload)
- Using ARCH vocabulary without operational alignment (e.g., claiming resilience without testing failover)
- Overengineering controls that violate the simplicity mandate

---

## Summary
The ARCH Tactical Implementation Guide transforms a security philosophy into a field-deployable playbook. It helps teams ask better questions:
- "Where does the adversary gain advantage — and how do we break it?"
- "What is the minimum we must protect to stay operational?"
- "How do we make security easier to do right — and harder to ignore?"

By walking through phased deployment, mapped controls, team responsibilities, and measurable outcomes, this guide empowers Security Architects and leaders to build programs that are asymmetric by design, resilient under attack, and hardened by simplification.

> "You don’t need more security. You need smarter security. ARCH helps you build it."
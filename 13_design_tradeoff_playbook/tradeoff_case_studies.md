# Tradeoff Case Studies

This document provides real-world examples of design tradeoffs made during Security Architecture decisions.

Each case study illustrates the competing forces at play, the decision rationale, and lessons learned. These examples are intended to build critical thinking skills and show how strategic Security Architects operate in imperfect environments.

---

## Case Study 1: MFA Deployment for Customer Portal

**Scenario:**
- A large financial services company launched a new customer portal for account management.
- Security recommended mandatory MFA for all users.
- Product management argued that additional login friction would negatively impact customer retention metrics.

**Tradeoff:**
- Security vs Usability

**Decision:**
- Implement MFA as optional at launch but highly encourage it through incentives (e.g., faster service access, enhanced features).
- Monitor adoption rates and phased in mandatory MFA over six months based on customer feedback.

**Lesson:**
- Immediate enforcement is not always the only secure path. Gradual adoption strategies can achieve better long-term outcomes.

---

## Case Study 2: Cloud Egress Monitoring vs Performance Impact

**Scenario:**
- A SaaS company needed full packet inspection on all cloud egress traffic for sensitive customer workloads.
- Enabling TLS decryption and inspection through a cloud firewall service added 25 percent latency to certain user transactions.

**Tradeoff:**
- Security Visibility vs Performance

**Decision:**
- Limited deep inspection to high-risk workloads.
- Applied lightweight metadata monitoring (e.g., NetFlow, DNS logs) to lower-risk traffic to maintain performance.

**Lesson:**
- Align inspection depth with risk tiers rather than applying a one-size-fits-all control.

---

## Case Study 3: Endpoint Hardening on Developer Workstations

**Scenario:**
- A global e-commerce company planned to apply aggressive endpoint lockdown policies (no USB access, forced software updates, restricted installations) to all corporate devices.
- Developer teams protested, citing that restrictions would significantly slow innovation and increase build failures.

**Tradeoff:**
- Standardization vs Flexibility

**Decision:**
- Created a separate "Developer Secure Zone" with hardened controls but greater flexibility on tool installation.
- Required stricter network segmentation, additional monitoring, and frequent compliance audits within the secure zone.

**Lesson:**
- Secure by isolation and enhanced monitoring can sometimes achieve better outcomes than rigid, one-size-fits-all lockdowns.

---

## Case Study 4: Incident Response Automation vs Analyst Discretion

**Scenario:**
- The Security Operations Center (SOC) wanted to fully automate endpoint isolation through SOAR playbooks when certain malware signatures were detected.
- Analysts expressed concern that automatic isolation could cause unnecessary business disruption for false positives.

**Tradeoff:**
- Speed of Response vs Risk of Operational Disruption

**Decision:**
- Implemented tiered automation:
  - Critical high-confidence detections triggered immediate isolation.
  - Medium-confidence detections created prioritized alerts requiring human validation before action.

**Lesson:**
- Automation must be tuned not only for technical detection accuracy but also for business impact tolerance.

---

*Security Architecture is not about avoiding tradeoffs. It is about making them visible, defensible, and aligned to what matters most for the business and its mission.*


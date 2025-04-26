# Tradeoff Guidance Sheet

This guidance sheet provides a set of tactical questions Security Architects can use during design reviews, project meetings, or architecture assessments to uncover hidden or implicit tradeoffs.

Good tradeoff identification comes from asking focused, risk-aware questions. This sheet is designed to build critical thinking skills and strengthen architectural governance.

---

## 1. Security vs Usability

- How will this design affect user experience or operational workflows?
- Are there ways to improve security without significantly degrading usability?
- What incentives or education could offset any user friction introduced by security controls?

---

## 2. Security vs Cost

- What would it cost to implement the "ideal" security solution here?
- What is the risk of not implementing the ideal solution?
- Are there risk-prioritized areas where investment is non-negotiable?

---

## 3. Security vs Performance

- Will any security controls introduce noticeable latency or system bottlenecks?
- Can the security mechanism be applied selectively based on risk tiers?
- Is the system designed to degrade gracefully if security services (e.g., decryption gateways) fail or slow down?

---

## 4. Security vs Agility

- Will this design slow down deployment velocity or change delivery practices?
- Are security gates proportional to the risk of the change?
- Can we embed "shift-left" security controls to minimize disruption?

---

## 5. Risk Acceptance vs Risk Mitigation

- If we cannot mitigate this risk immediately, can we document it clearly and assign ownership?
- Is the residual risk aligned to the organization's documented risk appetite?
- What monitoring or compensating controls can we implement if full mitigation is deferred?

---

## 6. Standardization vs Flexibility

- Is this a core system that must strictly follow enterprise standards?
- Are there areas where controlled exceptions are acceptable?
- How will deviation from standards be monitored, reviewed, and managed over time?

---

## Closing Thought

Every design decision carries implicit assumptions about risk, performance, cost, and usability.
The Security Architect's role is not to prevent tradeoffs, but to illuminate them so that the organization chooses its risks with full understanding.

*Good questions make risks visible. Visible risks enable better decisions.*
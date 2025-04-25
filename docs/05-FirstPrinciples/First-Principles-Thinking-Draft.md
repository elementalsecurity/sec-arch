# First-Principles Thinking for Security Architects

Apply first-principles reasoning to every architecture problem. Derive controls from fundamentals rather than follow trends.

## 1. Define Invariants
- Identify the core asset properties that must hold under any circumstance:
  - Confidentiality: sensitive data must not be disclosed.
  - Integrity: data and code must not be tampered with.
  - Availability: critical services must remain online.
  - Non-repudiation: key actions must be provable.

- Ask: If any invariant fails, what is the business impact?

## 2. Decompose the System
- Draw a minimal data-flow diagram.
- Mark trust boundaries, implicit dependencies (certificate authorities, build pipelines, root stores).
- Call out assumptions such as network reachability, identity federations, and hardware roots of trust.

## 3. Identify Natural Forces
- Map relevant adversary capabilities from MITRE ATT&CK.
- Consider system entropy: hardware failure, clock drift, human error.
- Assess which forces act independent of controls.

## 4. Quantify Risk
- For each threat scenario, estimate:
  - Likelihood (P) of occurrence.
  - Impact (I) on business objectives.
- Compute rough risk: R = sum(P × I).
- Challenge: Which variables can we influence most cost-effectively?

## 5. Derive Control Objectives
- For each risk, state a target condition:
  - Example: "All data requests must include a tenant-level attestation token."
- Ensure objectives eliminate root causes, not only detect them.

## 6. Select Mechanisms
- Only after objectives are fixed, choose implementations:
  - Mutual TLS, JWT lifecycles, key wrapping.
- Verify: Can the mechanism fail safe? Can it be tested automatically?

## 7. Validate Assumptions
- Perform counter-example exercises:
  - Remove the mechanism; check if invariants break.
  - Simulate credential theft or insider compromise.
- Record new assumptions and iterate.

## Guiding Principles
1. Trust cannot be created, only transferred or degraded.
2. Minimize attack surface before adding controls.
3. Separate key material (system secrets) from credentials (user secrets).
4. Default deny data flow and operations.
5. Make integrity observable: attest and log every change.
6. Prefer simple, robust mechanisms over complex overlapping controls.
7. Align control cost with risk reduction potential.

## Training Exercises
- Reverse-engineer a breach and identify failed principles.
- Redesign a legacy network with zero implicit trust.
- Write a short explainer (300 words) of one principle without acronyms.
- Quantify a risk weekly using a whiteboard formula.
- Conduct a jargon-free presentation of first-principles thinking.

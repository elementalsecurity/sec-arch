# ADR Format and Structure

A well-structured Architecture Decision Record (ADR) captures critical information about a design decision in a way that is clear, traceable, and useful over time.

This document defines a simple, professional ADR format that balances completeness with usability.

---

## Standard ADR Template

### 1. Title

A short, descriptive name for the decision.

*Example:* "Adopt Zero Trust Access Model for Cloud Services"

---

### 2. Status

Current state of the decision.

- Proposed
- Accepted
- Deprecated
- Superseded

---

### 3. Context

Background information explaining why the decision is needed.

- What problem or opportunity triggered this decision?
- What assumptions, constraints, or requirements influence it?
- What stakeholders or domains are affected?

---

### 4. Decision

The decision made.

- What choice was made?
- What are the key details that define the decision?
- What scope boundaries or limitations apply?

---

### 5. Alternatives Considered

Other options that were considered, along with reasons for rejection.

- Option 1: Description, pros, cons.
- Option 2: Description, pros, cons.
- Option 3: Description, pros, cons.

---

### 6. Consequences

Expected results and tradeoffs resulting from the decision.

- Benefits gained.
- Risks accepted.
- Technical debt introduced (if any).
- Implications for future changes.

---

### 7. Related ADRs or References

Links to:
- Related ADRs that influenced or will be influenced by this decision.
- External standards, documentation, or reference architectures.

*(Optional, but strengthens traceability.)*

---

## Example Skeleton

```markdown
# ADR-001: Adopt Zero Trust Access Model for Cloud Services

**Status:** Accepted

## Context
- Growing adoption of multi-cloud services and remote workforce.
- Perimeter-based security models insufficient for modern threat landscape.
- Compliance requirements emphasize adaptive access controls.

## Decision
- Implement a Zero Trust Access model.
- Authenticate and authorize every access request dynamically based on user identity, device posture, and context.
- De-prioritize reliance on network location as a trust factor.

## Alternatives Considered
- Continue perimeter-based security model (Rejected: inadequate for modern architectures).
- Implement VPN enhancements alone (Rejected: VPN does not address application-level authorization needs).

## Consequences
- Increased security posture through adaptive trust evaluation.
- Initial complexity in integrating identity providers and conditional access systems.
- Need for continuous monitoring and incident response tuning.

## Related ADRs
- ADR-002: Select Identity Provider for Zero Trust Architecture
- NIST SP 800-207: Zero Trust Architecture
```

---

## Best Practices for Writing ADRs

- Keep language clear and objective.
- Capture "why now" reasoning as clearly as "what was decided".
- Write ADRs for significant decisions that shape architecture, security posture, or operational resilience.
- Number ADRs sequentially for easy reference.
- Keep ADRs small and focused on one major decision per record.

---

*Good ADRs do not just record technical facts. They capture strategic thinking, risk acceptance, and learning that strengthens architectural resilience over time.*


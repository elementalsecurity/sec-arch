# Threat Checklist Quick Reference

Use this quick reference during threat modeling or design reviews to brainstorm common threats. This checklist is designed to spark thinking and should be adapted based on system context.

---

# Threat Categories and Prompts

## Authentication and Authorization

- [ ] Can authentication mechanisms be bypassed?
- [ ] Can authorization checks be skipped or manipulated?
- [ ] Are privileged operations properly restricted?
- [ ] Are session tokens protected against theft or reuse?

---

## Data Protection

- [ ] Could sensitive data be exposed in storage or transmission?
- [ ] Are encryption keys properly managed and rotated?
- [ ] Are backups protected against unauthorized access?

---

## Input and Output Handling

- [ ] Can attackers inject malicious input (e.g., SQL injection, command injection)?
- [ ] Are user inputs validated, sanitized, and constrained?
- [ ] Could output leaks reveal sensitive internal state?

---

## Communications and API Security

- [ ] Are communications encrypted and authenticated?
- [ ] Can APIs be abused through excessive requests (e.g., denial of service)?
- [ ] Are third-party integrations trusted and validated?

---

## Infrastructure and Operations

- [ ] Could system configuration drift expose vulnerabilities?
- [ ] Are logging and monitoring in place to detect security events?
- [ ] Are administrative interfaces securely restricted and monitored?

---

## Availability and Resilience

- [ ] Can system resources be exhausted (e.g., CPU, memory, storage)?
- [ ] Are redundancy and failover mechanisms in place?
- [ ] Can upstream service failures cascade into larger outages?

---

## Insider Threats and Supply Chain Risks

- [ ] Could insiders abuse legitimate access for malicious purposes?
- [ ] Are codebases and dependencies protected against tampering?
- [ ] Are supply chain partners assessed for security posture?

---

# Additional Considerations

- [ ] Are privacy requirements (e.g., GDPR, CCPA) adequately addressed?
- [ ] Are regulatory and compliance obligations mapped to system designs?
- [ ] Are threat models reviewed periodically as systems evolve?

---

*Threat checklists guide thinking, but threat modeling is ultimately about understanding the system, its environment, its adversaries, and its mission.*


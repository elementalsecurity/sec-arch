# Risk Register Template (Security Program Edition)

This document provides a flexible risk register structure tailored for security architecture programs. It can be used to document, assess, track, and prioritize security risks across projects, business units, or enterprise portfolios. It supports both qualitative and semi-quantitative risk scoring and is ideal for integrating into GRC platforms or managing within Excel/Markdown.

---

## Suggested Columns

| Risk ID | Description | Affected Asset(s) | Threat Scenario | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Owner | Current Controls | Control Effectiveness | Residual Risk | Treatment Plan | Target Resolution Date | Status |
|---------|-------------|--------------------|------------------|------------------|--------------|------------|-------------|------------------|------------------------|----------------|------------------|--------------------------|--------|
| RSK-001 | S3 bucket open to the internet | Customer data lake | External data exfiltration | 4 | 5 | 20 | Cloud Security Lead | IAM, public access block | Medium | Moderate | Restrict access via VPC endpoint and policy | 2024-12-01 | Open |
| RSK-002 | Hardcoded credentials in CI pipeline | Source code repository | Credential theft, lateral movement | 3 | 4 | 12 | DevSecOps Lead | Secrets scanning alert | Low | Low | Refactor to Vault-based dynamic credentials | 2024-10-01 | In Progress |

---

## Likelihood/Impact Scoring (1–5)
| Score | Likelihood | Impact |
|-------|------------|--------|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost Certain | Critical |

> **Risk Score = Likelihood x Impact**

---

## Risk Treatment Categories
- **Accept**: Residual risk is within tolerance.
- **Mitigate**: Implement controls to reduce likelihood or impact.
- **Transfer**: Shift risk through insurance or vendor contract.
- **Avoid**: Change process or deprecate system to eliminate risk.

---

## Usage Recommendations
- Use unique risk IDs and version history to support traceability.
- Link risks to security controls, owners, and architecture layers.
- Periodically review risks with architecture or GRC committees.
- Integrate with vulnerability management, threat modeling, and audit processes.

---

## Summary
The risk register helps bridge technical issues and business impact. A good risk register not only tracks problems — it informs prioritization, ownership, and control maturity.

> "Risk isn’t just what you haven’t fixed, it’s what you haven’t acknowledged. Track it to own it."



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

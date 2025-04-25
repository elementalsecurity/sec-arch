# Tradeoff Patterns

Security Architecture requires balancing competing forces. Every system design involves implicit or explicit tradeoffs that impact risk, usability, cost, performance, and strategic flexibility.

This document outlines common tradeoff patterns that Security Architects must recognize, evaluate, and manage thoughtfully.

---

## 1. Security vs Usability

| Tradeoff | Considerations |
|:---------|:---------------|
| Stricter authentication controls (e.g., MFA, device certificates) vs seamless user access | Increased friction can lead to workarounds or user resistance. Risk-adjust authentication requirements based on sensitivity of resources. |
| Network segmentation vs system discoverability and collaboration | Tighter segmentation protects assets but can impede business workflows if not mapped carefully. |

---

## 2. Security vs Cost

| Tradeoff | Considerations |
|:---------|:---------------|
| Full encryption of all data at rest and in transit vs selective encryption of sensitive fields | Encrypting everything increases cloud storage, CPU, and performance costs. Prioritize based on data classification. |
| Dedicated security appliances (WAFs, DLP, CASB) vs native platform controls | Third-party tools offer depth but require licensing and integration overhead. Balance breadth of protection with operational efficiency. |

---

## 3. Security vs Performance

| Tradeoff | Considerations |
|:---------|:---------------|
| Inline inspection of all network traffic (e.g., TLS decryption) vs latency and throughput impact | Monitoring depth must be risk-tuned to avoid unacceptable performance degradation. |
| Secure coding practices (e.g., input validation, output encoding) vs application response times | Proper validation adds microseconds but prevents catastrophic injection vulnerabilities. |

---

## 4. Security vs Agility

| Tradeoff | Considerations |
|:---------|:---------------|
| Mandatory security architecture reviews for all changes vs rapid delivery pipelines | Introduce tiered reviews based on change risk to maintain velocity without sacrificing oversight. |
| Comprehensive threat modeling vs minimum viable design shipping | Embed lightweight threat modeling early and iterate as designs mature. |

---

## 5. Risk Acceptance vs Risk Mitigation

| Tradeoff | Considerations |
|:---------|:---------------|
| Immediate technical fixes vs formal risk acceptance for deferred remediation | Sometimes business deadlines dictate proceeding with managed residual risk. Ensure acceptance is documented, visible, and assigned to an accountable owner. |

---

## 6. Standardization vs Flexibility

| Tradeoff | Considerations |
|:---------|:---------------|
| Strict adherence to enterprise reference architectures vs enabling team autonomy | Standardize where risk is highest (e.g., IAM, network edge) but allow safe innovation zones (e.g., sandbox environments, non-critical apps). |

---

## Closing Thought

Security Architects do not eliminate tradeoffs. They make them visible, reasoned, and aligned to organizational priorities and risk appetite.

*Tradeoff decisions made blindly create hidden risk. Tradeoff decisions made thoughtfully create informed trust.*


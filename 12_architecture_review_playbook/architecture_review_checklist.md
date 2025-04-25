# Architecture Review Checklist

This checklist provides a structured guide for Security Architects to evaluate the security, resilience, and compliance of system designs during Architecture Reviews.

Use this checklist to ensure consistent coverage of key domains. Adapt the depth of assessment based on the scope, complexity, and risk profile of the project.

---

## 1. Identity and Access Management

- [ ] Are all user and system identities authenticated through a trusted Identity Provider (IdP)?
- [ ] Is Multi-Factor Authentication (MFA) enforced for administrative and remote access?
- [ ] Are authorization models based on least privilege and role-based access control (RBAC) principles?
- [ ] Is privilege escalation monitored and controlled?
- [ ] Are service accounts secured with proper credential rotation and minimal permissions?

---

## 2. Data Protection and Privacy

- [ ] Is sensitive data classified and documented?
- [ ] Is data encrypted in transit using secure protocols (TLS 1.2 or higher)?
- [ ] Is data encrypted at rest with managed key services or Hardware Security Modules (HSMs)?
- [ ] Are data retention and deletion policies clearly defined and implemented?
- [ ] Are Privacy by Design principles applied where personal or regulated data is handled?

---

## 3. Network Security and Segmentation

- [ ] Are networks segmented based on sensitivity and function?
- [ ] Are only necessary ports, protocols, and services open?
- [ ] Are firewalls, security groups, and access control lists (ACLs) appropriately configured?
- [ ] Is remote access secured through bastion hosts, VPNs, or Zero Trust principles?
- [ ] Are network monitoring and intrusion detection/prevention capabilities in place?

---

## 4. Application and API Security

- [ ] Are applications protected against common OWASP Top 10 vulnerabilities?
- [ ] Are APIs secured with strong authentication, authorization, and rate limiting?
- [ ] Is input validation enforced on both client and server sides?
- [ ] Are secrets (API keys, credentials) managed securely outside of source code?
- [ ] Are libraries, frameworks, and dependencies scanned for vulnerabilities?

---

## 5. Cloud Security and Shared Responsibility

- [ ] Are cloud-native security controls (IAM, network policies, encryption) fully leveraged?
- [ ] Are administrative actions logged and monitored?
- [ ] Are cloud resources organized with tagging standards for ownership and compliance?
- [ ] Are serverless, container, and VM workloads secured according to best practices?
- [ ] Is the division of security responsibilities between the organization and the cloud provider clearly understood and documented?

---

## 6. Threat Detection and Monitoring

- [ ] Are critical events and security logs collected, centralized, and protected from tampering?
- [ ] Are log retention and integrity requirements aligned with regulatory and investigative needs?
- [ ] Are monitoring solutions mapped to MITRE ATT&CK techniques or similar frameworks?
- [ ] Are alerting thresholds tuned to balance fidelity and noise?
- [ ] Is threat hunting or anomaly detection integrated into operational practices?

---

## 7. Resilience and Recovery

- [ ] Are backup strategies defined, tested, and protected against ransomware or tampering?
- [ ] Are disaster recovery and business continuity plans in place and tested?
- [ ] Is high availability or failover designed into critical system components?
- [ ] Are single points of failure identified and mitigated where feasible?

---

## 8. Compliance and Regulatory Alignment

- [ ] Are applicable regulatory requirements (PCI DSS, HIPAA, GDPR, SOX, etc.) identified and mapped to design controls?
- [ ] Are audit trails sufficient to demonstrate compliance for in-scope systems and data?
- [ ] Are system owners aware of their regulatory and policy obligations?
- [ ] Is data residency and cross-border transfer compliance addressed if applicable?

---

## 9. Operational and Organizational Readiness

- [ ] Are support teams trained on secure operations and incident response for the system?
- [ ] Are Standard Operating Procedures (SOPs) defined for critical workflows?
- [ ] Are escalation paths and communication plans established for security events?
- [ ] Are monitoring and maintenance plans aligned with the system's criticality and risk profile?

---

*This checklist is a guide, not a script. Adapt it thoughtfully based on the system being reviewed, the risk appetite of the organization, and the broader business context.*
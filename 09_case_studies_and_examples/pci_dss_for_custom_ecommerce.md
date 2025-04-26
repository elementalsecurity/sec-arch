# Case Study: PCI DSS Compliance for a Custom E-Commerce Platform

## Context and Business Problem
A digital-first retail brand decided to build its own custom checkout experience to reduce fees and maintain full control of the customer journey. This included the development of a proprietary front-end storefront, a Node.js-based backend, and integrations with Stripe and other third-party processors.

Because the platform processed, transmitted, and stored cardholder data (CHD), the company was classified as a **Level 2 Merchant** and required to demonstrate compliance with **PCI DSS 4.0.1**, including completion of a **Report on Compliance (ROC)**.

Security and engineering leadership needed to ensure:
- The platform could pass a formal PCI audit
- Controls did not inhibit checkout performance or uptime
- Logging, vulnerability management, and segmentation met PCI standards

---

## Architecture Requirements
- Ensure end-to-end encryption of cardholder data
- Segregate the Cardholder Data Environment (CDE) from the corporate network
- Limit CHD storage and implement tokenization where feasible
- Harden the custom web application and APIs against OWASP Top 10
- Support quarterly ASV scans and annual penetration tests
- Maintain audit-ready logging, access control, and change tracking

---

## Constraints and Risks
- Development deadlines tied to product launch
- High transaction volume with minimal latency tolerance
- Third-party vendors involved in portions of the codebase
- Custom APIs and payment logic lacked standardized validation
- PCI scope creep risk due to shared infrastructure components

---

## Security Strategy

### Network Segmentation and Scope Definition
- Deployed isolated Kubernetes clusters on GCP for the CDE
- Limited ingress/egress through Google Cloud Armor and internal Cloud NAT
- Built VPC Service Controls and firewall rules to restrict traffic to payment services
- Separated logging, monitoring, and CI/CD pipelines between CDE and non-CDE environments

### Application Security and Tokenization
- Integrated Stripe.js and Elements to tokenize CHD before reaching the backend
- Stored only non-sensitive tokens and transaction metadata in application DBs
- Hardened web application with HTTP security headers, CSRF protection, and input validation
- Implemented OpenAPI schema validation for all inbound API traffic

### Encryption and Key Management
- All transmission protected with TLS 1.2 or higher (HSTS enforced)
- Data at rest encrypted using Google CMEK (Customer-Managed Encryption Keys)
- Keys rotated quarterly and managed with GCP KMS policies aligned to PCI DSS 3.6

### Access Control and Monitoring
- Enforced least privilege using IAM roles scoped to microservices
- Mandatory MFA for all privileged users and developers accessing production
- Centralized log collection via Google Cloud Logging and integration with Chronicle SIEM
- Alerting pipelines for failed logins, code pushes to protected branches, and configuration drift

### Vulnerability and Patch Management
- Weekly SCA scans via Snyk and container image scans via Trivy
- WAF-enabled APIs protected with Google Cloud Armor custom ruleset
- Quarterly ASV scans via Tenable.io and annual pentest with retest validation
- Automated patch deployment pipeline for base images and application libraries

---

## Control Framework Mapping

| PCI DSS Requirement | Control Implementation |
|----------------------|------------------------|
| 1: Firewalls & Routers | VPC segmentation, Cloud Armor, NAT restrictions |
| 3: Protect CHD | Tokenization, TLS 1.2+, CMEK encryption |
| 6: Secure Systems | SAST, DAST, dependency scanning, secure SDLC policies |
| 7: Access Control | RBAC, MFA, scoped permissions, audit logging |
| 10: Logging & Monitoring | Cloud Logging, SIEM alerts, immutable storage |
| 11: Vulnerability Management | Trivy, Snyk, WAF, ASV scans, pentesting |
| 12: Policy & Governance | PCI policy, roles/responsibilities matrix, quarterly reviews |

---

## Outcome and Lessons Learned

- Successfully passed ROC audit with no major findings
- Reduced PCI scope by 70% through tokenization and microsegmentation
- Increased deployment velocity after integrating security gates into CI/CD
- SOC reduced alert fatigue by prioritizing CHD-related anomaly detections

### Lessons Learned
- Tokenization is your friend by moving CHD handling to third-party JS reduced audit complexity
- Early alignment with developers on OWASP Top 10 remediation saved rework late in testing
- Treat PCI DSS like a system design problem, not just a checklist AND architecture drove compliance

---

## Summary
This case study demonstrates how a custom e-commerce platform can be built to support business goals without compromising compliance. By tightly integrating PCI DSS 4.0.1 controls into the architecture and development lifecycle, the team ensured both agility and defensibility under regulatory scrutiny.


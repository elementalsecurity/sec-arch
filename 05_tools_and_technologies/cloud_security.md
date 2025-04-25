# Cloud Security Tools and Technologies

This document explores the tools and platforms Security Architects must evaluate when designing secure cloud environments. It covers core categories such as **cloud-native security services**, **infrastructure as code (IaC) scanning**, **identity and access management**, and **cloud workload protection**.

---

## Strategic Objectives
- Secure cloud infrastructure across multi-cloud environments
- Detect and respond to misconfigurations and active threats
- Ensure visibility, governance, and compliance in shared responsibility models
- Implement preventative and detective controls across compute, storage, network, and identity layers

---

## Cloud-Native Security Services

### AWS
- **AWS Security Hub**: Centralized findings aggregation from GuardDuty, Inspector, Macie
- **AWS Config**: Continuous resource compliance monitoring
- **Amazon GuardDuty**: Threat detection via DNS, VPC flow logs, and CloudTrail
- **IAM Access Analyzer**: Policy analysis and least privilege design

### Microsoft Azure
- **Microsoft Defender for Cloud**: CSPM and workload protection (VMs, containers, App Services)
- **Azure Policy & Blueprints**: Resource compliance and governance as code
- **Entra ID Protection**: Conditional access, identity risk scoring

### Google Cloud
- **Security Command Center (SCC)**: Asset inventory, misconfiguration scanning, threat detection
- **IAM Recommender**: Principle of least privilege suggestions
- **Cloud Armor**: DDoS protection and WAF

---

## Identity and Access Management (IAM)
- **AWS IAM**, **Azure Entra ID**, **GCP IAM**: Role-based access control, resource scoping, service accounts
- **CIEM Tools**: Ermetic, Sonrai, Palo Alto Prisma Cloud – Analyze and enforce least privilege across cloud IAM

---

## Cloud Workload Protection Platforms (CWPP)
Tools that secure compute workloads across IaaS, PaaS, and container environments:

- **Palo Alto Prisma Cloud**
- **Trend Micro Cloud One**
- **Microsoft Defender for Servers**
- **Lacework**
- **Aqua Security**

Capabilities often include:
- File integrity monitoring (FIM)
- Vulnerability scanning for images and hosts
- Runtime anomaly detection (behavioral)
- Container security and Kubernetes policy enforcement

---

## Cloud Security Posture Management (CSPM)
- Detects misconfigurations, policy violations, and insecure defaults
- Examples: Wiz, Orca Security, Prisma Cloud, Microsoft Defender for Cloud, AWS Config

Architects should prioritize:
- Multi-cloud coverage
- CIS/NIST policy packs
- Native integration with ticketing/SIEM/SOAR
- Near real-time scanning and remediation support

---

## Infrastructure as Code (IaC) Scanning
Security scanning of Terraform, CloudFormation, Bicep, etc. to detect misconfigurations before deployment.

| Tool | Description |
|------|-------------|
| **Checkov** | Open-source IaC scanner (Terraform, Kubernetes, etc.) by Bridgecrew |
| **tfsec** | Lightweight Terraform scanner |
| **Terrascan** | YAML/TOML/JSON policies, supports multiple IaC languages |
| **Snyk IaC** | SaaS-based scanning with GitHub/GitLab CI integration |
| **KICS** | Open-source multi-IaC scanner (by Checkmarx) |

---

## Cloud-Native Secrets Management
| Platform | Built-in Secrets Management |
|----------|------------------------------|
| **AWS Secrets Manager** | Rotation, encryption, audit, lambda integration |
| **Azure Key Vault** | RBAC + access policies, integration with Azure Pipelines |
| **GCP Secret Manager** | IAM-based access, API integration, versioning |

---

## Design Considerations for Architects
- Avoid multi-cloud vendor lock-in unless value justifies complexity
- Use **centralized logging (CloudTrail, Azure Monitor, GCP Logging)** for unified visibility
- Prioritize **native controls + layered commercial tooling** for defense-in-depth
- Map tooling to **compliance mandates** (e.g., PCI, HIPAA, ISO 27001)
- Build a **Cloud Security Reference Architecture** per provider

---

## Summary

Securing the cloud requires a deep understanding of provider-native controls and how third-party platforms can enhance visibility, enforcement, and response. Security Architects must be fluent in evaluating CSPM, CWPP, CIEM, and IaC tools, ensuring their selection aligns with the organization's operating model, maturity, and compliance obligations.
# Identity Governance and Privileged Access Management Tools

This document outlines key tools and technologies that Security Architects must understand to design secure and scalable identity governance and privileged access solutions. Identity is often the most targeted and exploited attack surface, and a mature identity program is essential for enforcing least privilege and regulatory compliance.

---

## Strategic Objectives

- Manage identity lifecycle across cloud, on-prem, and hybrid environments
- Enforce least privilege and access control policies
- Detect and prevent misuse of privileged accounts
- Demonstrate compliance with internal and external governance requirements

---

## Core Categories

### 1. Identity Governance and Administration (IGA)

IGA platforms manage the identity lifecycle, access requests, approvals, certifications, and policy enforcement.

| Tool | Description |
|------|-------------|
| **SailPoint IdentityNow** | Cloud-native IGA platform with access certification, role modeling, and analytics |
| **Saviynt** | Unified platform for IGA, application GRC, and privileged access management |
| **Microsoft Entra ID Governance** | Identity lifecycle, access reviews, and entitlements within Azure/M365 ecosystems |
| **One Identity Manager** | On-prem and hybrid IGA with SAP and AD integration |
| **IBM Security Verify** | Cloud and hybrid identity governance with adaptive access and analytics |

### Common IGA Functions
- Joiner/Mover/Leaver workflows
- Access review and attestation
- Separation of duties (SoD) policy enforcement
- Role-based access control (RBAC)
- Delegated administration

---

### 2. Privileged Access Management (PAM)

PAM platforms manage, monitor, and protect accounts with elevated privileges across infrastructure and applications.

| Tool | Description |
|------|-------------|
| **CyberArk** | Industry-leading vaulting, session monitoring, and credential brokering |
| **BeyondTrust** | Endpoint privilege management and secure remote access |
| **Delinea (formerly Thycotic)** | Secrets management, password vault, and session recording |
| **HashiCorp Vault** | API-driven secrets management and dynamic credential brokering for cloud and DevOps |
| **Senhasegura** | PAM with strong automation, certificate management, and cloud support |

### Core PAM Capabilities
- Vaulting and rotation of credentials (passwords, SSH keys, API tokens)
- Session recording and real-time monitoring
- Just-in-time (JIT) privilege elevation
- Adaptive access control and multi-factor authentication
- Integration with SIEM, ticketing, and workflow platforms

---

### 3. Directory Services and Identity Federation

| Technology | Description |
|------------|-------------|
| **Microsoft Entra ID (Azure AD)** | Cloud-based directory for modern access control and federation |
| **Active Directory (AD)** | Core on-premises directory for users, groups, and policy enforcement |
| **Okta Universal Directory** | Cloud identity store with integration to thousands of SaaS apps |
| **Ping Identity** | Identity federation, SSO, and access policies for hybrid environments |
| **ForgeRock Identity Platform** | Enterprise-grade IAM with full identity lifecycle and access orchestration |

---

## Design Considerations for Security Architects

- **Map access policies** to business roles and data sensitivity
- Use **automated access reviews** to reduce entitlement creep
- Enforce **MFA** and JIT access for all privileged operations
- Integrate IGA and PAM into **onboarding and offboarding workflows**
- Design for **zero trust principles**, not just perimeter security
- Consider **compliance obligations** (PCI, HIPAA, SOX, GDPR) in access control design

---

## Summary

Identity Governance and PAM tools are critical for securing access across enterprise environments. By integrating IGA for lifecycle governance and PAM for privilege control, Security Architects can design scalable, auditable, and compliant identity infrastructures that reduce insider risk and increase operational agility.
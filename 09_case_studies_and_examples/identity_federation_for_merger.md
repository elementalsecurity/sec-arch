# Case Study: Identity Federation for Post-Merger Integration

## Context and Business Problem
A large manufacturing conglomerate acquired a mid-sized regional brand to expand its European operations. Both companies operated mature IT environments, but with distinct identity infrastructures:
- The parent company used Microsoft Entra ID with hybrid on-prem AD
- The acquired entity relied entirely on Okta with multiple SaaS integrations

Business leaders required:
- Immediate but secure collaboration between merged teams
- Cross-tenant access to shared applications (ERP, document storage, DevOps tools)
- Gradual unification of user identity and access policy governance

The goal was to implement a secure identity federation architecture without breaking user workflows or delaying access to shared systems. Data protection requirements under GDPR, NIS2, and internal security policies mandated full auditability and role separation.

---

## Architecture Requirements
- Enable cross-directory authentication and SSO for users across both entities
- Support phased migration of identity services and access policies
- Ensure MFA enforcement and session trust evaluation in both environments
- Provide clear control boundaries for administrative accounts and privileged roles
- Support long-term consolidation to a unified governance model

---

## Constraints and Risks
- Short timeline for day-one access to merged systems
- GDPR requirement to minimize and audit cross-entity data flows
- Different MFA mechanisms in each directory (Okta Verify vs Microsoft Authenticator)
- Overlapping UPNs, domain names, and conflicting group naming conventions
- Risk of trust sprawl or access over-provisioning during the transition

---

## Security Strategy

### Identity Federation Architecture
- Established **cross-tenant B2B collaboration** using Microsoft Entra ID External Identities
- Configured **Okta-to-Entra SAML federation** for initial external access to Microsoft-hosted resources
- Standardized user principal name (UPN) normalization and suffix routing to reduce namespace collisions

### Access Governance
- Created shared security groups with scoped permissions and lifecycle governance
- Used **Access Packages in Microsoft Entitlement Management** to bundle resources, approval flows, and access reviews
- Limited guest access using Conditional Access with risk scoring, device checks, and session controls

### MFA and Trust Enforcement
- Required MFA in both tenants and enforced **strong authentication context propagation** between IdPs
- Tagged external users with risk flags and conditional access evaluation to reduce over-trust during federation
- Established **step-up authentication policies** for access to sensitive apps (ERP, HRIS, DevOps pipelines)

### Administrative Isolation
- Created separate M365 Admin Units for the acquired entity with scoped delegated admins
- Blocked elevation of external identities to privileged roles in either directory
- Segregated audit logging and reporting pipelines for cross-tenant activity

---

## Control Framework Mapping

| Domain | Controls Implemented |
|--------|----------------------|
| Identity Federation | SAML, Entra B2B, guest access policy enforcement |
| IAM Governance | Access Packages, periodic review automation, scoped roles |
| Authentication | MFA in both IdPs, conditional access policies, device compliance |
| Administrative Boundaries | Admin Units, role restriction, audit segregation |
| Compliance | Logging for all federated access, GDPR-aligned access scoping |

---

## Outcome and Lessons Learned

- Day-one collaboration across Teams, SharePoint, and Confluence achieved using SSO federation and access packages
- Migrated 74 SaaS apps from Okta to Entra SSO over 90 days with no critical downtime
- 98 percent of users successfully onboarded to MFA under the unified policy within 60 days
- Detected and blocked five access attempts from deprovisioned accounts during early consolidation

### Lessons Learned
- Don’t rush domain unification because namespace conflicts can silently break access
- Access packages simplify temporary or scoped collaboration across tenants
- MFA parity must be designed early to avoid inconsistent trust signals
- External identities need clear visibility and expiration policies

---

## Summary
This case study illustrates how identity federation can bridge disparate environments during M&A, enabling collaboration without compromising control. By focusing on structured governance, scoped privilege, and phased migration, organizations can unify identity over time without sacrificing agility or auditability.



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

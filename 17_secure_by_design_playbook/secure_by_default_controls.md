# Secure-by-Default Controls

Secure-by-Default means designing systems, products, and services so that the initial configuration prioritizes security without requiring users to take additional steps.

It is easier, safer, and more effective to start with secure settings that can be loosened with deliberate action than to start insecure and expect users to harden the system correctly.

This document outlines key principles and practices for implementing Secure-by-Default Controls.

---

## Why Secure-by-Default Matters

- **Reduces User Error:** Users often lack the expertise or time to configure systems securely on their own.
- **Increases Adoption of Secure Practices:** Friction is minimized when security is built in, not bolted on.
- **Minimizes Attack Surface:** Defaults enforce strong protection even for systems that are deployed quickly or forgotten over time.
- **Supports Compliance:** Many regulatory frameworks prefer or mandate Secure-by-Default settings.

---

## Core Principles for Secure-by-Default Controls

### 1. Deny by Default

Access to sensitive resources should be denied unless explicitly permitted.

**Examples:**
- New firewall rules deny all inbound traffic until specific rules are added.
- APIs require authentication and authorization for all endpoints by default.

---

### 2. Secure Communication by Default

All communication channels should be encrypted without requiring users to opt in.

**Examples:**
- Applications use HTTPS/TLS connections by default.
- Cloud storage services enable server-side encryption automatically.

---

### 3. Minimal Privilege Assignment

New accounts, roles, services, and components should have the fewest privileges necessary to function.

**Examples:**
- Default IAM roles for cloud services have read-only permissions.
- Database users are created without administrative rights unless explicitly granted.

---

### 4. Hardened System Configurations

Default system and service configurations should disable unnecessary features, ports, and services.

**Examples:**
- SSH access is disabled by default on cloud instances unless enabled by policy.
- Web servers ship with directory listing disabled and strong security headers applied.

---

### 5. Strong Identity and Access Requirements

Authentication and authorization mechanisms should be enforced from the start.

**Examples:**
- Multi-Factor Authentication (MFA) required for all administrative accounts.
- Default password policies require strong complexity and expiration settings.

---

### 6. Logging and Monitoring Enabled

Security-relevant events should be logged and monitored automatically.

**Examples:**
- Access logs are enabled by default on APIs and storage services.
- Administrative actions are logged and sent to centralized monitoring systems.

---

## Practical Guidelines for Architects

- Make security settings the easiest path, not an optional or hidden configuration.
- Clearly document secure defaults so that security teams and auditors can verify them.
- Enable audit logging for configuration changes to detect deviations from secure defaults.
- Regularly review and update defaults as threats and best practices evolve.
- Test user workflows to ensure that secure defaults do not create undue friction that encourages insecure workarounds.

---

*Designing Secure-by-Default is an act of leadership. It shifts the burden of security from individual users to system designers, improving safety for everyone without sacrificing usability.*



---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.

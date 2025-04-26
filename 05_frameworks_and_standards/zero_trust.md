# Zero Trust Architecture (ZTA)

Zero Trust Architecture (ZTA) is a security model that assumes no implicit trust (like me) inside or outside the network perimeter. Instead, it advocates for continuous verification of identities, devices, and access context, and restricts access to only what is necessary.

"Never trust, always verify."

## Core Principles of Zero Trust

1. **Verify Explicitly**
   - Authenticate and authorize every user, device, and application based on multiple factors (MFA, device health, risk, geolocation).

2. **Use Least Privilege Access**
   - Grant just-in-time (JIT) and just-enough-access (JEA), minimizing access scope and duration.

3. **Assume Breach**
   - Design systems with breach containment in mind (microsegmentation, kill chains, behavioral monitoring).

## Pillars of Zero Trust

1. **Identity**
   - Strong identity verification, MFA, and continuous monitoring
2. **Devices**
   - Device compliance checks, inventory management, EDR
3. **Applications and Workloads**
   - Secure access gateways, container security, secure DevOps practices
4. **Data**
   - Encryption, classification, DLP, data rights management
5. **Network**
   - Microsegmentation, software-defined perimeters, private access
6. **Visibility and Analytics**
   - Security telemetry, user behavior analytics (UBA), SIEM/SOAR integration

## Key Technologies Supporting ZTA

- Identity Providers (IdPs): Microsoft Entra, Okta, Ping
- Conditional Access and Risk-Based Policies
- Zero Trust Network Access (ZTNA) tools: Zscaler, Cloudflare, Palo Alto Prisma Access
- Endpoint Detection and Response (EDR)
- Microsegmentation Platforms: Illumio, Akamai Guardicore
- CASBs, DLP, SIEM, and SOAR platforms

## NIST SP 800-207: Zero Trust Architecture

This NIST publication defines a vendor-neutral approach to implementing ZTA:
- Abstract architecture components
- Logical design models
- Deployment scenarios

It provides a foundation for integrating Zero Trust into enterprise security architecture.

## Implementation Strategy

- Start with identity and access management
- Inventory and segment assets and data
- Adopt strong telemetry and analytics
- Align organizational policy and governance with ZTA principles
- Build incrementally with continuous validation

## Benefits

- Limits lateral movement
- Reduces insider and external threat impact
- Improves detection and containment
- Supports remote work and BYOD security

## Role of Security Architects

Security Architects are responsible for designing the trust boundaries and integrating Zero Trust principles across identity, access, network, and workload layers. They drive:
- Technical enforcement of ZTA policies
- Mapping of business needs to trust decisions
- Roadmaps for adopting Zero Trust in legacy and hybrid environments

ZTA is not a product but a strategic shift in security architecture that modern Security Architects must champion.


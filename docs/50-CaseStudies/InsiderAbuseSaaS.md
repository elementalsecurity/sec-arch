# Case Study: Insider Abuse in Multi-Tenant SaaS

**Overview**
A privileged employee exploited admin access to view and exfiltrate customer data from a multi-tenant SaaS platform.

## Incident Summary
- Platform: Multi-tenant SaaS for financial services
- Threat: Malicious insider with elevated permissions
- Outcome: Unauthorized data access for multiple tenants

## Root Cause Analysis
- Issue: Single admin role had full access to all tenant data
- No audit controls to detect abusive queries

## First Principles Review
- Invariant failure: Tenant isolation integrity was compromised
- Decomposition: Access control enforced only at application layer, not data layer
- Control objective: Enforce data isolation per tenant with mandatory audit
- Mechanism: Implement row-level security in database with tenant context enforced in query layer

## Lessons Learned
- Separate duties and enforce segmentation of admin roles
- Implement audit logging for all high privilege actions
- Use mandatory encryption with tenant-specific keys

## References
- OWASP Insider Threat Project
- Database row-level security documentation

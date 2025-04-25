# Security Architecture Reference Diagram Index

This document outlines suggested architecture diagrams that support visual understanding of key security design concepts. These diagrams are not exhaustive, but they serve as baseline illustrations to support documentation, presentations, or solution reviews. All visuals referenced here should be stored in a `secure_architecture_reference_diagrams/` subfolder of the `resources/` directory.

---

## 1. Zero Trust Logical Architecture
**Purpose**: Illustrates trust boundaries, policy enforcement points, and user-to-resource pathways.
- Components: Entra ID / IdP, Policy Engine, Resource Segments, Device Trust, Risk Signals
- Use: Executive briefings, roadmap slides, onboarding new architects

## 2. Cloud Segmentation Reference Diagram
**Purpose**: Shows hub-and-spoke network design with VPC/VNet segmentation and tiered trust zones.
- Components: Management VPC, App VPC, Data VPC, Transit Gateway, Firewall
- Use: Secure cloud landing zone design reviews

## 3. Data Flow Classification Example
**Purpose**: Depicts data movement across systems, with classification and protection markers.
- Components: Source Systems, Sensitive Data Flags, Transformation Layers, Storage Targets
- Use: Privacy reviews, risk assessments, compliance audits

## 4. Detection Pipeline Architecture
**Purpose**: Maps security telemetry ingestion, normalization, enrichment, and automated response.
- Components: Data Sources, SIEM, Threat Intel, SOAR, Incident Management
- Use: Detection engineering documentation and stakeholder visibility

## 5. Identity Federation for M&A Integration
**Purpose**: Shows Entra ID, Okta, or SAML federation between acquired and parent environments.
- Components: External Identities, Conditional Access, Trust Boundaries, Admin Isolation
- Use: Post-merger security planning, IAM unification strategy

## 6. Secure DevOps Flow (CI/CD Security Overlay)
**Purpose**: Illustrates security gates across the software delivery pipeline.
- Components: SCM, CI Pipelines, IaC Scanning, Secrets Detection, Artifact Signing, ArgoCD/GitOps
- Use: Secure SDLC governance, DevSecOps workshops

## 7. Application Security Zoning
**Purpose**: Demonstrates layered app architecture and security boundaries.
- Components: Presentation Layer, Business Logic, API Gateway, Data Services, Web WAF, DAST
- Use: AppSec program planning, SDLC coaching

---

## Diagram Format Recommendations
- Use **SVG** or high-resolution **PNG** for easy embedding
- Maintain consistent icons and labeling (consider Lucidchart or draw.io libraries)
- Version and document each diagram (e.g., v1.0, Last Reviewed Date)

---

## Summary
These reference diagrams provide visual anchors for explaining core security design decisions. They’re not just illustrations — they’re tools for education, alignment, and clarity. Every architecture file should include diagrams when possible.

> "A good diagram can clarify what 5 pages of text cannot. Build your visual library with care."


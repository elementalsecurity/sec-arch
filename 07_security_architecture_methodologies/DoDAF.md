# DODAF (Department of Defense Architecture Framework)

**DODAF** is a formal framework created by the U.S. Department of Defense (DoD) to define a structured approach for developing, presenting, and integrating systems architecture across all branches of defense operations. It enables decision-makers to design and assess complex systems with a focus on interoperability, lifecycle integration, and mission alignment.

---

## Purpose of DODAF

- Provide a comprehensive architecture framework for the development of integrated defense systems
- Enable effective communication across stakeholders through standardized architectural views
- Ensure alignment with mission needs, acquisition strategies, and compliance with defense regulations
- Support system-of-systems analysis and enterprise-wide decision making

---

## DODAF Viewpoints and Models

DODAF organizes architecture data into **eight viewpoints**, each with specific models (or "views") used to describe different aspects of the system:

### 1. **All Viewpoint (AV)**
Provides overarching context for all other views:
- AV-1: Overview and Summary Information
- AV-2: Integrated Dictionary (taxonomy and glossary)

### 2. **Capability Viewpoint (CV)**
Focuses on strategic capabilities and mission objectives:
- CV-1: Vision
- CV-2: Capability Taxonomy
- CV-3: Capability Phasing

### 3. **Operational Viewpoint (OV)**
Describes operational scenarios, activities, and information exchanges:
- OV-1: High-Level Operational Concept
- OV-2: Operational Resource Flow Description
- OV-5a/5b: Operational Activities and Processes
- OV-6a/6b/6c: Rules, Timelines, and Events

### 4. **Systems Viewpoint (SV)**
Details systems, their components, and interconnections:
- SV-1: Systems Interface Description
- SV-2: Systems Resource Flow
- SV-4: Functional Descriptions
- SV-6: Resource Flow Matrix

### 5. **Services Viewpoint (SvcV)**
Focuses on services (SOA and microservices architectures):
- SvcV-1: Services Context Description
- SvcV-4: Functional Services Description

### 6. **Standards Viewpoint (StdV)**
Specifies applicable standards and protocols:
- StdV-1: Standards Profile
- StdV-2: Standards Forecast

### 7. **Program Viewpoint (PV)**
Covers acquisition and project timelines:
- PV-1: Project Portfolio Relationships
- PV-2: Project Timelines

### 8. **Data and Information Viewpoint (DIV)**
Describes data relationships and structures:
- DIV-1: Conceptual Data Model
- DIV-2: Logical Data Model
- DIV-3: Physical Data Model

---

## Methodology and Meta-Model

DODAF is supported by the **DODAF Meta-Model (DM2)**, which ensures consistency across all viewpoints and supports integration with architectural tools. The DM2 outlines the structure and semantics of architectural data.

---

## Cybersecurity and Risk Alignment

Though DODAF does not define security controls directly, it supports cybersecurity integration through:
- Modeling of authorization boundaries, trust zones, and communication pathways
- Alignment with **RMF (NIST SP 800-37)** for accreditation and risk management
- Use of **OV**, **SV**, and **DIV** views for vulnerability, dependency, and threat modeling
- Integration with **NIST SP 800-160**, **NIST CSF**, and **MITRE ATT&CK** models

---

## Tool Support

| Tool | Capabilities |
|------|--------------|
| **Cameo Systems Modeler** | UAF, SysML, DoDAF integration |
| **Sparx EA** | DoDAF and DM2-compliant modeling |
| **ArchiMate with Custom Profiles** | Lightweight modeling overlays |
| **DoD-provided tools** | Customized repositories for internal use |

---

## Strategic Role for Security Architects

Security and Systems Architects use DODAF to:
- Document and analyze complex defense systems
- Identify security boundaries and integration points
- Model system interactions, data exchanges, and threat surfaces
- Provide traceability from mission goals to technical implementations

---

## Summary

DODAF offers a **multi-layered, formally structured methodology** for modeling and governing defense architectures. By leveraging its viewpoints and supporting tools, Security Architects can ensure that systems are resilient, compliant, and aligned with mission-critical objectives, making DODAF a foundational element in defense and high-assurance system design.
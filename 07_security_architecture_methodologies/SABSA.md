# SABSA (Sherwood Applied Business Security Architecture)

**SABSA** is a layered framework and methodology for developing business-driven, risk-aligned security architectures. Unlike general enterprise architecture frameworks, SABSA focuses explicitly on **security architecture** through a model that ties security objectives directly to business drivers.

---

## Purpose of SABSA

- Align security design and controls with business needs and risk
- Provide a traceable method from business attributes to technical controls
- Enable reusable architecture blueprints across projects and domains
- Establish governance, assurance, and lifecycle management for security architecture

---

## SABSA Layers of Architecture
SABSA adopts a layered approach, similar in concept to the Zachman framework:

| Layer | Focus | Key Question |
|-------|-------|---------------|
| **Contextual** | Business context and goals | Why are we doing this? |
| **Conceptual** | Business processes and security services | What needs to be done? |
| **Logical** | Architectures and policies | How will it be done? |
| **Physical** | Systems and technologies | With what will it be done? |
| **Component** | Product selection, configuration | Who will do it, and with what tools? |
| **Operational** | Run-time security operations | How is it managed and maintained? |

---

## SABSA Lifecycle Phases

1. **Strategy & Planning**
   - Derive security attributes from business risk and objectives
2. **Design**
   - Develop layered architecture views based on security services
3. **Implementation**
   - Deliver controls and processes that fulfill architectural models
4. **Operation**
   - Run, monitor, and maintain controls
5. **Governance**
   - Evaluate effectiveness and compliance, manage lifecycle

---

## Business Attributes Profiling
SABSA uses a taxonomy of **business attributes** (e.g., accountability, integrity, confidentiality, availability, trustworthiness) to:
- Link business objectives to security requirements
- Drive traceability across architectural layers

---

## Risk and Assurance in SABSA
- Risk management is central and continuous
- Provides assurance frameworks tied to attributes, metrics, and KPIs
- Enables qualitative and quantitative risk analysis

---

## SABSA vs. TOGAF

| Feature | SABSA | TOGAF |
|--------|-------|-------|
| Primary Focus | Security architecture and risk | Enterprise architecture (business + IT) |
| Structure | Layered (Zachman-like) | ADM Phases (iterative) |
| Traceability | End-to-end from risk to controls | Less granular traceability |
| Security Coverage | Comprehensive and explicit | Indirect (requires overlays) |

---

## Integration with Other Frameworks
- **TOGAF**: Align TOGAF ADM with SABSA layers for complete EA + security architecture
- **NIST CSF / ISO 27001**: Map SABSA controls to standards-based control catalogs
- **COBIT / ITIL**: Integrate SABSA’s governance principles into ITSM and IT governance

---

## Tooling and Artifacts
- SABSA Attribute Profiles
- Security Services Catalogs
- Security Policy Architecture
- Control Objectives Matrices
- Assurance Maps

---

## Summary

SABSA provides a **rigorous, structured methodology** for developing security architectures that are truly aligned to business risk and strategy. For Security Architects, SABSA bridges the gap between security operations, enterprise architecture, and governance by ensuring traceability, consistency, and defensibility across the entire lifecycle of the security program.


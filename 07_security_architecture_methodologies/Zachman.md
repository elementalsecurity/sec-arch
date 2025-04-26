# Zachman Framework for Enterprise Architecture

The **Zachman Framework** is one of the earliest and most foundational enterprise architecture frameworks. Developed by **John Zachman** in the 1980s, it provides a structured taxonomy for organizing architectural artifacts across multiple perspectives and abstraction levels.

Unlike methodology-based frameworks (e.g., TOGAF or DODAF), Zachman is a **classification schema**, not a process. It helps organizations answer the fundamental questions: *What, How, Where, Who, When, and Why* across key stakeholder viewpoints.

---

## Purpose of the Zachman Framework

- Organize and classify architectural artifacts across enterprise domains
- Enable consistency and traceability between business and IT views
- Support full lifecycle architecture planning and documentation
- Encourage comprehensive stakeholder coverage

---

## Structure of the Framework

The Zachman Framework is a **6x6 matrix**:

### Columns: Interrogatives
| Interrogative | Focus Area | Example |
|---------------|------------|---------|
| **What** | Data | Entity-relationship models, data catalogs |
| **How** | Function | Process models, logic flows |
| **Where** | Network | Infrastructure diagrams, physical distribution |
| **Who** | People | Organizational roles, actor models |
| **When** | Time | Events, schedules, SLAs |
| **Why** | Motivation | Business goals, rules, policies |

### Rows: Perspectives
| Perspective | Stakeholder | Focus |
|-------------|-------------|-------|
| **Planner** | Executive | Scope and business context |
| **Owner** | Business Manager | Business model and operations |
| **Designer** | Architect | Logical system architecture |
| **Builder** | Developer | Physical implementations |
| **Subcontractor** | Engineer | Component-level details |
| **Functioning System** | System in Use | Operational reality |

---

## Artifact Examples

| Perspective | What (Data) | How (Function) | Where (Network) |
|-------------|-------------|----------------|------------------|
| Planner | Business object list | Value chain model | Locations list |
| Owner | Semantic model | Business process model | Logistics architecture |
| Designer | Logical data model | Application architecture | Network topology diagram |
| Builder | Database schema | Program specs | Cloud infrastructure diagram |
| Subcontractor | SQL scripts | Code modules | Load balancer config |
| Functioning System | Data in motion | Executing processes | Live traffic maps |

---

## Strengths of Zachman

- Universally applicable regardless of technology or industry
- Clear separation of concerns
- Encourages holistic enterprise thinking
- Easily integrated with other frameworks (TOGAF, FEAF, SABSA)

---

## Limitations

- Not a methodology — no process or governance guidance
- Requires discipline to maintain artifact consistency
- Can be difficult to adopt without supporting practices/tools

---

## Integration with Security Architecture

- Overlay **SABSA business attributes** on rows to introduce security context
- Use Zachman to classify **risk, control, and audit artifacts** across stakeholder layers
- Map **compliance requirements** and **security policies** into motivation (Why) and functional (How) columns

---

## Tooling Support

- Most EA tools (Sparx EA, MEGA, BizzDesign) allow Zachman templates
- Spreadsheet and matrix-based modeling tools for entry-level adoption

---

## Summary

The **Zachman Framework** is a powerful classification tool for organizing complex enterprise systems. While not a methodology, it provides a foundational schema to ensure that every architectural perspective and question is addressed. Security Architects can use Zachman to map risks, controls, and governance across layers, making it a versatile addition to a mature architecture program.
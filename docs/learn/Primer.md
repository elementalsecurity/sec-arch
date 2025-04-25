# So You Want to Be a Security Architect?
### A Field Manual for Building - and - Breaking - Secure Systems

Welcome.
This repository is a public, vendor-neutral knowledge base that teaches security architecture from first principles all the way to runnable, cloud-native reference implementations. Clone it, fork it, rip it apart, improve it - just keep rigorous clarity.

---

## 1 Why This Repo Exists - Mission

>**Raise the bar** for security design across the industry by sharing battle-tested patterns, end-to-end reference architectures, and hands-on labs - free and forever.

We prioritise:

* First-principles reasoning over cargo-cult "best practices"
* Concrete artifacts (diagrams -> IaC -> tests) over slideware
* Open governance - every control or pattern is open to scrutiny and debate

---

## 2 Who Should Use This

| You are…                       | This repo gives you…                                  |
|--------------------------------|-------------------------------------------------------|
| **Practicing architect**       | Reference diagrams, trade-off logs, compliance overlays |
| **Cloud engineer / DevOps**    | IaC blueprints (Bicep, CDK, GCP Blueprints) you can deploy today |
| **GRC / compliance pro**       | Mappings from technical controls to PCI DSS 4.0, NIS 2, GDPR |
| **Student / career-changer**   | A structured learning path, labs, and first-principles drills |

---

## 3 Architect’s Core Mindset (Memorise These)

| Focus                   | Why It Matters                                            |
|-------------------------|-----------------------------------------------------------|
| **Systems Thinking**    | Controls interact - design the whole, not point fixes.    |
| **Risk Orientation**    | Architecture exists to manage business risk, not chase "perfect" security. |
| **Adversary Empathy**   | Model how a real attacker crosses each trust boundary.    |
| **Engineering Pragmatism** | Patterns must be deployable by real teams, under real deadlines. |
| **Continuous Learning** | Stacks change quarterly; mental models outlive products. |

---

## 4 First-Principles Thinking (30-second Version)

1. Define the irreducibles - the asset properties that must never break.
2. Decompose the system - minimal data-flow diagram; locate implicit trust.
3. Identify natural forces - adversary capabilities, entropy, human error.
4. Quantify risk - even rough math beats hand-waving.
5. Derive control objectives before naming products.
6. Select mechanisms last - ensure they can fail safe and be tested.
7. Validate with counter-examples - prove each invariant really holds.

*→ Full treatise in [First Principles](FirstPrinciples.md)*

---

## 5 Roadmap and Structure

To understand where this project is heading, visit the [Roadmap](../meta/Roadmap.md)

The site is organized into:

- **learn/** - Mental models and strategic mindset
- **patterns/** - Modular building blocks (e.g., IdentityBroker, mTLS)
- **reference/** - End-to-end architectures (Zero Trust, etc.)
- **guides/** - IaC-based deployment walkthroughs
- **labs/** - Interactive exercises
- **case-studies/** - Breach deep dives
- **compliance/** - PCI, NIS2, GDPR mappings
- **meta/** - Roadmap, changelog, contributor standards

---

## 6 Quick Start

```bash
git clone https://github.com/<you>/security-architecture-kb.git
cd security-architecture-kb
python -m venv .venv && source .venv/bin/activate
pip install mkdocs-material
mkdocs serve
```

Visit http://127.0.0.1:8000 to browse the docs site.

---

## 7 Licensing

This repo follows a dual-license model:

- Code & Infrastructure-as-Code — Apache 2.0 (LICENSE-APACHE)
- Documentation — Creative Commons BY-SA 4.0 (LICENSE-CC-BY-SA)

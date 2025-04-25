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

*→ Full treatise in docs/05-FirstPrinciples/First-Principles-Thinking.md.*

---

## 5 Repository Layout (CamelCase)

```text
docs/
  index.md
  05-FirstPrinciples/
  10-ReferenceArchitectures/
      ZeroTrust/
  20-Patterns/
  30-ImplementationGuides/
  40-Labs/
  50-CaseStudies/
  60-ComplianceOverlays/
  90-Meta/
scripts/
.github/workflows/
```

---

## 6 Roadmap (live status)

| Phase | Goal                                                        | Status |
|-------|-------------------------------------------------------------|--------|
| 0     | Bootstrap repo + CI scaffold                                | ✅     |
| 1     | Publish primer & first principles                           | ✅     |
| 2     | MkDocs site auto-deploy to GitHub Pages                     | ⬜     |
| 3     | Full ZeroTrust reference architecture                       | ⬜     |
| 4     | PCI DSS 4.0 overlay                                         | ⬜     |
| 5     | Cloud-native labs (Azure Bicep → AWS CDK → GCP Blueprint)   | ⬜     |
| 6     | External contribution model (DCO, labels, PR templates)     | ⬜     |
| 7     | Public launch & office hours                                | ⬜     |

---

## 7 Quick Start

```bash
git clone https://github.com/<you>/security-architecture-kb.git
cd security-architecture-kb
python -m venv .venv && source .venv/bin/activate
pip install mkdocs-material
mkdocs serve
```

---

## 8 Contributing

1. Fork → feature branch → PR.
2. Sign commits (`git commit -s`).
3. Pass Markdown lint & docs build workflows.
4. For new patterns or controls: include threat description, design rationale, and tests/lint for any IaC.

See CONTRIBUTING.md for full details.

---

## 9 Licensing

This repo follows a dual-license model:

* Code & IaC — Apache 2.0 (LICENSE-APACHE)
* Documentation — Creative Commons BY-SA 4.0 (LICENSE-CC-BY-SA)

See NOTICE for directory mapping.

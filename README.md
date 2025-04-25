# So You Want to Be a Security Architect?
### A Field Manual for Building - and - Breaking - Secure Systems

Welcome. This repository is a public, vendor-neutral knowledge base that teaches security architecture from first principles through cloud-native reference implementations. Clone it, fork it, and adapt it while maintaining rigorous clarity.

## Why This Repo Exists - Mission

Raise the bar for security design by sharing battle-tested patterns, end-to-end reference architectures, and hands-on labs - free and forever.

## Who Should Use This

| You are...                 | This repo gives you...                                                  |
|----------------------------|--------------------------------------------------------------------------|
| Practicing security architect | Reference diagrams, trade-off logs, compliance mappings                |
| Cloud engineer / DevOps      | Deployable IaC blueprints (Bicep, CDK, GCP Blueprints)                |
| GRC / compliance professional | Controls mapped to PCI DSS, NIS 2, GDPR, ISO 27001                     |
| Learner / career-changer     | Structured learning paths, labs, and first-principles exercises        |

## Architect’s Core Mindset

- Systems thinking - design the whole system, not point fixes  
- Risk orientation - manage business risk, not chase perfect security  
- Adversary empathy - model real attackers crossing trust boundaries  
- Engineering pragmatism - ensure patterns are deployable under real constraints  
- Continuous learning - mental models outlast any single product  

## Documentation Structure

- Primer & First Principles - core mental models  
- Reference Architectures - ZeroTrust design  
- Patterns - reusable control building blocks  
- Implementation Guides - step-by-step IaC playbooks  
- Labs - hands-on exercise environments  
- Case Studies - real-world post-mortems  
- Compliance Overlays - controls mapped to regulations  
- Meta - project roadmap and style guide  

## Roadmap

For details on upcoming phases and current status, see [docs/90-Meta/Roadmap.md](docs/90-Meta/Roadmap.md).

## Quick Start

```bash
git clone https://github.com/<you>/security-architecture-kb.git
cd security-architecture-kb
python -m venv .venv && source .venv/bin/activate
pip install mkdocs-material
mkdocs serve
```

Open http://127.0.0.1:8000 in your browser.

## Contributing

Fork the repo, create a feature branch, and open a pull request. Sign commits with -s, then pass the lint and docs build workflows. See CONTRIBUTING.md for more details.

## Licensing

This repo uses a dual-license model:
- Code & IaC - Apache 2.0 (LICENSE-APACHE)  
- Documentation - Creative Commons BY-SA 4.0 (LICENSE-CC-BY-SA)  

See NOTICE for directory mappings.

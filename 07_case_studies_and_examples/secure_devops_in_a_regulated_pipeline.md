# Case Study: Secure DevOps in a Regulated CI/CD Pipeline

## Context and Business Problem
A health-tech startup building a SaaS platform for patient engagement needed to implement a full CI/CD pipeline that complied with HIPAA and supported continuous deployment. The platform handled protected health information (PHI) and was hosted on AWS using containerized microservices.

The engineering team required:
- Automated build, test, and deploy workflows
- Integration of security controls without slowing down development
- Coverage for vulnerability management, secrets detection, and auditability
- Compliance with HIPAA Security Rule and third-party SOC 2 audit requirements

---

## Architecture Requirements
- Implement a secure SDLC with integrated code, dependency, and IaC scanning
- Ensure least privilege access and auditability for pipeline users and automation accounts
- Detect and prevent secrets leakage in code repositories
- Ensure artifacts and infrastructure met security baselines before deployment
- Provide evidence of compliance through automated logs, reports, and policy enforcement

---

## Constraints and Risks
- Lean DevOps team with limited security engineering resources
- Rapid release cycles and short sprints (weekly deploys)
- Use of open-source libraries and third-party APIs
- Developers had access to production namespaces for hotfixing
- PHI had to be encrypted and access-controlled throughout the deployment lifecycle

---

## Security Strategy

### Pipeline Security Design
- CI/CD platform: GitHub Actions with GitHub Enterprise
- Infrastructure as Code (IaC): Terraform with OPA-based policy-as-code (Checkov)
- Secrets Management: HashiCorp Vault with GitHub Actions integration via dynamic credentials

### Secure Build and Scan Phases
- Static Application Security Testing (SAST) using Semgrep during PR review
- Software Composition Analysis (SCA) with Snyk for open-source dependency risk
- IaC scanning with tfsec and Checkov on every Terraform plan
- Docker image scanning with Trivy during build step
- Custom workflows enforced required pass/fail gates before merge to main branch

### Artifact Signing and Promotion
- All Docker images signed with Cosign before promotion
- Artifacts stored in AWS ECR with lifecycle policies and version tracking
- Approved artifacts manually reviewed and promoted through staging to prod

### Deployment and Runtime Protections
- Environments deployed via ArgoCD with GitOps workflows
- PodSecurity Policies and OPA Gatekeeper enforced runtime constraints
- PHI encrypted at rest using AWS KMS and in transit using TLS 1.2+
- Audit logging via AWS CloudTrail and Kubernetes Audit Logs aggregated in Elastic

### Access Control and Compliance
- IAM roles scoped per GitHub Action runner with time-limited session tokens
- Developers removed from direct production access post-migration to GitOps
- Compliance dashboard built with real-time checks for:
  - Code review enforcement
  - Secrets detection incidents
  - Deployment approvals and logs
  - Failed security scans

---

## Control Framework Mapping

| HIPAA Safeguard | Control Implementation |
|-----------------|------------------------|
| Access Control | Scoped IAM roles, Vault-based secrets, role reviews |
| Audit Controls | Full CI/CD logging, GitHub audit trail, CloudTrail, EKS audit logs |
| Integrity | Artifact signing, image immutability, GitOps with merge protections |
| Transmission Security | TLS 1.2+, mTLS between services, network segmentation |
| Workforce Security | PR approval workflows, Just-in-Time access controls |

---

## Outcome and Lessons Learned

- Maintained weekly release cadence while passing third-party SOC 2 Type II audit
- Identified and remediated 124 critical and high SCA vulnerabilities within 90 days
- Replaced 100+ hardcoded secrets with Vault-managed dynamic secrets
- Developers gained confidence in automation through clear logging and visibility

### Lessons Learned
- Early investment in policy-as-code pays off — Checkov and Gatekeeper prevented bad infrastructure from reaching prod
- Secrets detection should happen pre-commit — GitHub Advanced Security added after an incident exposed test credentials
- Build trust through transparency — dashboards showing scan results, access logs, and compliance helped bridge gaps between DevOps and InfoSec

---

## Summary
This case study demonstrates how regulated DevOps environments can achieve both speed and security. By embedding controls into the pipeline and aligning them with HIPAA safeguards and SOC 2 principles, the engineering team delivered with confidence, precision, and audit-readiness. Security became a feature of the platform, not a barrier to innovation.
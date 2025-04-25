# Case Study: Kubernetes RBAC Misconfiguration

**Overview**
A misconfigured Role and RoleBinding granted cluster-admin privileges to a service account, enabling full control of the cluster.

## Incident Summary
- Environment: Production Kubernetes cluster
- Misconfiguration: RoleBinding applied at cluster scope instead of namespace
- Outcome: Service account was able to delete all namespaces and workloads

## Root Cause Analysis
- Issue: Failure to apply least privilege principle in RBAC setup
- Missing reviews in deployment pipeline allowed the error to persist

## First Principles Review
- Invariant failure: Integrity of cluster state was not protected
- Decomposition: RBAC definitions were defined in a shared YAML without isolation
- Control objective: Ensure RBAC roles are scoped to intended resources
- Mechanism: Use namespace-limited Role and RoleBinding with strict role-check pipeline tests

## Lessons Learned
- Adopt templates that enforce scope in IaC
- Include RBAC policy tests in CI pipeline
- Monitor for creation of high-privilege bindings

## References
- Kubernetes documentation on RBAC
- CIS Kubernetes Benchmark recommendations

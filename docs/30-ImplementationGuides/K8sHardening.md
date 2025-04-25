# Kubernetes Hardening Guide

**Summary**  
Harden a Kubernetes cluster using PodSecurity, network policies, and CIS benchmark controls.

## Prerequisites
- kubectl configured for the target cluster
- Cluster Admin or equivalent privileges
- Access to apply admission controller configurations

## Steps
1. **Enable PodSecurity Admission**  
   Define `restricted` policies for production namespaces.  
2. **Implement Network Policies**  
   Use Calico or Cilium to restrict pod-to-pod communication.  
3. **CIS Benchmark Controls**  
   Audit and remediate based on the CIS Kubernetes Benchmark.  
4. **RBAC Hardening**  
   Create minimal roles and bindings; avoid `cluster-admin`.  
5. **Admission Controllers**  
   Enable `ImagePolicyWebhook`, `SecurityContextDeny`, and others.  

## Example Snippet
```yaml
apiVersion: policy/v1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  runAsUser:
    rule: 'MustRunAsNonRoot'
```

## References
- CIS Kubernetes Benchmark v1.6  
- Kubernetes PodSecurity Admission Documentation  

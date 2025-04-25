# Zero Trust GCP Deployment Lab (Blueprint)

**Objective**  
Deploy a Zero Trust foundation in GCP using Deployment Manager or Blueprint YAML.

## Prerequisites
- gcloud CLI authenticated
- GCP project with Owner role
- Deployment Manager or Terraform CLI

## Lab Steps
1. Clone blueprint repository:
   ```bash
   git clone https://github.com/<org>/gcp-zero-trust-lab.git
   ```
2. Review `foundation.yaml` for network and IAM definitions.
3. Deploy blueprint:
   ```bash
   gcloud deployment-manager deployments create zero-trust --config foundation.yaml
   ```
4. Test access controls by attempting cross-project resource reads without IAM bindings.

## Validation
- Inspect Cloud IAM policies for least-privilege.
- Check VPC Service Controls perimeter logs.

## Cleanup
```bash
gcloud deployment-manager deployments delete zero-trust
```

## References
- Google Cloud Foundation blueprint  
- GCP VPC Service Controls documentation  

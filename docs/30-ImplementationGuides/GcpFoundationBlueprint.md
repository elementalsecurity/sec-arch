# GCP Foundation Blueprint

**Summary**  
Implement a GCP foundation blueprint using Deployment Manager or Terraform Blueprint YAML for organization, networking, IAM, and logging.

## Prerequisites
- gcloud CLI installed and authenticated
- Deployment Manager or Terraform CLI configured
- GCP Organization and billing account access

## Steps
1. **Organization & Folders**  
   Create folders for Shared Services, Security, and Workloads.  
2. **Networking**  
   - Deploy VPC with shared VPC host project and service projects.  
   - Configure subnets, firewall rules, and Private Google Access.  
3. **IAM Structure**  
   - Assign IAM roles at folder and project levels.  
   - Implement least-privilege via custom roles.  
4. **Logging & Monitoring**  
   - Enable Cloud Audit Logs and VPC Flow Logs.  
   - Deploy Logging sink to centralized logging project.  
5. **Policy Enforcement**  
   - Define Organization Policy constraints (e.g., restrict regions).  
   - Apply Folder-level policy assignments.  

## Example Snippet
```yaml
resources:
- name: vpc-network
  type: compute.v1.network
  properties:
    autoCreateSubnetworks: false
```

## References
- Google Cloud Foundation toolkit  
- GCP Deployment Manager Docs  

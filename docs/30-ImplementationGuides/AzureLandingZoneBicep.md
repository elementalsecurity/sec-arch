# Azure Landing Zone with Bicep

**Summary**  
Deploy a scalable Azure landing zone using Bicep modules, including networking, resource groups, management groups, and policy assignments.

## Prerequisites
- Azure CLI installed and authenticated
- Bicep CLI installed
- Appropriate Azure subscription with contributor access
- Git repository for source control

## Steps
1. **Bootstrap management groups**  
   Define root, landing zones, and subscription management groups in `managementGroups.bicep`.
2. **Networking**  
   - `networking.bicep`: Deploy virtual network, subnets (hub, spoke, firewall).  
   - Configure peering between hub and spokes.
3. **Resource Organizations**  
   - Deploy resource groups for identity, shared services, logging, and workload.  
   - Tag resources with environment and cost center.
4. **Policy and Blueprint**  
   - `policyDefinitions.bicep`: Assign policies for resource naming, tag enforcement, and security baseline.  
   - Deploy Initiative definitions and assignments.
5. **Shared Services**  
   - Deploy Azure Firewall or NAC in the hub.  
   - Configure managed identity and Key Vault for secrets.
6. **CI/CD Pipeline**  
   - Configure GitHub Actions or Azure Pipelines to build and deploy Bicep on push to main.

## Example Snippet
```bicep
module network 'networking.bicep' = {
  name: 'networkDeployment'
  params: {
    vnetName: 'landingZone-vnet'
    addressPrefixes: [
      '10.0.0.0/16'
      '10.1.0.0/16'
    ]
  }
}
```

## References
- Microsoft Cloud Adoption Framework  
- Azure Bicep Documentation  

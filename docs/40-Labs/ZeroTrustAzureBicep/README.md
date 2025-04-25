# Zero Trust Azure Deployment Lab (Bicep)

**Objective**  
Deploy a basic Zero Trust environment in Azure using Bicep modules.

## Prerequisites
- Azure CLI and Bicep CLI installed
- Contributor access to an Azure subscription
- GitHub repo with Bicep modules for network, identity, and logging

## Lab Steps
1. Clone the lab repository.
   ```bash
   git clone https://github.com/<org>/ZeroTrust-Azure-Lab.git
   ```
2. Review `main.bicep` and understand module structure.
3. Deploy the resources:
   ```bash
   az deployment sub create --location eastus --template-file main.bicep
   ```
4. Verify resource groups: `LandingZone-RG`, `Identity-RG`, `Logging-RG`.
5. Test Zero Trust policy by attempting to access a VM in the spoke without proper identity token.

## Validation
- Confirm Azure Policy enforcement for tagging and naming standards.
- Inspect logs in Log Analytics for denied network flows.

## Cleanup
```bash
az group delete --name LandingZone-RG --yes --no-wait
az group delete --name Identity-RG --yes --no-wait
az group delete --name Logging-RG --yes --no-wait
```

## References
- Microsoft Cloud Adoption Framework for Azure  
- Azure Bicep documentation  

# Purple Team Logging and Detection Lab

**Objective**  
Simulate an adversary attack and validate detection rules using cloud-native logging pipelines.

## Prerequisites
- Lab environment with vulnerable app and SIEM integration
- Access to CloudWatch or Azure Monitor
- Scripts for simulating attacks

## Lab Steps
1. Deploy vulnerable application:
   ```bash
   terraform apply -var-file=dev.tfvars
   ```
2. Run attack simulation:
   ```bash
   ./attack-simulate.sh --phishing --lateral-movement
   ```
3. Observe logs in SIEM: filter for suspicious authentication events.
4. Tweak detection rule and test again:
   - Modify regex in `detection-rule.yml`.
   - Re-run attack simulation.

## Validation
- Confirm SIEM alerts are generated for simulated attacks.
- Review dashboard visualizing attack timelines.

## Cleanup
```bash
terraform destroy -var-file=dev.tfvars
```

## References
- MITRE ATT&CK Framework  
- OCSF Logging Guide  

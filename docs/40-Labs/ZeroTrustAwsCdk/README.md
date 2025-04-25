# Zero Trust AWS Deployment Lab (CDK)

**Objective**  
Use AWS CDK to deploy a Zero Trust multi-account landing zone and verify service segmentation.

## Prerequisites
- AWS CLI and AWS CDK installed
- AWS account with Administrator access
- Node.js environment

## Lab Steps
1. Initialize CDK app:
   ```bash
   cd aws-zero-trust-lab
   cdk bootstrap aws://<ACCOUNT_ID>/us-east-1
   ```
2. Inspect stacks: `NetworkStack`, `IdentityStack`, `LoggingStack`.
3. Deploy stacks:
   ```bash
   cdk deploy NetworkStack IdentityStack LoggingStack
   ```
4. Validate network segmentation by testing connectivity between isolated subnets.

## Validation
- Check AWS Config rules for VPC flow logs.
- Verify IAM roles and trust relationships in the Identity OU.

## Cleanup
```bash
cdk destroy LoggingStack IdentityStack NetworkStack
```

## References
- AWS CDK Documentation  
- AWS Well-Architected Framework  

# Case Study: Capital One S3 Breach

**Overview**
In 2019, a misconfigured web application firewall allowed unauthorized access to AWS S3 buckets, exposing data of over 100 million customers.

## Incident Summary
- Target: Capital One cloud environment on AWS
- Attack vector: SSRF vulnerability against a metadata service
- Outcome: Data exfiltration from S3 buckets

## Root Cause Analysis
- Issue: Identity and Access Management policies were overly permissive for metadata role
- Lack of segmentation allowed lateral movement between compute and storage

## First Principles Review
- Invariant failure: Confidentiality was not enforced at the data-plane level
- Decomposition: Shared IAM roles with wide scope
- Control objective: Enforce least privilege on metadata access
- Mechanism: Use separate roles for metadata retrieval and restrict network paths

## Lessons Learned
- Always isolate metadata endpoints behind stricter controls
- Implement fine grained IAM roles per workload
- Monitor API calls to metadata service and log anomalies

## References
- https://www.sec.gov/Archives/edgar/data/0001300953/000130095319000048/a201910caponeex21.htm
- AWS security blog posts on the breach

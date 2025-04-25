# PCI DSS 4.0.1 Overlay for ZeroTrust Reference Architecture

This document maps ZeroTrust controls to PCI DSS 4.0.1 requirements.

| ZeroTrust Control                          | PCI DSS Requirement             |
|--------------------------------------------|---------------------------------|
| Short-lived JWTs + anomaly detection       | 8.2.5 – Invalidate sessions     |
| Sidecar proxies with mutual TLS            | 4.1 – Encrypt all non-console traffic |
| Envelope encryption via KMS                | 3.4 – Render PAN unreadable     |
| Centralized logging + SIEM ingestion       | 10.2 – Implementation of audit trails |
| Policy-as-code drift prevention            | 11.2 – Vulnerability scanning   |

_Further mappings to be filled out in detail._

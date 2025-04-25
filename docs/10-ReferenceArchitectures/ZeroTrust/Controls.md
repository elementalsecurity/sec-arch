Risk Scenario | Control Objective | Mechanism / Implementation
Compromised credentials (phish) | Block replayed tokens and detect stolen sessions | Short-lived JWTs + anomaly detection
Lateral movement after breach | Prevent east-west without re-auth at each trust boundary | Sidecar enforcement + mutual TLS
Data-at-rest exfiltration | Ensure tenant-specific keys with audit-grade logging | Envelope encryption via KMS; SIEM ingest
# Controls Mapping

| Risk Scenario                   | Control Objective                                | Mechanism / Implementation              |
|---------------------------------|--------------------------------------------------|-----------------------------------------|
| Compromised credentials (phish) | Block replayed tokens and detect session theft   | Short-lived JWTs and anomaly detection  |
| Lateral movement after breach   | Enforce re-authentication at each trust boundary | Sidecar proxies with mutual TLS         |
| Data-at-rest exfiltration       | Enforce tenant-specific encryption with audit logs | Envelope encryption via KMS and logging |

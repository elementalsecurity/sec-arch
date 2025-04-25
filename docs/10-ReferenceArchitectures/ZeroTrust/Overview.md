# Zero Trust Reference Architecture – Overview

## 1. Context & Scope
- Business drivers (cloud adoption, perimeter erosion, regulatory mandates)
- In-scope workloads (VMs, containers, serverless, SaaS integrations)
- Out-of-scope items (legacy on-prem apps, OT networks, etc.)

## 2. Objectives & Design Principles
- Never implicitly trust any network segment or identity
- Enforce least privilege end-to-end
- Ensure strong telemetry for detection & audit
- Automate policy-as-code for drift prevention

## 3. High-Level Components
- Identity broker (AuthN/AuthZ)
- Policy enforcement points (API gateway, sidecar proxies)
- Data protection plane (KMS, envelope encryption)
- Telemetry & detection ingestion

## 4. Threat Model Summary
- Primary adversaries (insider, supply-chain compromise, credential theft)
- Key attack vectors we mitigate

## 5. How to Read the Diagram
- Legend for trust boundaries, control zones, and data flows
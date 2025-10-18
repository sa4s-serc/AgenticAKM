---
### ADR-005: Decouple inference and retraining as separate pipelines

Status: Inferred
Context: Dedicated scripts inference.py and retrain.py, plus MAPE plan/execute stages, indicate a separation between online/offline tasks and controlled retraining triggers.
Decision: Keep inference and retraining in separate, invocable scripts, orchestrated by the MAPE-K loop or manual operators.
Consequences:
- Positive: Operational simplicity; safer rollouts and retries; easier resource isolation and scheduling.
- Negative: Requires coordination for model versioning and deployment; potential lag between detection and updated model availability.
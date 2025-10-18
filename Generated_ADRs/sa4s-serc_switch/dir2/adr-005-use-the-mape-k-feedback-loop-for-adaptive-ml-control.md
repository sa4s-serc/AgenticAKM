---
### ADR-005: Use the MAPE-K feedback loop for adaptive ML control

Status: Inferred
Context: NAVIE includes modules named Monitor, Analyzer, Planner, and Execute along with knowledge files (knowledge.csv, naive_knowledge.csv, model.csv, metrics.csv, monitor.csv), suggesting a self-adaptive control loop.
Decision: Structure the adaptive ML system around the MAPE-K pattern—monitoring runtime metrics, analyzing conditions, planning adaptations, and executing changes using a knowledge base.
Consequences:
- Positive: Clear separation of adaptive concerns; easier experimentation with adaptation strategies; extensible knowledge-driven control.
- Negative: Additional architectural complexity; requires robust knowledge curation and consistency across loop components.
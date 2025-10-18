---
### ADR-002: Implement MAPE-K components as modular Python modules orchestrated by a single entry point (App.py)

Status: Inferred
Context: Files include App.py alongside Monitor/Analyzer/Planner/Execute modules and process.py, suggesting centralized orchestration in a single process.
Decision: Implement each MAPE-K phase as a Python module and coordinate them via a central orchestrator (App.py) rather than distributed services.
Consequences:
- Positive: Simplifies development, debugging, and reproducible experiments; lowers deployment complexity.
- Negative: Limits scalability and fault isolation compared to microservices; tighter coupling to Python runtime.
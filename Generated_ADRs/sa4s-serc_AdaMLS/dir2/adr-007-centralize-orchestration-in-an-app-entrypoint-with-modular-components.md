---
### ADR-007: Centralize orchestration in an App entrypoint with modular components

**Status:** Inferred
**Context:** Each pipeline folder contains App.py alongside Monitor/Analyzer/Planner/Execute modules and a command.sh. This indicates a central coordinator invoking modular steps.
**Decision:** Use App.py as the orchestrator that wires Monitor, Analyzer, Planner, and Execute; execution is initiated via command-line scripts.
**Consequences:** 
- Positive: Clear execution flow, easy to run experiments, and straightforward lifecycle control. 
- Negative: Tighter coupling in a single process; harder to distribute components across nodes. 
- Trade-off: Favored a monolithic but modular composition for simplicity over distributed microservices.
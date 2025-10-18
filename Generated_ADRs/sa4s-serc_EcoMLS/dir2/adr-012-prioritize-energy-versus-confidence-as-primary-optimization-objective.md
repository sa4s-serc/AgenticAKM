---
### ADR-012: Prioritize energy versus confidence as primary optimization objective

Status: Inferred
Context: Multiple outputs focus on Energy vs Confidence trends across EcoMLS and baselines; plots and result files target this trade-off.
Decision: Define the core optimization objective as minimizing energy consumption while achieving acceptable prediction confidence, guiding analyzer/planner logic.
Consequences:
- Positive: Aligns the system with energy-aware ML serving goals; measurable, comparable outcomes.
- Negative: Other QoS metrics (latency/throughput) may receive less emphasis; potential trade-offs not fully explored.
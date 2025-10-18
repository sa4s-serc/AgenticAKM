---
### ADR-013: Bridge mode to aggregate or proxy metrics

Status: Inferred
Context: bridge.c and BRIDGE.md, plus remote.c, suggest a mode to bridge/aggregate metrics from remote instances.
Decision: Implement a bridge capability to proxy or consolidate metrics across nodes/exporters.
Consequences:
- Positive: Centralized scraping; simplifies network topology; can overcome connectivity constraints.
- Negative: Adds complexity and potential bottlenecks; careful loop/duplication avoidance required.
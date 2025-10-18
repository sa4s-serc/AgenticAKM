---
### ADR-011: Embed benchmarking, capacity search, and workload generation

Status: Inferred
Context: sarathi/benchmark contains a comprehensive framework: request generators (synthetic, trace), interval/length distributions (Poisson, Gamma, Zipf), capacity search orchestration with Ray, and visualization dependencies (matplotlib, seaborn, plotly).
Decision: Ship an integrated benchmarking and capacity search suite to evaluate scheduling/block policies and deployment capacity under realistic and synthetic loads.
Consequences:
- Positive: Data-driven optimization; reproducible experiments; easier regression detection.
- Negative: Additional maintenance and dependencies; increases repository scope.
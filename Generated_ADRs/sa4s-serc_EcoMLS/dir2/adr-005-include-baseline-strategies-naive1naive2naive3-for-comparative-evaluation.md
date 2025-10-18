---
### ADR-005: Include baseline strategies (NAIVE1/NAIVE2/NAIVE3) for comparative evaluation

Status: Inferred
Context: NAIVE1/2/3 each provide Analyzer.py and Planner.py; Results have separate logs/energy files per NAIVE variant.
Decision: Implement and evaluate naive Analyzer/Planner baselines alongside EcoMLS to benchmark adaptive strategies.
Consequences:
- Positive: Provides experimental baselines; clarifies benefits of the adaptive approach; supports ablation studies.
- Negative: Increases maintenance burden; potential duplication across planners/analyzers.
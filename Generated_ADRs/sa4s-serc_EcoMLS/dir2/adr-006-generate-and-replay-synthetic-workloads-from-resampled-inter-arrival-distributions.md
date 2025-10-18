---
### ADR-006: Generate and replay synthetic workloads from resampled inter-arrival distributions

Status: Inferred
Context: resampled_scaled_inter_arrivals.csv and Request_send.py indicate workload generation; no evidence of integration with an external live system.
Decision: Use a synthetic request generator based on resampled inter-arrival times to drive controlled experiments.
Consequences:
- Positive: Repeatable, controllable load; facilitates deterministic comparisons across strategies.
- Negative: May not reflect real-world variability; limits external validity of energy/confidence results.
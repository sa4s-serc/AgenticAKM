---
### ADR-009: Use Locust for workload generation and inter-arrival modeling

Status: Inferred
Context: Locust is pinned in requirements; port 8089 exposed; Experiments include inter_arrival_rate_* CSVs and load/log artifacts; Request_send.py present.
Decision: Employ Locust for synthetic workload generation and rate control during experimentation, using CSV-defined inter-arrival profiles.
Consequences:
- Positive: Repeatable and controlled performance testing; integrated developer workflow; ties into monitoring/metrics.
- Negative: Additional operational component to run/manage; load generation can skew resource usage on shared hosts.
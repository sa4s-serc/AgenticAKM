---
### ADR-013: Expose application metrics and provide a Grafana dashboard

Status: Inferred
Context: routes/metrics.ts and monitoring/grafana-dashboard.json are present; an “exposedMetricsChallenge” also exists.
Decision: Provide a metrics endpoint (Prometheus-style) and a reference Grafana dashboard for observability.
Consequences:
- Positive: Improves operability and demos observability practices.
- Negative: Potential information exposure if misconfigured; additional monitoring infrastructure needed.
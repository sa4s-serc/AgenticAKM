---
### ADR-005: Prometheus as the primary observability integration via an embedded HTTP endpoint

Status: Inferred
Context: prometheus.c, prometheus_client.c, http.c, docs (Prometheus and Grafana) and dashboards indicate Prometheus exposition as the primary interface.
Decision: Expose metrics using the Prometheus text format over HTTP.
Consequences:
- Positive: Standard integration with Prometheus and Grafana; easy adoption in cloud-native stacks.
- Negative: Assumes Prometheus-style pull model; less direct support for other telemetry systems without adapters.
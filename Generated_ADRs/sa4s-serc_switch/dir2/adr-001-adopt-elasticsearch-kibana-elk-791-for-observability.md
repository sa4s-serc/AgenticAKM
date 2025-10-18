### ADR-001: Adopt Elasticsearch + Kibana (ELK) 7.9.1 for observability

Status: Inferred
Context: The system generates logs and metrics for ML experiments and runtime behavior (e.g., NAVIE/logs, metrics_to_es.py, logs_to_es.py, Experiments/Exported_*). A consistent way to store, explore, and visualize these data is required during development and experimentation.
Decision: Provision a single-node Elasticsearch 7.9.1 and Kibana 7.9.1 stack via docker-compose for local observability, exposing ports 9200 and 5601 on a dedicated elk network.
Consequences:
- Positive: Quick, reproducible local observability; easy dashboarding via Kibana; straightforward developer setup.
- Negative: Older ES/Kibana version; no authentication enabled (dev only); not horizontally scalable; production hardening required.
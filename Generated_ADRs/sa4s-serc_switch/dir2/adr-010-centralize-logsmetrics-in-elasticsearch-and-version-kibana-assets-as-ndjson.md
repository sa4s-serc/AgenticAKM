---
### ADR-010: Centralize logs/metrics in Elasticsearch and version Kibana assets as NDJSON

Status: Inferred
Context: Scripts logs_to_es.py and metrics_to_es.py, export.ndjson files (root and NAVIE/) and exported logs/metrics under Experiments indicate ES ingestion and Kibana asset versioning.
Decision: Push runtime logs and metrics to ES via custom scripts and keep Kibana saved objects as NDJSON files in the repo for reproducible dashboards.
Consequences:
- Positive: Consistent, automatable observability setup; dashboards are reproducible and reviewable in code review.
- Negative: Tight coupling to ES 7.9.* formats/APIs; manual import/export steps unless scripted; migration effort when upgrading ELK.
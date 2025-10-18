---
### ADR-012: Bootstrap services with shell scripts rather than containerizing each service

Status: Inferred
Context: Numerous bootstrap-*.sh scripts across services; only Kafka uses docker-compose; most app services don’t have Dockerfiles in the repo.
Decision: Use shell bootstrap scripts for installing dependencies and starting services; containerize only infrastructure like Kafka.
Consequences:
- Positive: Quick start for development; fewer containerization tasks initially.
- Negative: Harder to standardize deployments; environment drift; more challenging CI/CD and scaling in production.
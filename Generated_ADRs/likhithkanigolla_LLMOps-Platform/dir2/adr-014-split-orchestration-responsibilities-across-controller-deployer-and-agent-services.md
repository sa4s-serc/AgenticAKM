---
### ADR-014: Split orchestration responsibilities across controller, deployer, and agent services

Status: Inferred
Context: Presence of controller-Service (with Kafka setup), deployer-service/server.py, and agent services suggests a layered orchestration model: controller coordinates, deployer handles deployment logic, agents execute on hosts.
Decision: Separate orchestration concerns into controller (workflow and events), deployer (deployment actions), and agents (execution and telemetry).
Consequences:
- Positive: Clear responsibility boundaries; improved testability; scalability by tier.
- Negative: More inter-service communication; requires robust observability and retries to manage cross-service workflows.
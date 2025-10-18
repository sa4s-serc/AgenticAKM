---
### ADR-006: Use agent processes to manage deployments via the Docker Python SDK and system metrics (psutil)

Status: Inferred
Context: agent-Service/agent.py and vm-service/agent.py both depend on docker and psutil; agents likely run on target hosts/VMs to manage containers and report status.
Decision: Deploy lightweight agents on target machines to orchestrate Docker containers and gather host metrics using psutil.
Consequences:
- Positive: Fine-grained control of deployments; locality-aware operations; reduced central controller load.
- Negative: Requires secure agent management, upgrades, and authentication; increases the number of moving parts and potential failure points.
---
### ADR-004: Orchestrate Services with Docker Compose

Status: Inferred
Context: docker-compose.yml defines a multi-service setup (app + sqliteweb), a custom network, shared volumes, and .env-based configuration. Compose simplifies local development and deployment for small stacks.
Decision: Use Docker Compose (version 3.8) to define and run the application and auxiliary services.
Consequences: Provides a repeatable, single-command setup and clear service boundaries. It couples local development and deployment to Docker, and scaling/production concerns (e.g., swarm/Kubernetes) would require additional work.
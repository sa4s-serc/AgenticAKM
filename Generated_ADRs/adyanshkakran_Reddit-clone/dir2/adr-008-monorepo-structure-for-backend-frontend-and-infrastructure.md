---
### ADR-008: Monorepo structure for backend, frontend, and infrastructure

Status: Inferred
Context: The repo contains backend/, frontend/, and nginx/ directories, plus a single docker-compose.yml at the root.
Decision: Keep all services and infra configuration in a single repository to streamline development and orchestration.
Consequences:
- Positive: Single source of truth; easier local orchestration; simplified CI/CD pipelines across services.
- Negative: Larger repository size; potential coupling of release cycles; requires discipline to manage boundaries.
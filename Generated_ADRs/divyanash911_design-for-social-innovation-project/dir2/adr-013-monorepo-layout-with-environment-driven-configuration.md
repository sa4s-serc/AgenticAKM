---
### ADR-013: Monorepo layout with environment-driven configuration

Status: Inferred
Context: Frontend and backend live under code/; backend has sample.env and uses python-dotenv.
Decision: Keep frontend and backend in a single repository with environment variables managed via .env for backend configuration.
Consequences:
- Positive: Easier coordination and shared versioning; straightforward local setup.
- Negative: Mixed tech stacks increase repo complexity; deployment pipelines must target subprojects explicitly.
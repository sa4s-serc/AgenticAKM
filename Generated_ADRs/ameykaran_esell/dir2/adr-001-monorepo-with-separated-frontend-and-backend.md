### ADR-001: Monorepo with separated frontend and backend

Status: Inferred
Context: The repository contains distinct frontend and backend directories, each with its own tooling and dependency management (Node/Next.js in frontend, Python/FastAPI in backend).
Decision: Use a single monorepo with logical separation between a Next.js frontend and a FastAPI backend.
Consequences: 
- Positive: Clear separation of concerns; independent build/deploy pipelines; easier local development for full-stack work.
- Negative: Requires coordinating versioning and cross-cutting changes; CI/CD needs to handle two ecosystems.
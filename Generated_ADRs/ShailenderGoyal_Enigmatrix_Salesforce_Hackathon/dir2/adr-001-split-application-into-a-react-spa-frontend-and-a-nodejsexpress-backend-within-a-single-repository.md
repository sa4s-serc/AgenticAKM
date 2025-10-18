### ADR-001: Split application into a React SPA frontend and a Node.js/Express backend within a single repository

Status: Inferred
Context: The repository contains a client application under learn-spark-ai-buddy and a server application under server, each with its own package.json and tooling. The application domain includes AI chat, knowledge base, notes, pre-assessment, and user management, which benefits from a clear separation between UI/UX concerns and backend services.
Decision: Adopt a two-tier architecture with a React SPA frontend and a Node.js/Express backend, co-located in a single repository for convenience.
Consequences: 
- Positive: Clear separation of concerns; independent build/run pipelines; easier local development across FE/BE; cohesive versioning.
- Negative: Requires CORS and API contract management; no shared types between FE/BE by default; CI/CD must handle two build artifacts.
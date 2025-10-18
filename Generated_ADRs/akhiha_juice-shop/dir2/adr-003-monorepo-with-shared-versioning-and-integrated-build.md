---
### ADR-003: Monorepo with shared versioning and integrated build

Status: Inferred
Context: The repository hosts both backend and frontend. Root package.json postinstall builds frontend and then server. The version is synchronized (17.1.1) across root and frontend.
Decision: Keep backend and frontend in a single repository with shared lifecycle scripts and coordinated versioning.
Consequences:
- Positive: Simplifies coordination and releases; consistent versioning; easier cross-cutting changes.
- Negative: Heavier installs; tighter coupling; CI/CD pipelines need careful caching and orchestration.
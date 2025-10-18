---
### ADR-011: Use a single solution to organize multiple projects

Status: Inferred
Context: carbonQL.sln aggregates carbonQLBackend and carbonQLConsole; the console ships with the backend DLL.
Decision: Manage all related projects within a single solution for coordinated development.
Consequences:
- Positive: Easier navigation, consistent configuration, simplified local builds and debugging across projects.
- Negative: Tight coupling of repo lifecycle across components; scaling to many independent services may require restructuring later.
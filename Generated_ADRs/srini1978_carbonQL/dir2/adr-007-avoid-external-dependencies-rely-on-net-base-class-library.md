---
### ADR-007: Avoid external dependencies; rely on .NET Base Class Library

Status: Inferred
Context: NuGet asset files (project.assets.json) and build artifacts show no third-party dependencies; only standard SDK-generated files are present.
Decision: Implement functionality using only the .NET Base Class Library, avoiding third-party packages.
Consequences:
- Positive: Simpler builds, fewer security and licensing concerns, reduced supply chain risk.
- Negative: Potentially more custom code and effort; missing out on established libraries that could accelerate development.
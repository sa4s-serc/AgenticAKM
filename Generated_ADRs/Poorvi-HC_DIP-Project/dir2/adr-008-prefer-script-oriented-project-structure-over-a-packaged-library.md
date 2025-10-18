---
### ADR-008: Prefer script-oriented project structure over a packaged library

Status: Inferred
Context: The repository is a flat collection of scripts without packaging metadata or module hierarchy, indicating a research/prototype orientation.
Decision: Organize the project as executable scripts in a single directory rather than a fully packaged Python library.
Consequences:
- Positive: Minimal setup, easy to run and modify; suitable for short-lived experiments and academic work.
- Negative: Limited reusability and testability; no enforced APIs; harder integration into larger systems and CI/CD pipelines.
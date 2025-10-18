---
### ADR-016: Packaging with pyproject and Reproducible Environments

Status: Inferred
Context: The library requires modern Python packaging and reproducibility across environments.
Decision: Use pyproject.toml for packaging; include a uv.lock for dependency locking; separate documentation environment (docs/ with Pipfile and requirements.txt).
Consequences:
- Positive: Standards-compliant packaging; reproducible installs; isolation between core and docs dependencies.
- Negative: Multiple environment definitions to maintain (pyproject, uv, Pipfile/requirements for docs); potential drift between locks.
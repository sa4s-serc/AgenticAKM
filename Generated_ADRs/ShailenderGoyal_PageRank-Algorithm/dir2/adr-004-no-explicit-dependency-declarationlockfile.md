---
### ADR-004: No explicit dependency declaration/lockfile

**Status:** Inferred
**Context:** The repository lacks common dependency manifests (requirements.txt, pyproject.toml, Pipfile, poetry.lock). Dependency information is therefore not declared in the repo.
**Decision:** Omit an explicit dependency manifest; rely on implicit imports or standard library.
**Consequences:** 
- Positive: Lower maintenance overhead if only standard library is used; simpler repository.
- Negative: If third-party packages are needed, users must infer and install them manually; no version pinning; reproducibility and onboarding may suffer.
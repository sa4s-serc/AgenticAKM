---
### ADR-006: Defer formal testing and CI/CD integration

**Status:** Inferred
**Context:** No test files or CI configuration files (e.g., .github/workflows/, .gitlab-ci.yml) are listed. This suggests automated testing and CI/CD are not established in-repo.
**Decision:** Proceed without committed automated tests and CI/CD configuration.
**Consequences:** 
- Positive: Faster initial development; reduced setup complexity.
- Negative: Higher risk of regressions; manual verification required; more difficult to ensure quality and repeatable builds.
---
### ADR-006: Continuous Integration using Travis CI

Status: Inferred
Context: Presence of .travis.yml indicates automated CI builds configured on Travis CI.
Decision: Use Travis CI to build, test, and validate the project on commits and pull requests.
Consequences:
- Positive: Automated feedback loop; easy integration for open-source workflows.
- Negative: Service limitations/quotas; Travis CI’s ecosystem and support have evolved, possibly requiring migration in the future.
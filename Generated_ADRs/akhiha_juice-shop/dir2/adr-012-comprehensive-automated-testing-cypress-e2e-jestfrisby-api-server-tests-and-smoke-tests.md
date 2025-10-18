---
### ADR-012: Comprehensive automated testing: Cypress E2E, Jest/Frisby API, server tests, and smoke tests

Status: Inferred
Context: test/cypress for E2E, Jest setup and Frisby API tests, server-side unit tests, plus a separate smoke test Docker image.
Decision: Adopt a layered testing approach with E2E (Cypress), API tests (Jest/Frisby), server tests, and a containerized smoke test.
Consequences:
- Positive: High confidence in quality; good coverage across layers; facilitates CI pipelines.
- Negative: Longer CI time; requires maintenance as features and routes evolve.
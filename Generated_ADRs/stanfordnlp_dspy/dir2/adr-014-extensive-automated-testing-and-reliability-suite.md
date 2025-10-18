---
### ADR-014: Extensive Automated Testing and Reliability Suite

Status: Inferred
Context: The framework spans many modules (adapters, clients, predictors, optimizers, datasets) and must be reliable across providers and data types.
Decision: Implement broad unit/integration tests (tests/...), including reliability suites that generate complex schemas/programs, and an in-repo LiteLLM test server for end-to-end flows.
Consequences:
- Positive: Higher stability and confidence; regression protection across diverse features.
- Negative: Longer CI times; test flakiness risk with external services; maintenance overhead.
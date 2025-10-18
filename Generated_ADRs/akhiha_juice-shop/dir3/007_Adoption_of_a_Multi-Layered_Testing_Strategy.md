# ADR-007: Adoption of a Multi-Layered Testing Strategy

**Date**: 2025-10-10
**Status**: Proposed

## Context
As a mature and complex open-source project, ensuring correctness, preventing regressions, and validating both intended functionality and the deliberate vulnerabilities required a rigorous testing approach.

## Decision
A multi-layered testing strategy was implemented using different frameworks for each layer: Cypress for end-to-end browser testing, Jest and Frisby for API testing, and Mocha/Chai for server-side unit and integration tests.

## Consequences
This comprehensive approach provides very high confidence in the stability and correctness of the application. It allows for the detection of a wide range of issues from UI defects to API contract violations. The drawback is an increased learning curve for new contributors, who may need to be familiar with multiple testing ecosystems, and a longer execution time for the full test suite.
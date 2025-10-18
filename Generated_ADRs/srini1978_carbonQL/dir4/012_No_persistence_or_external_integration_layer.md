# ADR-012: No persistence or external integration layer

**Date**: 2025-10-09
**Status**: Proposed

## Context
Only in-memory models and calculations are indicated; no data access or API clients are present.

## Decision
Focus on computational logic without adding storage or integration concerns.

## Consequences
Keeps the domain logic simple and self-contained. Adding databases or external services later will require introducing new layers (e.g., repositories, gateways) and refactoring to isolate side effects.
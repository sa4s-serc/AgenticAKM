# ADR-006: Shared candidate selection utility

**Date**: 2025-10-14
**Status**: Proposed

## Context
Algorithms use a helper (find_closest2.py) to rank/select likely frame matches based on similarity signals.

## Decision
Factor common candidate-ranking logic into a reusable utility module.

## Consequences
Pros: consistency across algorithms, reduced duplication, centralized optimization point. Cons: creates a shared dependency/API that must remain stable; potential single bottleneck if inefficient.
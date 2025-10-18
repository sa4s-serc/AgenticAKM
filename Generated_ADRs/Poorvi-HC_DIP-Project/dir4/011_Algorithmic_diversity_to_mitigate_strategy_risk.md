# ADR-011: Algorithmic diversity to mitigate strategy risk

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository includes greedy growth, end-candidate comparison, pair/group seeding with merging, and a model-augmented variant.

## Decision
Pursue multiple complementary heuristics for temporal ordering rather than committing to a single approach early.

## Consequences
Pros: broader coverage across data regimes; enables comparative analysis and ensemble opportunities. Cons: increased maintenance and testing surface; requires robust, shared evaluation.
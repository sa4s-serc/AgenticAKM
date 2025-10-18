# ADR-012: Precompute-and-reuse design for scalability

**Date**: 2025-10-14
**Status**: Proposed

## Context
Feature extraction is an expensive step executed once, with artifacts reused across training and reconstruction runs.

## Decision
Cache preprocessed frames and features to amortize cost across experiments.

## Consequences
Pros: significant time savings for iterative research; facilitates hyperparameter sweeps. Cons: storage overhead; must detect staleness and manage cache invalidation when code/parameters change.
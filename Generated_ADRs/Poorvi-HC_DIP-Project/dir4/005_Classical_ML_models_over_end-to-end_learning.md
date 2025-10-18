# ADR-005: Classical ML models over end-to-end learning

**Date**: 2025-10-14
**Status**: Proposed

## Context
Training utilities provide SVM and linear regression for scoring adjacency or similarity, trained on precomputed features.

## Decision
Adopt lightweight, classical models trained on fixed features rather than deep, end-to-end models.

## Consequences
Pros: faster training, simpler dependencies, easier interpretability and integration. Cons: potential performance ceiling vs. deep models; greater reliance on feature quality/engineering.
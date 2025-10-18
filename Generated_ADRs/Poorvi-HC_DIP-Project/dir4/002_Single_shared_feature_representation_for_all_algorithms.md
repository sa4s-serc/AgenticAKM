# ADR-002: Single shared feature representation for all algorithms

**Date**: 2025-10-14
**Status**: Proposed

## Context
All five reconstruction algorithms consume the same precomputed per-frame features/keypoints.

## Decision
Centralize feature extraction in extract_features.py and treat the resulting artifact as the contract across algorithms.

## Consequences
Pros: fair comparability across methods, faster iteration (one extraction for many runs), simplified benchmarking. Cons: algorithms are constrained by the chosen feature schema; any schema change forces re-extraction and coordinated updates.
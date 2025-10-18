# ADR-007: Ground-truth mapping preserved for evaluation

**Date**: 2025-10-14
**Status**: Proposed

## Context
shuffle_frames.py records the original-to-shuffled index mapping to support metrics and validation.

## Decision
Persist the shuffle mapping as an artifact separate from the video for later evaluation.

## Consequences
Pros: precise metric computation and reproducibility. Cons: requires careful handling to avoid leakage into reconstruction steps; adds artifact management overhead.
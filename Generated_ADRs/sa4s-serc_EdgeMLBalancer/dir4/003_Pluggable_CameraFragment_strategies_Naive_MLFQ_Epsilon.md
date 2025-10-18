# ADR-003: Pluggable CameraFragment strategies (Naive, MLFQ, Epsilon)

**Date**: 2025-10-10
**Status**: Proposed

## Context
Three alternative CameraFragment.kt implementations exist in parallel directories, suggesting experimentation with scheduling/selection policies.

## Decision
Maintain multiple fragment implementations to compare and iterate on runtime scheduling strategies (e.g., naive vs. MLFQ vs. epsilon-based).

## Consequences
Enables A/B comparisons and rapid experimentation but increases code duplication and integration burden; a canonical implementation and abstraction boundaries are needed for maintainability.
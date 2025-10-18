# ADR-014: In-model instrumentation hooks for profiling

**Date**: 2025-10-14
**Status**: Proposed

## Context
To diagnose bottlenecks, visibility is needed inside the model forward paths in addition to end-to-end metrics.

## Decision
Integrate optional CUDA timing and profiling hooks within model execution paths (e.g., Falcon, Mixtral) tied into the central metrics system.

## Consequences
Facilitates fine-grained performance tuning with minimal code intrusion; must be carefully gated to avoid perturbing performance during production runs.
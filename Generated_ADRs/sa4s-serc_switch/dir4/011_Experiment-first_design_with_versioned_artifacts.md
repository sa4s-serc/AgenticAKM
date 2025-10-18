# ADR-011: Experiment-first design with versioned artifacts

**Date**: 2025-10-10
**Status**: Proposed

## Context
Research requires reproducibility and traceability of adaptive behavior under varied workloads.

## Decision
Check in experiment logs, metrics, inter-arrival profiles, and notebooks to generate/switch workload traces.

## Consequences
Enables repeatable benchmarking and regression; simplifies analysis; increases repository size and risk of stale artifacts; requires curation to avoid leaking sensitive data.
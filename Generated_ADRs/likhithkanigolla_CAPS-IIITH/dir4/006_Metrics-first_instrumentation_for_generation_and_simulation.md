# ADR-006: Metrics-first instrumentation for generation and simulation

**Date**: 2025-10-09
**Status**: Proposed

## Context
Evaluating LLM-assisted generation and simulation performance requires observability and reproducibility.

## Decision
Integrate metrics collection (LLM token/usage, timing, codegen stats, runtime/memory) with dedicated tooling and stored results under llmbased/metrics_results.

## Consequences
Enables empirical comparisons, cost tracking, and debugging; introduces runtime overhead and data management concerns; improves auditability of LLM behavior and pipeline health.
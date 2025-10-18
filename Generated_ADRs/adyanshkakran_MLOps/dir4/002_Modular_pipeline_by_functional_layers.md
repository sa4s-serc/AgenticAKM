# ADR-002: Modular pipeline by functional layers

**Date**: 2025-10-14
**Status**: Proposed

## Context
Separate modules exist for data loading, model setup, training, evaluation, saving, and orchestration.

## Decision
Structure the codebase into small, single-responsibility modules (data.py, model.py, train.py, eval.py, save.py, pipeline.py).

## Consequences
Improves clarity, reuse, and testability of components, but introduces coordination overhead and some duplication (e.g., persistence overlapping with MLflow).
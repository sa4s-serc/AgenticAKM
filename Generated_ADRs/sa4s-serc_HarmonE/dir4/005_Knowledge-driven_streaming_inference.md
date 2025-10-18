# ADR-005: Knowledge-driven streaming inference

**Date**: 2025-10-09
**Status**: Proposed

## Context
The active model for streaming predictions must reflect the latest adaptation decisions.

## Decision
inference.py reads knowledge/model.csv at each step to select the current model; it logs per-inference predictions, true values, chosen model, latency, and energy.

## Consequences
Tight coupling between adaptation outcomes and runtime inference; complete traceability per prediction. File-read overhead each step and potential race conditions without locking.
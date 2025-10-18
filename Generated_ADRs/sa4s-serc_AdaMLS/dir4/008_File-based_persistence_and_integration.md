# ADR-008: File-based persistence and integration

**Date**: 2025-10-10
**Status**: Proposed

## Context
Experiments prioritize simplicity, inspectability, and reproducibility over distributed robustness.

## Decision
Use CSVs for telemetry and decisions, pickles for models, and shell scripts/notebooks to orchestrate runs and analysis.

## Consequences
Low barrier to entry and easy post-hoc analysis; limited concurrency guarantees and potential file-locking issues; not ideal for production-scale, multi-process deployments.
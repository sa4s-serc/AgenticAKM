# ADR-007: Script-based orchestration without a workflow engine

**Date**: 2025-10-14
**Status**: Proposed

## Context
An imperative pipeline.py coordinates data loading, training, evaluation, and saving.

## Decision
Compose the end-to-end workflow in a simple Python script rather than using a workflow/DAG tool.

## Consequences
Keeps the system lightweight and easy to run locally, but limits scalability, parameterization, scheduling, retries, and observability typical of orchestration platforms.
# ADR-013: Evaluation-first design with comprehensive logging and visualization

**Date**: 2025-10-10
**Status**: Proposed

## Context
Demonstrating gains in utility and switching behavior is essential for validation.

## Decision
Persist per-strategy logs (e.g., AdaMLS_log.csv, NAVIE_log.csv, Nano_log.csv) and provide notebooks to plot utility and switching timelines.

## Consequences
Traceability and quick insight into behavior; manual, notebook-driven workflows are less CI-friendly; encourages data-driven iteration.
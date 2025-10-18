# ADR-012: Single repository as RL sandbox

**Date**: 2025-10-14
**Status**: Proposed

## Context
Mix of trading tasks and classic benchmarks, multiple algorithms, utilities like plot.py, stats CSVs, and saved checkpoints.

## Decision
Use one repo as a general-purpose RL experimentation workspace rather than separate domain-specific projects.

## Consequences
Convenient for iterative research and cross-pollination of ideas; increases cognitive load, encourages heterogeneous patterns, and can blur boundaries between domain-specific assumptions and general RL best practices.
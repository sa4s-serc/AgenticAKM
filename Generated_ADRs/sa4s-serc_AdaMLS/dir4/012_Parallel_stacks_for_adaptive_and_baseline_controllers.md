# ADR-012: Parallel stacks for adaptive and baseline controllers

**Date**: 2025-10-10
**Status**: Proposed

## Context
Isolation reduces coupling and allows independent evolution of strategies.

## Decision
Maintain AdaMLS/ and NAVIE/ directories with analogous modules (App, Monitor, Analyzer, Planner, Execute).

## Consequences
Clean separation and easier comparisons; duplicates code patterns and raises risk of inconsistencies; shared utilities may be beneficial long-term.
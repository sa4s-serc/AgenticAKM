# ADR-011: Unified policy layer for scheduling and admission control

**Date**: 2025-10-14
**Status**: Proposed

## Context
Scheduling heuristics and admission control must be applied consistently regardless of the underlying scheduler implementation.

## Decision
Introduce a policy layer that encapsulates common heuristics and admission logic, decoupled from individual scheduler mechanics.

## Consequences
Simplifies experimentation with policies and ensures consistent behavior; risks abstraction leakage if policies need scheduler-specific nuances.
# ADR-001: Explicit MAPE-K feedback-loop architecture

**Date**: 2025-10-09
**Status**: Proposed

## Context
The system must continuously balance predictive accuracy and energy consumption for streaming time-series workloads under data drift.

## Decision
Implement the control logic as a clear MAPE-K decomposition with dedicated modules (Monitor, Analyse, Plan, Execute) and a Manage layer to orchestrate iterations.

## Consequences
Improves separation of concerns, testability, and extensibility of adaptation logic; enables auditing of each phase. Adds coordination overhead and requires consistent state passing across modules.
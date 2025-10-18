# ADR-011: Manual hyperparameter and architecture variation

**Date**: 2025-10-14
**Status**: Proposed

## Context
Logs and directories include architectural hints like 2x256-…; multiple runs per algorithm/environment exist.

## Decision
Vary network sizes and hyperparameters manually across runs without an integrated sweeper.

## Consequences
Quick ad hoc exploration; lacks systematic search, provenance tracking, and reproducibility; harder to aggregate results or guarantee fair comparisons.
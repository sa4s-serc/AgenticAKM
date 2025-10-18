# ADR-008: Knowledge base as rolling aggregates

**Date**: 2025-10-10
**Status**: Proposed

## Context
The planner needs up-to-date yet stable estimates of per-model energy and confidence to score options reliably.

## Decision
Analyzer computes and maintains rolling averages of energy and confidence for each model in knowledge.csv.

## Consequences
Smoothing improves robustness to noise and reduces memory needs. It can lag during workload shifts, loses distributional/contextual information, and may bias decisions under non-stationarity.
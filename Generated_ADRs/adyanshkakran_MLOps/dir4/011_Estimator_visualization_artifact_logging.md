# ADR-011: Estimator visualization artifact logging

**Date**: 2025-10-14
**Status**: Proposed

## Context
Each run contains an estimator.html artifact with an interactive view of the estimator and its hyperparameters.

## Decision
Generate and log HTML visualizations of the estimator as part of the experiment artifacts.

## Consequences
Improves transparency and reviewability of model configurations at low additional cost, with minor storage overhead.
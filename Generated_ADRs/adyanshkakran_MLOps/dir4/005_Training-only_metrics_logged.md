# ADR-005: Training-only metrics logged

**Date**: 2025-10-14
**Status**: Proposed

## Context
MLflow runs show only training metrics (MAE, MSE, RMSE, R2, score) with no validation/test metrics logged.

## Decision
Evaluate and log model performance on training data only.

## Consequences
Speeds up runs and simplifies instrumentation, but increases overfitting risk and yields overly optimistic, non-generalizable metrics.
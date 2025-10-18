# ADR-003: Use of Ensemble Models Over Simple Linear Models

**Date**: 2025-10-14
**Status**: Proposed

## Context
The regression problem at hand likely involved complex, non-linear relationships in the data that a simple linear model could not capture effectively, necessitating a more powerful modeling approach.

## Decision
Despite the project's name, tree-based ensemble models (inferred to be RandomForestRegressor) were selected over a basic linear regression model. This was evidenced by the logged hyperparameters like `n_estimators` and `max_depth`.

## Consequences
This choice likely led to significantly higher predictive accuracy and better overall performance on the task. The increased model complexity is effectively managed and documented via MLflow, but it also results in a less interpretable model and a misleading project name which could cause confusion.
# ADR-003: Tree-ensemble regressor as default model

**Date**: 2025-10-14
**Status**: Proposed

## Context
Logged parameters align with scikit-learn RandomForestRegressor despite the package name suggesting linear regression.

## Decision
Adopt a RandomForestRegressor as the primary estimator for the regression pipeline.

## Consequences
Provides robust non-linear performance and sensible defaults, but reduces interpretability versus linear models and creates naming mismatch that can confuse users.
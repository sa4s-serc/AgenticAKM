# ADR-010: MLflow autologging for scikit-learn

**Date**: 2025-10-14
**Status**: Proposed

## Context
Runs include standard scikit-learn metrics, parameters, estimator.html, and environment artifacts consistent with MLflow autologging behavior.

## Decision
Use MLflow autologging to automatically capture parameters, metrics, model artifacts, and visualizations.

## Consequences
Minimizes boilerplate and ensures consistent logging, but reduces control over what gets logged and can miss custom evaluation logic without additional instrumentation.
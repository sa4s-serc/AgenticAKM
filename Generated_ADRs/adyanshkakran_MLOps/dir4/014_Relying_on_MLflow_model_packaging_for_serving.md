# ADR-014: Relying on MLflow model packaging for serving

**Date**: 2025-10-14
**Status**: Proposed

## Context
MLflow artifacts include pyfunc/sklearn flavors and environment specs suitable for mlflow models serve; no separate serving code is provided.

## Decision
Depend on MLflow’s model packaging to enable loading/inference and optional serving, rather than implementing a custom serving layer.

## Consequences
Allows quick, standardized serving and inference with minimal code, but ties deployment to the MLflow ecosystem and leaves gaps for custom APIs, performance tuning, and production readiness.
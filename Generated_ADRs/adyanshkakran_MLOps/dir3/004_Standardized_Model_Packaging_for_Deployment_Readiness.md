# ADR-004: Standardized Model Packaging for Deployment Readiness

**Date**: 2025-10-14
**Status**: Proposed

## Context
For a model to be useful, it must be reliably and consistently deployable into a production environment. This requires a packaging standard that encapsulates the model and its dependencies.

## Decision
The project leverages the standard MLflow model format, which bundles the serialized model (`model.pkl`) with its specific environment dependencies (`conda.yaml`, `requirements.txt`) and necessary metadata into a single artifact.

## Consequences
This creates portable, self-contained artifacts that are ready for deployment using MLflow's serving tools or other compatible platforms. It drastically reduces environment-related deployment failures and ensures consistency between training and serving environments. This approach, however, ties the deployment strategy closely to MLflow's conventions.
# ADR-009: Per-run environment capture via MLflow without project-level manifest

**Date**: 2025-10-14
**Status**: Proposed

## Context
MLflow artifacts include conda.yaml/python_env/requirements.txt for each run, but there is no top-level requirements.txt or pyproject.

## Decision
Rely on MLflow’s per-run environment specifications instead of maintaining a shared development environment manifest.

## Consequences
Improves reproducibility for loading individual model artifacts, but creates onboarding friction, inconsistent dev environments, and complicates CI/CD setup.
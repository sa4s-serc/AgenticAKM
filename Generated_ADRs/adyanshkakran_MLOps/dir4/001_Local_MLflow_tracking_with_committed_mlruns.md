# ADR-001: Local MLflow tracking with committed mlruns

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository contains linear_regression/mlruns with multiple runs under the default experiment and artifacts per run.

## Decision
Use MLflow as a local backend and artifact store and commit the mlruns directory to version control.

## Consequences
Enables immediate, offline experiment tracking and reproducible artifacts, but bloats the repository, couples environment-specific artifacts to source control, complicates collaboration, and discourages use of a centralized/remote tracking server.
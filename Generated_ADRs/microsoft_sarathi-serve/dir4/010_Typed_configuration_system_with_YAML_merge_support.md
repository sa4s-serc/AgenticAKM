# ADR-010: Typed configuration system with YAML merge support

**Date**: 2025-10-14
**Status**: Proposed

## Context
Complex experiments and deployments need reliable, composable configuration management.

## Decision
Use typed dataclasses for configs with utilities to load and merge YAML-based settings, ensuring validation and consistent defaults.

## Consequences
Improves safety, readability, and reproducibility of runs; adds schema evolution overhead and requires disciplined config versioning.
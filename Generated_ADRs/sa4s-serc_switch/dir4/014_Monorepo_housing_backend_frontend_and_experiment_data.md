# ADR-014: Monorepo housing backend, frontend, and experiment data

**Date**: 2025-10-10
**Status**: Proposed

## Context
Tight iteration across components and artifacts is needed for research velocity.

## Decision
Keep NAVIE backend, CRA frontend, Docker configs, and experiment artifacts in a single repository.

## Consequences
Simplifies cross-component versioning and collaboration; increases repo size and CI time; couples release cycles; requires discipline to manage large artifacts.
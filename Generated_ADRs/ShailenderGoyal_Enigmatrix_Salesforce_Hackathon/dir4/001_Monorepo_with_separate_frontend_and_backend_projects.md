# ADR-001: Monorepo with separate frontend and backend projects

**Date**: 2025-10-16
**Status**: Proposed

## Context
The repository houses React frontend, Node/Express backend, Colab notebooks, and architecture assets under one root.

## Decision
Maintain a simple monorepo with flat directories (no workspace manager) for the app, API, and experiments.

## Consequences
Eases cross-cutting changes and shared versioning but lacks shared packages/types and workspace tooling; potential duplication and tighter coupling between services; CI/CD must handle independent build/test steps.
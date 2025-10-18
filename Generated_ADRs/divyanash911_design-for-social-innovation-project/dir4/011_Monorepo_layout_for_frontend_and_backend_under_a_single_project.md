# ADR-011: Monorepo layout for frontend and backend under a single project

**Date**: 2025-10-13
**Status**: Proposed

## Context
Both React (code/) and Flask (code/backend/) live in the same repository and directory tree.

## Decision
Maintain frontend and backend in a single repository for coordinated development and versioning.

## Consequences
Simplifies cross-team coordination and atomic changes, but CI/CD must isolate builds and deployments; coupling may hinder independent release cadences.
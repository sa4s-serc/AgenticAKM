# ADR-008: Code quality enforcement via CI linting

**Date**: 2025-10-13
**Status**: Proposed

## Context
A GitHub Actions workflow runs pylint on pushes/PRs.

## Decision
Enforce static code analysis standards with pylint in continuous integration.

## Consequences
Drives consistent coding style and early defect detection, acting as a quality gate for contributions; overly strict rules may increase friction and require configuration tuning.
# ADR-009: ADR-009: Code quality baseline with ESLint and Prettier across projects

**Date**: 2025-10-13
**Status**: Proposed

## Context
ESLint configs exist for both frontends. The backend does not show a linter configuration.

## Decision
Adopt ESLint and Prettier for all three apps. Add a minimal Node ESLint config to backend, align formatting rules, and provide npm scripts (lint, format) in each package.

## Consequences
- Consistent style and fewer regressions.
- Initial formatting churn; developers must run lint/format before commits.
- Enables future CI hooks for automated checks.
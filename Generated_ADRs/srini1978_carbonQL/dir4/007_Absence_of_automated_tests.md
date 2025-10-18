# ADR-007: Absence of automated tests

**Date**: 2025-10-09
**Status**: Proposed

## Context
No test projects or test directories are present in the solution.

## Decision
Proceed without unit or integration tests at this stage.

## Consequences
Reduces initial setup effort but lowers confidence in changes, impedes refactoring, and limits CI quality gates. Increases risk of regressions and slows future feature development.
# ADR-007: Testing emphasis on core model

**Date**: 2025-10-13
**Status**: Proposed

## Context
tests/test_shapes.py focuses on shape-related logic; there are no tests for UI or XML export modules.

## Decision
Prioritize unit testing of domain logic (shapes) while deprioritizing UI and persistence tests.

## Consequences
Improves confidence in geometric/model correctness and refactoring safety, but leaves UI flows and export correctness more vulnerable to regressions and integration issues.
# ADR-011: Testing tooling present but no suites included

**Date**: 2025-10-10
**Status**: Proposed

## Context
Testing-library packages and web-vitals are dependencies, but test files are not enumerated.

## Decision
Include testing infrastructure without implementing test coverage initially.

## Consequences
On-ramp for future tests with familiar tooling; current lack of automated regression protection increases risk as features evolve.
# ADR-005: First-Class Stubbing and Sample Data

**Date**: 2025-10-14
**Status**: Proposed

## Context
Deterministic tests and offline development benefit from reliable request stubbing.

## Decision
Embed stubbing in the provider with configurable strategies and require sampleData on targets.

## Consequences
Pros: Excellent testability, fast unit/integration tests, supports API-first development. Cons: Sample data can drift from server behavior, maintenance burden to keep fixtures current, risk of false confidence if validation is weak.
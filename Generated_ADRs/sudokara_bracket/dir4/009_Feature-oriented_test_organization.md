# ADR-009: Feature-oriented test organization

**Date**: 2025-10-14
**Status**: Proposed

## Context
Maintaining clarity of coverage and easing debugging require tests to be discoverable by topic.

## Decision
Group tests by language features (e.g., if/, functions/), each with their own input and expected outputs.

## Consequences
Aids targeted development and diagnosis of regressions, and simplifies incremental extension of the language. Cross-feature interactions may need tests duplicated or additional integration suites.
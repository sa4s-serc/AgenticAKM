# ADR-007: Diagnostics treated as a first-class subsystem

**Date**: 2025-10-14
**Status**: Proposed

## Context
Accurate and testable error reporting is critical for developer experience and language usability.

## Decision
Provide a dedicated diagnostics module in Basic and include negative tests that assert error output.

## Consequences
Encourages precise, consistent error messages and guards against regressions. Increases initial design effort and can constrain later changes to wording or formatting due to golden tests.
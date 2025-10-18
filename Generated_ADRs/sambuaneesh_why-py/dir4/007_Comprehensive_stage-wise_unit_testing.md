# ADR-007: Comprehensive stage-wise unit testing

**Date**: 2025-10-11
**Status**: Proposed

## Context
Interpreter changes can easily introduce regressions across stages.

## Decision
Use Python unittest with focused tests for lexer, parser, AST, and evaluator, plus end-to-end pipeline coverage.

## Consequences
Improves confidence and enables safe refactoring; tests serve as executable specifications; increases maintenance cost of updating tests as the language evolves.
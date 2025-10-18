# ADR-003: AST as canonical intermediate representation

**Date**: 2025-10-11
**Status**: Proposed

## Context
Separating syntax recognition from execution requires a stable IR.

## Decision
Define all AST node types and helpers in ast1.py, independent of the parser and evaluator.

## Consequences
Decouples parsing from evaluation, improves testability, and makes transformations/optimizations possible; introduces duplication risk if node schema changes are not reflected across parser, evaluator, and tests.
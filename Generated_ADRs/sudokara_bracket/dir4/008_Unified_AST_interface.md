# ADR-008: Unified AST interface

**Date**: 2025-10-14
**Status**: Proposed

## Context
Parser, semantic analysis, and code generation all depend on a common program representation.

## Decision
Expose a central AST header (include/llracket/AST/AST.h) as the shared contract among phases.

## Consequences
Ensures a single canonical model of program structure and simplifies cross-phase integration. Can increase compile-time coupling and may require future refactoring (e.g., header partitioning) as the AST grows.
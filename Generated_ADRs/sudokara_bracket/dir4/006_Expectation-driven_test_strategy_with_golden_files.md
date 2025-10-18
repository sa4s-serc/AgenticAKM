# ADR-006: Expectation-driven test strategy with golden files

**Date**: 2025-10-14
**Status**: Proposed

## Context
Compiler behavior must be validated deterministically across many small programs, including error paths.

## Decision
Organize tests around .rkt inputs with .out/.err/.in expectation files, run via Python harness scripts and CMake integration.

## Consequences
Fast, reproducible regression tests that naturally capture both success and failure diagnostics. Golden outputs can become brittle and require bulk updates when messages or formatting legitimately change.
# ADR-006: Lexically scoped environment with nested bindings

**Date**: 2025-10-11
**Status**: Proposed

## Context
Variable resolution and mutation need a predictable scoping model.

## Decision
Implement an Environment abstraction (environment.py) that supports nested scopes and variable bindings.

## Consequences
Enables lexical scoping, shadowing, and closure capture; requires careful handling of mutation and lifetime to avoid subtle bugs.
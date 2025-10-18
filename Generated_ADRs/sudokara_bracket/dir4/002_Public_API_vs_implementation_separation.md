# ADR-002: Public API vs implementation separation

**Date**: 2025-10-14
**Status**: Proposed

## Context
Consumers and internal modules need stable interfaces while enabling internal refactoring and modular builds.

## Decision
Place public headers under include/llracket and corresponding implementations under lib, mirroring the module structure.

## Consequences
Enables treating the compiler as a library, supports incremental compilation, and enforces encapsulation. Requires disciplined API versioning and can increase the effort to evolve cross-cutting changes.
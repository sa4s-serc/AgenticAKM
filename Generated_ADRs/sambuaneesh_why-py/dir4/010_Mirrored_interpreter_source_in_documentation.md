# ADR-010: Mirrored interpreter source in documentation

**Date**: 2025-10-11
**Status**: Proposed

## Context
Docs need close alignment with the code and potential in-page code references.

## Decision
Copy core interpreter files into documentation/public/interpreter via copy-interpreter.js to keep the docs’ code mirror in sync.

## Consequences
Improves discoverability and guarantees examples match the codebase; creates duplication that must be actively synchronized (risk of staleness if scripts are not run in CI or before deploy).
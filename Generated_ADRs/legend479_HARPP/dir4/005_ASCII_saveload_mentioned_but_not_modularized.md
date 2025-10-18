# ADR-005: ASCII save/load mentioned but not modularized

**Date**: 2025-10-13
**Status**: Proposed

## Context
README describes saving/loading ASCII text files, yet the repository has no dedicated ASCII import/export module and no obvious location for that logic.

## Decision
Treat ASCII save/load as an aspirational or inline-implemented feature without a clearly separated module.

## Consequences
Creates a mismatch between documentation and visible code, potentially confusing users and contributors; if implemented inline, it risks scattering persistence logic across modules, increasing coupling and reducing testability.
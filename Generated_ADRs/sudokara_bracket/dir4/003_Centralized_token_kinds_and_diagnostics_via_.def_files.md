# ADR-003: Centralized token kinds and diagnostics via .def files

**Date**: 2025-10-14
**Status**: Proposed

## Context
Tokens and diagnostics are referenced across multiple phases and must remain consistent without duplication.

## Decision
Use .def files (X-macro pattern) for TokenKinds and Diagnostic definitions to generate shared enums/tables.

## Consequences
Single source of truth reduces drift and eases adding new tokens/diagnostics. The pattern can be less discoverable to newcomers and demands careful include discipline to avoid surprises.
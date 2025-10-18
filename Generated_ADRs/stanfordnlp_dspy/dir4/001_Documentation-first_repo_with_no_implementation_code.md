# ADR-001: Documentation-first repo with no implementation code

**Date**: 2025-10-13
**Status**: Proposed

## Context
The repository contains MkDocs docs, release assets, and CI/CD workflows but no src/ or tests.

## Decision
Separate documentation and release/configuration infrastructure from the implementation codebase.

## Consequences
Pros: decoupled release cadence for docs, simpler public consumption, safer contributions without touching core code. Cons: risk of drift between docs and code, manual/extra coordination for versioning, harder to auto-generate API docs from source.
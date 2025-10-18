# ADR-010: JavaScript-only codebase (no TypeScript)

**Date**: 2025-10-10
**Status**: Proposed

## Context
A file named 'typescript' exists at root, but no tsconfig or .ts/.tsx files are present in src.

## Decision
Proceed with plain JavaScript for the application code.

## Consequences
Lower initial friction and faster onboarding; fewer static guarantees leading to more runtime errors; weaker IDE/autocomplete and refactor safety; potential future migration cost if type safety becomes necessary.
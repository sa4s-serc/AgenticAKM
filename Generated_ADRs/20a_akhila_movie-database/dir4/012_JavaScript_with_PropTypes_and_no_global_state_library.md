# ADR-012: JavaScript with PropTypes and no global state library

**Date**: 2025-10-10
**Status**: Proposed

## Context
The stack uses React with prop-types; no TypeScript or Redux-like libraries are present.

## Decision
Rely on JavaScript with PropTypes for runtime type checking and avoid introducing a global state solution.

## Consequences
Lower complexity and quicker iteration for a small app; weaker type safety and potentially harder refactors at scale, with increased risk of runtime type errors and ad hoc state sharing patterns.
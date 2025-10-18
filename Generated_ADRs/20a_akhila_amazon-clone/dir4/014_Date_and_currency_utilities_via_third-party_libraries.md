# ADR-014: Date and currency utilities via third-party libraries

**Date**: 2025-10-10
**Status**: Proposed

## Context
moment and react-currency-format are dependencies.

## Decision
Leverage utility libraries for date formatting and currency display.

## Consequences
Accelerates development with proven APIs; moment increases bundle size compared to modern alternatives (e.g., date-fns, Luxon, Intl APIs); should ensure consistent locale/currency handling across the app.
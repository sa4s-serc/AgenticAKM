# ADR-013: Payments and orders flow scoped to dedicated components

**Date**: 2025-10-10
**Status**: Proposed

## Context
Presence of Payment, Orders, Order, Checkout, and Subtotal components suggests clear functional decomposition.

## Decision
Organize core commerce flows into dedicated components aligned with domain concerns (catalog, cart, checkout, orders).

## Consequences
Improves readability and testability of business flows; cross-cutting concerns (auth, currency, error handling) must be consistently applied across components; global state shape becomes critical to avoid tight coupling.
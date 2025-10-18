# ADR-006: Optional Reactive Integrations as Separate Targets

**Date**: 2025-10-14
**Status**: Proposed

## Context
Teams vary in reactive preferences; not all apps need Rx or Combine.

## Decision
Ship CombineMoya, RxMoya, and ReactiveMoya as opt-in modules that wrap the core provider.

## Consequences
Pros: Keeps core lightweight, broad ecosystem compatibility, avoids forcing reactive dependencies. Cons: Extra maintenance surface and version compatibility matrix, potential API surface divergence, increased binary size when included.
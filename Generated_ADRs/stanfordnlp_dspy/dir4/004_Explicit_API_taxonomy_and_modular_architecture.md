# ADR-004: Explicit API taxonomy and modular architecture

**Date**: 2025-10-13
**Status**: Proposed

## Context
Docs organize the public surface into Adapters, Models, Modules, Optimizers, Evaluation, Primitives, Signatures, Tools, Utils, and Experimental.

## Decision
Define a clear, composable taxonomy for the framework’s extension points and core abstractions.

## Consequences
Pros: predictable extensibility, easier onboarding, cleaner contracts between layers. Cons: maintaining stability across many surfaces, potential fragmentation if contracts drift.
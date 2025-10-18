# ADR-007: Strong Response and Error Types

**Date**: 2025-10-14
**Status**: Proposed

## Context
Consistent response handling and error propagation are essential for reliability and clarity.

## Decision
Expose a Response type with status code and data plus convenience filters, and centralize failures in MoyaError.

## Consequences
Pros: Predictable error modeling, safer status validation, less leakage of transport specifics into app code. Cons: Another abstraction layer to learn, may obscure some underlying Alamofire/URLSession details unless surfaced deliberately.
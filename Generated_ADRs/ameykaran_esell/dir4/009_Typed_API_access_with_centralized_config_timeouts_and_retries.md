# ADR-009: Typed API access with centralized config, timeouts, and retries

**Date**: 2025-10-14
**Status**: Proposed

## Context
src/utils/api.ts wraps network calls with headers, validation, AbortController timeouts, and retries; endpoints centralized in src/config/api.ts.

## Decision
Encapsulate API calls in a typed utility layer with consistent error handling and resilience features.

## Consequences
Pros: reduces duplicated fetch logic, improves UX via timeouts/retries, eases endpoint changes. Cons: adds an abstraction layer to maintain; retry policies must be tuned to avoid thundering herds.
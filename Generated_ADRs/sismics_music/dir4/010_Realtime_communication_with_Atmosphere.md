# ADR-010: Realtime communication with Atmosphere

**Date**: 2025-10-14
**Status**: Proposed

## Context
Atmosphere runtime is included in managed dependencies.

## Decision
Provide realtime updates via Atmosphere (WebSocket/Comet abstraction).

## Consequences
Broad transport compatibility and fallback support; adds server complexity and debugging overhead; modernizing to native WebSocket/SSE frameworks may require refactoring.
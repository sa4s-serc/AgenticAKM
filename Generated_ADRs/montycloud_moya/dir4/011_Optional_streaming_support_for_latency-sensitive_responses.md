# ADR-011: Optional streaming support for latency-sensitive responses

**Date**: 2025-10-11
**Status**: Proposed

## Context
Interactive applications benefit from partial output to reduce perceived latency.

## Decision
Expose a streaming flag in the agent contract and implement streaming where provider APIs permit.

## Consequences
Better UX for long responses. Adds complexity to client handling and cross-provider differences; non-stream-capable providers require graceful degradation.
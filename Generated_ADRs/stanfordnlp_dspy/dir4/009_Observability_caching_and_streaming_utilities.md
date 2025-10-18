# ADR-009: Observability, caching, and streaming utilities

**Date**: 2025-10-13
**Status**: Proposed

## Context
Utilities include configure_cache, asyncify, streamify, StreamListener, history inspection, and logging toggles (incl. LiteLLM).

## Decision
Bundle cross-cutting utilities for performance and debuggability.

## Consequences
Pros: better visibility, lower latency/cost via caching, easier async adoption. Cons: potential coupling to specific logging backends (LiteLLM), added config surface.
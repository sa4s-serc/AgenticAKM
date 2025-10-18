# ADR-008: Per-record Invocation of External Search

**Date**: 2025-10-09
**Status**: Proposed

## Context
For each input record, the function issues a Bing Custom Search request and returns a corresponding output record.

## Decision
Process records independently, performing one outbound API call per record.

## Consequences
Simplifies logic and aligns with Cognitive Search’s record model but can amplify latency and cost under high cardinality; requires rate limiting, retry/backoff, potential caching, and concurrency controls to avoid throttling.
# ADR-008: Provider Pattern with Inflight Request Deduplication

**Date**: 2025-10-14
**Status**: Proposed

## Context
Apps often issue duplicate requests and need a central orchestrator for configuration and lifecycle.

## Decision
Use MoyaProvider as the primary entry point with options like trackInflights for deduplicating concurrent identical requests.

## Consequences
Pros: Centralized control, fewer redundant network calls, consistent plugin application and configuration. Cons: Requires careful concurrency understanding, historical race conditions needed fixes, global providers can become implicit dependencies.
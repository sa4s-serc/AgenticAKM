# ADR-011: MVP-first reliability posture (retries and resumable uploads deferred)

**Date**: 2025-10-14
**Status**: Proposed

## Context
Implementing robust transfer semantics increases complexity and time-to-market, but the initial goal is a functional prototype.

## Decision
Defer exponential backoff, resumable/chunked uploads, deduplication, and versioning to later phases; implement simple synchronous uploads now.

## Consequences
Smaller code surface and faster delivery; higher risk of failure on transient network issues and poor support for large files; technical debt that must be addressed for production readiness.
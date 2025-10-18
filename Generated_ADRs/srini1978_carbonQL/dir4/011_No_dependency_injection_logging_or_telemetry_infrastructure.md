# ADR-011: No dependency injection, logging, or telemetry infrastructure

**Date**: 2025-10-09
**Status**: Proposed

## Context
No DI container, logging framework, or observability packages are present.

## Decision
Keep composition and diagnostics minimal within the codebase.

## Consequences
Reduces complexity for a small app but increases coupling and reduces testability and observability. Scaling to larger features or troubleshooting production issues will be harder without structured logging and DI.
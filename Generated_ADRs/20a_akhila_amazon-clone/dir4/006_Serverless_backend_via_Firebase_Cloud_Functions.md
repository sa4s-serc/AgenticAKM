# ADR-006: Serverless backend via Firebase Cloud Functions

**Date**: 2025-10-10
**Status**: Proposed

## Context
functions/ scaffold with index.js indicates serverless endpoints are planned/used.

## Decision
Implement backend logic as Firebase Cloud Functions for tasks like payment intent creation or secure operations.

## Consequences
Auto-scaling and pay-per-use with minimal ops; cold starts can affect latency; execution time limits and regional constraints; local emulation/testing required for robust dev workflows; versioning and CI/CD for functions must be managed.
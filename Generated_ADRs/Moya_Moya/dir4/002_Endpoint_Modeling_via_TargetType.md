# ADR-002: Endpoint Modeling via TargetType

**Date**: 2025-10-14
**Status**: Proposed

## Context
Apps need a consistent, type-safe way to define API endpoints and their configuration.

## Decision
Introduce TargetType (typically implemented by enums) to declare baseURL, path, method, task, headers, and sampleData.

## Consequences
Pros: Compile-time safety, explicit and centralized API specification, easier discoverability and refactoring. Cons: Can feel rigid for highly dynamic endpoints, may introduce boilerplate, requires patterns like MultiTarget for mixed types.
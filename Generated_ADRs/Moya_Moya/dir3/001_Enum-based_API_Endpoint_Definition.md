# ADR-001: Enum-based API Endpoint Definition

**Date**: 2025-10-14
**Status**: Proposed

## Context
Managing API endpoints using scattered string-based definitions is prone to runtime errors, difficult to maintain, and leads to tight coupling between the networking layer and business logic. A more robust and centralized approach was needed to define the API contract.

## Decision
To abstract network endpoints into a Swift `enum`, where each case represents a distinct endpoint. This enum is required to conform to a `TargetType` protocol, which enforces the definition of all necessary request components like URL, path, method, and parameters.

## Consequences
This design provides compile-time checking for all API calls, drastically reducing runtime errors. It centralizes the entire network layer definition, creating a single source of truth and effectively decoupling networking logic from other parts of the application.
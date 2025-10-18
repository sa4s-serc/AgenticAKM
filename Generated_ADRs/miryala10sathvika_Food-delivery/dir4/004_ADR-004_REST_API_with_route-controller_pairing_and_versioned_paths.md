# ADR-004: ADR-004: REST API with route-controller pairing and versioned paths

**Date**: 2025-10-13
**Status**: Proposed

## Context
Routes and controllers exist for users, foods, orders, and cart. Naming and structure indicate a REST style.

## Decision
Continue using REST with explicit route-controller pairs for each resource. Standardize endpoint naming and introduce a versioned base path (e.g., /api/v1). Use conventional HTTP methods and consistent error/response shapes.

## Consequences
- Predictable API surface and easier documentation.
- Enables non-breaking evolution via path versioning.
- Adoption requires aligning existing routes to /api/v1 and updating frontends accordingly.
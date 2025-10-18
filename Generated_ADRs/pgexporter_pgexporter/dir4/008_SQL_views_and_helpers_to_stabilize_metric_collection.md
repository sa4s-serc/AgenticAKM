# ADR-008: SQL views and helpers to stabilize metric collection

**Date**: 2025-10-16
**Status**: Proposed

## Context
Directly querying system catalogs can be verbose and version-sensitive.

## Decision
Provide helper SQL views and documentation to normalize and simplify metric queries.

## Consequences
More stable and readable metric collection; easier extension of metric sets; requires deploying views and managing database permissions.
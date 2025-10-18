# ADR-003: Composite pattern for grouping and nested structures

**Date**: 2025-10-13
**Status**: Proposed

## Context
group.py provides grouping constructs for shapes with support for nesting; shapes.py defines shape abstractions and concrete types.

## Decision
Model groups and individual shapes via a shared abstraction, enabling nested groups using the Composite pattern.

## Consequences
Enables uniform operations (select, move, copy, delete) across shapes and groups and supports deep nesting, but requires careful handling of transformations, selection propagation, and persistence of hierarchical relationships.
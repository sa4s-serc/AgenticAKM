# ADR-012: Common abstractions consolidated in object.py

**Date**: 2025-10-13
**Status**: Proposed

## Context
object.py contains common object/model abstractions shared across drawable entities.

## Decision
Provide a shared base of model abstractions in a dedicated module named object.py.

## Consequences
Encourages reuse and consistent interfaces across shapes and groups; the module name risks confusion with Python’s built-in object and may impact readability or tooling, suggesting careful import patterns.
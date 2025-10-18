# ADR-005: Dedicated runtime object model

**Date**: 2025-10-11
**Status**: Proposed

## Context
Language semantics should not leak Python internals.

## Decision
Model language values in object.py with explicit runtime types instead of using bare Python types.

## Consequences
Provides a clear semantic boundary, enables custom behaviors and future type extensions; adds wrapping/unwrapping overhead and more code paths to maintain.
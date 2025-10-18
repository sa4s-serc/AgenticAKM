# ADR-004: RESTful API via Jersey (JAX-RS)

**Date**: 2025-10-13
**Status**: Proposed

## Context
Dependency management includes Jersey artifacts, indicating a JAX-RS based web/API layer.

## Decision
Implement the web and API layer using Jersey as the JAX-RS implementation.

## Consequences
Provides a standards-based REST framework with rich features; reduces need for heavier web frameworks; ties API behavior to Jersey version compatibility; requires separate choices for dependency injection and validation strategy.
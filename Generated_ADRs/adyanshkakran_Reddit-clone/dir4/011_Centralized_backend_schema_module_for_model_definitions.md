# ADR-011: Centralized backend schema module for model definitions

**Date**: 2025-10-14
**Status**: Proposed

## Context
A backend/schema.js file exists (database technology not identified in the summary).

## Decision
Define data models and related validation in a single schema module consumed by routes and handlers.

## Consequences
Provides a single source of truth for model structure and reuse across routes; actual persistence mechanics and migrations remain unspecified and must be aligned; changes require coordinated updates across API and client types.
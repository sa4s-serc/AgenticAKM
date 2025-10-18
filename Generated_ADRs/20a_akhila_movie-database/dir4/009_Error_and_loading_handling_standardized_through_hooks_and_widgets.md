# ADR-009: Error and loading handling standardized through hooks and widgets

**Date**: 2025-10-10
**Status**: Proposed

## Context
Hooks expose loading/error flags and the UI includes Spinner and Button components to signal status.

## Decision
Surface asynchronous state (loading/error) from hooks and render dedicated UI feedback components.

## Consequences
Consistent feedback patterns and reduced duplication; no global error boundary or retry/backoff strategy, and limited offline resiliency.
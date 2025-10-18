# ADR-010: Minimal global state via React Context for PDF handling

**Date**: 2025-10-14
**Status**: Proposed

## Context
PdfContext provides shared state for PDF interactions across components.

## Decision
Use a light-weight React Context for PDF state rather than heavier state managers.

## Consequences
Pros: simple, fewer dependencies, clear ownership. Cons: can lead to unnecessary re-renders at scale; limited ergonomics for complex workflows.
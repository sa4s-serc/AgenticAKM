# ADR-009: Direct DOM injection for output rendering

**Date**: 2025-10-10
**Status**: Proposed

## Context
Populate the UI with the generated story text.

## Decision
Programmatically set the story content in the target paragraph and make it visible.

## Consequences
Straightforward and performant for small content; must use safe text insertion (e.g., textContent) to avoid XSS; not reactive beyond explicit updates.
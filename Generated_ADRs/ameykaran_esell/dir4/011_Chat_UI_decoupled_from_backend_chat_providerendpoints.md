# ADR-011: Chat UI decoupled from backend chat provider/endpoints

**Date**: 2025-10-14
**Status**: Proposed

## Context
ChatInterface and related components exist, but no explicit backend chat routes or provider bindings are shown.

## Decision
Provide a chat UX layer without committing to a specific backend chat API, keeping the provider pluggable.

## Consequences
Pros: flexibility to integrate varied providers later; enables parallel UI work. Cons: integration risk deferred; potential mismatch between UI expectations and eventual API semantics.
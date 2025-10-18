# ADR-007: Conversation primitives for role-structured history

**Date**: 2025-10-11
**Status**: Proposed

## Context
Consistent representation of dialogue history is needed across providers and orchestrators.

## Decision
Introduce Message and Thread abstractions carrying roles (system/user/assistant/tool) and content to standardize context construction.

## Consequences
Provider-agnostic context management and easier persistence. Some providers’ rich features may not map 1:1, requiring adapters to translate structures efficiently.
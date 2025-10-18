# ADR-006: Per-user thread reuse via wa_id-to-thread_id mapping (policy-dependent)

**Date**: 2025-10-14
**Status**: Proposed

## Context
A mapping layer persists association between WhatsApp user IDs and OpenAI thread IDs, but current behavior may create new threads depending on code paths.

## Decision
Provide infrastructure for thread reuse but allow behavior to vary based on configuration or implementation paths.

## Consequences
Offers flexibility to tune continuity vs. isolation; if reuse is not consistently enforced, conversation history can fragment, increasing token usage and reducing context quality. Requires explicit policy and tests to avoid regressions.
# ADR-005: OpenAI Assistants threads/runs model for conversation management

**Date**: 2025-10-14
**Status**: Proposed

## Context
The bot generates replies through OpenAI using assistants-style threads and runs rather than plain chat completions.

## Decision
Adopt the Assistants API with per-user threads to maintain conversational context.

## Consequences
Enables built-in conversation continuity and richer assistant features; introduces higher latency and complexity versus simple completions and tightly couples the bot to Assistants API semantics and lifecycle.
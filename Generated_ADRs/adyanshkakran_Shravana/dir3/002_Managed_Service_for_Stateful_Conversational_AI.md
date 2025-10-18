# ADR-002: Managed Service for Stateful Conversational AI

**Date**: 2025-10-14
**Status**: Proposed

## Context
The WhatsApp bot required the ability to handle complex, multi-turn conversations while maintaining context for each user. Building a state management engine for a conversational AI from scratch is a significant engineering challenge.

## Decision
To leverage the OpenAI Assistants API as the core engine for conversational logic and state management. The backend creates and persists a unique conversation 'thread' for each user, offloading the complexity of context-aware interaction to this specialized third-party service.

## Consequences
This dramatically accelerates the development of sophisticated conversational features. The primary trade-offs are a hard dependency on an external vendor (OpenAI), which introduces potential operational risks, data privacy considerations, and recurring API usage costs. The local file-based storage of thread IDs is a simple solution that may not scale effectively.
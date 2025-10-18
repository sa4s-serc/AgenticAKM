# ADR-001: Layered, modular architecture separating Agents, Orchestrators, Tools, Memory, Conversation, and Registries

**Date**: 2025-10-11
**Status**: Proposed

## Context
The framework must support diverse LLM backends, tool use, and complex multi-agent control flows while remaining extensible.

## Decision
Adopt a clear separation of concerns: Agents encapsulate LLM/tool-calling, Orchestrators manage control flow and routing, Tools provide bounded capabilities via schemas, Memory handles state, Conversation structures messages/threads, and Registries centralize discovery.

## Consequences
Enables composability, parallel evolution of components, easier testing and extension. Increases integration surface area and requires disciplined contracts between layers to avoid leaky abstractions.
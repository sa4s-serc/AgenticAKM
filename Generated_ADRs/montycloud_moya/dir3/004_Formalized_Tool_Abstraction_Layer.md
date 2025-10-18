# ADR-004: Formalized Tool Abstraction Layer

**Date**: 2025-10-11
**Status**: Proposed

## Context
Agents need to interact with external systems via tools (or functions). However, each LLM provider has its own unique, often complex, and proprietary API schema for defining and invoking these tools.

## Decision
To create a high-level `Tool` and `ToolRegistry` system that abstracts away the provider-specific implementation details. The framework is responsible for translating the abstract tool definition into the specific JSON schema required by the underlying LLM.

## Consequences
This dramatically improves developer productivity and code portability. Developers can define tools in a simple, provider-agnostic way and use them with any supported agent, shielding them from the boilerplate and complexity of underlying function-calling APIs.
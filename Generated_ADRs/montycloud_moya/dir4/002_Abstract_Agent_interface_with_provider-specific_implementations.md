# ADR-002: Abstract Agent interface with provider-specific implementations

**Date**: 2025-10-11
**Status**: Proposed

## Context
Support multiple LLM providers (OpenAI, Azure, Bedrock, Ollama, CrewAI, remote) with a consistent developer experience.

## Decision
Define an Agent base class with a stable handle_message contract, tool-calling and optional streaming, configured via a dataclass. Implement concrete agents per provider.

## Consequences
Backends are pluggable and interchangeable. Some provider-specific features may be constrained by the common interface, and adapters must keep pace with evolving provider APIs.
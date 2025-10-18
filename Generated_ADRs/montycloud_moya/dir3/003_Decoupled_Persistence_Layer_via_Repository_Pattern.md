# ADR-003: Decoupled Persistence Layer via Repository Pattern

**Date**: 2025-10-11
**Status**: Proposed

## Context
Agent state and conversation history must be persisted. However, storage needs vary widely, from simple in-memory storage for testing and development to durable file systems or databases for production environments.

## Decision
To use the Repository design pattern for the memory component, abstracting the storage logic behind a common interface. The framework provides default implementations for `InMemoryRepository` and `FileSystemRepo`.

## Consequences
This design makes the persistence layer highly extensible and testable. It is trivial to add support for new storage backends (e.g., a SQL database or Redis) without affecting the core agent or orchestrator logic. It also allows for fast, dependency-free unit testing using the in-memory repository.
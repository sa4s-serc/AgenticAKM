# ADR-003: File-Based Knowledge Base for State Management

**Date**: 2025-10-09
**Status**: Proposed

## Context
The MAPE-K loop requires a central, shared repository (the 'Knowledge' base) for components to communicate and persist system state, including configurations, metrics, and logs.

## Decision
A simple, file-based system using formats like CSV and JSON within a dedicated `knowledge/` directory was chosen to act as the shared knowledge base. This avoids the overhead and dependency of an external database for core operations.

## Consequences
The benefit is simplicity, ease of debugging (human-readable state), and zero external dependencies for the core loop, making the framework highly portable and easy to set up. The major drawback is a lack of scalability; this approach is not suitable for high-concurrency or distributed environments and is susceptible to race conditions without proper file locking mechanisms.
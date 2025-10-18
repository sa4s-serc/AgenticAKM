# ADR-014: File-based decoupling over in-memory IPC or a database

**Date**: 2025-10-10
**Status**: Proposed

## Context
Components need loose coupling and simple deployment without standing up stateful services.

## Decision
Use the filesystem for decoupling and persistence rather than a message bus, shared memory, or a database.

## Consequences
Very low operational overhead and easy portability. Limits concurrency and scalability, complicates atomic updates, and is fragile under failures or concurrent writers.
# ADR-008: Pluggable memory repositories with an EphemeralMemory tool

**Date**: 2025-10-11
**Status**: Proposed

## Context
Different use cases require short-lived context and persistent recall without binding to a specific storage technology.

## Decision
Define memory repository interfaces with in-memory and filesystem implementations and expose short-lived context via a dedicated tool.

## Consequences
Supports stateful interactions and simple persistence while enabling future backends (DBs, vector stores). Current implementations may not scale or cover retrieval-augmented generation needs without extensions.
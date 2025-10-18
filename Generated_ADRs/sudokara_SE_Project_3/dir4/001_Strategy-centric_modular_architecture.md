# ADR-001: Strategy-centric modular architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system must support multiple observation modes, compression and encryption algorithms, and cloud providers while remaining easy to extend and maintain.

## Decision
Adopt the Strategy pattern across core subsystems (observation, compression, encryption, key management, uploaders) with CEManager and OManager acting as coordinating facades.

## Consequences
Enables plug-and-play implementations and runtime selection via config/CLI; improves testability and separation of concerns; introduces indirection and wiring complexity; minor performance overhead from abstraction layers.
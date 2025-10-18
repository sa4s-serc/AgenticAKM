# ADR-012: Dataclass-based configuration and default parameter merging

**Date**: 2025-10-11
**Status**: Proposed

## Context
Agents need consistent configuration management including model settings and metadata.

## Decision
Use a dataclass (AgentConfig) to validate and merge default LLM parameters and agent metadata.

## Consequences
Type-safe, consistent configuration and simpler defaults. Runtime mutability and dynamic reconfiguration need careful handling to avoid surprising state.
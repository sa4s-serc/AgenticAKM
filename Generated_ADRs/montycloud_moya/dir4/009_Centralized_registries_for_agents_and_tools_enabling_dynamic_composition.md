# ADR-009: Centralized registries for agents and tools enabling dynamic composition

**Date**: 2025-10-11
**Status**: Proposed

## Context
Systems must evolve at runtime (e.g., add agents/tools) and keep discovery synchronized.

## Decision
Use AgentRegistry and ToolRegistry to register, list, and fetch components; support dynamic agent creation and updates.

## Consequences
Enables runtime extensibility and dynamic routing. Requires thread-safety, lifecycle management, and governance to avoid inconsistencies or stale classifier context.
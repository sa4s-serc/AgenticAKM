# ADR-002: Pluggable Orchestration Strategies

**Date**: 2025-10-11
**Status**: Proposed

## Context
Different multi-agent applications require vastly different interaction patterns. A simple Q&A bot needs a different control flow than a complex autonomous agent that must reason, act, and use tools over multiple steps.

## Decision
To implement multiple, swappable `Orchestrator` components. The framework provides distinct orchestrators for different patterns, such as a `SimpleOrchestrator` for single-agent tasks, a `MultiAgentOrchestrator` for routing, and a `ReactOrchestrator` for complex reasoning cycles.

## Consequences
The framework is highly adaptable to a wide range of use cases. Developers are not forced into a single, rigid workflow and can select the orchestration logic that best matches their application's complexity, from simple delegation to sophisticated, stateful reasoning.
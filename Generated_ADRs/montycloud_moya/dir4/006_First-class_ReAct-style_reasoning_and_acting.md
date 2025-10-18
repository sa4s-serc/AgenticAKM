# ADR-006: First-class ReAct-style reasoning and acting

**Date**: 2025-10-11
**Status**: Proposed

## Context
Many tasks benefit from iterative reasoning with tool use guided by the LLM.

## Decision
Provide a ReActOrchestrator that structures reasoning steps and tool invocations, distinct from simple single-shot flows.

## Consequences
Improves problem-solving capability and tool effectiveness. Increases token usage, latency, and complexity; requires strong observability to debug chains of thought and tool effects.
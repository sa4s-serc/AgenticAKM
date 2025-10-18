# ADR-003: Function-calling tool system with JSON schemas and a ToolRegistry

**Date**: 2025-10-11
**Status**: Proposed

## Context
Agents need safe, machine-discoverable capabilities that LLMs can call during reasoning.

## Decision
Represent tools with structured JSON schemas registered in a ToolRegistry; expose schemas to the LLM, execute requested tools, and feed results back into the loop.

## Consequences
Improves safety and validation of tool inputs and enables discoverability. Requires careful schema design and execution guards; the system must handle hallucinated or invalid tool calls robustly.
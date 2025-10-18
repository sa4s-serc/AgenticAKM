# ADR-004: Controlled tool invocation with iteration limits

**Date**: 2025-10-11
**Status**: Proposed

## Context
Unbounded LLM-driven tool loops can lead to high cost, latency, or runaway behavior.

## Decision
Constrain tool-calling loops with a configurable maximum number of iterations per request.

## Consequences
Predictable cost and failure bounds; prevents infinite loops. Risk of premature termination for complex tasks and the need for error messaging or fallback strategies when limits are hit.
# ADR-015: Observability delegated to integrators with suggested hooks

**Date**: 2025-10-11
**Status**: Proposed

## Context
Complex multi-agent flows and tool chains are hard to debug without tracing.

## Decision
Keep the core light and recommend integrating logging/telemetry around agent decisions, tool calls, and routing.

## Consequences
Framework remains minimal and flexible. Places responsibility on adopters to implement tracing and structured logs; hampered diagnosability without added instrumentation.
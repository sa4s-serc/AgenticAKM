# ADR-014: Security and safety by design for tool execution

**Date**: 2025-10-11
**Status**: Proposed

## Context
LLM-invoked tools can have side effects; untrusted inputs must be contained.

## Decision
Constrain tool schemas, validate inputs, and recommend sandboxing; enforce iteration limits for tool loops.

## Consequences
Reduces risk of unsafe actions and runaway behavior. Requires additional hardening in production (sandboxing, authz, rate limits) that is not provided out of the box.
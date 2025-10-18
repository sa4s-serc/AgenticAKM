# ADR-005: Classifier-driven routing in orchestrators rather than agents

**Date**: 2025-10-11
**Status**: Proposed

## Context
The system must direct user intents to the most suitable agent and support multi-agent sequences.

## Decision
Place an LLM-based classifier in orchestrators to select agents and shape flows (Simple, ReAct, MultiAgent), decoupled from agent logic.

## Consequences
Flexible, domain-specific routing with centralized control. Adds non-determinism, latency, and ongoing prompt/governance maintenance for the classifier when agents change.
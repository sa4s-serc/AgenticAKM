# ADR-005: Adapter pattern for model I/O and structured outputs

**Date**: 2025-10-13
**Status**: Proposed

## Context
Adapters include Adapter, ChatAdapter, JSONAdapter, and TwoStepAdapter; utilities cover streaming.

## Decision
Abstract model interaction behind adapters that can enforce formats (e.g., JSON) and multi-pass behaviors.

## Consequences
Pros: decouples from specific LLM providers, supports structured output and streaming uniformly. Cons: added complexity in adapter implementations, edge-case handling across providers.
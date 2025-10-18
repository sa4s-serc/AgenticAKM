# ADR-003: Centralized, pluggable LLM abstraction

**Date**: 2025-10-14
**Status**: Proposed

## Context
llm.py centralizes LLM calls used across modules; provider details are unspecified and treated as pluggable.

## Decision
Abstract LLM access behind a single module to share prompting policies, retries, and schemas across features.

## Consequences
Pros: consistent LLM usage, easier provider swaps, centralized cost/logging hooks. Cons: risk of a hotspot module; changes can ripple across features; must design for concurrency and rate limits.
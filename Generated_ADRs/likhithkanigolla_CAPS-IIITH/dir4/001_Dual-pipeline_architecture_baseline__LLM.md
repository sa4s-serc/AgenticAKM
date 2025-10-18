# ADR-001: Dual-pipeline architecture (baseline + LLM)

**Date**: 2025-10-09
**Status**: Proposed

## Context
Need to transform CAPSSAML models into runnable DEVS-style simulations while enabling experimentation with AI-assisted generation.

## Decision
Maintain two complementary pipelines: a deterministic procedural generator (generator/, BASE/) and an LLM-based pipeline (llmbased/) that produces equivalent artifacts plus metrics.

## Consequences
Provides redundancy, comparative evaluation, and fallbacks; increases maintenance burden and consistency management across two code paths; enables A/B testing of quality, speed, and cost.
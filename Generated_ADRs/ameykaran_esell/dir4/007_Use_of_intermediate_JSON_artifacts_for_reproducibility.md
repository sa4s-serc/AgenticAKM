# ADR-007: Use of intermediate JSON artifacts for reproducibility

**Date**: 2025-10-14
**Status**: Proposed

## Context
Examples include input/chunks.json, prompts/transcript.json, and template_map.json within the video pipeline.

## Decision
Materialize intermediate LLM outputs and parsing results as JSON artifacts between steps.

## Consequences
Pros: debuggability, caching, resumability, and auditability of LLM calls. Cons: storage growth, potential drift if schemas change; must manage versioning/migration of intermediates.
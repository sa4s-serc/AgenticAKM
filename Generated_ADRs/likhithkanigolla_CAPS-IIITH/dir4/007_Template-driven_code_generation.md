# ADR-007: Template-driven code generation

**Date**: 2025-10-09
**Status**: Proposed

## Context
Generated code must be consistent and maintainable across multiple component types and pipelines.

## Decision
Use templates (LLM prompt templates and file templates in llmbased/generator, plus procedural file_generators.py) to standardize component, model, and experiment scaffolding.

## Consequences
Improves consistency and accelerates evolution; centralizes structure changes; necessitates template versioning and testing to prevent template drift or breaking changes.
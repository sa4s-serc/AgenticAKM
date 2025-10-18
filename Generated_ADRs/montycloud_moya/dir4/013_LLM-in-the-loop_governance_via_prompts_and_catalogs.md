# ADR-013: LLM-in-the-loop governance via prompts and catalogs

**Date**: 2025-10-11
**Status**: Proposed

## Context
Routing quality depends on the classifier’s knowledge of available agents and their capabilities.

## Decision
Treat classifier prompts as governance artifacts that must be updated when agents change; maintain a catalog through registries.

## Consequences
Improves routing accuracy and transparency. Introduces operational overhead and change management requirements; mismatches lead to misroutes.
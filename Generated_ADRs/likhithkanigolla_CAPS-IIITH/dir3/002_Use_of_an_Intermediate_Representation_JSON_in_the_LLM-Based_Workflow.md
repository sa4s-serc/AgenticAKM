# ADR-002: Use of an Intermediate Representation (JSON) in the LLM-Based Workflow

**Date**: 2025-10-09
**Status**: Proposed

## Context
Directly generating a multi-file, syntactically correct simulation from a high-level model description is a complex task for an LLM that can lead to unreliable or inconsistent results. A mechanism was needed to structure the LLM's output and decouple the model interpretation logic from the final code rendering logic.

## Decision
The LLM's role was scoped to translating the input SAML model into a structured, intermediate JSON representation. This well-defined JSON object then serves as the single source of truth for all downstream generators, including those for Python simulation code and web-based visualizations.

## Consequences
This improves the overall reliability and modularity of the system. Code generators work against a predictable schema, simplifying their logic. It also enables the efficient generation of multiple output formats (simulation code, web UI) from a single, initial LLM-driven analysis. The trade-off is the added effort of designing, documenting, and maintaining the intermediate JSON schema.
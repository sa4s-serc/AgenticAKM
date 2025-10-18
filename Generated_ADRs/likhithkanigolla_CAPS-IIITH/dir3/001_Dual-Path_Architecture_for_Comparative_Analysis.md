# ADR-001: Dual-Path Architecture for Comparative Analysis

**Date**: 2025-10-09
**Status**: Proposed

## Context
The project's primary objective is to evaluate the viability of a novel, LLM-based approach for transforming system models into executable simulations. To validate this new method, a direct comparison against an established, conventional technique was required to provide a clear benchmark for performance, reliability, and flexibility.

## Decision
Implement two distinct, parallel transformation pipelines. The first path utilizes an LLM (Gemini) to interpret the SAML model and generate code. The second, baseline path employs a traditional XML parser and template-based generators to achieve the same outcome. This creates a controlled experimental setup within a single repository.

## Consequences
This architecture provides a robust framework for quantitative comparison and research, allowing for data-driven evaluation of the LLM's effectiveness. However, it significantly increases development and maintenance overhead, as two separate, complex code generation systems must be managed and kept in sync with the core modeling language.
# ADR-001: Declarative Programming Paradigm over Prompt Engineering

**Date**: 2025-10-13
**Status**: Proposed

## Context
Traditional development with Large Language Models (LLMs) relies heavily on manual, brittle, and often intuitive 'prompt engineering'. This approach is difficult to scale, maintain, and systematically improve.

## Decision
Abstract the LLM interaction into a declarative programming model. Developers define the computational flow and logic using 'Signatures' (data schemas) and 'Modules' (reasoning patterns), rather than writing raw prompts directly.

## Consequences
This decouples the program's logic from the specific prompt text, making the system more modular, maintainable, and reusable. It shifts the developer's focus from 'prompt artistry' to structured program design and enables systematic, algorithmic optimization of the underlying prompts.
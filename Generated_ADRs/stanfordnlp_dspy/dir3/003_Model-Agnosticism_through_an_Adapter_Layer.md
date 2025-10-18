# ADR-003: Model-Agnosticism through an Adapter Layer

**Date**: 2025-10-13
**Status**: Proposed

## Context
The LLM ecosystem is diverse and rapidly evolving, with numerous providers (OpenAI, Anthropic) and open-source models. Tightly coupling the framework to a single LLM provider would severely limit its applicability and longevity.

## Decision
Implement a model-agnostic architecture where the core framework logic is separated from specific LLM APIs. Communication with different backends is handled through a set of dedicated adapters.

## Consequences
This provides users with flexibility and future-proofs the framework. Developers can switch between different models (e.g., from GPT-4 to a local Llama model) without rewriting their core program logic, allowing them to balance cost, performance, and privacy. The maintenance burden falls on keeping the adapters updated with changing APIs.
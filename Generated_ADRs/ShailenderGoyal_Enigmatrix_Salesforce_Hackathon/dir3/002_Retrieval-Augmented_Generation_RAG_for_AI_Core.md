# ADR-002: Retrieval-Augmented Generation (RAG) for AI Core

**Date**: 2025-10-16
**Status**: Proposed

## Context
To provide a personalized, adaptive, and factually grounded learning experience, the platform needed to go beyond the general knowledge of a standard Large Language Model (LLM).

## Decision
A Retrieval-Augmented Generation (RAG) architecture was implemented. The backend orchestrates interactions with Google's Generative AI, first retrieving relevant, specific information (from a presumed knowledge base) and then using it to generate a contextualized response for the user.

## Consequences
This approach significantly improves the accuracy and relevance of the AI tutor's responses and reduces the risk of AI 'hallucination'. It allows the platform's knowledge to be updated by simply managing the source documents. The trade-off is increased complexity, latency, and cost per AI interaction due to the multi-step retrieval and generation process.
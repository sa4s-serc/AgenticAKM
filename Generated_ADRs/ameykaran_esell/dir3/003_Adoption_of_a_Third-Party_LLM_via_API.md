# ADR-003: Adoption of a Third-Party LLM via API

**Date**: 2025-10-14
**Status**: Proposed

## Context
The platform's central feature is the intelligent understanding and transformation of complex documents. Developing, training, and maintaining a proprietary Large Language Model is prohibitively expensive and complex for most projects.

## Decision
The system was designed to use Google Gemini as its core intelligence engine, accessed via an external API. The backend is responsible for interfacing with this API to drive all content analysis and generation tasks.

## Consequences
This decision provides immediate access to state-of-the-art AI capabilities without the massive overhead of in-house model development. However, it creates a hard dependency on an external vendor (Google), introducing potential risks related to API costs, rate limiting, service availability, and future changes to the API or pricing model.
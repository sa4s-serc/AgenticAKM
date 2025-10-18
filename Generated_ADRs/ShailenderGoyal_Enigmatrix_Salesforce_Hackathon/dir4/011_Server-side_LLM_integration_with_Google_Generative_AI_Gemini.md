# ADR-011: Server-side LLM integration with Google Generative AI (Gemini)

**Date**: 2025-10-16
**Status**: Proposed

## Context
The app provides AI tutoring, chat, and knowledge operations leveraging LLMs.

## Decision
Integrate Gemini APIs from the backend, keeping keys and prompts server-side.

## Consequences
Centralized control over prompts, costs, and data handling; avoids exposing credentials; introduces vendor lock-in, latency, and usage cost management; requires PII/redaction policies.
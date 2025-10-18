# ADR-004: Domain and API Shape via DTOs (QuestionWrapper, QuizResponse)

**Date**: 2025-10-16
**Status**: Proposed

## Context
When serving quiz questions, the system must not leak correct answers to clients, while still accepting submissions for scoring.

## Decision
Introduce DTOs to decouple external representations from internal entities: QuestionWrapper omits answers when delivering questions; QuizResponse structures user submissions for scoring.

## Consequences
Prevents accidental data leakage and stabilizes API contracts; adds mapping overhead and potential divergence between entity and API models; not a security boundary against privileged data access.
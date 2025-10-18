# ADR-005: Questionnaire-centric state modeled in Redux slices and hooks

**Date**: 2025-10-13
**Status**: Proposed

## Context
Redux reducers (question_reducer, result_reducer) and custom hooks (FetchQuestion, FetchQuestionnaireId, setResult) are present.

## Decision
Encapsulate questionnaire, question, and result logic in Redux slices with reusable custom hooks for data fetching and state updates.

## Consequences
Centralizes domain state for consistency and reuse, but increases coupling to Redux patterns and requires careful side-effect management.
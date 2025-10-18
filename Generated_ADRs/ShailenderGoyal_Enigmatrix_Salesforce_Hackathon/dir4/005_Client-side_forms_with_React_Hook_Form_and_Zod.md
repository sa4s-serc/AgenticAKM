# ADR-005: Client-side forms with React Hook Form and Zod

**Date**: 2025-10-16
**Status**: Proposed

## Context
Onboarding quiz, authentication, and configuration forms require validation and performance.

## Decision
Implement forms using React Hook Form for performant control and Zod for schema-based validation.

## Consequences
Better UX and type-safe client validation; duplication with backend Joi schemas risks drift; consider shared schema generation or contracts to reduce mismatch.
# ADR-014: Backend input validation with Joi

**Date**: 2025-10-16
**Status**: Proposed

## Context
The API receives user-provided data for auth, notes, and assessments.

## Decision
Validate request payloads using Joi schemas within controllers/middleware.

## Consequences
Protects API surfaces and ensures data integrity; duplication with Zod on the client adds maintenance overhead; consider shared contracts or code generation to align schemas.
# ADR-010: Declarative Signatures for program interfaces

**Date**: 2025-10-13
**Status**: Proposed

## Context
Signatures include Signature, InputField, and OutputField as first-class primitives.

## Decision
Use declarative signatures to define inputs/outputs and document contracts.

## Consequences
Pros: clearer contracts, static-like validation and discoverability, easier composition. Cons: mismatch risk if not enforced at runtime; adds boilerplate for simple cases.
# ADR-012: Explicitly non-committal DEVS semantics

**Date**: 2025-10-09
**Status**: Proposed

## Context
Ambiguities around DEVS time-advance and event handling can constrain generator design and user expectations.

## Decision
Document that DEVS-style semantics are implementation-specific unless confirmed in code; avoid asserting strict engine behavior in docs.

## Consequences
Provides flexibility to evolve internals; reduces risk of misrepresentation; may create uncertainty for users expecting standard DEVS semantics and requires clear release notes.
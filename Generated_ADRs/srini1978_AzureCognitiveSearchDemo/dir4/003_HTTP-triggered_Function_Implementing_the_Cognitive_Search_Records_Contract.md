# ADR-003: HTTP-triggered Function Implementing the Cognitive Search Records Contract

**Date**: 2025-10-09
**Status**: Proposed

## Context
The function expects and returns the standard Cognitive Search custom skill payload (records array with data, warnings, errors).

## Decision
Use an HTTP POST trigger adhering to the Cognitive Search skillset input/output schema.

## Consequences
Enables drop-in use within skillsets and indexers, but tightly couples the API shape to Cognitive Search’s contract, requiring careful versioning and validation to avoid pipeline failures when payloads evolve.
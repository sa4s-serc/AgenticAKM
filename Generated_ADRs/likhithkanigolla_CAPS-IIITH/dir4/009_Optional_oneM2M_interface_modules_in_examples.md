# ADR-009: Optional oneM2M interface modules in examples

**Date**: 2025-10-09
**Status**: Proposed

## Context
Some target systems integrate with IoT messaging and standards like oneM2M.

## Decision
Include oneM2M interface examples under BASE/basic-model without making them core pipeline dependencies.

## Consequences
Demonstrates extensibility and realistic integration; avoids coupling the generator to a specific protocol; can cause confusion about supported message semantics if treated as canonical.
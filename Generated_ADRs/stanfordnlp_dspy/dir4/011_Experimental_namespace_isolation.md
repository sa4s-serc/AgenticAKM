# ADR-011: Experimental namespace isolation

**Date**: 2025-10-13
**Status**: Proposed

## Context
Docs have an Experimental section (e.g., Citations, Document).

## Decision
Isolate unstable features behind an experimental namespace and docs section.

## Consequences
Pros: encourages innovation without destabilizing core APIs, sets user expectations. Cons: fragmentation and potential API churn; migration overhead when graduating features.
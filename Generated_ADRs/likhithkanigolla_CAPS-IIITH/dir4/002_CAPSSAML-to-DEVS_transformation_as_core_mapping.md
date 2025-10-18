# ADR-002: CAPSSAML-to-DEVS transformation as core mapping

**Date**: 2025-10-09
**Status**: Proposed

## Context
The input modeling language is CAPSSAML and the desired execution platform is a DEVS-style simulator in Python.

## Decision
Parse CAPSSAML to extract components and connections, then generate DEVS-style Python components, a composed model, and experiment runners.

## Consequences
Creates a clear model-driven transformation flow; demands a stable mapping of SAML constructs to DEVS semantics; any CAPSSAML evolution requires generator updates; encourages consistent model-driven practices.
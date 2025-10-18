# ADR-006: Permissive TLS trust strategy included for debugging

**Date**: 2025-10-10
**Status**: Proposed

## Context
TrustAllCerts.java exists in the project, implying a trust-all SSL configuration may be used.

## Decision
Provide a trust-all SSL trust manager for development or testing scenarios.

## Consequences
Facilitates quick iteration when dealing with test endpoints but is a critical security risk if not strictly limited to debug builds; must be gated by build variants and excluded from production.
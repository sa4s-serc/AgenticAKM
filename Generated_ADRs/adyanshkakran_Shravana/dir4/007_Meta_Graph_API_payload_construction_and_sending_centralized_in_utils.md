# ADR-007: Meta Graph API payload construction and sending centralized in utils

**Date**: 2025-10-14
**Status**: Proposed

## Context
Outbound WhatsApp replies and formatting are handled in a dedicated utility module without relying on unverified third-party helpers.

## Decision
Encapsulate Graph API payload building, formatting, and error-safe sending in meta/utils.py.

## Consequences
Improves maintainability, testability, and consistency of WhatsApp responses; reduces external dependency risk but concentrates change impact in one module and requires careful alignment with evolving Graph API schemas.
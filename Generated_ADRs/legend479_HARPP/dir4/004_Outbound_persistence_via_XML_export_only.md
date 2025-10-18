# ADR-004: Outbound persistence via XML export only

**Date**: 2025-10-13
**Status**: Proposed

## Context
export.py handles XML export; no dedicated XML import module is present; README mentions exporting to XML.

## Decision
Provide one-way persistence by implementing XML export in a dedicated export module while deferring XML import functionality.

## Consequences
Simplifies persistence and reduces parsing complexity; users can share or archive documents as XML, but cannot re-import them, limiting round-trip workflows and integration with external tools without additional development.
# ADR-005: Lectures and tutorials modeled as flat pages

**Date**: 2025-10-08
**Status**: Proposed

## Context
Lectures/ and Tutorials/ directories contain markdown files but are not defined as collections.

## Decision
Keep lectures and tutorials as simple pages rather than Jekyll collections.

## Consequences
Simplifies authoring and avoids extra configuration, but reduces ability to auto-generate indexes, sort by metadata, paginate, or uniformly template items; more manual maintenance is required.
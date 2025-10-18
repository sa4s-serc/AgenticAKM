# ADR-007: Binary slide assets stored in repository

**Date**: 2025-10-08
**Status**: Proposed

## Context
Multiple PDFs and PPTX slides are committed under slides and mirrored in the built site.

## Decision
Version control large binary teaching materials within the main repository.

## Consequences
Simple linking and hosting without external storage, but increases repository size and clone time; binary diffs are inefficient; may merit Git LFS if assets grow.
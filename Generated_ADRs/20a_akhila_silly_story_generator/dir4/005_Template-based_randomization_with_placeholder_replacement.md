# ADR-005: Template-based randomization with placeholder replacement

**Date**: 2025-10-10
**Status**: Proposed

## Context
Create varied whimsical stories from a base template.

## Decision
Use a template string with placeholders and randomly select values to replace them on each generation.

## Consequences
Simple to extend by adding options; risk of brittle string replacement rules and harder internationalization; non-deterministic output complicates reproducibility.
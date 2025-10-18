# ADR-007: Localization through US/UK selection with runtime unit conversion

**Date**: 2025-10-10
**Status**: Proposed

## Context
Support different measurement systems for weight and temperature.

## Decision
Provide US/UK radio buttons; when UK is selected, convert temperature to centigrade and weight to stones before rendering.

## Consequences
Minimal UI complexity and no external data; limited to two locales and two unit types; correctness depends on hard-coded conversion logic; radio change alone won’t update an already-rendered story.
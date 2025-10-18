# ADR-004: Event-driven story generation on button click

**Date**: 2025-10-10
**Status**: Proposed

## Context
User initiates story creation through the UI.

## Decision
Attach a click handler to the Generate random story button to compose and display the story.

## Consequences
Predictable flow and easy reasoning; inputs (name, locale) do not retroactively affect an already displayed story without another click.
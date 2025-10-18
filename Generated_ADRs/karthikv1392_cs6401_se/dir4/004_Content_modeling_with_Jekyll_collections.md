# ADR-004: Content modeling with Jekyll collections

**Date**: 2025-10-08
**Status**: Proposed

## Context
Collections exist for announcements, modules, schedules, and staffers with dedicated layouts.

## Decision
Use Jekyll collections to represent repeatable content types and drive templated pages.

## Consequences
Improves structure, reuse, and metadata-driven rendering across content types; requires familiarity with Jekyll’s collections and Liquid, and adds configuration overhead.
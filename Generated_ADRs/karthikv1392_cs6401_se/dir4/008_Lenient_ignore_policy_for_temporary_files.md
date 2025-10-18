# ADR-008: Lenient ignore policy for temporary files

**Date**: 2025-10-08
**Status**: Proposed

## Context
A temporary Office auto-save file (~$...) is present in the repository.

## Decision
No strict .gitignore rules preventing temporary and editor-generated files from being committed.

## Consequences
Adds noise and risk of accidental artifact leakage; signals need to harden .gitignore and review practices to keep history clean.
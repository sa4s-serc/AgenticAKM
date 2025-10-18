# ADR-008: Basic CI via GitHub Actions workflow

**Date**: 2025-10-09
**Status**: Proposed

## Context
A .github/workflows/dotnet-desktop.yml workflow exists, contents not reviewed.

## Decision
Enable CI with a prebuilt .NET desktop-oriented workflow template.

## Consequences
Provides automated build/validation on pushes/PRs. Template focus on desktop may include unnecessary steps or Windows-specific assumptions; fine-tuning could improve speed and cross-platform coverage.
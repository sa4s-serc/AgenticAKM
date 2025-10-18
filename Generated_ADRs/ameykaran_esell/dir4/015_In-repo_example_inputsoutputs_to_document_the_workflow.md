# ADR-015: In-repo example inputs/outputs to document the workflow

**Date**: 2025-10-14
**Status**: Proposed

## Context
backend/uploads/, backend/posters/, backend/video/final_output/ include sample PDFs and generated artifacts.

## Decision
Check in representative inputs and outputs to illustrate the end-to-end pipeline and aid development.

## Consequences
Pros: accelerates onboarding, enables quick demos and regression checks. Cons: repository bloat, potential licensing/privacy concerns for sample content; must gate large binaries.
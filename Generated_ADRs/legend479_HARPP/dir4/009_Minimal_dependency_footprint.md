# ADR-009: Minimal dependency footprint

**Date**: 2025-10-13
**Status**: Proposed

## Context
requirements.txt lists PySimpleGUI, xml-python, and typing; no heavy frameworks beyond the UI and XML handling.

## Decision
Keep external dependencies minimal, selecting PySimpleGUI for UI and xml-python for XML serialization, and explicitly listing typing.

## Consequences
Simplifies installation and reduces supply-chain risk; reliance on xml-python over the standard library may constrain API choices; listing typing (standard in modern Python) may cause confusion or version pinning concerns.
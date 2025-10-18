# ADR-001: GUI framework and UI architecture

**Date**: 2025-10-13
**Status**: Proposed

## Context
requirements.txt lists PySimpleGUI; window.py constructs and manages the application’s GUI; main.py coordinates interaction and UI.

## Decision
Use PySimpleGUI for the desktop UI, centralizing UI construction and event handling in window.py with main.py as the top-level coordinator.

## Consequences
Accelerates UI development with a simple, event-driven model and minimal boilerplate, but constrains advanced/custom UI behaviors, complicates automated UI testing, and ties the app to PySimpleGUI’s capabilities and look-and-feel.
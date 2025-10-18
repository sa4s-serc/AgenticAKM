# ADR-001: GUI Framework Selection

**Date**: 2025-10-13
**Status**: Proposed

## Context
The project is a desktop 2D vector drawing application requiring a graphical user interface for user interaction, including a drawing canvas, tool palettes, and menu bars for file operations.

## Decision
The application was built using `tkinter`, the de facto standard GUI library that is included with most Python installations. This choice avoids the need for any external dependencies.

## Consequences
This decision makes the application highly portable and easy to run on any system with Python, as no separate installation of GUI libraries is needed. However, `tkinter` offers a relatively basic and sometimes dated look and feel compared to more modern frameworks like Qt or wxWidgets. It may also present performance challenges for highly complex drawings with a large number of objects on the canvas.
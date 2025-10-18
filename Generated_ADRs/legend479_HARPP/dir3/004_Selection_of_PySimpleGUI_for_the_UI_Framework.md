# ADR-004: Selection of PySimpleGUI for the UI Framework

**Date**: 2025-10-13
**Status**: Proposed

## Context
A GUI framework was needed to build the desktop application's user interface. The choice would directly influence development speed, complexity, and the final look and feel of the application.

## Decision
PySimpleGUI was chosen as the GUI library. It acts as a high-level abstraction layer over underlying toolkits like Tkinter or Qt, simplifying the creation of window layouts and event handling.

## Consequences
The use of PySimpleGUI significantly accelerates UI development and reduces boilerplate code. The main drawback is a dependency on this abstraction layer, which may limit access to advanced, low-level features of the underlying native GUI framework and could potentially introduce performance constraints for very complex interfaces.
# ADR-004: Choice of Java Swing for Desktop Management UI

**Date**: 2025-10-14
**Status**: Proposed

## Context
The `music-agent` required a cross-platform graphical user interface to provide an accessible way for non-technical users to manage the music server's lifecycle.

## Decision
Java Swing was chosen for the UI of the desktop agent. This choice leverages a mature framework that is part of the standard Java Runtime Environment (JRE).

## Consequences
Using Swing makes the agent lightweight and self-contained, with no external UI framework dependencies, ensuring it can run on any machine with Java installed. While highly functional, Swing is an older technology, and the application's look and feel may seem dated compared to modern UI frameworks.
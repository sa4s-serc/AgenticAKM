# ADR-002: Data Persistence and Interchange Format

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application required a method to save and load vector drawings. The format needed to preserve the object-oriented nature of the drawing (e.g., shapes, coordinates, color) rather than storing it as a flat pixel-based image.

## Decision
A custom XML schema was designed and implemented for data persistence. Shapes like lines and rectangles are stored with their specific attributes (coordinates, color, etc.) in a structured, human-readable format.

## Consequences
Using a custom XML format provides a human-readable and easily debuggable file structure. It's extensible, allowing new shape types or properties to be added in the future. The main drawback is the lack of interoperability; the drawings cannot be opened by standard vector graphics software like Inkscape or Adobe Illustrator, which typically use formats like SVG. The verbosity of XML can also lead to larger file sizes compared to binary formats.
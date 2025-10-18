# ADR-002: Implementation of the Composite Design Pattern for Shape Management

**Date**: 2025-10-13
**Status**: Proposed

## Context
The drawing application needed to handle both individual shapes (primitives like lines, rectangles) and groups of shapes uniformly. Operations such as selecting, moving, and deleting should apply consistently to both single objects and complex groupings.

## Decision
The Composite design pattern was implemented through the `group.py` module. This allows a collection of `Shape` objects to be treated as a single `Shape` instance, creating a tree-like object structure.

## Consequences
This simplifies client code (the Controller), which can now treat individual and grouped objects identically, reducing conditional logic. It provides a flexible and scalable way to represent complex drawings. The main trade-off is a slightly more complex object model.
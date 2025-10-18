# ADR-003: Decoupled Persistence Layer with Multi-Format Support

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application required a mechanism to save and load user drawings. There was a dual need for a simple, native format for regular use and a standardized, interoperable format (like XML) for potential integration with other tools.

## Decision
A dedicated persistence service (`export.py`) was created, isolating all serialization and deserialization logic from the core application. This service was designed to support multiple file formats: a custom ASCII format and a structured XML format.

## Consequences
This follows the Single Responsibility Principle, making the core application cleaner and the persistence logic easier to extend (e.g., to support SVG or JSON). Supporting multiple formats enhances utility, but also increases the maintenance and testing overhead for the persistence layer.
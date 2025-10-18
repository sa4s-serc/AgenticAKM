# ADR-008: Developer Productivity and Code Readability

**Date**: 2025-10-16
**Status**: Proposed

## Context
Java's verbosity, particularly in model classes (POJOs/Entities), often leads to a large amount of boilerplate code for constructors, getters, and setters, which can obscure the core logic.

## Decision
Project Lombok was incorporated into the project to automate the generation of boilerplate code via annotations.

## Consequences
This results in significantly cleaner and more concise model classes, improving readability and maintainability. Developers can focus on the data fields and their relationships rather than writing and managing repetitive methods. The main trade-off is a reliance on IDE plugins and the build tool's annotation processing.
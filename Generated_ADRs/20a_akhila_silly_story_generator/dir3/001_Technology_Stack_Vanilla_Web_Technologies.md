# ADR-001: Technology Stack: "Vanilla" Web Technologies

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project required a client-side application for generating a simple, randomized story. A key decision was whether to use a modern JavaScript framework (like React, Vue, etc.) or to rely on fundamental browser technologies.

## Decision
To build the application using only standard "vanilla" JavaScript, HTML, and CSS, with no external frameworks or libraries. This makes the project entirely self-contained.

## Consequences
This results in a lightweight application with zero dependencies, leading to faster load times and a simplified or non-existent build process. However, it forgoes the benefits of modern frameworks, such as declarative UI, component-based architecture, and advanced state management, which would be critical for a more complex or scalable application. All DOM manipulation must be handled manually.
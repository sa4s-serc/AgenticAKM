# ADR-004: DOM Overlay for UI and Game State Management

**Date**: 2025-10-14
**Status**: Proposed

## Context
The game required a user interface for various states, including a start menu, an in-game Head-Up Display (HUD) for laps and fuel, and game-over screens. A solution was needed that was simple to implement and decoupled from the complex 3D rendering loop.

## Decision
A hybrid UI architecture was chosen, where standard HTML elements are defined in `index.html` and overlaid on the 3D canvas. JavaScript in `main.js` controls the visibility and content of these DOM elements to reflect the current game state.

## Consequences
This is a lightweight and performant approach that leverages familiar web technologies (HTML/CSS) for the UI, avoiding the overhead of rendering UI with WebGL. It cleanly separates UI logic from game logic, but can make it more difficult to create UI elements that are deeply integrated within the 3D scene.
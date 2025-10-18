---
### ADR-007: Use vanilla JavaScript without a UI framework

Status: Inferred
Context: No React/Vue/Svelte/etc. dependencies; the application relies on index.html, style.css, and JS modules. The UI needs are minimal and mostly 3D scene driven.
Decision: Implement the app in plain JavaScript and DOM/CSS without a frontend framework.
Consequences:
- Positive: Lower bundle size, reduced complexity, fewer abstractions to manage; direct control over Three.js lifecycle and rendering.
- Negative: Manual handling of any UI state or DOM interactions; fewer built-in patterns for complex UI should the scope grow.
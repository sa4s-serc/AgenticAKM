---
### ADR-002: Use vanilla JavaScript instead of a front-end framework

**Status:** Inferred
**Context:** The presence of a single index.js file and no signs of framework-specific files or configurations (e.g., no React/Vue/Angular scaffolding, no node_modules, no package.json) imply direct use of browser APIs.
**Decision:** Implement interactivity using plain JavaScript (vanilla JS) without a front-end framework.
**Consequences:** 
- Positive: Zero framework overhead, smaller bundle size, faster initial load, fewer dependencies to maintain.
- Negative: Less structure for complex state management or routing, more manual DOM manipulation, potential maintainability challenges as complexity grows.
---
### ADR-012: Styling with plain CSS files per component

Status: Inferred
Context: Numerous .css files colocated with components; no CSS-in-JS or utility framework dependency in use.
Decision: Use plain CSS stylesheets scoped by convention to each component.
Consequences:
- Positive: Simple, framework-agnostic; no runtime styling overhead.
- Negative: Potential for style leakage/selector conflicts; lacks theming and composition features of CSS-in-JS or utility-first frameworks.
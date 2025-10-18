---
### ADR-007: Documentation Site Built with Astro, Starlight, and React

Status: Inferred
Context: The documentation folder is a Node-based project using Astro, @astrojs/starlight, and React with an InteractiveRepl.jsx component and content-driven docs.
Decision: Use Astro + Starlight for a statically generated documentation site with React for interactive components.
Consequences:
- Positive: Modern, fast docs with a strong content system; easy theming/navigation; React enables rich interactive examples.
- Negative: Introduces a Node toolchain alongside Python; increases repository complexity and build steps; cross-language maintenance.
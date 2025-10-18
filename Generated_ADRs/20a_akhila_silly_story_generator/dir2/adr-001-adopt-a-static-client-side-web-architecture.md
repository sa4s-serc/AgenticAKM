### ADR-001: Adopt a static client-side web architecture

**Status:** Inferred
**Context:** The repository contains only three files: index.html, index.js, and style.css. There is no server-side code, backend framework, or deployment configuration. This suggests the application is intended to be delivered as static assets that the browser executes directly.
**Decision:** Build and deliver the application as a static site composed of a single HTML file, a JavaScript file for behavior, and a CSS file for styling.
**Consequences:** 
- Positive: Simple hosting (e.g., GitHub Pages, Netlify), low operational complexity, fast initial setup, minimal infrastructure.
- Negative: Limited server-side capabilities (auth, data persistence, SEO-friendly dynamic rendering), any complex logic must run in the browser, potential SEO limitations if content is rendered dynamically.
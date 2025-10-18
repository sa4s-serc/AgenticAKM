---
### ADR-009: Use Server-Side Rendering with Jinja2 Templates and Static Assets

Status: Inferred
Context: The repository includes multiple Jinja2 templates (templates/*.html) and static assets (static/css, static/js). No SPA framework is present.
Decision: Implement the UI as server-rendered HTML templates with light JavaScript enhancements.
Consequences: Reduced complexity, better initial load/SEO, and fewer build tool dependencies. Interactivity and client-side state management are limited compared to a full SPA, and richer client features would require additional JS code.
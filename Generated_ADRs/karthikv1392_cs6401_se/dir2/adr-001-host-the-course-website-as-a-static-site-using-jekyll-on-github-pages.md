### ADR-001: Host the course website as a static site using Jekyll on GitHub Pages

**Status:** Inferred
**Context:** The repository contains many Markdown pages, Jekyll-specific folders (e.g., _includes, _layouts, _sass), and a Gemfile specifying the github-pages gem. This indicates a need for a simple, version-controlled, low-ops way to publish a course site with structured content.
**Decision:** Use Jekyll as the static site generator and GitHub Pages as the hosting/build platform.
**Consequences:** 
- Positive: Simple publishing workflow; tight integration with GitHub; no servers to manage; Markdown-first authoring; good support for templating and theming.
- Negative: Limited dynamic features; constrained to plugins supported by GitHub Pages; Ruby/Jekyll toolchain required for local builds.
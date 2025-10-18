---
### ADR-002: Pin the Jekyll toolchain to the GitHub Pages gem

**Status:** Inferred
**Context:** The Gemfile includes gem 'github-pages', which locks Jekyll and plugins to versions supported by GitHub Pages.
**Decision:** Depend on the github-pages meta-gem to ensure local builds match GitHub Pages’ production environment.
**Consequences:**
- Positive: Consistent local vs. hosted builds; reduced dependency/version drift; fewer build surprises.
- Negative: Slower adoption of latest Jekyll/plugins; limited customization outside GitHub Pages’ supported set.
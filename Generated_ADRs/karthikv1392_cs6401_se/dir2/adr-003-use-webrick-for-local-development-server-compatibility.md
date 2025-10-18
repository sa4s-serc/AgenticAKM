---
### ADR-003: Use Webrick for local development server compatibility

**Status:** Inferred
**Context:** The Gemfile includes gem "webrick", "~> 1.7". Ruby 3 removed Webrick from the standard library, and Jekyll serve depends on it.
**Decision:** Explicitly include Webrick to support jekyll serve for local preview.
**Consequences:**
- Positive: Reliable local development and preview experience; compatibility with modern Ruby versions.
- Negative: Extra gem dependency to manage.
---
### ADR-004: Abstract external API access behind a dedicated module and use environment variables for secrets

Status: Inferred
Context: Files include API.js and config.js, and a .env is present. Components and hooks suggest The Movie Database (TMDB) usage based on asset names and typical RMDB structure.
Decision: Centralize API calls in API.js, with configuration and secrets (e.g., API key) sourced from .env via config.js.
Consequences:
- Positive: Cleaner separation of concerns; easier to swap APIs or modify endpoints; secrets kept out of source control.
- Negative: Requires build-time environment configuration; client-side apps cannot fully hide secrets, so rate-limiting and usage constraints are needed.
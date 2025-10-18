---
### ADR-016: Static assets strategy mixes local SPA assets and uploaded media from API

Status: Inferred
Context: /src/assets contains many icons/images; API also serves uploaded images from backend/uploads; assets.js files centralize paths.
Decision: Keep UI icons and placeholders bundled with SPAs; serve dynamic media (food images) from the API’s uploads directory.
Consequences:
- Positive: Predictable, cacheable UI assets; dynamic content decoupled from SPA builds.
- Negative: Two asset origins and caching strategies to manage; requires absolute URLs/config for images across environments.
---
### ADR-010: Use SPA static assets and web app manifest from CRA public folder

Status: Inferred
Context: public/manifest.json, icons (logo192.png, logo512.png), favicon, and robots.txt exist; index.html follows CRA conventions.
Decision: Serve static assets and the web app manifest from CRA’s public folder to support standard metadata and icons.
Consequences:
- Positive: Conventional asset handling; compatibility with install prompts and platform meta; straightforward customization.
- Negative: Not a full PWA by default (no service worker configured); relying on CRA defaults may limit advanced asset strategies unless extended.
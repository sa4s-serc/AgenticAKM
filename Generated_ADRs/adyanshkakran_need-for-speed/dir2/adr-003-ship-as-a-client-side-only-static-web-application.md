---
### ADR-003: Ship as a client-side only, static web application

Status: Inferred
Context: The repository contains only frontend assets (index.html, style.css, src/*.js) with no backend code. Vite’s preview/build imply static hosting is sufficient.
Decision: Implement the application entirely on the client side and deploy as static files.
Consequences:
- Positive: Simple deployment (CDN/static hosting), minimal infrastructure, low operational complexity.
- Negative: No server-side capabilities (e.g., persistence, multiplayer, server-authoritative logic); all performance and state are limited to the client device and browser.
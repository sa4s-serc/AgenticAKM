---
### ADR-006: Defer Progressive Web App (PWA) features

**Status:** Inferred
**Context:** The provided manifest_content is empty, and there are no service worker files. This indicates PWA capabilities (installability, offline caching) are not currently implemented.
**Decision:** Do not include a Web App Manifest or Service Worker at this stage.
**Consequences:** 
- Positive: Reduced complexity, fewer moving parts to test and maintain.
- Negative: No offline support, no “Add to Home Screen” installability, fewer app-like capabilities on mobile.
---
### ADR-002: Use Angular SPA for the frontend

Status: Inferred
Context: The frontend/ subproject uses Angular 15 with Angular Material, ngx-translate, and a build pipeline integrated into root scripts. The app’s UI appears extensive (many components/services, i18n, themes).
Decision: Build the UI as an Angular single-page application (SPA) and ship a production build served by the backend.
Consequences:
- Positive: Rich client-side UX; componentized structure; AOT build; mature ecosystem.
- Negative: Larger client bundle; upgrade complexity across major Angular versions.
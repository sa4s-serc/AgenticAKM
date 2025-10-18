---
### ADR-006: Host on Netlify with SPA-friendly redirects; integrate CLI and CI

Status: Inferred
Context: netlify-cli is a dependency; public/_redirects is present (typical for SPA routing on Netlify). The repository includes .gitlab-ci.yml, implying CI on GitLab.
Decision: Deploy the SPA to Netlify using netlify-cli and configure redirects to support client-side routing; use GitLab CI for build/deploy automation.
Consequences:
- Positive: Fast global CDN delivery, simple deploys, and correct handling of SPA deep links; automated CI/CD via GitLab.
- Negative: Ties deployment to Netlify-specific configuration; requires maintaining CI pipeline and environment variables in two systems.
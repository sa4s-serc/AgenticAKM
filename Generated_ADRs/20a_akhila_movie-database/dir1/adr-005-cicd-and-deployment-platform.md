---
### ADR-005: CI/CD and Deployment Platform

**Status:** Inferred
**Context:** The project requires an automated, reliable, and efficient process to build the application and deploy it to a hosting environment. Manual deployments are slow and error-prone.
**Decision:** The project will use **GitLab CI for Continuous Integration/Continuous Deployment** to deploy the static build output to the **Netlify** platform. This decision is inferred from the presence of `.gitlab-ci.yml` (for GitLab's pipeline) and both `netlify-cli` in `package.json` and a `public/_redirects` file, which is a Netlify-specific configuration file for handling SPA routing.
**Consequences:**
*   **Positive:**
    *   **Automation:** Every push or merge can automatically trigger a build, test, and deploy, reducing manual effort and speeding up release cycles.
    *   **Integrated Workflow:** GitLab CI is tightly integrated with the GitLab source control repository.
    *   **High-Performance Hosting:** Netlify is optimized for hosting static sites, providing a global CDN, atomic deploys, and easy rollbacks out-of-the-box.
*   **Negative:**
    *   **Vendor Lock-in:** The project becomes dependent on both GitLab and Netlify platforms. Migrating to a different CI/CD or hosting provider would require effort.
    *   **Configuration Complexity:** While powerful, CI/CD pipeline configuration in `.gitlab-ci.yml` can become complex and requires specific expertise to maintain.
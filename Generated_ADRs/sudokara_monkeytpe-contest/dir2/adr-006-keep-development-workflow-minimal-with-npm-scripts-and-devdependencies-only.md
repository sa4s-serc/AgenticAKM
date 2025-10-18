---
### ADR-006: Keep development workflow minimal with npm scripts and devDependencies only

Status: Inferred
Context: package.json includes a single start script ("electron ."), electron as a devDependency, and no test or packaging scripts. package-lock.json is committed.
Decision: Use npm for dependency management and a minimal start script for running the app in development, without automated testing or packaging configuration.
Consequences:
- Positive: Low barrier to entry; quick run workflow for contributors; reproducible installs via lockfile.
- Negative: Not production-packaging ready (no installers/build pipeline); lacks automated tests and CI, increasing risk of regressions; distribution requires additional tooling later (e.g., electron-builder/electron-forge).
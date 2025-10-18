---
### ADR-017: Use Grunt for packaging/distribution tasks

Status: Inferred
Context: Gruntfile.js exists and root scripts reference grunt for packaging.
Decision: Rely on Grunt to orchestrate packaging/release steps in addition to npm scripts.
Consequences:
- Positive: Mature task runner for build/release steps not covered by default scripts.
- Negative: Another tool to maintain; overlapping responsibilities with npm scripts.
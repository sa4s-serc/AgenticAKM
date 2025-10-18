---
### ADR-009: Target Node.js 14 runtime for Cloud Functions

Status: Inferred
Context: functions/package.json specifies "engines": { "node": "14" }.
Decision: Run Firebase Cloud Functions on Node 14.
Consequences:
- Positive: Stable LTS environment, compatibility with Stripe SDK versions used, predictable runtime behavior.
- Negative: Must plan upgrades as Firebase deprecates older Node runtimes; potential incompatibility with newer language features without transpilation.
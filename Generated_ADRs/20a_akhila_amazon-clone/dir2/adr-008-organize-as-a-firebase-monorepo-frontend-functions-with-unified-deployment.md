---
### ADR-008: Organize as a Firebase monorepo (frontend + functions) with unified deployment

Status: Inferred
Context: The repository contains /functions and a React app at root, with Firebase config files (.firebaserc, firebase.json). Functions package.json includes emulator and deploy scripts.
Decision: Co-locate frontend and Cloud Functions in a single repository, using Firebase CLI for local emulation and one-step deployments.
Consequences:
- Positive: Simplified developer workflow, consistent environment management, atomic deployments, easier CI/CD wiring.
- Negative: Tighter coupling between frontend and backend release cycles; repository can grow in complexity; requires Firebase CLI tooling for all contributors.
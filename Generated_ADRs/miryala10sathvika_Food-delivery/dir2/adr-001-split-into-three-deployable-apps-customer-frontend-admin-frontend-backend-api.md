### ADR-001: Split into three deployable apps (Customer Frontend, Admin Frontend, Backend API)

Status: Inferred
Context: The repository contains three separate projects: frontend (customer-facing SPA), admin (back-office SPA), and backend (Node/Express API). Each has its own package.json, build tooling, and dev scripts.
Decision: Maintain three independent apps: two React SPAs (customer and admin) and a Node.js/Express backend API.
Consequences:
- Positive: Clear separation of concerns; independent deployment cadence; different auth/UX per audience; simpler client bundles.
- Negative: Multiple deployments and environments to manage; duplicated UI tooling/config; cross-origin communication needed between SPAs and API.
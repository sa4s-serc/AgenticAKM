### ADR-001: Monorepo housing mobile client and WhatsApp bot backend

Status: Inferred
Context: The repository contains two distinct applications: a React Native/Expo app (shravana-app) and a Python Flask-based WhatsApp bot (whatsapp-bot). Coordinating changes across client and bot, sharing assets/documentation, and simplifying CI/CD are common concerns when multiple components evolve together.
Decision: Keep both the mobile app and the WhatsApp bot in a single repository organized by top-level folders.
Consequences:
- Positive: Easier cross-component coordination, single source of truth, simpler developer onboarding, shared issue tracking/versioning.
- Negative: Larger repo size, potential coupling of release cycles, more complex CI pipelines to avoid unnecessary builds of unaffected parts.
---
### ADR-003: Use TypeScript and Jest for the mobile app

Status: Inferred
Context: The app includes a tsconfig.json and TypeScript dependencies, along with jest and jest-expo for testing. Type safety and testability are important for long-term maintainability.
Decision: Author mobile app components in TypeScript; use Jest with jest-expo for unit testing.
Consequences:
- Positive: Improved developer experience via typing, better IDE tooling, reduced runtime bugs, standard testing setup for RN/Expo.
- Negative: Slightly higher upfront typing overhead; maintaining type definitions and tests increases initial effort.
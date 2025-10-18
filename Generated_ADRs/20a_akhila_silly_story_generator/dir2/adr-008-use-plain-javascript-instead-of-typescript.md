---
### ADR-008: Use plain JavaScript instead of TypeScript

**Status:** Inferred
**Context:** The codebase uses index.js and lacks TypeScript configuration (tsconfig.json) or build tooling that would compile TS.
**Decision:** Implement application logic using JavaScript, not TypeScript.
**Consequences:** 
- Positive: No compilation step, reduced setup complexity, faster iteration for small scope.
- Negative: Lack of static typing can increase runtime errors and reduce maintainability as the codebase grows; fewer type-driven refactoring safeguards.
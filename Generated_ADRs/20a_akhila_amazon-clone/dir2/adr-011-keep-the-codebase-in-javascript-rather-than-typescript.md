---
### ADR-011: Keep the codebase in JavaScript rather than TypeScript

Status: Inferred
Context: There are no TypeScript dependencies or tsconfig; source files are .js and .css. Despite a “typescript” path listed, the project configuration shows a JS stack.
Decision: Implement the application in JavaScript (React 17 + CRA) across frontend and Node-based Cloud Functions.
Consequences:
- Positive: Faster onboarding; fewer build-time constraints; simpler tooling.
- Negative: Lack of static typing can allow type-related bugs; reduced IDE/type-safety benefits; potential refactor cost if TypeScript is adopted later.
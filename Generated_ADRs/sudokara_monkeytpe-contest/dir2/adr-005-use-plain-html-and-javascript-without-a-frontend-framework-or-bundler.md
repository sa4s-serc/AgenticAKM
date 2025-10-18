---
### ADR-005: Use plain HTML and JavaScript without a frontend framework or bundler

Status: Inferred
Context: No evidence of React/Vue/Angular or bundlers (e.g., Webpack/Vite). The codebase contains vanilla HTML/JS files (renderer.js, leaderboard.js).
Decision: Implement the UI with vanilla HTML/CSS/JS, relying on Electron’s built-in Chromium runtime without additional build tooling.
Consequences:
- Positive: Minimal dependencies; fast startup for development; reduced build complexity; easier for contributors familiar with plain JS.
- Negative: Less structure and tooling support for large-scale UI; manual management of modules/components; fewer optimizations and dev ergonomics (e.g., HMR, code splitting).
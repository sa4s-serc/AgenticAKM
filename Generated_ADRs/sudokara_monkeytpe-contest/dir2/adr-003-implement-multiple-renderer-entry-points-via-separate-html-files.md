---
### ADR-003: Implement multiple renderer entry points via separate HTML files

Status: Inferred
Context: The repository includes index.html and leaderboard.html, each with its own JS (renderer.js, leaderboard.js). This suggests distinct windows/pages instead of a single-page app.
Decision: Use multiple HTML files as independent renderer entry points, likely loaded in separate BrowserWindow instances or navigations for different application views.
Consequences:
- Positive: Simpler mental model per view; easier to develop features in isolation; decouples feature-specific scripts.
- Negative: Potential duplication of shared UI/state; window lifecycle management overhead; harder to share routing/state compared to a SPA.
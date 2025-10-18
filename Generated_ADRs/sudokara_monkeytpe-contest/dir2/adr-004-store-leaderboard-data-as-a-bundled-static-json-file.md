---
### ADR-004: Store leaderboard data as a bundled static JSON file

Status: Inferred
Context: A leaderboard.json file is present, implying data is read locally rather than fetched from a backend service.
Decision: Bundle leaderboard data as a local JSON asset for the application to read at runtime.
Consequences:
- Positive: Offline-first behavior; no backend infrastructure required; deterministic data access and simpler debugging.
- Negative: No real-time updates; requires app updates or file replacement to change data; potential for larger package size as data grows.
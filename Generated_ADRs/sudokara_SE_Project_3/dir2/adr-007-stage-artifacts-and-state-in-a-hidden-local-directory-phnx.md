---
### ADR-007: Stage artifacts and state in a hidden local directory (.phnx)

**Status:** Inferred
**Context:** The repository includes src/phoenix/CLI/.phnx with compressed and encrypted artifacts, plus logs (log, log.csv). No external DB or cache is present.
**Decision:** Use a hidden per-environment .phnx directory to store intermediate and final artifacts (compressed and encrypted), along with operational logs.
**Consequences:** 
- Positive: Simple, file-based state management; easy inspection and cleaning; minimal dependencies.
- Negative: Disk usage can grow; requires housekeeping; not transactional; concurrent access must be managed to avoid partial artifacts.
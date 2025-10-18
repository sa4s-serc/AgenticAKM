---
### ADR-007: Prioritize unit tests for geometry/domain logic over GUI tests

**Status:** Inferred
**Context:** The tests directory contains test_shapes.py but no UI-focused tests. GUI frameworks like PySimpleGUI are harder to test headlessly compared to pure logic.
**Decision:** Write unit tests for core geometry and domain behavior (e.g., shapes), and limit or avoid automated UI tests.
**Consequences:** 
- Positive: Reliable, fast tests for critical logic; easier CI integration.
- Negative: Limited automated coverage for UI behavior; potential reliance on manual testing for interaction flows.
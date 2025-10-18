---
### ADR-007: Command-line oriented workflows with progress and offline visualization

Status: Inferred
Context: Presence of tqdm and matplotlib in requirements; no web service framework; multiple CLI tools under tools/.
Decision: Deliver functionality as CLI scripts with progress bars (tqdm) and offline plots/analysis (matplotlib).
Consequences:
- Positive: Lightweight, easy to run locally or in batch; low operational overhead.
- Negative: Not a long-running service; limited interactivity; requires external schedulers for automation.
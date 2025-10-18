---
### ADR-012: Drive execution via shell commands for reproducible experiments

**Status:** Inferred
**Context:** Both AdaMLS and NAVIE contain command.sh; there are per-run CSV logs and a Results directory for consolidated outputs.
**Decision:** Standardize execution through shell scripts invoking App.py, producing structured CSV artifacts for later analysis.
**Consequences:** 
- Positive: Improves reproducibility and ease-of-use for repeated trials and batch runs. 
- Negative: Less flexible than parameterized experiment frameworks; limited cross-platform ergonomics. 
- Trade-off: Favored simplicity and consistency for research workflows over sophisticated experiment orchestration tools.
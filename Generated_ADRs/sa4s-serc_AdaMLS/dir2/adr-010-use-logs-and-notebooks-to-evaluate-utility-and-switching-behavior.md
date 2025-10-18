---
### ADR-010: Use logs and notebooks to evaluate utility and switching behavior

**Status:** Inferred
**Context:** Results include utility and switching plots; notebooks (Utility_Plot.ipynb, Model_Switching_Plot.ipynb) consume CSV logs from runs.
**Decision:** Instrument the system to write detailed logs (monitor, model, overall), then analyze via Jupyter notebooks to visualize utility and switching patterns.
**Consequences:** 
- Positive: Facilitates rapid iteration and clear reporting for experiments. 
- Negative: Analysis workflow depends on manual notebook execution; limited automation. 
- Trade-off: Chose transparency and flexibility in analysis over fully automated dashboards.
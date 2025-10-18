---
### ADR-010: Charts and analytics with Chart.js via react-chartjs-2

Status: Inferred
Context: Dependencies include chart.js and react-chartjs-2; components like MonthlyAnalysis and AnalysisTable exist.
Decision: Use Chart.js (with react-chartjs-2) for rendering analytics visualizations in the SPA.
Consequences:
- Positive: Mature charting library; good React integration; sufficient for common chart types.
- Negative: Complex custom visualizations may be harder; bundle size impact.
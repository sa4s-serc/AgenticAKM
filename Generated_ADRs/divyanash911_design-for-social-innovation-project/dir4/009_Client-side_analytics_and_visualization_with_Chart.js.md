# ADR-009: Client-side analytics and visualization with Chart.js

**Date**: 2025-10-13
**Status**: Proposed

## Context
Chart.js is listed in dependencies and components like AnalysisTable and MonthlyAnalysis exist.

## Decision
Render analytical views and charts on the client using Chart.js.

## Consequences
Provides interactive visualizations with minimal backend complexity, but large datasets may require server-side aggregation to avoid performance and bandwidth issues.
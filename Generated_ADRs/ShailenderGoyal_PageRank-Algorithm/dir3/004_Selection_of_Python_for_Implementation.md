# ADR-004: Selection of Python for Implementation

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project required a technology stack capable of efficiently handling numerical computations for the graph algorithm and generating sophisticated data visualizations.

## Decision
Python was selected as the primary programming language for the entire implementation.

## Consequences
Leveraging Python provides access to a powerful ecosystem of scientific computing and plotting libraries (e.g., NumPy, Matplotlib), which greatly accelerates development. The language's readability makes the implementation accessible to a broad audience. For extremely large graphs, the performance of a pure Python implementation might be a limitation compared to lower-level languages or distributed computing platforms.
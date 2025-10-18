# ADR-003: Multi-modal Result Presentation

**Date**: 2025-10-16
**Status**: Proposed

## Context
The goal was to provide a comprehensive and intuitive understanding of the PageRank algorithm's output, catering to both quantitative analysis and visual interpretation.

## Decision
The application was designed to present its findings in three distinct formats: a ranked list of nodes and scores printed to the console, a network diagram visualizing node importance, and a line chart showing score convergence.

## Consequences
This strategy delivers a rich and effective user experience, making the tool highly valuable for demonstration and educational purposes. The trade-off is that the generation of these outputs is tightly integrated, making it difficult to run the core algorithm in a headless environment or to independently modify the visualization components.
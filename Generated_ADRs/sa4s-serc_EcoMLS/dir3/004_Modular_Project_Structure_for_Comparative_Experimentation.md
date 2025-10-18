# ADR-004: Modular Project Structure for Comparative Experimentation

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project is fundamentally a research framework designed to prove the effectiveness of the sophisticated 'EcoMLS' strategy against several simpler, 'naive' strategies. The architecture needed to support this comparative analysis cleanly and reproducibly.

## Decision
The repository is structured with separate, parallel directories for each adaptation strategy (`EcoMLS/`, `NAIVE1/`, `NAIVE2/`, etc.). Each directory contains its own implementation of the decision-making logic, while likely sharing common infrastructure. A central `Results/` directory is used to store all logs, data, and visualizations from experiments.

## Consequences
This structure is ideal for academic and experimental work. It ensures a clean separation of concerns between experiments, making the results easy to reproduce, compare, and analyze. The clear organization of outputs in the `Results` folder directly supports the project's validation goals. The main drawback is potential code duplication across the different strategy directories if common components are not managed carefully.
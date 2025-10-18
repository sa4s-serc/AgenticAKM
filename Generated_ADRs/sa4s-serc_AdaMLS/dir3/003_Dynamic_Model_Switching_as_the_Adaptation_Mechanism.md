# ADR-003: Dynamic Model Switching as the Adaptation Mechanism

**Date**: 2025-10-10
**Status**: Proposed

## Context
A single ML model cannot simultaneously optimize for speed, accuracy, and resource usage under all conditions. A mechanism was needed to dynamically trade off these conflicting goals based on the current context, such as input data complexity or system load.

## Decision
The system's primary adaptation action is to switch between different pre-trained sizes of a YOLOv5 model (from `nano` to `xlarge`) at runtime. The Planner component selects the most suitable model variant based on the current context identified by the Analyzer.

## Consequences
This provides a direct and effective way to adapt performance. The system can choose a fast, less-accurate model during high load and a slow, more-accurate model for complex inputs. This flexibility improves overall utility. The trade-off is the added complexity of managing multiple models and the potential latency or resource spike incurred during the model-switching operation itself.
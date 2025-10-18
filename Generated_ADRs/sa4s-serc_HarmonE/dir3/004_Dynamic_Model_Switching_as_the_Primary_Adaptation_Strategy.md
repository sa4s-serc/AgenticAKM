# ADR-004: Dynamic Model Switching as the Primary Adaptation Strategy

**Date**: 2025-10-09
**Status**: Proposed

## Context
When the active model's performance degrades, the system needs an efficient recovery mechanism that is faster and less computationally expensive than full retraining.

## Decision
The system was designed to maintain a versioned pool of diverse, pre-trained models (e.g., LSTM, SVR, Linear). Adaptation is primarily achieved by dynamically switching the active model at runtime. The 'Execute' phase simply updates a configuration file (`knowledge/model.csv`) which the inference process reads to load the new model.

## Consequences
This allows for near-instantaneous, low-cost adaptation to changing conditions. It provides flexibility by enabling the system to select the most appropriate model architecture for the current data. However, its effectiveness is limited by the diversity and quality of the pre-trained model pool; if no existing model is a good fit for a new data distribution, this strategy will fail.
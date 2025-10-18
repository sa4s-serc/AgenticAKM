# ADR-002: Development of a Custom Financial Trading Environment

**Date**: 2025-10-14
**Status**: Proposed

## Context
The core problem is automated stock portfolio management, a domain for which standard pre-built RL environments (like those in OpenAI Gym) are unsuitable. A simulation was needed to process historical stock data, execute trading actions (portfolio allocations), and calculate performance-based rewards.

## Decision
To create a custom simulation environment from scratch, named `PortfolioEnv` and defined in `env.py`. This environment is specifically designed to handle the state representation, action space, and reward logic inherent to financial portfolio management.

## Consequences
This decision provided a highly tailored and domain-specific simulation, enabling the agents to be trained on a problem that closely mirrors the real-world task. The primary trade-off is the engineering overhead of building, validating, and maintaining a custom environment, as opposed to using a battle-tested, off-the-shelf one.
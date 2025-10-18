### ADR-001: Reinforcement Learning Approach for Financial Trading

**Status:** Inferred
**Context:** The project needed to develop an automated agent capable of making sequential decisions in a financial market environment to maximize returns. Traditional algorithmic trading often relies on fixed rules or supervised learning models that may not adapt well to dynamic market conditions. The challenge was to create a system that could learn an optimal trading strategy through interaction and feedback from the market.

**Decision:** The project adopted a Reinforcement Learning (RL) approach. A custom trading environment was created (indicated by `env.py` and the `gym-trading-env` dependency) to simulate market interactions. The system was designed to experiment with multiple RL algorithms, as evidenced by dedicated implementation files for DQN (`DQN.py`), DDPG (`DDPG.py`), SAC (`SAC.py`), and VPG (`VPG-continuous.py`, `VPG-discrete.py`).

**Consequences:**
*   **Positive:**
    *   The system can learn complex, non-obvious strategies that adapt over time.
    *   The framework allows for direct comparison of different state-of-the-art RL algorithms on the same problem.
    *   The use of stock data (`data/IBM.csv`, `data/KO.csv`, etc.) and the `ccxt` library suggests the architecture is applicable to both traditional stock markets and cryptocurrency exchanges.
*   **Negative:**
    *   RL models are notoriously difficult to train and require significant hyperparameter tuning and computational resources.
    *   The "black box" nature of the learned policies can make them difficult to interpret and trust in a high-stakes financial setting.
    *   Simulation-to-reality gap: Strategies that work well in the simulated environment may not perform as expected in the live market due to factors like latency and slippage.
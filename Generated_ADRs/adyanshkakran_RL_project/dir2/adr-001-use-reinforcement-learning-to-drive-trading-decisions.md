### ADR-001: Use reinforcement learning to drive trading decisions

Status: Inferred
Context: The repository contains multiple RL algorithm implementations (DQN.py, DDPG.py, SAC.py, VPG-continuous.py, VPG-discrete.py) and an environment wrapper (env.py), along with market data (data/IBM.csv, data/KO.csv, data/PEP.csv, data/WBA.csv). Rewards, actions, and cumulative rewards are logged per asset under rewards/sac/.
Decision: Adopt reinforcement learning as the core approach for algorithmic trading, implementing several algorithms (DQN, DDPG, SAC, VPG) to compare and apply across assets and action spaces.
Consequences: 
- Positive: Flexibility to match algorithm to problem characteristics; ability to benchmark and iterate quickly; broader coverage of discrete and continuous trading strategies.
- Negative: Increased code surface and maintenance across several algorithms; higher experimentation and hyperparameter-management overhead.
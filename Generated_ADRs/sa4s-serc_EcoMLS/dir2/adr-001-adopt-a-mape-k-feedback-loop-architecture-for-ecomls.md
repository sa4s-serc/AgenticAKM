### ADR-001: Adopt a MAPE-K feedback-loop architecture for EcoMLS

Status: Inferred
Context: The repository contains Monitor.py, Analyzer.py, Planner.py, Execute.py, and multiple CSVs that resemble a Knowledge base (knowledge.csv, model.csv, monitor.csv). The presence of MAPEK_energy.csv and an architecture diagram file suggests a deliberate control-loop-based design.
Decision: Structure the system around the MAPE-K (Monitor, Analyze, Plan, Execute + Knowledge) feedback loop to adapt model selection during inference.
Consequences: 
- Positive: Clear separation of concerns; enables adaptive behavior and experimentation with different analysis/planning strategies. 
- Negative: Adds orchestration overhead and complexity; requires consistent knowledge management across components.
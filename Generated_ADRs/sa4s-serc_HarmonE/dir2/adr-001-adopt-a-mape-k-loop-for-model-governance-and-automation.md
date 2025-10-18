### ADR-001: Adopt a MAPE-K loop for model governance and automation

Status: Inferred
Context: The repository includes a structured set of modules under mape/ (monitor.py, analyse.py, plan.py, execute.py, manage.py) and a knowledge/ directory containing thresholds, logs, and model/prediction artifacts. This strongly indicates a need to continuously monitor model performance, analyze deviations, plan corrective actions, and execute them, while persisting state and knowledge.
Decision: Implement the MAPE-K (Monitor–Analyze–Plan–Execute over a shared Knowledge base) architecture to manage model operations, drift detection, and retraining.
Consequences: 
- Positive: Clear separation of concerns; extensible control loop; explicit knowledge base improves auditability and transparency; supports autonomous/closed-loop ML operations.
- Negative: Increased orchestration complexity; requires careful coordination and scheduling; potential for tight coupling to the chosen knowledge representation.
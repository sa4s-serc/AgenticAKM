---
### ADR-012: Experimental scheduling strategies encapsulated as interchangeable CameraFragment variants

Status: Inferred
Context: Separate directories contain alternative CameraFragment implementations (contains_camerafrag_naive, contains_camerafrag_mlfq, contains_camerafrag_epsilon) and outputs folder includes CSVs and plots (Naive.csv, MLFQ.csv, Epsilon.csv).
Decision: Isolate and swap camera/inference scheduling strategies by implementing alternative CameraFragment variants to facilitate experimentation and measurement.
Consequences:
- Positive: Enables A/B testing and empirical evaluation; clean comparison of policies; straightforward metric collection.
- Negative: Code duplication across variants; risk of divergence; merging improvements across variants requires discipline.
---
### ADR-003: Scikit-learn for Machine Learning Implementation

**Status:** Inferred
**Context:** The system's core functionality involves making predictions and adapting its predictive models. A machine learning library was required to implement this functionality. Key considerations would have included the ease of use, the availability of standard algorithms, and community support. The presence of `inference.py` and `retrain.py` indicates distinct operational phases for the ML models.
**Decision:** The Scikit-learn library was chosen as the primary machine learning framework. This is confirmed by its inclusion in `requirements.txt`. Scripts like `tools/train_models.py` and `retrain.py` likely leverage this library to build and update the models used by `inference.py`.
**Consequences:**
*   **Positive:** Scikit-learn provides a comprehensive suite of well-established, pre-implemented machine learning algorithms. Its consistent API simplifies the process of training, evaluating, and deploying models. The library is well-documented and widely used, making it easy to find support and resources.
*   **Negative:** While excellent for classical machine learning, Scikit-learn is not the primary choice for deep learning applications. The system is therefore likely not using complex neural network architectures. The decision focuses the system on traditional ML models, which may be a limiting factor for certain types of problems.
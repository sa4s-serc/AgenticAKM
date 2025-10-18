---
### ADR-003: Hybrid Deep Learning Framework Adoption

**Status:** Inferred
**Context:** The project requires implementing various deep neural network architectures for the different RL agents (e.g., Q-networks, policies, critics). Different deep learning frameworks have different strengths, community support, and pre-existing implementations for specific algorithms. The team needed to select a framework or frameworks to build these models.

**Decision:** A hybrid approach was taken, utilizing both PyTorch and TensorFlow/Keras. The presence of `.pth` files (`actor_DDPG.pth`, `SAC_Best.pth`) is a clear indicator of PyTorch usage. Concurrently, the existence of `saved_model.pb` and `keras_metadata.pb` files within the `models/` directory points to the use of the TensorFlow/Keras `SavedModel` format. This suggests that some components or experiments were implemented in PyTorch (like DDPG and SAC), while others (like DQN) were implemented in TensorFlow.

**Consequences:**
*   **Positive:**
    *   **Flexibility:** Allows developers to use the best framework for a specific task or leverage existing high-quality implementations of RL algorithms regardless of the source framework.
    *   Facilitates collaboration among team members who may have different framework preferences or expertise.
*   **Negative:**
    *   **Increased Complexity:** The project has dependencies on two major deep learning libraries, which can complicate dependency management, environment setup, and deployment.
    *   **Inconsistency:** The code for model definition, training, and inference will be different between the PyTorch and TensorFlow components, potentially increasing the learning curve for new developers.
    *   Potential for interoperability issues when trying to combine or compare models from the different frameworks.
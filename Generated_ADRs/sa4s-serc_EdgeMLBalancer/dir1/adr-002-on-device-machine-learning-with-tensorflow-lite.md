---
### ADR-002: On-Device Machine Learning with TensorFlow Lite

**Status:** Inferred
**Context:** The core functionality of the application is real-time object detection. Performing this task in the cloud would introduce significant network latency, making real-time feedback impossible. It would also require a constant internet connection and raise potential data privacy concerns.
**Decision:** To implement on-device machine learning using the TensorFlow Lite (TFLite) framework. This is strongly indicated by the package name `org.tensorflow.lite.examples.objectdetection`, the inclusion of multiple `.tflite` model files (e.g., `efficientdet-lite0.tflite`, `mobilenetv1.tflite`) in the application's assets, and native libraries related to TensorFlow Lite's GPU delegate (`libtensorflowlite_gpu_jni.so`).
**Consequences:**
*   **Positive:**
    *   Enables low-latency, real-time inference directly on the user's device.
    *   The application can function entirely offline.
    *   User data (camera images) remains on the device, enhancing privacy.
*   **Negative:**
    *   The application's performance is constrained by the processing power of the user's device.
    *   Including ML models within the app package increases the overall application size (`.apk`).
*   **Trade-offs:** Sacrificed the potential processing power of cloud servers for the benefits of low latency, offline capability, and user privacy.
---
### ADR-005: Uncompressed Packaging of TFLite Models

**Status:** Inferred
**Context:** For optimal performance, TensorFlow Lite needs to load model files into memory quickly. The default Android build process compresses files in the `assets` directory to reduce APK size. This would force the TFLite runtime to first decompress the model into memory before loading it, adding latency and increasing memory usage.
**Decision:** Configure the Gradle build process to explicitly prevent the compression of `.tflite` files. This decision is directly visible in the `app/build.gradle` file with the `androidResources { noCompress 'tflite' }` configuration.
**Consequences:**
*   **Positive:**
    *   Enables the TFLite interpreter to use memory mapping (`mmap`) to load the model directly from the APK.
    *   Significantly reduces model loading time and lowers the application's memory footprint during initialization.
*   **Negative:**
    *   The final `.apk` file size is slightly larger than it would be if the models were compressed.
*   **Trade-offs:** Prioritized runtime performance and memory efficiency over the smallest possible application download size, which is a critical optimization for an ML-heavy application.
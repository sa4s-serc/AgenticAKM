---
### ADR-004: Ship ML models as app assets and disable compression of .tflite files

Status: Inferred
Context: Models live under app/src/main/assets; androidResources { noCompress 'tflite' } is set in Gradle to avoid APK compression of model files.
Decision: Bundle TFLite models in the APK as static assets and disable compression to reduce load time and memory overhead.
Consequences:
- Positive: Predictable availability and fast startup; no network dependency.
- Negative: Larger APK size; updating models requires shipping a new app version.
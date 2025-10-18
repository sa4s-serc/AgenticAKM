---
### ADR-003: On-device object detection with TensorFlow Lite Task Library

Status: Inferred
Context: Presence of ObjectDetectorHelper, OverlayView, and TFLite models (efficientdet-lite0/1/2.tflite, mobilenetv1.tflite) in assets. Native libraries include libtask_vision_jni.so and libimage_processing_util_jni.so. The package is org.tensorflow.lite.examples.objectdetection.
Decision: Use TensorFlow Lite (Task Library) for on-device object detection, rendering results via a custom OverlayView.
Consequences:
- Positive: Runs offline with low latency; well-supported, mobile-optimized inference; simple integration APIs.
- Negative: Device heterogeneity (performance/accuracy vary); model updates require app updates unless a dynamic mechanism is introduced.
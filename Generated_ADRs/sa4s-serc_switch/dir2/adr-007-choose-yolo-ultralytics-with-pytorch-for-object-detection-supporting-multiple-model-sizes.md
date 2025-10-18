---
### ADR-007: Choose YOLO (Ultralytics) with PyTorch for object detection, supporting multiple model sizes

Status: Inferred
Context: Requirements include torch, torchvision, ultralytics; AdaMLs contains knowledge for yolov5[n/s/m/l/x] variants and cluster mappings; OpenCV is included.
Decision: Standardize on Ultralytics YOLO with PyTorch for object detection, enabling dynamic selection among model variants based on input clustering/knowledge.
Consequences:
- Positive: Strong accuracy/speed trade-offs; large model family coverage; community support and tooling.
- Negative: Heavy dependencies increase image size and build time; model management complexity; GPU acceleration considerations.
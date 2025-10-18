### ADR-001: Split edge–cloud inference using speculative decoding

Status: Inferred
Context: The repository is named SpecECD (Speculative Edge-Cloud Decoding) and includes distinct cloud and edge components (cloud/server.py, cloud/target_model.py, edge/client.py, edge/draft_model.py). Requirements files differentiate “Cloud Server (CUDA GPU only)” and “Edge Client (CPU, GPU, NPU support)”. Tests include comparative performance evaluation, implying a coordinated inference flow across edge and cloud.
Decision: Adopt a two-tier inference architecture where a lightweight “draft” model runs on the edge device and a more accurate “target” model runs on a cloud GPU. The system performs speculative decoding: the edge proposes token drafts and the cloud confirms/rectifies them.
Consequences: 
- Positive: Reduces end-to-end latency and bandwidth by offloading heavy validation to the cloud while leveraging local compute for draft generation; improves perceived responsiveness.
- Negative: Increases system complexity (synchronization, error handling, fallback paths); requires reliable networking; introduces consistency and drift concerns between draft and target models.
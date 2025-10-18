---
### ADR-004: Standardize on glTF 2.0 for 3D models and serve them from /public

Status: Inferred
Context: The project includes many GLTF assets (scene.gltf/scene.bin) and textures for cars, stadium, and props, as well as a GLB (adyansh.glb). Vite’s public folder is used for direct serving of static assets.
Decision: Use glTF 2.0 (GLTF/GLB) as the primary 3D asset format and place all runtime assets under public/ for direct fetch at runtime.
Consequences:
- Positive: glTF is efficient for web delivery and widely supported by Three.js; PBR-ready, straightforward to load; public/ works seamlessly with Vite’s static serving.
- Negative: Large uncompressed assets can increase initial load time; no evidence of mesh compression (e.g., Draco/KTX2), so potential optimization work remains; assets are included in-repo, increasing repository size.
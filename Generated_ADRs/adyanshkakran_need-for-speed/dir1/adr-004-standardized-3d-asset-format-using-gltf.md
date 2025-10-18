---
### ADR-004: Standardized 3D Asset Format using glTF

**Status:** Inferred
**Context:** The 3D application needs to load numerous complex assets, including car models, the stadium, and other objects, complete with their geometry, materials, and textures. An efficient, web-optimized, and standardized file format was required to ensure fast loading times and compatibility with the chosen rendering library (Three.js).
**Decision:** The **glTF (GL Transmission Format)** was chosen for 3D models. The repository contains numerous models in this format, indicated by the presence of `scene.gltf` and `scene.bin` files for assets like `mcqueen`, `hudson`, `stadium`, and `chick_hicks`.
**Consequences:**
*   **Positive:** glTF is the industry standard for transmitting 3D assets on the web. It is compact, designed for fast parsing, and is fully supported by Three.js. This choice streamlines the asset pipeline from 3D modeling software to the browser.
*   **Negative:** The art and modeling workflow must be capable of exporting to the glTF 2.0 standard. Some highly complex or proprietary shader effects from modeling software may not translate perfectly to the glTF format, requiring adjustments for the web.
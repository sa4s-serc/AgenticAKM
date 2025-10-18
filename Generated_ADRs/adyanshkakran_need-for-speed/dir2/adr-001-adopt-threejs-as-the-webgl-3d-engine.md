### ADR-001: Adopt Three.js as the WebGL 3D engine

Status: Inferred
Context: The application is a browser-based 3D car racing experience, evidenced by multiple 3D assets (GLTF/GLB, textures) and source files like car.js, racetrack.js, and fuel.js. A robust, widely supported WebGL abstraction was needed to render 3D scenes and load assets efficiently in the browser.
Decision: Use Three.js (dependency three@^0.149.0) as the rendering engine.
Consequences: 
- Positive: Mature ecosystem, broad community support, straightforward asset loading (GLTFLoader), good documentation, and easy integration with vanilla JS and modern bundlers.
- Negative: Requires hand-rolled game loop and scene management; lacks built-in high-level game features (physics, entity systems), increasing custom code burden compared to full game engines.
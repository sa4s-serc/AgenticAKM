### ADR-001: Build the application as a cross-platform desktop app using Electron

Status: Inferred
Context: The repository is structured as an Electron app with "main": "index.js" and a start script of "electron .". This suggests a need to deliver a desktop experience using web technologies (HTML/JS) while accessing local resources.
Decision: Use Electron (v37.x) to package and run the application as a desktop app, with index.js as the main process entry point.
Consequences: 
- Positive: Cross-platform support (Windows/Mac/Linux), ability to use web tech for UI, access to Node.js APIs, straightforward developer onboarding.
- Negative: Larger app footprint and memory usage vs. native/web, security surface area of Electron must be managed, packaging/distribution complexity when moving beyond dev.
### ADR-001: Split frontend SPA and backend API

Status: Inferred
Context: The repository contains a React application (Create React App) under code/ and a Python Flask backend under code/backend. Components, hooks, and Redux slices indicate a rich client-side app, while Flask, Flask-CORS, PyJWT, and pymongo indicate a separate HTTP API.
Decision: Adopt a client–server architecture with a React Single Page Application consuming a Flask REST API over HTTP.
Consequences: 
- Positive: Clear separation of concerns, independent deployment and scaling, familiar developer workflow.
- Negative: Requires CORS handling and duplication of validation/auth logic across client and server; more complex local dev setup (two servers).